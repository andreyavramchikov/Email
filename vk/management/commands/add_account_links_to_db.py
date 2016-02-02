from BeautifulSoup import BeautifulSoup
from optparse import make_option

from django.core.management.base import BaseCommand

from selen.utils import DriverProvider
from vk.models import Account

class Command(BaseCommand):
    APP_NAME = 'vk'

    option_list = BaseCommand.option_list + (
        make_option('--link', dest='link', help='Link from which will get vk account links'),
        make_option('--username', dest='username', help='Username of the account'),
        make_option('--password', dest='password', help='Password of the account'),
    )

    def handle(self, *args, **options):
        driver_provider = DriverProvider()
        driver = driver_provider.driver
        link = options.get('link')
        username = options.get('username')
        password = options.get('password')
        driver.get(link)
        driver_provider.login_user(username, password)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver_provider.scroll_bottom_times(300)
        response = driver.execute_script('return document.documentElement.innerHTML;')
        soup = BeautifulSoup(response)
        results_td = soup.find("td", {"id": "results"})
        all_accounts = results_td.findAll('a')
        for people in all_accounts:
            try:
                account, created = Account.objects.get_or_create(link=people['href'])
            except Exception as e:
                print e