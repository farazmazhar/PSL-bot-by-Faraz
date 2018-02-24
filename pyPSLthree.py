# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 12:45:14 2018

@author: faraz
"""

import standings

html_link = "http://www.espncricinfo.com/table/series/8679/season/2018/pakistan-sl"

pslStandings = standings.Standing(html_link)

print(pslStandings.getStandings())