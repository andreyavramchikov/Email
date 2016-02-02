# -*- coding: utf-8 -*-
import time
from PIL import Image
from optparse import make_option

from django.core.management.base import BaseCommand

from selen.utils import DriverProvider
from utils.common import generate_hash, crop_image, get_captcha
from vk.credentials import ACCOUNTS
from vk.models import Account

from selenium.common.exceptions import NoSuchElementException


#python manage.py add_friends_to_account  --username=andrey-pasan@mail.ru --password=aldrsonchiK1
#python manage.py add_friends_to_account --file=true
class Command(BaseCommand):

    def _vk_recaptcha(self, driver):
        _hash = generate_hash()
        screenshot_path = '/'.join([self.APP_NAME, 'screenshots', _hash + '.jpg'])
        captcha_path = '/'.join([self.APP_NAME, 'captchas', _hash + '.jpg'])
        driver.save_screenshot(screenshot_path)
        img = Image.open(screenshot_path)
        sizes = driver.get_window_size()
        width = sizes['width']
        height = sizes['height']
        x1 = int(width/2) - 200
        y1 = int(height/2) - 200
        x2 = x1 + 400
        y2 = y1 + 200
        crop_image(img, captcha_path, x1, y1, x2, y2)
        return get_captcha(captcha_path)

    VK_PREFIX = 'https://vk.com'
    APP_NAME = 'vk'

    option_list = BaseCommand.option_list + (
        make_option('--username', dest='username', help='Username of the account'),
        make_option('--password', dest='password', help='Password of the account'),
        make_option('--file', dest='file',  help='File with accounts credentials')
    )

    def add_persons(self, driver, driver_provider):
        time.sleep(2)
        for account in Account.objects.filter(added=False).order_by('date_added'):
            driver.get(self.VK_PREFIX + account.link)
            time.sleep(2)
            try:
                driver.find_element_by_xpath("//*[contains(text(), 'Добавить в друзья')]").click()
            except NoSuchElementException:
                account.added = True
                account.save()
                continue
            time.sleep(2)
            try:
                if driver.find_element_by_class_name('flat_button').text == u'\u0417\u0430\u043a\u0440\u044b\u0442\u044c':
                    # it means that I already added 40 people need to exit program
                    account.added = False
                    account.save()
                    driver_provider.logout_user()
                    # exit('You already added 40 people today')
                    break
            except NoSuchElementException:
                pass
            try:
                # this line mean that vk generate captcha popup
                box_layout = driver.find_element_by_class_name('box_layout')
            except NoSuchElementException:
                account.added = True
                account.save()
                continue
            if box_layout:
                # recaptcha
                captcha_id = self._vk_recaptcha(driver)
                captcha_input = driver.find_element_by_class_name('big_text')
                captcha_input.send_keys(captcha_id)
                try:
                    driver.find_element_by_class_name('flat_button').click()
                except NoSuchElementException:
                    print "Can't find blue button in captcha popup"
                    continue
                print captcha_id
            time.sleep(2)
            account.added = True
            account.save()

    def handle(self, *args, **options):
        driver_provider = DriverProvider()
        driver = driver_provider.driver
        username = options.get('username')
        password = options.get('password')
        filename = options.get('file')
        driver.get(self.VK_PREFIX)
        if filename:
            for account in ACCOUNTS:
                username = account['username']
                password = account['password']
                driver_provider.login_user(username, password)
                self.add_persons(driver, driver_provider)
            driver.close()
            exit('Finished list')


        driver_provider.login_user(username, password)
        self.add_persons(driver, driver_provider)



