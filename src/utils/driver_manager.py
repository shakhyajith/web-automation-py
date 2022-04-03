from selenium import webdriver
import os
from selenium.webdriver.chrome.service import Service
from src.utils.config_reader import ConfigReader


class DriverManager:
    __cr = ConfigReader()
    __driver = None
    __cwd = os.getcwd()
    __driver_path = os.path.dirname(__cwd) + "/" + __cr.read_config("drivers.dir")

    def get_chrome_driver(self):
        chrome_driver_path = self.__driver_path + "/" + "chromedriver"
        service = Service(chrome_driver_path)

        if self.__driver is None:
            self.__driver = webdriver.Chrome(service=service)

        self.__driver.maximize_window()
        return self.__driver

    def quit_driver(self):
        if self.__driver is not None:
            self.__driver.quit()
            self.__driver = None
