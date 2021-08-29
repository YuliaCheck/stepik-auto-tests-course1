from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
#browser.execute_script("window.scrollBy(0, 100);") # команда которая проскроллит страницу
browser.find_element_by_xpath("//button[@id='book']").click()

x_element = browser.find_element_by_xpath("//span[@id='input_value']")
x = int(x_element.get_attribute("textContent"))

def calc(x):
  return str(math.log(abs(12*math.sin(int(x))))) # вычисляем x

y = calc(x)
inputField = browser.find_element_by_xpath("//input[@id='answer']") # находим строчку куда вставить ответ
inputField.send_keys(y) # вставляем ответ

browser.find_element_by_xpath("//button[@id='solve']").click()  # Отправляем заполненную форму

browser.quit()


