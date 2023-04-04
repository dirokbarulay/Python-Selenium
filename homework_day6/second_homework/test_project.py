from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from pathlib import Path
from datetime import date
import openpyxl
from constants.globalConstants import *

class Test_Project:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get(sauce_Url)
        
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)
        
    def teardown_method(self):
        self.driver.quit()
        
    def login(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
    #hatalı giriş
    def test_error_login(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("")
        passwordInput.send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        
        self.driver.find_elements(By.CLASS_NAME, "svg-inline--fa fa-times-circle fa-w-16 error_icon")
        self.driver.save_screenshot(f"{self.folderPath}/test-icon.png")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button").click()
            
    #sepete ürün ekleme, sepete gitme ve ürün silme
    def test_shopping_cart_container(self):
        self.login()
        
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.save_screenshot(f"{self.folderPath}/test-add-product.png")
        
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click() #btnShppingCartContainer
        self.driver.save_screenshot(f"{self.folderPath}/test-shopping-cart-container.png")
        
        #self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
        #self.driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirtt").click()
        #self.driver.save_screenshot(f"{self.folderPath}/test-remove-product.png")
        
    #continue shopping butonu kontrol etme
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])    
    def test_continue_shopping(self, username, password):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password)
        
        self.driver.find_element(By.ID, "login-button").click()
        
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click() #btnShppingCartContainer
        self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
        
        self.driver.save_screenshot(f"{self.folderPath}/test-continue-shopping.png")
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[1]").click() #btnContinueShopping
        
    #checkout butonu çalışıyor mu?
    #Çalışıyorsa cancel butonunu kontrol et ve anasayfaya dön
    def test_checkoutBtn(self):
        self.login()
        
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click() #btnShppingCartContainer
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]").click() #btnCheckout
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/button").click() #btnCancel
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[1]").click() #btnContinueShopping
        
    #checkout butonu ile açılan sayfada tüm bilgilerin boş bırakılması
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])
    def test_null_all_information(self, username, password):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password)
        
        self.driver.find_element(By.ID, "login-button").click()
        
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click() #btnShppingCartContaier
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]").click() #btnCheckout
        
        firstName = self.driver.find_element(By.ID, "first-name")
        lastName = self.driver.find_element(By.ID, "last-name")
        postalCode = self.driver.find_element(By.ID, "postal-code")
        firstName.send_keys("")
        lastName.send_keys("")
        postalCode.send_keys("")
        
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input").click() #btnContinue
        
        error = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-null-all-information.png")
        assert error.text == null_name_error
        
    #Checkout ile açılan sayfada sadece postal code boş bırakılması
    def test_null_postalCode(self):
        self.login()
        
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[1]/div[3]/a").click() #btnShppingCartContaier
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/div[2]/button[2]").click() #btnCheckout
        
        firstName = self.driver.find_element(By.ID, "first-name")
        lastName = self.driver.find_element(By.ID, "last-name")
        postalCode = self.driver.find_element(By.ID, "postal-code")
        firstName.send_keys("kullaniciAdi")
        lastName.send_keys("kullanici123")
        postalCode.send_keys("")
        
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div/form/div[2]/input").click() #btnContinue
        
        error = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/div/form/div[1]/div[4]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-null-postalCode.png")
        assert error.text == null_postalCode_error
        
    # Yandan açılır menü butonunu açma
    def test_react_menu(self):
        self.login()
        
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        sleep(3)
        self.driver.save_screenshot(f"{self.folderPath}/test-react-menu.png")
                #self.driver.find_element(By.ID, "react-burger-menu-cross-btn").click()

    
    
    #react burger menu butonun logout_link ile çıkış yapma
    def test_logout(self):
        self.login()
        
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        self.driver.save_screenshot(f"{self.folderPath}/test-logout.png")
        
    #sosyal medya butonlarını kontrol etme        
    def test_socialMedia(self):
        self.login()
        
        for i in socialMedia_links:
            self.driver.find_element(By.XPATH,i).click()
            self.driver.save_screenshot(f"{self.folderPath}/test-socialMedia.png")
