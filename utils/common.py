import os
from django.conf import settings
from antigate import AntiGate


def write_list_to_file(array, file_path):
    new_file = open(file_path, 'w')
    for elem in array:
        new_file.write(elem + '\n')


def generate_hash():
    return os.urandom(16).encode('hex')


def crop_image(img, path, x1, y1, x2, y2 ):
    box = (x1, y1, x2, y2)
    area = img.crop(box)
    area.save(path, 'jpeg')


def get_captcha(captcha_path):
    gate = AntiGate(settings.ANTIGATE_API_KEY, captcha_path)
    return gate.get(gate.captcha_id)