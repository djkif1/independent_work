# import pytest
# from selenium import webdriver
#
# @pytest.fixture
# def chrome():
#     driver = webdriver.Chrome(executable_path="chromedriver")
#     yield driver
#     driver.quit()


import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="Lesson_19/chromedriver")
    yield driver
    driver.quit()