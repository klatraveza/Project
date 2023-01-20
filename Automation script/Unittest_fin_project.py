from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import unittest
import f_project_keys
import time


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_chrome_max(self):
        driver = self.driver
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        url = "https://qasvus.wixsite.com/ca-marketing"
        driver.get(url)
        # Code starts here
        driver.get(url)
        driver.maximize_window()
        driver.delete_all_cookies()
        # Printing something just to know that we are in the right place
        print(driver.title)
        print(driver.current_url)
        time.sleep(3)
        # Lets log in) TC №1
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Sign up with email')]")))
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[contains(text(),'Log in with Email')]").click()
        time.sleep(3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@class='KvoMHf has-custom-focus focus-within']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@class='KvoMHf has-custom-focus focus-within']").click()
        e_inp = driver.find_element(By.XPATH, "//input[@class='KvoMHf has-custom-focus focus-within']")
        e_inp.send_keys(f_project_keys.e_mail)
        time.sleep(2)
        p_inp = driver.find_element(By.XPATH, "//input[@type='password']")
        p_inp.click()
        p_inp.send_keys(f_project_keys.password)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@class='R6ex7N']").click()
        time.sleep(10)
        print("TC 1 completed")
        # Let's go to the shop and check the products
        # TC №2
        driver.find_element(By.XPATH, "//p[@id='comp-ksocy9ii2label']").click()
        time.sleep(8)
        print("TC 2 completed")
        # TC №3
        ele_finder = driver.find_element
        ele_finder(By.XPATH, "//h3[contains(text(),'Product 1')]").click()
        time.sleep(4)
        driver.back()
        time.sleep(4)
        ele_finder(By.XPATH, '//h3[contains(text(),"I\'m a producd 2")]').click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, '//h3[contains(text(),"4")]').click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, '//h3[contains(text(),"I\'m a product3")]').click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, "//span[contains(text(),'$7.50')]").click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, '//h3[contains(text(),"I\'m a product 12")]').click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[@id='site-root']/div["
                             "@id='masterPage']/main[@id='PAGES_CONTAINER']/div[@id='SITE_PAGES']/div["
                             "@id='SITE_PAGES_TRANSITION_GROUP']/div[@id='vdow0']/div[2]/div[1]/div[1]/div[1]/div[1]/div["
                             "1]/div[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[7]/div[1]/div[1]/a[1]/div[1]/h3[1]").click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[@id='site-root']/div["
                             "@id='masterPage']/main[@id='PAGES_CONTAINER']/div[@id='SITE_PAGES']/div["
                             "@id='SITE_PAGES_TRANSITION_GROUP']/div[@id='vdow0']/div[2]/div[1]/div[1]/div[1]/div[1]/div["
                             "1]/div[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[8]/div[1]/div[1]/a[1]/div[1]").click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        print("TC 3 completed")
        # TC №4
        driver.find_element(By.XPATH, "//h3[contains(text(),'Product 1')]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@class="ColorPickerItem3577115324__radioOuter"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[contains(text(),'Add to Card')]").click()
        time.sleep(3)
        # driver.find_element(By.TAG_NAME,"html").send_keys(Keys.ESCAPE)
        driver.get(
            "https://qasvus.wixsite.com/ca-marketing/cart?appSectionParams=%7B%22origin%22%3A%22cart-popup%22%7D")
        print("TC 4 completed")
        time.sleep(3)
        # TC №5
        driver.find_element(By.XPATH, "//p[@id='comp-ksocy9ii0label']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,
                            "//header/div[@id='SITE_HEADER']/div[2]/div[2]/div[1]/div[1]/section[1]/div[2]/div["
                            "2]/div[2]/div[1]/div[3]/div[1]/a[1]/div[1]/*[1]")
        print("TC 5 completed")
        print("ALL POSITIVE TEST ARE PASSED")

    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()

    def test_edge_max_size(self):
        driver = self.driver
        driver.maximize_window()
        wait = WebDriverWait(driver, 10)
        url = "https://qasvus.wixsite.com/ca-marketing"
        driver.get(url)
        # Code starts here
        driver.get(url)
        driver.maximize_window()
        driver.delete_all_cookies()
        # Printing something just to know that we are in the right place
        print(driver.title)
        print(driver.current_url)
        time.sleep(3)
        # Lets log in) TC №1
        driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        time.sleep(2)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Sign up with email')]")))
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[contains(text(),'Log In')]").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//*[contains(text(),'Log in with Email')]").click()
        time.sleep(3)
        wait.until(
            EC.visibility_of_element_located((By.XPATH, "//input[@class='KvoMHf has-custom-focus focus-within']")))
        time.sleep(3)
        driver.find_element(By.XPATH, "//input[@class='KvoMHf has-custom-focus focus-within']").click()
        e_inp = driver.find_element(By.XPATH, "//input[@class='KvoMHf has-custom-focus focus-within']")
        e_inp.send_keys(f_project_keys.e_mail)
        time.sleep(2)
        p_inp = driver.find_element(By.XPATH, "//input[@type='password']")
        p_inp.click()
        p_inp.send_keys(f_project_keys.password)
        time.sleep(3)
        driver.find_element(By.XPATH, "//*[@class='R6ex7N']").click()
        time.sleep(10)
        print("TC 1 completed")
        # Let's go to the shoop and check the products
        # TC №2
        driver.find_element(By.XPATH, "//p[@id='comp-ksocy9ii2label']").click()
        time.sleep(8)
        print("TC 2 completed")
        # TC №3
        ele_finder = driver.find_element
        ele_finder(By.XPATH, "//h3[contains(text(),'Product 1')]").click()
        time.sleep(4)
        driver.back()
        time.sleep(4)
        ele_finder(By.XPATH, '//h3[contains(text(),"I\'m a producd 2")]').click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, '//h3[contains(text(),"4")]').click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, '//h3[contains(text(),"I\'m a product3")]').click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, "//span[contains(text(),'$7.50')]").click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, '//h3[contains(text(),"I\'m a product 12")]').click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[@id='site-root']/div["
                             "@id='masterPage']/main[@id='PAGES_CONTAINER']/div[@id='SITE_PAGES']/div["
                             "@id='SITE_PAGES_TRANSITION_GROUP']/div[@id='vdow0']/div[2]/div[1]/div[1]/div[1]/div[1]/div["
                             "1]/div[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[7]/div[1]/div[1]/a[1]/div[1]/h3[1]").click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        ele_finder(By.XPATH, "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[@id='site-root']/div["
                             "@id='masterPage']/main[@id='PAGES_CONTAINER']/div[@id='SITE_PAGES']/div["
                             "@id='SITE_PAGES_TRANSITION_GROUP']/div[@id='vdow0']/div[2]/div[1]/div[1]/div[1]/div[1]/div["
                             "1]/div[1]/div[1]/div[1]/section[1]/div[1]/ul[1]/li[8]/div[1]/div[1]/a[1]/div[1]").click()
        time.sleep(4)
        driver.back()
        time.sleep(3)
        print("TC 3 completed")
        # TC №4
        driver.find_element(By.XPATH, "//h3[contains(text(),'Product 1')]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, '//*[@class="ColorPickerItem3577115324__radioOuter"]').click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//span[contains(text(),'Add to Card')]").click()
        time.sleep(3)
        # driver.find_element(By.TAG_NAME,"html").send_keys(Keys.ESCAPE)
        driver.get(
            "https://qasvus.wixsite.com/ca-marketing/cart?appSectionParams=%7B%22origin%22%3A%22cart-popup%22%7D")
        print("TC 4 completed")
        time.sleep(3)
        # TC №5
        driver.find_element(By.XPATH, "//p[@id='comp-ksocy9ii0label']").click()
        time.sleep(5)
        driver.find_element(By.XPATH,
                            "//header/div[@id='SITE_HEADER']/div[2]/div[2]/div[1]/div[1]/section[1]/div[2]/div["
                            "2]/div[2]/div[1]/div[3]/div[1]/a[1]/div[1]/*[1]")
        print("TC 5 completed")
        print("ALL POSITIVE TEST ARE PASSED")

    def tearDown(self):
        self.driver.quit()
