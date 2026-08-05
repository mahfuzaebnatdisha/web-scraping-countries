from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
driver.get("https://www.scrapethissite.com/pages/simple/")

soup = BeautifulSoup(driver.page_source, "html.parser")
countries = soup.find_all("div", class_="country")

all_countries = []

for c in countries:
    name = c.find("h3", class_="country-name").text.strip()
    capital = c.find("span", class_="country-capital").text
    population = c.find("span", class_="country-population").text
    area = c.find("span", class_="country-area").text
    
    all_countries.append({
        "Name": name,
        "Capital": capital,
        "Population": population,
        "Area (km2)": area
    })

driver.quit()

df = pd.DataFrame(all_countries)
df.to_csv("countries.csv", index=False)
print(f"{len(df)}টা দেশের তথ্য CSV-তে সেভ হয়েছে")