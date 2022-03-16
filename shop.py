import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)


## ////////////////////////////////////////
# # 1. Отображение страницы товара
# # 1) Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
#
# # 2) Залогиньтесь
# MyAccount_lnk = driver.find_element_by_xpath("//li[@id='menu-item-50']/a")
# MyAccount_lnk.click()
# email_textarea = driver.find_element_by_id("username")
# email_textarea.send_keys("elenabudkina@yandex.ru")
# passWD_textarea = driver.find_element_by_id("password")
# passWD_textarea.send_keys("ElenaBudkina12345")
# LoginBtn = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
# LoginBtn.click()
#
# # 3) Нажмите на вкладку "Shop"
# # //li[@id='menu-item-40']/a
# ShopBtn = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
# ShopBtn.click()
# time.sleep(3)
#
# # 4) Откройте книгу "HTML 5 Forms"
# # //ul[@class='products masonry-done']/li[3]/a/h3
# Book_link = driver.find_element_by_xpath("//ul[@class='products masonry-done']/li[3]/a/h3")
# Book_link.click()
# time.sleep(3)
#
# # 5) Добавьте тест, что заголовок книги назвается: "HTML5 Forms"
# # product_title entry-title
# TitleBook = driver.find_element_by_class_name("product_title")
# Ttext = TitleBook.text
# assert Ttext == "HTML5 Forms"

## ////////////////////////////////////////
# # 2. Количество товаров в категории
# # 1) Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
#
# # 2) Залогиньтесь
# MyAccount_lnk = driver.find_element_by_xpath("//li[@id='menu-item-50']/a")
# MyAccount_lnk.click()
# email_textarea = driver.find_element_by_id("username")
# email_textarea.send_keys("elenabudkina@yandex.ru")
# passWD_textarea = driver.find_element_by_id("password")
# passWD_textarea.send_keys("ElenaBudkina12345")
# LoginBtn = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
# LoginBtn.click()
#
# # 3) Нажмите на вкладку "Shop"
# ShopBtn = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
# ShopBtn.click()
# time.sleep(3)
#
# # 4) Откройте категорию "HTML"
# # //ul[@class='product-categories']/li[2]/a
# Category_lnk = driver.find_element_by_xpath("//ul[@class='product-categories']/li[2]/a")
# Category_lnk.click()
# time.sleep(3)
#
# # 5) Добавьте тест, что отображается три товара
# Books = driver.find_elements_by_class_name("product")
# assert len(Books) == 3

## ////////////////////////////////////////
# # 3. Сортировка товаров
# # 1) Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
#
# # 2) Залогиньтесь
# MyAccount_lnk = driver.find_element_by_xpath("//li[@id='menu-item-50']/a")
# MyAccount_lnk.click()
# email_textarea = driver.find_element_by_id("username")
# email_textarea.send_keys("elenabudkina@yandex.ru")
# passWD_textarea = driver.find_element_by_id("password")
# passWD_textarea.send_keys("ElenaBudkina12345")
# LoginBtn = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
# LoginBtn.click()
#
# # 3) Нажмите на вкладку "Shop"
# ShopBtn = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
# ShopBtn.click()
# time.sleep(3)
#
# # 4) Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию (Используйте проверку по value)
# # orderby
# Sort_ = driver.find_element_by_class_name("orderby")
# Val = Sort_.get_attribute("value")
# assert Val == "menu_order"
#
# # 5) Отсортируйте товары по цене от большей к меньшей (в селекторах используйте класс Select)
# # price-desc
# select = Select(Sort_)
# select.select_by_value("price-desc")
#
# # 6) Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
# Sort_default = driver.find_element_by_class_name("orderby")
#
# # 7) Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
# # Используйте проверку по value
#
# Val_2 = Sort_default.get_attribute("value")
# if Val_2 == "price-desc":
#     print("В селекторе выбран вариант сортировки по цене от большей к меньшей")
# else:
#     print("В селекторе выбран иной вариант сортировки")

