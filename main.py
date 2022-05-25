from internet_speed_twitter_bot import *

# contansts
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
TWITTER_URL = "https://twitter.com/i/flow/login"
SPEED_TEST_URL = "https://www.speedtest.net"
PROMISED_DOWN = YOUR PROMISED INTERNET DOWNLOAD SPEED
PROMISED_UP = YOUR PROMISED INERNET UPLOAD SPEED
TWITTER_EMAIL = "YOUR TWITTER E-MAIL"
TWITTER_PASS = "YOUR TWITTER PASSWORD"

# creating the object from the class.
speed_test_obj = InternetSpeedTwitterBot(CHROME_DRIVER_PATH, SPEED_TEST_URL)
speed_test_obj.get_internet_speed()
print(speed_test_obj.down, speed_test_obj.up)

TWEET_TEMPLATE = "IT IS A TEMPLATE OF TWEET, SET IT AS YOUT WISH IF YOU WANT TO COMPLAINT ABOUT THE INTERNET SPEED OR JUST A RANODM TWEET."

# checking if the internet speed(Upload/Download) is less then the promised speed by the internet provider.
if float(speed_test_obj.down) < PROMISED_DOWN or float(speed_test_obj.up) < PROMISED_UP:
    # creating the object from the class
    twitter_obj = InternetSpeedTwitterBot(CHROME_DRIVER_PATH, TWITTER_URL)
    twitter_obj.tweet_at_provider(TWITTER_EMAIL, TWITTER_PASS, TWEET_TEMPLATE)
