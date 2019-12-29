#!/usr/bin/python3

    # A small Python 3 library to pixel your photos.
    # Copyright (C) 2019  ArisuFox

    # This program is free software: you can redistribute it and/or modify
    # it under the terms of the GNU General Public License as published by
    # the Free Software Foundation, either version 3 of the License, or
    # (at your option) any later version.

    # This program is distributed in the hope that it will be useful,
    # but WITHOUT ANY WARRANTY; without even the implied warranty of
    # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    # GNU General Public License for more details.

    # You should have received a copy of the GNU General Public License
    # along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import urllib.request as r

"""
Pixel your photos.
Depends:
    - catimg (sudo apt install catimg)
"""

class Photo():
    """
    A class for your photo.
    """
    def __init__(self, path: str):
        self.path = path

    def __str__(self):
        return self.path

def pixel(Photo, weight: int = 300):
    """
    A function to pixel your photos.
    Default value for weight is 300.
    """
    os.system('catimg -w {w} {p}'.format(w=weight, p=Photo.path))

if __name__ == "__main__":
    print('This is a Python 3 module by @ArisuFox, called PixeLib.')
    print('Please note, that I AM NOT A CREATOR OF CATIMG.')
    print('Do you want to load a template photo and pixel it?')
    a = input('[N/y]: ').lower()
    if a in ('y', 'д'):
        PHOTO_URL = 'https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png'
        FILENAME = 'google.png'
        r.urlretrieve(PHOTO_URL, FILENAME)
        template = Photo(FILENAME)
        pixel(template)
