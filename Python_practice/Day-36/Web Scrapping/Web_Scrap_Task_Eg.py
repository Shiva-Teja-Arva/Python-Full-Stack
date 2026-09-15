import requests
from bs4 import BeautifulSoup
import pandas as pd


url="https://timely-sunshine-e821b3.netlify.app/"
# Loading the webpage using requests module
page = requests.get(url)
# Checking the status code
print("Status Code:", page.status_code)
# Parsing the HTML Content if approved
soup = BeautifulSoup(page.text, 'html.parser') # text or content can be used
# Finding all the product items
items = soup.find_all('div',class_='a')
# lists to store the extracted data
names=[]
prices=[]
images=[]
# Loop through each product and extract name, price and image
for item in items:
    name = item.find('div',class_='name').text.strip()
    price = item.find('div',class_='price').text.strip()
    image_tag = item.find('div',class_='image').find('img')
    image_src = image_tag['src'] if image_tag else None

    names.append(name)
    prices.append(price)
    images.append(image_src)
# Creating a Data Frame to store these items in the tabular format
df=pd.DataFrame({'Product Name':names,'Product Price(MRP)':prices,'Image_SRC':images})
# Displaying the Data Frame
print("\n Scrapped Data")
print(df)

# Saving to CSV to download the data
csv_name = "products.csv"
df.to_csv(csv_name, index=False)
print(f"\n CSV File saved as: {csv_name}")