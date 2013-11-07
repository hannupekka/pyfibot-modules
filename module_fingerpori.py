#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

def command_fingerpori(bot, user, channel, args):
	"""Fetches latest Fingerpori from hs.fi"""
	url = "http://www.hs.fi/fingerpori/"

	f = urllib2.urlopen(url)
	d = f.read()
	f.close()

	bs = BeautifulSoup(d)
	date = bs.find('div', {'class': 'comic-date'}).string
	url = bs.find('div', {'id': 'full-comic'}).find('img')['src']

	output = "%s: %s" % (str(date), str(url))

	return(bot.say(channel, output))