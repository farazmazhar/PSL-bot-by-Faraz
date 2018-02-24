# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:45:14 2018

@author: faraz
"""
from disco.bot import Bot, Plugin
import standings

class PSLbot(Plugin):
    @Plugin.listen('standings')
    def getStandings(self, event):
        html_link = "http://www.espncricinfo.com/table/series/8679/season/2018/pakistan-sl"
        pslStandings = standings.Standing(html_link)
        event.msg.reply(pslStandings.getStandings())