#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Kausikram
#
# Created:     03-02-2014
# Copyright:   (c) Kausikram 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import config
import requests

def fetch_data():
    r = requests.get(config.COUNT_URL,params=config.PARAMS,auth=config.AUTH)
    total_count = int(r.json()["EntryCount"])
    start = 0
    final_data = []
    while start < total_count:
        run_config = {"pageStart":start,"pageSize":100}
        run_config.update(config.PARAMS)
        r = requests.get(config.DATA_URL,params=run_config,auth=config.AUTH)
        data = r.json()["Entries"]
        print len(data)
        final_data.extend(data)
        start += 100
    return final_data

if __name__ == '__main__':
    print fetch_data()