## ////////////////////////////////////////
# # 4. Отображение, скидка товара
# # 1) Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
#
# # 2) Залогиньтесь
# MyAccount_lnk = driver.find_element_by_xpath("//li[@id='menu-item-50']/a")
# MyAccount_lnk.click()
# email_textarea = driver.find_element_by_id("username")
# email_textarea.send_keys("elenabudkina@yandex.ru")
# passWD_textarea = driver.find_element_by_id("password")
# passWD_textarea.send_keys("ElenaBudkina12345")
# LoginBtn = driver.find_element_by_css_selector(".form-row > input:nth-child(3)")
# LoginBtn.click()
#
# # 3) Нажмите на вкладку "Shop"
# ShopBtn = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
# ShopBtn.click()
# time.sleep(3)
#
# # 4) Откройте книгу "Android Quick Start Guide"
# Book_link = driver.find_element_by_xpath("//ul[@class='products masonry-done']/li[1]/a/h3")
# Book_link.click()
# time.sleep(3)
#
# # 5) Добавьте тест, что содержимое старой цены = ₹600.00  # используйте assert
# # .price > del > span
# Old_price = driver.find_element_by_css_selector(".price > del > span")
# Text_price = Old_price.text
# assert Text_price == "₹600.00"
#
# # 6) Добавьте тест, что содержимое новой цены = ₹450 .00   # используйте assert
# New_price = driver.find_element_by_css_selector(".price > ins > span")
# Text_price2 = New_price.text
# assert Text_price2 == "₹450.00"
#
# # 7) Добавьте явное ожидание и нажмите на обложку книги
# # Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
# # .images > a
# Image_big = WebDriverWait(driver, 40).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a"))
# )
# Image_big.click()
# time.sleep(5)
#
# # 8) Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа)
# # pp_close
# Close_Img = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))
# )
# Close_Img.click()
# time.sleep(5)

## ////////////////////////////////////////
# # 5. Проверка цены в корзине
# # 1) Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
#
# # 2) Нажмите на вкладку "Shop"
# ShopBtn = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
# ShopBtn.click()
# time.sleep(3)
#
# # 3) Добавьте в корзину книгу "HTML5 WebApp Development"
# # .post-182 > a:nth-child(2)
# Book_addToBasket = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)")
# Book_addToBasket.click()
# time.sleep(2)
#
# # 4) Добавьте тест , что возле коризны(вверху справа) количество товаров = 1 Item"Item", а стоимость = ₹180.00 "
# # Используйте для проверки assert
# # .wpmenucart-contents > .cartcontents; amount
# Item_inBasket = driver.find_element_by_css_selector(".wpmenucart-contents > .cartcontents")
# Text_Item = Item_inBasket.text
# assert Text_Item == "1 Item"
# Price_inBasket = driver.find_element_by_css_selector(".wpmenucart-contents > .amount")
# Text_Price = Price_inBasket.text
# assert Text_Price == "₹180.00"
#
# # 5) Перейдите в корзину
# GoToBasket = driver.find_element_by_css_selector(".post-182 > a:nth-child(3)")
# GoToBasket.click()
# time.sleep(4)
#
# # 6) Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
# # .cart-subtotal >td> .woocommerce-Price-amount
# Subtotal_Price = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".cart-subtotal >td"), "₹180.00")
# )
# assert Subtotal_Price is True
#
# # 7) Используя явное ожидание, проверьте что в Total отобразилась стоимость
# # .order-total > td
# Total_Price = WebDriverWait(driver, 20).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total > td"), "₹189.00")
# )
# assert Total_Price is True

