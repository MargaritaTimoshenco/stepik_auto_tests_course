from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Создание драйвера браузера
browser = webdriver.Chrome()


link = "http://192.168.4.116:7413/admin3/"
browser.get(link)

    # Ввод логина
login_string = browser.find_element(By.ID, "fw_login_username_id")
login_string.send_keys('admin')

    # Ввод пароля
password_string = browser.find_element(By.XPATH, '//*[@id="fw_login_password_id"]')
password_string.send_keys('12345678')

    # Нажатие на кнопку авторизации
SignIn_button = browser.find_element(By.XPATH, '//*[@id="fw_login_submit"]').click()


    # Ожидание появления элемента строки быстрого поиска
wait = WebDriverWait(browser, 10)
search_string = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="x-auto-126-input"]')))

    # Ввод текста для быстрого поиска
search_string.send_keys('L cnt_7836')

    # Ожидание появления кнопки поиска и нажатие на неё
search_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="x-auto-127"]/div')))
search_button.click()

    # Ожидание завершения операции
time.sleep(5)

# Закрытие браузера

browser.quit()