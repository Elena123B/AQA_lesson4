
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

## ////////////////////////////////////////
# 1. добавление комментария
# 1) Откройте страницу
driver.get("http://practice.automationtesting.in/")

# 2) Проскролльте страницу вниз на 600 пикселей
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)

# 3) Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# //a[@data-product_id='160']
RM_button = driver.find_element_by_xpath("//a[@data-product_id='160']")
RM_button.click()
time.sleep(3)

# 4) Нажмите на вкладку "REVIEWS"
# .reviews_tab > a
RW_tab = driver.find_element_by_css_selector(".reviews_tab > a")
RW_tab.click()
time.sleep(3)

# 5) Поставьте 5 звёзд
fiveStars = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "star-5"))
)
fiveStars.click()
time.sleep(5)

# 6) Заполните поле "Review" сообщением : "Nice book!"
RW_textarea = driver.find_element_by_id("comment")
RW_textarea.send_keys("Nice book!")
time.sleep(3)

# 7) Заполните поле "Name"
Name_textarea = driver.find_element_by_id("author")
Name_textarea.send_keys("Elena")
time.sleep(3)

# 8) Заполните "Email"
Email_textarea = driver.find_element_by_id("email")
Email_textarea.send_keys("elenabudkina@yandex.ru")
time.sleep(3)

# 9) Нажмите на кнопку "SUBMIT"
SubmitBtn = driver.find_element_by_id("submit")
SubmitBtn.click()
time.sleep(3)

## ////////////////////////////////////////

driver.quit()