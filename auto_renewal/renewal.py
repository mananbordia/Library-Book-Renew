from datetime import datetime
from selenium import webdriver
import auto_renewal.logUtil as logUtil
from webdriver_manager.chrome import ChromeDriverManager
import os


def auto_renewal_func(userid, password):
    logger = logUtil.getLogUtil()

    # driver_options = webdriver.ChromeOptions()
    # driver_options.add_argument("headless")

    # driver_path = "chromedriver"
    # print(driver_path)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # driver = webdriver.Chrome(driver_path)

    driver.maximize_window()

    # driver = webdriver.Chrome(driver_path, options= driver_options)

    logger.info("WebDriver Started")
    logger.info("Connecting to Library Page")

    libserv_url = "http://libserv.iitk.ac.in"
    try:
        driver.get(libserv_url)
        logger.info("Connected to Library Page Successfully")
        driver.execute_script("window.scrollTo(0, 300)")

        logger.info("Logging in using userid and password")

        try:
            xpath_login_field = '//*[@id="userid"]'
            driver.find_element_by_xpath(xpath=xpath_login_field).send_keys(userid)
            xpath_password_field = '//*[@id="password"]'
            driver.find_element_by_xpath(xpath=xpath_password_field).send_keys(password)

            xpath_login_button = '//*[@id="auth"]/fieldset/fieldset/input'
            driver.find_element_by_xpath(xpath=xpath_login_button).click()

            driver.execute_script("window.scrollTo(0, 300)")
            logger.info("Logged in Successfully")

            xpath_renew_all_button = '//*[@id="renewall"]/input[4]'
            driver.find_element_by_xpath(xpath=xpath_renew_all_button).click()
            driver.execute_script("window.scrollTo(0, 300)")

            logger.info("Capturing screenshot.")

            cwd = os.getcwd()
            screenshot_file_path = cwd + "/screenshots/captureAt-" + datetime.now().strftime("%m-%d-%Y-%H-%M-%S") + ".png"
            driver.get_screenshot_as_file(screenshot_file_path)
            logger.info("Screenshot captured and saved at path : " + screenshot_file_path)
            logger.info("Logging out")
            xpath_logout = '//*[@id="logout"]'
            driver.find_element_by_xpath(xpath=xpath_logout).click()
            logger.info("Logged out Successfully")
        except:
            logger.info("Something went wrong")

        logger.info("Closing WebDriver")
        driver.close()
        logger.info("WebDriver closed")
    except:
        logger.error("Could not connect to Library Page")
