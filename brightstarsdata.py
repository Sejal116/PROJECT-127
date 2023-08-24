from bs4 import BeautifulSoup
import time
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

scraped_data = []

# Define Exoplanet Data Scrapping Method
def scrape():
        
        # BeautifulSoup Object     
        soup = BeautifulSoup(browser.page_source, "html.parser")

        bright_star_tables = soup.find("table",attrs = {"class","wikitable"})

        table_body = bright_star_table.find('tbody')           
        table_rows = table_body.find_all("tr")

        for row in table_rows:
            table_cols = row.find_all('td')
            temp_list = []

            for col_data in table_cols:
                data = col_data.text.strip()
                temp_list.append(data)

            scraped_data.append(temp_list)



        browser.find_element(by=By.XPATH, value='//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()

# Calling Method    
scrape()

stars _data = []

for i in range(0,len(scarped_data)):

    Star_names = scarped_data[i][1]
    Distance = scarped_data[i][3]
    Mass = scarped_data[i][5]
    Radius = scarped_data[i][6]
    Lum = scarped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum, stars_data.append(required_data)]

# Define Header
headers = ["Star_name", "Distance", "Mass", "Radius", "Luminosity"]

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(stars_data, columns=headers)

# Convert to CSV
stars_df_1.to_csv('scraped_data.csv',index=True, index_label="id")    