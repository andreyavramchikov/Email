# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
import time
from selen.utils import DriverProvider
from selenium import webdriver
# cd projects/commands/helpdesk/
# workon commands
# python manage.py slide_lingvoleo_words

class Command(BaseCommand):

    URL = 'http://lingualeo.com/ru/glossary/learn/dictionary'
    URL2 = 'http://ru.forvo.com/'
    driver2 = webdriver.Firefox()

    def spell_word(self, word):
        self.driver2.get(self.URL2)
        x = self.driver2.find_element_by_id('word_search_header')
        x.send_keys(word)
        button = self.driver2.find_element_by_class_name('actions').find_element_by_tag_name('button')
        button.click()
        try:
            self.driver2.find_element_by_class_name('search_words').find_elements_by_tag_name('li')[0].find_element_by_tag_name('a').click()
        except:
            pass
    def handle(self, *args, **options):

        from selenium import webdriver
        driver_provider = DriverProvider()
        driver = driver_provider.driver

        username = 'andrey-pasan@mail.ru' #options.get('username')
        password = 'andreypasan' #options.get('password')
        driver.get(self.URL)
        driver_provider.login_lingvoleo_user(username, password)
        x = driver.find_elements_by_class_name('item-word-translate ')
        x[0].click()
        word = driver.find_element_by_class_name('trans-detail-list').find_element_by_tag_name('li').text
        print word
        self.spell_word(word)
        for i in range(1, 1000):
            time.sleep(4)
            driver.find_element_by_class_name('icons-card-next').click()
            time.sleep(3)
            word = driver.find_element_by_class_name('trans-detail-list').find_element_by_tag_name('li').text
            print word
            self.spell_word(word)
