import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(name='driver')
def setup_chrome():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    return webdriver.Chrome(service=service)