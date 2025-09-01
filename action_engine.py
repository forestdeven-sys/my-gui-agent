import re
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

# A global variable to hold the WebDriver instance
driver: WebDriver = None

def open_chrome_and_go_to(url: str):
    """Opens a Chrome browser and navigates to the specified URL."""
    global driver
    if driver is None:
        # This setup assumes chromedriver is in the PATH or uses a manager
        try:
            driver = webdriver.Chrome()
        except Exception as e:
            print(f"Please install chromedriver. Error: {e}")
            return
    driver.get(url)
    time.sleep(2) # Wait for page to load

def find_element_by_id_and_click(element_id: str):
    """Finds an element by its ID and clicks it."""
    if driver is None:
        print("Browser not open.")
        return
    try:
        element = driver.find_element(By.ID, element_id)
        element.click()
        time.sleep(1)
    except Exception as e:
        print(f"Could not find or click element with ID '{element_id}': {e}")

def find_element_by_id_and_type(element_id: str, text_to_type: str):
    """Finds an element by its ID and types text into it."""
    if driver is None:
        print("Browser not open.")
        return
    try:
        element = driver.find_element(By.ID, element_id)
        element.send_keys(text_to_type)
        time.sleep(1)
    except Exception as e:
        print(f"Could not find or type in element with ID '{element_id}': {e}")

def find_element_by_xpath_and_click(xpath: str):
    """Finds an element by its XPath and clicks it."""
    if driver is None:
        print("Browser not open.")
        return
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.click()
        time.sleep(1)
    except Exception as e:
        print(f"Could not find or click element with XPath '{xpath}': {e}")

def find_element_by_xpath_and_type(xpath: str, text_to_type: str):
    """Finds an element by its XPath and types text into it."""
    if driver is None:
        print("Browser not open.")
        return
    try:
        element = driver.find_element(By.XPATH, xpath)
        element.send_keys(text_to_type)
        time.sleep(1)
    except Exception as e:
        print(f"Could not find or type in element with XPath '{xpath}': {e}")

def close_browser():
    """Closes the browser."""
    global driver
    if driver:
        driver.quit()
        driver = None

def execute_plan(plan: str):
    """
    Parses a numbered list of instructions and executes them using Selenium.
    """
    # Simple parsing of a numbered list
    steps = [step.strip() for step in plan.strip().split('\n') if re.match(r'^\d+\.', step.strip())]

    for i, step in enumerate(steps):
        print(f"Executing step {i+1}: {step}")
        # This is a very basic and brittle parser. A real agent would need something more robust.
        try:
            instruction = re.sub(r'^\d+\.\s*', '', step).lower()

            if instruction.startswith("open chrome and go to"):
                url = re.search(r'"(.*?)"', instruction).group(1)
                open_chrome_and_go_to(url)
            elif instruction.startswith("find element by id") and "and click" in instruction:
                element_id = re.search(r'"(.*?)"', instruction).group(1)
                find_element_by_id_and_click(element_id)
            elif instruction.startswith("find element by id") and "and type" in instruction:
                element_id = re.search(r'id "(.*?)"', instruction).group(1)
                text = re.search(r'type "(.*?)"', instruction).group(1)
                find_element_by_id_and_type(element_id, text)
            elif instruction.startswith("find element by xpath") and "and click" in instruction:
                xpath = re.search(r'"(.*?)"', instruction).group(1)
                find_element_by_xpath_and_click(xpath)
            elif instruction.startswith("find element by xpath") and "and type" in instruction:
                xpath = re.search(r'xpath "(.*?)"', instruction).group(1)
                text = re.search(r'type "(.*?)"', instruction).group(1)
                find_element_by_xpath_and_type(xpath, text)
            else:
                print(f"Unknown instruction: {instruction}")
        except Exception as e:
            print(f"Error executing step '{step}': {e}")
            break # Stop execution on error

    print("Plan execution finished. Closing browser.")
    close_browser()
