GMail Junk Finder
===========

Gmail Junk Finder is a little command line utility to find and quickly unsubscribe from junk messages in GMail. Tell it how far back to look in your inbox and it will put together a handy (if ugly) document with all the relevant unsubscribe links lined up for your clicking pleasure.

### Setup
Install these two helpful libraries:
1. [Gmail by Charlie Guo](https://github.com/charlierguo/gmail)
2. [Beautifulsoup](http://www.crummy.com/software/BeautifulSoup/)

### Usage
From the script's dirctory, run:

```python junk-finder.py '[USERNAME]' '[PASSWORD]' [DAYS]```

[USERNAME] and [PASSWORD] are obviously your GMail login credentials and [DAYS] is how many days in the past you want to look for junk.

For example...

```python junk-finder.py 'kavner' 'sma$h_mouth_roxx' 7```
