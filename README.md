# earthview-scraper
Download wallpaper images from https://earthview.withgoogle.com

When `scrape.py` doesn't work anymore.
Another way to download with wget as mirror offline site:
```
$ wget -mkEpnp earthview.withgoogle.com

# Press control key and Z key to suspense to background
$ Ctrl+Z

# Watch downladed count and press control key and C key to stop watching when number stop increasing after a while
$ watch -n 2 'ls -l earthview.withgoogle.com/download | wc -l'
716

$ Ctrl+C

# Bring it to foreground
$ fg

# Press control key and C key to stop wget download
$ Ctrl+C
```
