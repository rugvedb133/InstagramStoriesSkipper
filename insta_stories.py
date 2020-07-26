from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as b
import time
import sys

username= #username
password= #password

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()

print('loggin in')
chrome_browser.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
uid = WebDriverWait(chrome_browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(2) > div > label > input')))
uid.click()
uid.send_keys(username)
pswd = chrome_browser.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(3) > div > label > input')
pswd.click()
pswd.send_keys(password)
btn = chrome_browser.find_element_by_css_selector('#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(4)')
btn.click()
time.sleep(5)

print('getting homepage')
chrome_browser.get('https://www.instagram.com/')
try:
	not_now=WebDriverWait(chrome_browser, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]')))
	not_now.click()
except:
	pass

print('getting stories')
first_story=WebDriverWait(chrome_browser, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/section/div/div[1]/div/div/div/div/ul/li[4]/div/button')))
first_story.click()
time.sleep(5)

print('clicking next')
clickC=0
errorC=0
errorL=[]
for i in range(300):
	try:
		next_button=WebDriverWait(chrome_browser, 10). until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/div/div/section/div[2]/button[2]')))
		next_button.click()
		clickC+=1
	except:
		errorC+=1
		errorL.append(sys.exc_info()[0])

print(f'clicked next on {clickC} stories')
print(f'{errorC} errors occurred')
