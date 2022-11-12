from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import *


class TestConstructorPage:

    def test_constructor_page_scroll_to_sauce_successful_update_sauce_selector(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        selected_ingredient_before_scroll = driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_SELECTED_INGREDIENT)

        # Scroll from buns to sauces
        spicy_sauce_img = driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_SPICY_SAUCE_IMG)
        driver.execute_script("arguments[0].scrollIntoView();", spicy_sauce_img)
        WebDriverWait(driver, 3)

        selected_ingredient_after_scroll = driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_SELECTED_INGREDIENT)

        assert selected_ingredient_before_scroll.text == 'Булки'
        assert selected_ingredient_after_scroll.text == 'Соусы'

        driver.quit()

    def test_constructor_page_click_bun_link_successful_scroll_to_buns(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_SAUCE_DIV).click()
        WebDriverWait(driver, 3)

        selected_ingredient_before_click = driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_SELECTED_INGREDIENT)

        driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_BUN_DIV).click()
        WebDriverWait(driver, 3)

        selected_ingredient_after_click = driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_SELECTED_INGREDIENT)

        assert selected_ingredient_before_click.text == 'Соусы'
        assert selected_ingredient_after_click.text == 'Булки'

        driver.quit()

    def test_constructor_page_click_filling_link_successful_scroll_to_filling(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.nomoreparties.site")

        selected_ingredient_before_click = driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_SELECTED_INGREDIENT)

        driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_FILLING_DIV).click()
        WebDriverWait(driver, 3)

        selected_ingredient_after_click = driver.find_element(By.XPATH, CONSTRUCTOR_PAGE_SELECTED_INGREDIENT)

        assert selected_ingredient_before_click.text == 'Булки'
        assert selected_ingredient_after_click.text == 'Начинки'

        driver.quit()





