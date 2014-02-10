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
import urllib2
from test import ProfilePage

def main():
    with open("data2.csv") as f:
        data = f.read()
    lines = data.split("\n")

    counter = 1
    dumper = []
    page = 1
    for l in lines[1:-1]:
        items = l.split("\t")
        dumper.append([items[2],items[1],items[4],items[3],items[5]])
        if counter % 5 == 0:
            p = ProfilePage()
            p.run(dumper)
            dumper = []
            p.save(page)
            page += 1
        counter +=1
    p = ProfilePage()
    p.run(dumper)
    dumper = []
    p.save(page)



if __name__ == '__main__':
    main()