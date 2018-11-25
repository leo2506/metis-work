from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

import numpy as np
import pandas as pd

import pickle
import re
import time
import os

import single_page_scrap as sps

chromedriver = f"{os.environ['HOME']}/.local/bin/chromedriver" # path to the chromedriver executable
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)


def url_scrapper(total_page, url_destination):
    '''
        Given a total page number, this function scraps the very number of 
        overview pages of www.realtor.com website's rental section for urls
        of each indiviual property's detailed information page and writes it 
        to a csv file given by the argument url_destination.
    '''
    driver.get("https://www.realtor.com/apartments/Seattle_WA")
    
    # Scrap total_page pages of urls of apartment for leasing into a list
    j = 0 
    urls = []
    while j < total_page:
        next_button = driver.find_element_by_class_name("next ")
        next_button.click()
        time.sleep(5) # Let's give the computer 5 seconds rest 
                      # after scraping a whole page of urls
        soup = BeautifulSoup(driver.page_source,'html.parser')
        for link in soup.find_all(class_="photo-wrap"): 
            urls.append("https://www.realtor.com"+link.find("a")["href"])
        j += 1
    
    # Save the url list as a csv file
    url_file = open(url_destination, 'w')
    for url in urls:
        url_file.write(url + '\n')
    url_file.close()
    
def multiple_page_scraper(url_source, data_destination, total_url): 
    '''
        This function reads a list of urls from the source file specified
        by the argument url_source, scraps a given number of rentals pages 
        tied to the urls and saves the data as a csv-file named by the argument
        data_destination. The total number of pages to scrap is given by the
        argument total_url.
    '''
    cols = ["Name","Type","Address","Built",
           "Room Type","Bath","Sqft","Price",
           "Number of Schools","Average School Rating",
           "Median Rental Price", "Median Listing Price",
           "Community Features","Unit Features","url"]
    df = pd.DataFrame(columns = cols)
    
    with open(url_source, 'r') as f:
        urls = f.read().split('\n')
        urls = list(set(urls)) # Remove duplicates
        urls.remove('') # Remove empty strings
        f.close()

    i = 0
    
    for url in urls[:total_url]:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source,"html5lib")
        df_property = sps.single_page_scraper(soup)
        df_property["url"] = url
        df = pd.concat([df, df_property], ignore_index=True)
        df.to_csv(data_destination)
        time.sleep(1)
        i += 1
        print(i)
        
def pickle_files(name):
    '''
        Pickle the file to a same name ".pkl" extension file.
    '''
    if name.split('.')[1] == "csv":
        data = pd.read_csv(name)
    else: 
        f = open(name, 'r')
        data = f.read().split('\n')

    pkl = name.split('.')[0] + ".pkl"
    with open(pkl,'wb') as picklefile:
        pickle.dump(data, picklefile)    