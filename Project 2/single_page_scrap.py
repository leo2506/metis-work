from bs4 import BeautifulSoup

import numpy as np
import pandas as pd

import re

def floorplan_scrapper(soup, room_type):
    '''
        This function scraps a single floorplan table. 
        It is an auxiliary function for function
        floorplan_scrapper1(soup). It returns a DataFrame.
    '''
    content = soup.find(id=room_type)

    df = pd.DataFrame(columns=['Room Type','Bath','Sqft','Price'])

    for row in content.find_all('tr'):
        name = room_type.replace('floorplan-','')
        bath = float(row.find(class_="col-bath").text.strip()[0])
        sqft = float(row.
                     find(class_="col-sqft").
                     text.strip().
                     split()[0].
                     replace(',',''))
        price = row.find(class_="col-price").text.strip()
        if price == "N/A":
            continue
        price = float(price.replace('$','').replace(',',''))

        temp = [name,bath,sqft,price]
        df = df.append(pd.DataFrame([temp],
                       columns=['RoomType','Bath','Sqft','Price']),
                       ignore_index=True)

    return df

def floorplan_scrapper1(soup):
    '''
        This function scraps the whole floorplan panel if any 
        , and concatenates them into a single DataFrame.
    '''
    ids = []
    floorplan=soup.find(class_="list-floorplans")
    df = pd.DataFrame(columns=['Room Type','Bath','Sqft','Price'])
    if floorplan: 
        for panel in floorplan.find_all(class_="panel"):
            ids.append(panel["id"])

        for id_ in ids:
            df = df.append(floorplan_scrapper(soup, id_),ignore_index=True)

        return df
        

def get_address_str(address):
    '''
        This is an auxiliary function for function trait_scrapper(soup)
        to handle address strings and combine them into one single string.
    '''
    a = address.text.strip().split('\n')[1:]
    b = []
    for add in a:
        b.append(add.strip())
    return ' '.join(b)  

def get_features_list(list_a):    
    '''
        This is an auxiliary function for function trait_scrapper(soup)
        to handle property feature list such as Community Features and
        Unit Features, and combine them into one single list. 
    '''
    la = []
    for l in list_a:
        la.append(l.text.strip().split('\n'))
    lb = []
    for l in la:
        lbb = []
        for ll in l:
            lbb.append(ll.strip())
        lb.append(lbb)
    return lb 

    
def trait_scrapper(soup):
    '''
        This is a function scrap a rental property's traits if any, including
        its name, address, type, features, surrounding schools, neighborhood
        median rental price, median listing price. It returns a DataFrame.
    '''
    ty = soup.find("li", attrs={"data-label":"property-type"})
    bu = soup.find("li", attrs={"data-label":"property-year"})
        
    # Add columns of property type and year-built
    df = pd.DataFrame(columns=["Type", "Built"])
    if ty is not None:
        df["Type"] = (ty.
                      find(text=re.compile("Type")).
                      find_next("div").
                      contents) 
    if bu is not None:
        df["Built"] = (bu.
                       find(text=re.compile("Built")).
                       find_next("div").
                       contents)
    
    # Add columns of property name and address
    if soup.find(class_="ldp-header-address "):
        address = soup.find(class_="ldp-header-address ").find(itemprop="address")
        name = address.text.strip().split('\n')[0]
        if name[0].isnumeric():
            df["Address"] = name + ' ' + get_address_str(address)
        else:    
            df["Address"] = get_address_str(address)
            df["Name"] = name
            
    # Add columns of Community Features and Unit Features,
    # which are stored in a list
    section = soup.find(class_="listing-subsection-features")
    if section:
        list1 = get_features_list(section.find_all(class_="col-sm-6"))
    
    # Change df into object type to enable it to store list values
    df.astype(object)
    if soup.find(text=re.compile("Community Features")):
        df["Community Features"] = [list1[0]+list1[1]]
        if soup.find(text=re.compile("Unit Features")):       
            df["Unit Features"] = [list1[2]+list1[3]]
    elif soup.find(text=re.compile("Unit Features")):
        df["Unit Features"] = [list1[0]+list1[1]]        
            
    # Add columns of number of surrounding rated schools
    # and their average ratings 
    school = soup.find_all(class_="school-rating")

    rating_list = []
    for s in school:
        rating_list.append(s.text)

    rating = [int(a) for a in rating_list if a.isnumeric() ]
    df["Number of Schools"] = len(rating)
    df["Average School Rating"] = round(np.mean(rating),2)

    # Add columns of median rental price and median listing price
    # in the neighborhood
    nb = soup.find_all(class_ = "neighborhood-flex-item")

    if len(nb) != 0:
        nb_list = []
        for nb1 in nb:
            nb_list.append(nb1.text.strip().split('\n'))

        title1 = nb_list[0][-1].strip()
        title2 = nb_list[1][-1].strip()
        value1 = float(nb_list[0][0].replace('$','').replace(',',''))
        value2 = float(nb_list[1][0].replace('$','').replace(',',''))
        df[title1] = value1
        df[title2] = value2

    return df

def meta_extract(soup, info):
    '''
        This is an auxiliary function of single_page_scraper(soup)
        to extract meta information if the property does not have
        a floorplan panel existed.
    '''
    meta = soup.find(id="ldp-property-meta")
    if meta:
        l = meta.find("li", attrs={"data-label": f"property-meta-{info}"})
        if l:
            return l.text.strip().split()
        
def single_page_scraper(soup):
    '''
        This function scrap a single page of property details and 
        store it in a DataFrame.
    '''
    df_trait = trait_scrapper(soup)

    # Add floorplan to properties which have a table of floorplans,
    # othrewise extract meta property information
    if floorplan_scrapper1(soup) is not None:
        df_floorplan = floorplan_scrapper1(soup)
        # Avoid expanding the DataFrame for multiple times by accident
        if(df_trait.shape[0] != df_floorplan.shape[0]):
            df_trait = pd.concat([df_trait] * df_floorplan.shape[0], 
                           ignore_index=True)  
        # Right append the trait columns to the floorplan DataFram
        df1 = pd.concat([df_trait,df_floorplan], axis=1)

    else:
        df1 = df_trait
        beds = meta_extract(soup, "beds")
        bath = meta_extract(soup, "bath")
        sqft = meta_extract(soup, "sqft")
        pets = meta_extract(soup, "pets")
        price = soup.find(itemprop="price").text
        if beds:
            df1["Room Type"] = beds[0] + "-bedroom" 
        if bath:
            if len(bath) <= 2:
                df1["Bath"] = float(bath[0])
            else:
                df1["Bath"] = float(bath[0]) + float(bath[2])*0.5 
        if sqft:        
            df1["Sqft"] = float(sqft[0].replace(',',''))
        if pets:
            df1["Unit Features"] = ' '.join(pets)
        if len(price) != 0:
            df1["Price"] = float(price.
                                 strip().
                                 replace('$','').
                                 replace(',',''))

    # Reorder columns and fill missing values as Nan objects
    cols = ["Name","Type","Address","Built",
                     "Room Type","Bath","Sqft","Price",
                    "Number of Schools","Average School Rating",
                    "Median Rental Price", "Median Listing Price",
                    "Community Features","Unit Features"]     
    df2 = pd.DataFrame(columns = cols)
    df = pd.concat([df2,df1], ignore_index = True)
    df = df[cols]

    return df