# This is our [HackPrinceton](http://hackprinceton.com/) project: *[DownTime](http://www.hackerleague.org/hackathons/hackprinceton-fall-2013/hacks/downtime)*.

See [AUTHORS.md](https://github.com/jonmetz/DownTime/blob/master/AUTHORS.md) for a list of all the members of the downtime team.

A new git repository had to be created for the code because the initial repository became unmanageable due to duplicate commits and extremely large object, as well as API keys.

# Deployment

Most of the backend code is in PHP and should work well with standard, recent versions of PHP5, Apache2 and MongoDB.

Part of the backend code is solely responsible for fetching webpages using various APIs and is written in Python, they can be found in the scrape directory.

This code does not need to be connected to any of the server side PHP code and can be run using cron jobs, or other suitable methods.

In order to run two files in this directory, ```youtube.py``` and ```NYTimes.py```, you must first add your own API keys. Rather than substitute our own keys with blank strings, we have opted to simply remove the string entirely, that way the scripts will simply refuse to run until API keys are added.

# Demo

*Coming Soon*
