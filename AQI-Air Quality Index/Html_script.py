# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:00:44 2021

@author: sukes
"""
import os
import time
import requests

import sys

def retrieve_html():
    for year in range(2013,2019):
        print(year)
        for month in range(1,13):
            print(month)
            if(month<10):
                url = "https://en.tutiempo.net/climate/0{}-{}/ws-432950.html".format(month
                                                                             ,year)
            else:
                url = "https://en.tutiempo.net/climate/{}-{}/ws-432950.html".format(month
                                                                              ,year)
                
            text = requests.get(url)
            text_utf = text.text.encode('utf=8')
        
            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            
            with open("Data/Html_Data/{}/{}.html".format(year,month),'wb') as output:
                output.write(text_utf)
                    
            
        sys.stdout.flush()

if __name__ == "__main__":
    start_time = time.time()
    retrieve_html()
    stop_time = time.time()
    print("Time taken {}".format(stop_time-start_time))