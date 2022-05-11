from time import strftime
from selenium import webdriver
from datetime import  datetime
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_experimental_option("excludeSwitches", ['enable-automation']);
#option.add_argument("--headless") Use this and the following option to run Headless
#option.add_argument("disable-gpu")
browser = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver', options=option)

browser.get("Your google form link")
 
inputBoxes = browser.find_elements_by_class_name("Main element class name (for more info, see selenium docs)")

date = datetime.now()
currentDate= date.strftime("%d")
currentMonth= date.strftime("%m")
# email
inputBoxes[0].send_keys("cristovao.teles.farias@gmail.com")
# Date
inputBoxes[1].send_keys(currentDate)
# Month
inputBoxes[2].send_keys(currentMonth)
# hours
inputBoxes[3].send_keys("08")
# hours
inputBoxes[4].send_keys("00")
# Project
inputBoxes[5].send_keys("Empresa Sciensa - Magnum bank app")
 