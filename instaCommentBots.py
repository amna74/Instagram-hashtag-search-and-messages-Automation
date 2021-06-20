from selenium import webdriver
from time import sleep
# from secrets import pwe
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.webdriver.chrome.options import Options
from shutil import which
import random

username = "abc123"
pwe = "abc123"

usernames = []

hashtags = ["newstartup", "software", "coding", "python"]


class Bot():
    links = []

    comments = [
        'Wow have you seen the new cannabis app?  @khronicai', 'New cannabis start up you gotta check out @khronicai',
        'Upcoming cannabis app @khronicai', 'Personal Budender @khronicai',
    ]


    def __init__(self):

        self.login(username)
        self.like_comment_by_hashtag('#business')

    def login(self, username):

        chromeOptions = Options()
        # chromeOptions.add_argument("--headless")
        chromePath = which("chromedriver")
        self.driver = webdriver.Chrome(executable_path=chromePath, options=chromeOptions)
        self.driver.set_window_size(1920, 1080)

        self.driver.get('https://www.instagram.com/')
        sleep(5)
        username_input = self.driver.find_element_by_xpath(
            "//input[@name='username']")
        username_input.send_keys(username)
        password_input = self.driver.find_element_by_xpath(
            "//input[@name='password']")
        password_input.send_keys(pwe)
        submit_btn = self.driver.find_element_by_xpath(
            "//button[@type='submit']")
        submit_btn.click()
        sleep(5)
        try:
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        except:
            pass
        try:
            self.driver.find_element_by_xpath(
                '/html/body/div[4]/div/div/div[3]/button[2]').click()
        except:
            pass

    def like_comment_by_hashtag(self, hashtag):
        search_box = self.driver.find_element_by_xpath(
            "//input[@placeholder='Search']")
        search_box.send_keys('#' + hashtag)
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a').send_keys(Keys.ENTER)

        sleep(10)

        links = self.driver.find_elements_by_tag_name('a')
        valid_links = []
        for i in range(1, 10):  # Control Depth
            # ------------------------------------------------------------------------ #
            # Note that it Scrolls for defined depth first and then
            # extracts the URLs Because unlike twitter, each post is opened in different
            # URL so we can't just scroll and comment simultaneously.
            # ------------------------------------------------------------------------ #
            links = list(set(links))

            def condition(link):
                return '.com/p/' in link.get_attribute('href')

            valid_links = list(filter(condition, links))

            for vLink in valid_links:
                link = vLink.get_attribute('href')
                if link not in self.links:
                    self.links.append(link)

            self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')  # Scrolling
            sleep(10)
            links = self.driver.find_elements_by_tag_name('a')

        print(str(len(self.links)) + " Links are extracted to Like and Comment")

        for link in self.links:
            self.driver.get(link)

            # like
            self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button').click()
            sleep(3)

            # comment
            try:
                self.driver.find_element_by_class_name('RxpZH').click()
                sleep(1)
                self.driver.find_element_by_xpath(
                    "//textarea[@placeholder='Add a comment…']").send_keys(self.comments[randint(0, 3)])
                sleep(2)
                self.driver.find_element_by_xpath(
                    "/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button").click()
                sleep(3)
            except:
                print("Commenting was either OFF or has been limited for this post:\n" + link)


def main():
    my_bot = Bot()


if __name__ == '__main__':
    main()
