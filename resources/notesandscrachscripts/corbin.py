import requests
from lxml import etree
from bs4 import BeautifulSoup
#Function to Find the element from the Xpath
def Xpath(url):
  Dict_Headers = ({'User-Agent':
      'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
      (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
      'Accept-Language': 'en-US, en;q=0.5'})
  # Gets the requried data https browser's address bar
  webPage = requests.get(url,Dict_Headers)
  # Creating a soup Object from the html content
  Scraping = BeautifulSoup(webPage.content, "html.parser") 
  # Conveting Soup object to etree object for Xpath processing
  documentObjectModel = etree.HTML(str(Scraping)) 
  return (documentObjectModel.xpath('# //*[@id="block-fs-uswds-mainpagecontent"]/article/div/div/div/div/div/div[2]/div[2]/div/div/dl/dd[1]/div/dl/dd[36]/table/tbody/tr[1]/td[1]/strong')[0].text)
URL = "https://www.fs.usda.gov/managing-land/urban-forests/ucf/2023-grant-funding"
print(Xpath(URL))



# //*[@id="block-fs-uswds-mainpagecontent"]/article/div/div/div/div/div/div[2]/div[2]/div/div/dl/dd[1]/div/dl/dd[36]/table/tbody/tr[1]/td[1]/strong