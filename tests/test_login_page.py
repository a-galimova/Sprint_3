from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *


class TestLoginPage:

    def test_login_form_successful_login_from_main_page(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.XPATH, MAIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_PAGE_LOGIN_BUTTON)))

        # Filling login form
        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys("a_galimova_1000@yandex.ru")
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys("abc123")
        driver.find_element(By.XPATH, LOGIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

        order_button = driver.find_element(By.XPATH, MAIN_PAGE_ORDER_BUTTON)
        assert order_button.is_displayed()

        driver.quit()

    def test_login_form_successful_login_from_account_button(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.LINK_TEXT, "Личный Кабинет").click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_PAGE_LOGIN_BUTTON)))

        # Filling login form
        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys("a_galimova_1000@yandex.ru")
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys("abc123")
        driver.find_element(By.XPATH, LOGIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

        order_button = driver.find_element(By.XPATH, MAIN_PAGE_ORDER_BUTTON)
        assert order_button.is_displayed()

        driver.quit()

    def test_login_form_successful_login_from_registration_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        driver.find_element(By.LINK_TEXT, "Войти").click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_PAGE_LOGIN_BUTTON)))

        # Filling login form
        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys("a_galimova_1000@yandex.ru")
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys("abc123")
        driver.find_element(By.XPATH, LOGIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

        order_button = driver.find_element(By.XPATH, MAIN_PAGE_ORDER_BUTTON)
        assert order_button.is_displayed()

        driver.quit()

    def test_login_form_successful_login_from_forgot_password_form(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

        driver.find_element(By.LINK_TEXT, "Войти").click()
        WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, LOGIN_PAGE_LOGIN_BUTTON)))

        # Filling login form
        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys("a_galimova_1000@yandex.ru")
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys("abc123")
        driver.find_element(By.XPATH, LOGIN_PAGE_LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.url_changes("https://stellarburgers.nomoreparties.site/login"))

        order_button = driver.find_element(By.XPATH, MAIN_PAGE_ORDER_BUTTON)
        assert order_button.is_displayed()

        driver.quit()




