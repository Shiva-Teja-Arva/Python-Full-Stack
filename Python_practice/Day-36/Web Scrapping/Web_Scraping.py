import requests
from bs4 import BeautifulSoup

url = "https://codegnan.com"
response = requests.get(url)
print(response) # If status code is 200 then we can access the html source code in that website
print(response.status_code)
print(response.text[:500]) # slicing the html element in the source code
soup = BeautifulSoup(response.text, 'html.parser') # Soup object
print(soup.title) # provides the title of that website
print(soup.title.text) # provides the title in text
heading = soup.find_all("a")
for i in heading:
    print(i.text)