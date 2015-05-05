import os
import urllib
# import subprocess

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def create_dir(path):
    # subprocess.call(['mkdir', '-p', path])
    if not os.path.exists(path):
        os.makedirs(path)


def download_file(url, filename=None):
    filename = filename or url.split('/')[-1]
    print('Downloading ' + url + ' as ' + filename)
    urllib.urlretrieve(url, filename)


def scrape():
    dldir = BASE_DIR + '/downloads'
    create_dir(dldir)
    # from 1.jpg to 100.jpg
    for i in range(1, 101):
        download_file('https://earthview.withgoogle.com/images/wallpaper/%s.jpg' % i,
                      '%s/%s.jpg' % (dldir, i))


if __name__ == '__main__':
    scrape()
