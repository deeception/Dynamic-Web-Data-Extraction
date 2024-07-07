base_url = 'https://www.flipkart.com/'
column_names = ['Sr_No',  'product_name', 'product_url', 'rating', 'price', 'spec', 'category_labels', 'summary', 'full_article', 'sources']
import requests
import bs4
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC#webdriver path. The path where the chromedriver is stored in the system
base_url = 'https://www.flipkart.com/'
chrome_path = 'G:\softwares\chromedriver_win32\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get(base_url)
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()
driver.find_element_by_class_name("_3704LK").send_keys("laptop")
driver.find_element_by_xpath("//button[@class='L0Z3Pu']").submit()
time.sleep(2)
page_source = driver.page_source

soup = bs4.BeautifulSoup(page_source, 'html.parser')
total_search_results = soup.find_all('span',attrs={'class':'_10Ermr'})
print("total search results are ", total_search_results[0].text.split("of")[1].split()[0])
portfolio = soup.find_all('div',attrs={'class':'_2kHMtA'})
len(portfolio)
product_name_finder = portfolio[0].find_all('div',attrs={'class':'_4rR01T'})
price_finder = portfolio[0].find_all('div',attrs={'class':'_30jeq3 _1_WHN1'})
rating_finder = portfolio[0].find_all('div',attrs={'class':'_3LWZlK'})
spec_finder = portfolio[0].find_all('ul',attrs={'class':'_1xgFaf'})
url_finder = portfolio[0].find_all('a',attrs={'class':'_1fQZEK'})


if len(product_name_finder)!=0:
    print(product_name_finder[0].text)
if len(price_finder)!=0:
    print(price_finder[0].text)
if len(rating_finder)!=0:
    print(rating_finder[0].text)
if len(spec_finder)!=0:
    print(spec_finder[0].text)
if len(url_finder)!=0:
    print("https://www.flipkart.com" + url.get('href'))

for i in range(5):

    print("*********", i)

    product_name_finder = portfolio[i].find_all('div', attrs={'class': '_4rR01T'})
    price_finder = portfolio[i].find_all('div', attrs={'class': '_30jeq3 _1_WHN1'})
    rating_finder = portfolio[i].find_all('div', attrs={'class': '_3LWZlK'})
    spec_finder = portfolio[i].find_all('ul', attrs={'class': '_1xgFaf'})
    url_finder = portfolio[i].find_all('a', attrs={'class': '_1fQZEK'})

    if len(product_name_finder) != 0:
        print(product_name_finder[0].text)
    if len(price_finder) != 0:
        print(price_finder[0].text)
    if len(rating_finder) != 0:
        print(rating_finder[0].text)
    if len(spec_finder) != 0:
        print(spec_finder[0].text)
    if len(url_finder) != 0:
        print("https://www.flipkart.com" + url.get('href'))
driver.find_elements_by_class_name("_1LKTO3")



driver.find_element_by_class_name("yFHi8N").click()
time.sleep(2)
import requests
import bs4
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

column_names = ['Sr_No', 'product_name', 'rating', 'price', 'spec', 'product_url']
df = pd.DataFrame(columns=column_names)

k = 0

base_url = 'https://www.flipkart.com/'
chrome_path = 'G:\softwares\chromedriver_win32\chromedriver'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get(base_url)

# let the page load
time.sleep(2)

# closing the login window
driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()

# entering the laptop keyword
driver.find_element_by_class_name("_3704LK").send_keys("laptop")

# submitting the keyword
driver.find_element_by_xpath("//button[@class='L0Z3Pu']").submit()

# let the page load
time.sleep(10)

# get the page source. This way the server will send the complete webpage data to user
page_source = driver.page_source

# parsing the data
soup = bs4.BeautifulSoup(page_source, 'html.parser')

# total number of search results

total_search_results = soup.find_all('span', attrs={'class': '_10Ermr'})
total_products = int(total_search_results[0].text.split("of")[1].split()[0])
print("total search results are ", total_products)
j = 0

while True:

    print("Scraping page number ", j)
    if j == 0:
        page_source = driver.page_source
        time.sleep(10)
        soup = bs4.BeautifulSoup(page_source, 'html.parser')

    else:  # untill we have the next button available
        # clicking on the next button
        if j == 1:
            next_page_number = 0
        elif len(driver.find_elements_by_class_name("_1LKTO3")) == 2:
            next_page_number = 1
        else:
            break

        driver.find_elements_by_class_name("_1LKTO3")[next_page_number].click()
        time.sleep(2)
        page_source = driver.page_source
        time.sleep(10)
        soup = bs4.BeautifulSoup(page_source, 'html.parser')

    j += 1

    # getting the product portfolios of each page
    portfolio = soup.find_all('div', attrs={'class': '_2kHMtA'})

    for i in range(len(portfolio)):
        # getting the required data

        product_name_finder = portfolio[i].find_all('div', attrs={'class': '_4rR01T'})
        price_finder = portfolio[i].find_all('div', attrs={'class': '_30jeq3 _1_WHN1'})
        rating_finder = portfolio[i].find_all('div', attrs={'class': '_3LWZlK'})
        spec_finder = portfolio[i].find_all('ul', attrs={'class': '_1xgFaf'})
        url_finder = portfolio[i].find_all('a', attrs={'class': '_1fQZEK'})

        if len(product_name_finder) != 0:
            product_name = product_name_finder[0].text
        else:
            product_name = "None"
        ######
        if len(price_finder) != 0:
            price = price_finder[0].text
        else:
            rating = "None"
        ######
        if len(rating_finder) != 0:
            rating = rating_finder[0].text
        else:
            rating = "None"
        ######
        if len(spec_finder) != 0:
            spec = spec_finder[0].text
        else:
            spec = "None"
        ######
        if len(url_finder) != 0:
            product_url = "https://www.flipkart.com" + url.get('href')
        else:
            product_url = "None"

        df = df.append({'Sr_No': k,
                        'base_url': base_url,
                        'product_name': product_name,
                        'rating': rating,
                        'price': price,
                        'spec': spec,
                        'product_url': product_url
                        }, ignore_index=True)
        k += 1

df.head()
df.tail()
df.shape
df.to_excel(r'flipkart products.xlsx', index = True)