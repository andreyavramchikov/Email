from selenium import webdriver
import time


class DriverProvider(object):
    driver = webdriver.Firefox()
    VK_PREFIX = 'https://vk.com'
    def login_user(self, username, password):
        self.driver.find_element_by_id('quick_email').send_keys(username)
        self.driver.find_element_by_id('quick_pass').send_keys(password)
        self.driver.find_element_by_id('quick_login_button').click()

    def login_lingvoleo_user(self, username, password):
        self.driver.find_element_by_id('email').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)
        self.driver.find_element_by_class_name('btn-upper-orange').click()

    def logout_user(self):
        self.driver.get(self.VK_PREFIX)
        time.sleep(2)

        self.driver.find_element_by_id('logout_link_td').find_element_by_tag_name('a').click()
        time.sleep(2)

    def scroll_bottom_times(self, count):
        for i in range(0, count):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)


