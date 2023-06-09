from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

class Test_Saucedemo:
    def  test_invalid_username_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(20)


    def test_invalid_password_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("Sabahattin Ali")
        passwordInput.send_keys("")
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")
        sleep(20)

    
    def test_locked_out_user_login(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("locked_out_user")
        sleep(2)
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        errorMessage = driver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage == "Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")
        sleep(20)


    def test_icon(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("")
        passwordInput.send_keys("")
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)

        iconInput = driver.find_elements(By.CLASS_NAME, "svg-inline--fa fa-times-circle fa-w-16 error_icon")
        iconInputBtn = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
        iconInputBtn.click()
        sleep(20)


    def test_products_number(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)

        usernameInput = driver.find_element(By.ID, "user-name")
        passwordInput = driver.find_element(By.ID, "password")
        sleep(2)

        usernameInput.send_keys("standard_user")
        sleep(2)
        passwordInput.send_keys("secret_sauce")
        sleep(2)

        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(2)
        
        productsNumber = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Ürün Sayısı: {len(productsNumber)}")
        sleep(20)



testClass = Test_Saucedemo()
#testClass.test_invalid_username_login()
#testClass.test_invalid_password_login()
#testClass.test_locked_out_user_login()
#testClass.test_icon()
testClass.test_products_number()