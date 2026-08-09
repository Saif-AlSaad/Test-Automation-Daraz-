from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utilities.read_properties import ReadConfig


def test_06_search_product_3(driver):
    driver.get(ReadConfig.get_url())

    search_box = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.send_keys("kids toy")
    search_box.send_keys(Keys.ENTER)

    WebDriverWait(driver, 15).until(EC.url_contains("catalog"))

    assert "catalog" in driver.current_url.lower()