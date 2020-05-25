#This projects helps to get all the links present on a webpage by automatically opening it and gives a csv
#with all the links and their status code.

from selenium import  webdriver
import requests
import pandas as pd

driver=webdriver.Chrome("C:/bin/chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=xhN1xEZ0WLQ")      #for eg- youtube home page
links=[]
for a in driver.find_elements_by_xpath('.//a'):
    
    print(a.get_attribute('href'),r.status_code)               #status code with all the links.           
    links.append(a) 
df = pd.DataFrame({'Links':links}) 
df.to_csv('products1.csv')                                      # a file with all the links.
