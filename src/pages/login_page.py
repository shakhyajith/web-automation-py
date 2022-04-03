from lib2to3.pgen2 import driver
from src.utils.driver_manager import DriverManager


class LoginPage:
    dm = DriverManager()
    driver = None

    def __init__(self, driver) -> None:
        self.driver = driver

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
