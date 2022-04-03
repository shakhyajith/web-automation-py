import unittest
from src.utils.json_reader import JsonReader
from src.utils.driver_manager import DriverManager
from src.pages.login_page import LoginPage


class TestLogin(unittest.TestCase):
    driver_manager = DriverManager()
    json_reader = JsonReader()
    user = json_reader.read_json("user_data", "id", 100)
    login_page = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = cls.driver_manager.get_chrome_driver()
        cls.login_page = LoginPage(cls.driver)

    def test_user_login(self):
        self.login_page.login("standard_user", "secret_sauce")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver_manager.quit_driver()
