from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from configuration import config
import datetime
from infrastructure.utilities.base import driver

now = str(datetime.datetime.now()).replace(':', '-')[:-7]
page_img_name = config.img_repository_path + "page-image " + now + " .png"
element_img_name = config.img_repository_path + "element-image " + now + " .png"
action = ActionChains(driver)
wait = WebDriverWait(driver, 5)


def get_element(xpath):
    element = WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.XPATH, xpath)))
    return element


def take_page_screenshot():
    driver.implicitly_wait(3)
    driver.save_screenshot(page_img_name)


def take_element_screenshot(xpath):
    element = get_element(xpath)
    element.screenshot(element_img_name)


def get_text(xpath):
    element = get_element(xpath)
    return element.text


def click(xpath):
    element = get_element(xpath)
    element.click()


def send_text(xpath, text_to_send):
    element = get_element(xpath)
    element.send_keys(text_to_send)


def select_drop_down_by_text(xpath, text_to_select):
    element = get_element(xpath)
    drop = Select(element)
    drop.select_by_visible_text(text_to_select)


def select_drop_down_by_index(xpath, index):
    element = get_element(xpath)
    drop = Select(element)
    drop.select_by_index(index)


def drag_and_drop(source_xpath, target_xpath):
    source_element = get_element(source_xpath)
    target_element = get_element(target_xpath)
    action.drag_and_drop(source_element, target_element).perform()


def mouse_hover(first_xpath, second_xpath):
    first_elem = get_element(first_xpath)
    second_elem = get_element(second_xpath)
    action.move_to_element(first_elem).move_to_element(second_elem).click().perform()


def scroll_to_element(element_xpath):
    element = get_element(element_xpath)
    action.move_to_element(element).perform()
