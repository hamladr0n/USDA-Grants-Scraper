# Import Required Modules
from bs4 import BeautifulSoup
import requests

# HTML Code
html_content = """
<ul>
<li>Coffee</li>
<li>Tea</li>
<li>Milk</li>
</ul>
"""

data_list = []

url = "https://www.fs.usda.gov/managing-land/urban-forests/ucf/2023-grant-funding"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# Parse the html content
# soup = BeautifulSoup(html_content, "lxml")

# print(soup.prettify())


data_list = soup.find_all("table"

# for data in data_list:
#     print(data.text)
    
# print(f"Total {len(data_list)} strong tag found")

print(data_list)

# Loop through the rows and columns to extract data
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all(['th', 'tr', 'td')]):
        row_data.append(cell.text.strip())
    data_list.append(row_data)

# Convert the list of lists into a DataFrame
df = pd.DataFrame(data_list[1:], columns=data_list[0])

# Save the DataFrame to a CSV file
df.to_csv('usda_urban_forestry_grants.csv', index=False)

# # Find all li tag
# datas = soup.find_all("td")

# print(datas)

# # Iterate through all li tags
# for data in datas:
# 	# Get text from each tag
# 	print(data.text)

# print(f"Total {len(datas)} strong tag found")
