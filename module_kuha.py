#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

def command_lannista(bot, user, channel, args):
	url = "http://lannistajakuha.com/random"

	f = urllib2.urlopen(url)
	d = f.read()
	f.close()

	bs = BeautifulSoup(d)
	data = bs.find('div', {'class': 'lannistus'}).string

	nick = getNick(user)
	if args:
		nick = str(args).strip()

	lannistus = "%s, %s" % (nick, data.encode('utf-8').strip().lower())

	return(bot.say(channel, str(lannistus)))