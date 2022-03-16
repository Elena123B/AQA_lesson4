
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

## ////////////////////////////////////////
# # 1. Регистрация аккаунта
# # 1) Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
#
# # 2) Нажмите на вкладку "My Account Menu"
# # #menu-item-50 > a
# MyAcc_tab = driver.find_element_by_css_selector("#menu-item-50 > a")
# MyAcc_tab.click()
# time.sleep(3)
#
# # 3) В разделе " Register", введите email для регистрации
# Email_textarea = driver.find_element_by_id("reg_email")
# Email_textarea.send_keys("elenabudkina@yandex.ru")
# time.sleep(3)
#
# # 4) В разделе " Register", введите пароль для регистрации
# PassWd_textarea = driver.find_element_by_id("reg_password")
# PassWd_textarea.send_keys("ElenaBudkina12345")
# time.sleep(3)
#
# # 5) Нажмите на кнопку "Register"
# # .woocomerce-FormRow.form-row > input:nth-child(3)
# RegBtn = driver.find_element_by_css_selector(".woocomerce-FormRow.form-row > input:nth-child(3)")
# RegBtn.click()
# time.sleep(3)

## ////////////////////////////////////////
# 2. Логин в систему
# 1) Откройте http://practice.automationtesting.in/
driver.get("http://practice.automationtesting.in/")

# 2) Нажмите на вкладку "My Account Menu"
# //li[@id='menu-item-50']/a
MyAccount_lnk = driver.find_element_by_xpath("//li[@id='menu-item-50']/a")
MyAccount_lnk.click()
time.sleep(3)

# 3) В разделе "Login", введите email для логина
email_textarea = driver.find_element_by_id("username")
email_textarea.send_keys("elenabudkina@yandex.ru")

# 4) В разделе "Login", введите пароль для логина
passWD_textarea = driver.find_element_by_id("password")
passWD_textarea.send_keys("ElenaBudkina12345")

# 5) Нажмите на кнопку "Login"
# .form-row > input:nth-child(3)
LoginBtn = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
LoginBtn.click()
time.sleep(3)

# 6) Добавьте проверку, что на странице есть элемент "Logout"
Logout_linktext = driver.find_element_by_link_text("Logout")
# NoSuchElementException
if Logout_linktext == 'NoSuchElementException':
    print("Logout is not on the page")
else:
    print("Logout is exist on the page")

## ////////////////////////////////////////

driver.quit()