from bs4 import BeautifulSoup
import requests
from lxml import etree

url="https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"
list_urls=list()
for x in range(1,21):
    new_url=url.replace("_1", "_"+str(x))

    response = requests.get(new_url)
    a_webpage = response.text

    soup = BeautifulSoup(a_webpage, "html.parser")
    # product_info={"pro_url":[],"pro_name":[],"pro_price":[],"pro_rating":[],"pro_no_reviews":[]}

    url_list = soup.find_all(name="a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
    name_list = soup.find_all(name="span",class_="a-size-medium a-color-base a-text-normal")
    price_list = soup.find_all(name='span',class_="a-price-whole")
    pro_rating = soup.find_all(name="span",class_="a-icon-alt")
    pro_no_rev = soup.find_all(name="span",class_="a-size-base s-underline-text")

    # print(url_list)
    if(len(url_list)>0):
        for p in url_list:
            s=str(p.get("href"))
            list_urls.append(s)

# for x in range(len(url_list)):
#         product_info["pro_url"].append(url_list[x].get("href"))
#         product_info["pro_name"].append(name_list[x].text)
#         product_info["pro_price"].append(price_list[x].text)
#         product_info["pro_rating"].append(pro_rating[x].text)
#         product_info["pro_no_reviews"].append(pro_no_rev[x].text)
#

# print(product_info)
print(list_urls)

for pro in list_urls:
    response = requests.get("https://www.amazon.in"+pro)
    pro_webpage = response.text


    soup1 = BeautifulSoup(pro_webpage, "html.parser")
    # dom = etree.HTML(str(soup1))

    desc = soup1.find(name="span", id="productTitle")
    # pro_desc = soup.find(name='span', class_="a-price-whole")
    # pro_asin = soup.find(name="span", class_="a-icon-alt")
    # pro_mnf = print(dom.xpath("//*[@id='search']/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2")[0].text)

    print(desc.text)
    # print(pro_mnf)



