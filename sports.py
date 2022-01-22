import csv

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def chrome_options() -> Options:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    options = Options()
    # Don't change these options
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    return options


options = chrome_options()
driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install(), options=options)
url = "https://www.scrapethissite.com/pages/forms/?q="

driver.get(url)

all_rows = []  # empty list to store all row data

for i in range(3):
    next_page_element = driver.find_element_by_xpath("//span[normalize-space()='»']")
    next_page_element.click()

    # Select all tr(rows) of the table
    for row in driver.find_elements_by_class_name("team"):
        # select all td(columns) of the table
        cells = row.find_elements_by_tag_name("td")

        single_row = []  # empty list to store data of a single row
        for cell in cells:
            single_row.append(cell.text)  # store this row data in single row list

        all_rows.append(single_row)  # store this single row in all row list

driver.quit()

# header name of the csv file
fields = ["Team Name", "Year", "Wins", "Losses", "OT Losses", "Win %", "Goals For(GF)", "Goals Against(GA)", "+/-"]

with open("team_dataset.csv", 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)  # create a row with header names
    write.writerows(all_rows)  # save all_row list in the csv file
