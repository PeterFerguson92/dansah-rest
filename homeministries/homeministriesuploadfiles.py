import os
import random


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext


def home_ministries_upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "homeministries/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)

