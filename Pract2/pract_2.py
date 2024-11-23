import requests
from bs4 import BeautifulSoup
import nltk

#To get all the p tags from a webpage
page=requests.get("https://www.rjcollege.edu.in/about-us/")
soup=BeautifulSoup(page.content,'html.parser')
str1=soup.find_all('p')[0].get_text()
print("P tag with Index 0: ",str1)


# Extract text from all <p> tags & Print all the extracted text from the <p> tags
text = [x.get_text() for x in soup.find_all('p')]
print("\nAll P tag contents:")
for p_text in text:
    print(p_text)


nltk.download('punkt')


# Use NLTK to tokenize the text into sentences
joined_text = ' '.join(text)
sentence = nltk.tokenize.sent_tokenize(joined_text)

print("\nSentence Tokenizer: ")
for s in sentence:
    print(s)


page1 = requests.get("https://www.rjcollege.edu.in/pgadmission2022-23/")
soup1 = BeautifulSoup(page1.content, 'html.parser')
table1 = soup1.find('table', id='tablepress-57')
table1


page3 = requests.get('https://www.rjcollege.edu.in/gallery-2023/')
soup3 = BeautifulSoup(page3.content,'html.parser')
image_list=[]
images=soup3.select('img')
for image in images:
    src=image.get('src')
    alt=image.get('alt')
    image_list.append({"src": src, "alt": alt})

for image in image_list:
    print(image)



page4 = requests.get("https://maps2.dcgis.dc.gov/dcgis/rest/services/FEEDS/MPD/MapServer/2")

# Check the status code
if page4.status_code == 200:
    try:
        data_json = page4.json()
        print(type(data_json))  # Should print <class 'dict'> if valid JSON
    except ValueError as e:
        print("Error decoding JSON:", e)
else:
    print(f"Failed to fetch data, status code: {page4.status_code}")
