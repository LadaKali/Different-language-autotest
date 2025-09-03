import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.parametrize('language', ["es", "ru", "fr"])
def test_check_the_basket_button(browser, language):
    link = f'https://selenium1py.pythonanywhere.com/{language}/catalogue/hacking-exposed-wireless_208/'
    browser.get(link)
    time.sleep(5)
    button = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    assert button is not None, "No basket button"