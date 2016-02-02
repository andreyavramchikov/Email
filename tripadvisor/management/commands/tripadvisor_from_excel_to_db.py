# -*- coding: utf-8 -*-
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from xlrd import open_workbook
from tripadvisor.models import Restaurant
import time
import hashlib


# python manage.py tripadvisor_from_excel_to_db
def _get_files_in_directory(directory):
    return os.listdir(directory)


class Command(BaseCommand):
    APP_NAME = 'tripadvisor'
    FOLDER_NAME = 'restaurants_15'

    def handle(self, *args, **options):
        restaurants_directory = '/'.join([settings.BASE_DIR, self.APP_NAME, self.FOLDER_NAME])
        files = _get_files_in_directory(restaurants_directory)
        start_time = time.time()
        print start_time
        for xls_file in files:
            excel_file = open_workbook(restaurants_directory + '/' + xls_file, formatting_info=True, on_demand=True)
            sheet = excel_file.sheet_by_index(0)
            for rownum in range(sheet.nrows):
                row = sheet.row_values(rownum)
                email = row[0]
                name = row[1]
                state = row[2]
                postal = row[3]
                address = row[4]
                phone = row[5]
                city = row[6]
                hash_raw = email+name+state+postal+address+phone+city
                unique_hash = hashlib.md5(hash_raw.encode('ascii', 'ignore')).hexdigest()
                try:
                    Restaurant.objects.create(name=name, phone=phone, state=state, postal=postal, email=email,
                                              address=address, city=city, hash=unique_hash)
                except Exception as e:
                    print name
            print 'Finished' + str(xls_file)

        print time.time() - start_time
        print time.time()

