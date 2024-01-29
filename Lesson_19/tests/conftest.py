# import pytest
# from selenium import webdriver
#
# @pytest.fixture
# def chrome():
#     driver = webdriver.Chrome(executable_path="chromedriver")
#     yield driver
#     driver.quit()




# from selenium import webdriver
# import pytest
#
# @pytest.fixture
# def chrome():
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("executable_path=/chromedriver")
#     driver = webdriver.Chrome(options=chrome_options)
#     yield driver
#     driver.quit()

import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="Lesson_19/chromedriver")
    yield driver
    driver.quit()