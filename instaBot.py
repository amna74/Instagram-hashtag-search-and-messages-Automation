from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from shutil import which
import time

# chrome_options= Options()
# chrome_options.add_argument("--headless")

chrome_path = which("chromedriver")
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get("https://www.instagram.com/")
time.sleep(3)

emailBox = driver.find_element_by_name("username")
emailBox.send_keys("abc123@gmail.com")

password = driver.find_element_by_name("password")
password.send_keys("abc123%")


password.send_keys(Keys.ENTER)
time.sleep(5)

search = driver.find_element_by_xpath("//input[@placeholder='Search']")
search.send_keys("#saynotoplastic")              #Enter your desired hashtag name here
time.sleep(5)

search.send_keys(Keys.ENTER)
search.send_keys(Keys.ENTER)

time.sleep(5)
post = driver.find_element_by_xpath("//div[@class='v1Nh3 kIKUG  _bz0w']")
post.click()

time.sleep(5)
user = driver.find_element_by_xpath("(//a[@class='sqdOP yWX7d     _8A5w5   ZIAjV '])[1]")
user.click()

time.sleep(5)
follow = driver.find_element_by_xpath("//button[@class= '_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
follow.click()

time.sleep(5)
messageButton = driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy    _8A5w5    ']")
messageButton.click()
time.sleep(8)

notNow = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
notNow.click()


messageText = "hello....."            # Enter the general message here what you want to send

messageBox = driver.find_element_by_xpath("//textarea[@placeholder='Message...']")
messageBox.send_keys(messageText)

time.sleep(5)

messageBox.send_keys(Keys.ENTER)

time.sleep(5)


