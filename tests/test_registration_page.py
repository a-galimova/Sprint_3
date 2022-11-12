from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *


class TestRegistrationPage:

    def test_registration_form_successful_registration(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Filling registration form
        driver.find_element(By.XPATH, REGISTRATION_FORM_NAME_INPUT).send_keys("Anastasia")
        driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_INPUT).send_keys("a_galimova_1008@yandex.ru")
        driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_PASSWORD).send_keys("abc123")
        driver.find_element(By.XPATH, REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM_HEADER)))

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/login'

        driver.quit()

    def test_registration_form_empty_name_unsuccessful_registration(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Filling registration form
        driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_INPUT).send_keys("a_galimova_1007@yandex.ru")
        driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_PASSWORD).send_keys("abc123")
        driver.find_element(By.XPATH, REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3)

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/register'

        driver.quit()

    def test_registration_form_invalid_email_format_unsuccessful_registration(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Filling registration form
        driver.find_element(By.XPATH, REGISTRATION_FORM_NAME_INPUT).send_keys("Anastasia")
        driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_INPUT).send_keys("invalid_email")
        driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_PASSWORD).send_keys("abc123")
        driver.find_element(By.XPATH, REGISTRATION_FORM_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, REGISTRATION_FORM_ERROR_MESSAGE)))

        error_message = driver.find_element(By.XPATH, REGISTRATION_FORM_ERROR_MESSAGE)
        assert error_message.text == 'Такой пользователь уже существует'

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/register'

        driver.quit()

    def test_registration_form_invalid_password_unsuccessful_registration(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site/register")

        # Filling registration form
        driver.find_element(By.XPATH, REGISTRATION_FORM_NAME_INPUT).send_keys("Anastasia")
        driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_INPUT).send_keys("a_galimova_1007@yandex.ru")
        driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_PASSWORD).send_keys("1")
        driver.find_element(By.XPATH, REGISTRATION_FORM_BUTTON).click()

        error_message = driver.find_element(By.XPATH, REGISTRATION_FORM_ERROR_MESSAGE)
        assert error_message.text == "Некорректный пароль"

        current_url = driver.current_url
        assert current_url == 'https://stellarburgers.nomoreparties.site/register'

        driver.quit()

