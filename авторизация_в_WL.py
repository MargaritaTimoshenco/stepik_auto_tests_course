from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5) #добавляем ожидание, чтоб все прогрузилось

link = "http://192.168.4.116:7413/admin3/"
browser.get(link)

# Ввод логина
login_string = browser.find_element(By.XPATH, '//*[@id="fw_login_username_id"]')
login_string.send_keys('admin')

# Ввод неверного пароля
password_string = browser.find_element(By.XPATH, '//*[@id="fw_login_password_id"]')
password_string.send_keys('123456789')

# Нажатие на авторизацию
SignIn_button = browser.find_element(By.XPATH, '//*[@id="fw_login_submit"]')
SignIn_button.click()

time.sleep(5)  # Добавила, чтобы увидеть окно предупреждения. Можно убрать.

# Нажатие на "ок" в окне предупреждения
ok_button = browser.find_element(By.XPATH, '//*[@id="x-auto-20"]/tbody/tr[2]/td[2]/em/button')
ok_button.click()

# Ввод верного пароля
password_string = browser.find_element(By.XPATH, '//*[@id="fw_login_password_id"]')
password_string.send_keys('12345678')

# Нажатие на авторизацию
SignIn_button = browser.find_element(By.XPATH, '//*[@id="fw_login_submit"]')
SignIn_button.click()

time.sleep(5)

browser.quit()