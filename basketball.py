from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd
import re

url = "https://static.bearcatsports.com/custompages/stats/mbb/2020-21/teamcume.htm"
season_box_score_xpath = "/html/body/pre[2]/font"
season_box_score_xpath2 = "/html/body/pre[3]/font"

webdriver_path = r"C:\Users\S542403\Downloads\geckodriver.exe"
driver = webdriver.Firefox(executable_path=webdriver_path)

driver.get(url)
sleep(2)
assert "Northwest Mo. St. - Season Statistics" in driver.title

elem = driver.find_element_by_xpath(season_box_score_xpath)

val = elem.text

elem2 = driver.find_element_by_xpath(season_box_score_xpath2)
val2 = elem2.text
driver.quit()

text_data2 = val2.split('\n')
text_data2.pop(0)
text_data2.pop(1)
text_data2.pop(29)
text_data2.pop(31)

text_data = val.split('\n')
text_data.pop(0)
text_data.pop(1)
text_data.pop(29)
text_data.pop(31)
#print(text_data)

header_text = text_data.pop(0)
header = header_text
header_text2 = text_data2.pop(0)
header2 = header_text2
print(header)
print(header2)
