from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


# creating a class
class InternetSpeedTwitterBot:
    def __init__(self, driver_path, url):
        service_obj = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.get(url=url)
        self.up = 0
        self.down = 0

    # method to check internet speed
    def get_internet_speed(self):
        # getting hold of buttons
        go_btn = self.driver.find_element(By.XPATH,
                                          '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        sleep(60)
        close_btn = self.driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/a').click()
        
	# getting the dowload/upload speeds
	self.down = self.driver.find_element(By.XPATH,
                                             '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.driver.quit()

    # method to tweet on twitter
    def tweet_at_provider(self, email, pasw, tweet):
        # getting hold of input fields
        sleep(3)
	# email field
        email_field = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(
            email, Keys.ENTER)
        sleep(2)
        try:
	    # password field
            pasw_field = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(
                pasw, Keys.ENTER)
        except:
	    # mobile no. field, if asks for mobile no.
            mono_field = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(
                "Your Mobile No.", Keys.ENTER)
            sleep(2)
            pasw_field = self.driver.find_element(By.XPATH,
                                                  '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(
                pasw, Keys.ENTER)

        # getting hold of create tweet btn
        sleep(5)
        create_tweet_btn = self.driver.find_element(By.XPATH,
                                                    '/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a').click()
        sleep(1)
        # getting hold of input field
        tweet_content = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        sleep(2)
        tweet_content.click()
        sleep(2)
        tweet_content.send_keys(tweet)

        sleep(2)
        # getting hold of tweet btn
        tweet_btn = self.driver.find_element(By.XPATH,
                                             '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div/span/span').click()

        self.driver.quit()
