from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec #bekleme işleminin şartı
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date

class Test_Saucedemo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    def teardown_method(self):
        self.driver.quit()
    
    
    def  test_invalid_username_login(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        errorMessage = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-username-login.png")
        assert errorMessage.text == "Epic sadface: Username is required"

    @pytest.mark.parametrize("username",[("Nisan"), ("Kübra"), ("Özlem")])
    def test_invalid_password_login(self, username):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        self.driver.find_element(By.ID, "login-button").click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-invalid-login-{username}.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    
    def test_locked_out_user_login(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        errorMessage = self.driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-locked-out-user-login.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."


    def test_icon(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        self.driver.find_elements(By.CLASS_NAME, "svg-inline--fa fa-times-circle fa-w-16 error_icon")
        self.driver.save_screenshot(f"{self.folderPath}/test-icon.png")
        iconInputBtn = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button").click()


    def test_products_number(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        productsNumber = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        self.driver.save_screenshot(f"{self.folderPath}/test-products-number.png")
        assert len(productsNumber) == 6
        
    @pytest.mark.parametrize("username,password", [("standard_user","secret_sauce")])
    def test_menu_items(self,username,password):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        menuItems = self.driver.find_elements(By.CLASS_NAME, "menu-item")
        self.driver.save_screenshot(f"{self.folderPath}/test-menu-items.png")
        assert len(menuItems) == 4

    
    def test_shopping(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.save_screenshot(f"{self.folderPath}/test-shopping.png")
        
    def waitForElement(self, locator):
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(locator))