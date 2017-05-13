#!/usr/bin/env python
import os
import urllib
import time

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def download_file(url, filename=None):
    filename = filename or url.split('/')[-1]
    if not os.path.exists(filename) or os.path.getsize(filename) < 1500:
        try:
            print('Downloading {}'.format(url))
            urllib.urlretrieve(url, filename)
            time.sleep(0.1)
        except Exception:
            print('Error downloading: {}'.format(url))
        except KeyboardInterrupt:
            print('Stopping ...')
            os.sys.exit(2)
    else:
        print('Skipping {}. File exists: {}'.format(url, filename))


def remove_bad_files(dldir):
    for filename in os.listdir(dldir):
        filesize = os.path.getsize(filename)
        if filename.endswith('.jpg') and filesize < 2000:
            print('Removing bad file: {} with size: {}'.format(filename, filesize))
            os.remove(filename)


def scrape():
    dldir = BASE_DIR + '/downloads'
    create_dir(dldir)

    # from 1004.jpg to 7023.jpg
    for i in range(1004, 7023):
        download_file('https://www.gstatic.com/prettyearth/assets/full/%s.jpg' % i,
                      '%s/%s.jpg' % (dldir, i))

    remove_bad_files(dldir)


if __name__ == '__main__':
    scrape()