## ////////////////////////////////////////
# 6. Работа в корзине
# # 1) Откройте http://practice.automationtesting.in/
# driver.get("http://practice.automationtesting.in/")
#
# # 2) Нажмите на вкладку "Shop"
# ShopBtn = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
# ShopBtn.click()
#
# # 3) Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
# # Перед добавлением первой книги, проскролльте вниз на 300 пикселей
# # После добавления 1 й книги добавьте sleep
# driver.execute_script("window.scrollBy(0, 300);")
# Book1_addToBasket = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)")
# Book1_addToBasket.click()
# time.sleep(3)
# Book2_addToBasket = driver.find_element_by_css_selector(".post-180 > a:nth-child(2)")
# Book2_addToBasket.click()
#
# # 4) Перейдите в корзину
# Basket = driver.find_element_by_id("wpmenucartli")
# Basket.click()
#
# # 5) Удалите первую книгу
# # Перед удалением добавьте sleep
# time.sleep(5)
# DeleteFirstBook = driver.find_element_by_css_selector(".product-remove > a:nth-child(1)")
# DeleteFirstBook.click()
#
# # 6) Нажмите на Undo (отмена удаления)
# Undo_link = driver.find_element_by_css_selector(".woocommerce-message > a")
# Undo_link.click()
#
# # 7) В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and
# # Предварительно очистите поле с помощью локатор_поля .clear()
# JS_Book = driver.find_element_by_css_selector(".quantity > input:nth-child(1)")
# JS_Book.clear()
# JS_Book.send_keys(3)
#
# # 8) Нажмите на кнопку "UPDATE BASKET"
# UpdateBasketBtn = driver.find_element_by_css_selector(".actions>input")
# UpdateBasketBtn.click()
#
# # 9) Добавьте тест, что value элемента quantity для "JS Data Structures and равно 3   # используйте assert
# JS_Book3 = driver.find_element_by_css_selector(".product-quantity > div > input:nth-child(1)")
# val = JS_Book3.get_attribute("value")
# assert val == "3"
#
# # 10) Нажмите на кнопку "APPLY COUPON"
# # Перед нажатимем добавьте sleep
# time.sleep(4)
# CouponBtn = driver.find_element_by_css_selector(".coupon > input:nth-child(3)")
# CouponBtn.click()
#
# # 11) Добавьте тест, что возникло сообщение : "Please enter a coupon code"
# ErrorMessage = driver.find_element_by_class_name("woocommerce-error")
# TextMessage = ErrorMessage.text
# assert TextMessage == "Please enter a coupon code."

## ////////////////////////////////////////
# 7. Покупка товара
# 1) Откройте http://practice.automationtesting.in/   # в этом тесте логиниться не нужно
driver.get("http://practice.automationtesting.in/")

# 2) Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
ShopBtn = driver.find_element_by_xpath("//li[@id='menu-item-40']/a")
ShopBtn.click()
driver.execute_script("window.scrollBy(0, 300);")

# 3) Добавьте в корзину книгу "HTML5 WebApp Development"
Book_addToBasket = driver.find_element_by_css_selector(".post-182 > a:nth-child(2)")
Book_addToBasket.click()

# 4) Перейдите в корзину
GoToBasket = driver.find_element_by_css_selector(".post-182 > a:nth-child(3)")
GoToBasket.click()

# 5) Нажмите "PROCEED TO CHECKOUT"
# Перед нажатием, добавьте явное ожидание
ProceedBtn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".wc-proceed-to-checkout > a"))
)
ProceedBtn.click()

# 6) Заполните все обязательные поля
PlaceOrder_Btn = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "alt"))
)
FN = driver.find_element_by_css_selector(".col-1 > div > p > input")
FN.send_keys("Elena")
LN = driver.find_element_by_css_selector(".col-1 > div > p:nth-child(3) > input")
LN.send_keys("Budkina")
Email = driver.find_element_by_css_selector(".col-1 > div > p:nth-child(6) > input")
Email.send_keys("elenabudkina@yandex.ru")
Phone = driver.find_element_by_css_selector(".col-1 > div > p:nth-child(7) > input")
Phone.send_keys("12345678901")
# Country = driver.find_element_by_class_name("select2-search")
# Country.send_keys("Russia")

Address = driver.find_element_by_css_selector("#billing_address_1_field > #billing_address_1")
Address.send_keys("ул. Ткачёва, д. 13")
City = driver.find_element_by_css_selector("#billing_city_field > #billing_city")
City.send_keys("г. Волгоград")
Country2 = driver.find_element_by_css_selector("#billing_state_field > #billing_state")
Country2.send_keys("Russia")
ZIP = driver.find_element_by_css_selector("#billing_postcode_field > #billing_postcode")
ZIP.send_keys("400087")

# 7) Выберите способ оплаты "Check Payments"
# Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
CheckPay = driver.find_element_by_xpath("//ul[@class='wc_payment_methods payment_methods methods']/li[2]/input")
CheckPay.click()

# 8) Нажмите PLACE ORDER
ProceedBtn = driver.find_element_by_class_name("alt")
ProceedBtn.click()

# 9) Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
Text_1 = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received.")
)
assert Text_1 is True

# 10) Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
# //table[@class='shop_table order_details']/tfoot/tr[3]/td
Text_2 = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.XPATH, "//table[@class='shop_table order_details']/tfoot/tr[3]/td"), "Check Payments")
)
assert Text_2 is True



driver.quit()