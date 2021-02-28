from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")

usr=input("Please enter your kerberos id: ")
pas=input("Please enter your password:  ")

username=driver.find_element_by_id("username")
password=driver.find_element_by_id("password")

username.send_keys(usr)
password.send_keys(pas)

log=driver.find_element_by_id("login")
logText=(log.text).split("\n")
text=logText[3].split(" ")

if text[1] == 'add':
	answer= str(int(text[2])+int(text[4]))
elif text[1] == 'subtract':
	answer= str(int(text[2])-int(text[4]))
elif text[2] == 'first':
	answer= int(text[4])
else:
	answer= int(text[6])

captcha=driver.find_element_by_id("valuepkg3")	
captcha.clear()
captcha.send_keys(answer)

#auto-login
auto=driver.find_element_by_id('loginbtn')
auto.click()

time.sleep(5)