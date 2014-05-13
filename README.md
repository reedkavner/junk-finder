GMail Junk Finder
===========

Gmail Junk Finder is a little command line utility to find and quickly unsubscribe from junk messages in GMail. Tell it how far back to look in your inbox and it will put together a handy (if ugly) document with all the relevant unsubscribe links lined up for your clicking pleasure.

### Setup
Install these two helpful libraries:
- [Gmail by Charlie Guo](https://github.com/charlierguo/gmail)
- [Beautifulsoup](http://www.crummy.com/software/BeautifulSoup/)

### Usage
From the script's dirctory, run:

```python junk-finder.py '[USERNAME]' '[PASSWORD]' [DAYS]```

[USERNAME] and [PASSWORD] are obviously your GMail login credentials and [DAYS] is how many days in the past you want to look for junk.

For example...

```python junk-finder.py 'b_obama' 'sma$h_mouth_roxx' 7```

The script should automatically open the resulting HTML document in your default browser. If it's unable to, you'll have to do that manually.
