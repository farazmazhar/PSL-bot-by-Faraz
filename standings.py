# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 10:08:46 2018

@author: faraz
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup

class Standing:
    html_link = ""
    
    def __init__(self, html_link):
        self.html_link = html_link

    def getHtmlDoc(self):
        return requests.get(self.html_link).text
    
    def getSoup(self):
        return BeautifulSoup(self.getHtmlDoc(), 'lxml')
    
    """
    Function getStandings() will return a Data Frame containing
    information about standings.
    """
    def getStandings(self):
        soup = self.getSoup()
        table = soup.find('div', attrs={'class': 'responsive-table-wrap'})
        
        standingHeaderList = ["Team"]
        
        for tableHead in table.findAll('thead'):
            rows = tableHead.findAll('tr')
            for tr in rows:
                cols = tr.findAll('th')
                for td in cols:
                    spans = td.findAll('span')
                    for span in spans:
                        atags = span.findAll('a')
                        for a in atags:
                            standingHeaderList.append(a.text)
        
        standings = {}
        for tableBody in table.findAll('tbody'):
            rows = tableBody.findAll('tr')
            for tr in rows:
                pos = 0
                cols = tr.findAll('td')
                for td in cols:
                    spans = td.findAll('span')
                    
                    if not td.findAll('span'):                
                        standings[pos].append(td.text)
                    else:
                        for span in spans:
                            try:
                                pos = int(span.text)
                            except:
                                pass
                            
                            standings[pos] = [span.text]
        
        df = pd.DataFrame(standings).transpose()
        df.columns = standingHeaderList
        return df