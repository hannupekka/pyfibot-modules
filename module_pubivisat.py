#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

def command_pubivisat(bot, user, channel, args):
	"""Fetches todays pub quizzes for Tampere from pubivisat.fi"""
	url = "http://pubivisat.fi/tampere"

	f = urllib2.urlopen(url)
	d = f.read()
	f.close()

	bs = BeautifulSoup(d)
	data = bs.find('table', {'class': 'quiz_list'}).find('tbody').findAll('tr')

	quizzes = []
	for row in data:
		name = row.find('a').string
		time = row.findAll('td')[1].string

		quizzes.append("%s: %s" % (str(name), str(time)))

	output = ' | '.join(reversed(quizzes))
	return(bot.say(channel, output))