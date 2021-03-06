# How do you find your best value rental home?
![](https://github.com/leo2506/metis-work/blob/master/Project%202/moda-apartments-exterior.jpg)

# Objective
The objective of this project is to help customer who wants to rent a home find the best value property and budget their rental expenses. 
 
# Streamline of Data Analysis
* [Presentation](/Project_2/Slides/Home%20rental%20prediction.pdf)
* [Summary](https://liuriguang.wixsite.com/leo2506-1/blog/project-luther-how-do-you-find-the-best-value-rental-home)
* [Multipage_scrapping.ipynb](/Project_2/multipage_scrapping.ipynb) - walks through the process of web scrapping. 
* [Data_cleaning.ipynb](/Project_2/Data_cleaning.ipynb) - cleans the scrapped data and engineers new features.
* [Alternative_model.ipynb](/Project_2/Alternative_model.ipynb) - applies Ridge to address overfitting problems.
* [Final_model.ipynb](/Project_2/Final_model.ipynb) - applies variable transformation to address heteroskedasticity and overfitting problems.

# Description of Functions
* `single_page_scrap` - scraps detailed information of a single property(encapsulated).  
* `multiple_page_scrap` - iterates through multiple rental property pages by URLs, scraps each single page and stores data in a csv file(encapsulated). 

# Description of Folders
* `Version Control` - saves previous pieces of work not included in the final deliverable but good for debug purposes . 
* `Charts` - is a set of screenshots of charts and tables .  
* `Data` - includes URL, raw data and cleaned data .
* `Proposal` - describes original design of the project. There are some changes in the content. I choose to use realtor.com instead of zillow.com because of the robot testing and choose to predict rental prices because one of my classmates is doing prediction on sale prices . 
* `Slides` - includes pdf and ppt version of the slides . 

# Data sources
* URL and raw Data - https://www.realtor.com/realestateandhomes-search/Seattle_WA . 

