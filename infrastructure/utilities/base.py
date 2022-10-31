from selenium import webdriver
from configuration import config

driver = webdriver.Chrome(executable_path=config.web_driver)


def start_session():
    print("\n------------ STARTING SESSION ------------\n")
    driver.get(config.base_url)
    driver.maximize_window()
    print("\n------------ SESSION STARTED ------------\n")


def close_session():
    print("\n------------ CLOSING SESSION ------------\n")
    driver.quit()
    print("\n------------ SESSION CLOSED ------------")
