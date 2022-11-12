from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *


class TestAccountPage:

    def test_account_page_click_account_link_on_the_main_page_successful_redirect(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Login
        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys("a_galimova_1000@yandex.ru")
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys("abc123")
        driver.find_element(By.XPATH, LOGIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ACCOUNT_PAGE_SAVE_BUTTON)))

        dave_button = driver.find_element(By.XPATH, ACCOUNT_PAGE_SAVE_BUTTON)
        assert dave_button.is_displayed()

        driver.quit()

    def test_account_page_click_constructor_link_from_account_page_successful_redirect_to_main_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Login
        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys("a_galimova_1000@yandex.ru")
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys("abc123")
        driver.find_element(By.XPATH, LOGIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ACCOUNT_PAGE_SAVE_BUTTON)))

        driver.find_element(By.LINK_TEXT, "Конструктор").click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/account/profile"))

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_account_page_click_logo_from_account_page_successful_redirect_to_main_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Login
        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys("a_galimova_1000@yandex.ru")
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys("abc123")
        driver.find_element(By.XPATH, LOGIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ACCOUNT_PAGE_SAVE_BUTTON)))

        driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/account/profile"))

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/'

        driver.quit()

    def test_account_page_log_out_from_account_page_successful_redirect_to_login_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/login")

        # Login
        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys("a_galimova_1000@yandex.ru")
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys("abc123")
        driver.find_element(By.XPATH, LOGIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ACCOUNT_PAGE_SAVE_BUTTON)))

        driver.find_element(By.XPATH, ACCOUNT_LOG_OUT_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/account/profile"))

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()





