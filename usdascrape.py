import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

# Initialize an empty list to store the scraped data
data_list = []

# Define the URL to scrape
url = "https://www.fs.usda.gov/managing-land/urban-forests/ucf/2023-grant-funding"

# Fetch the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Locate the table or section containing the data (This part may need to be adjusted)
# table = soup.find('table', {'class': 'usa-table usa-table--stacked width-full'})
# table = soup.find('div', {'class': 'dialog-off-canvas-main-canvas'})
table = soup.find('dl', {'class': 'ckeditor-accordion'})


print(table)




for row in table.find_all('tr'):
    row_data = []
    
    for cell in row.find_all(['strong']):
        row_data.append(cell.text.strip())
        # print(cell.text.strip())
    for cell in row.find_all(['li']):
        row_data.append(cell.text.strip())
    
    
    
    data_list.append(row_data)
    # print(row)
        
print(data_list[0:])

# code it to write the data_list[] to a csv file

with open('usda.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    for row in data_list:
        writer.writerow(row) 
        

        



