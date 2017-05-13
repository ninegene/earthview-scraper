# earthview-scraper
Download wallpaper images from https://earthview.withgoogle.com

```
$ python scrape.py
```

When `scrape.py` doesn't work anymore.
Another way to download with wget as mirror offline site:
```
$ wget -mkEpnp earthview.withgoogle.com

FINISHED --2017-05-12 23:33:28--
Total wall clock time: 49m 34s
Downloaded: 3054 files, 1.0G in 7m 55s (2.19 MB/s)
```

Open another terminal window to watch downloaded image count:
```
$ watch -n 2 'ls -l earthview.withgoogle.com/download | wc -l'
```
