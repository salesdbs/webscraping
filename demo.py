from selenium import webdriver
import os
print(os.environ['SENHA_PKT'])
print(os.environ['EMAIL_PKT'])

SENHA_PKT = os.environ['SENHA_PKT']
EMAIL_PKT = os.environ['EMAIL_PKT']

#webdriver.Chrome("/home/keymaker/git/webscraping/chromedriver")

#Abre Chrome
browser = webdriver.Chrome("/home/keymaker/git/webscraping/chromedriver")
browser.get("https://subscription.packtpub.com/login")

#Login:
input = browser.find_element_by_css_selector("#login-input-email")
input.send_keys(EMAIL_PKT)
input = browser.find_element_by_css_selector("#login-input-password")
input.send_keys(SENHA_PKT)
clicar_login = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[2]/div/form/button[1]")
clicar_login.click()

#TODO: implementa a quebra do "I'm not robot"