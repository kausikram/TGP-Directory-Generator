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

def main():
    with open("data.csv") as f:
        data = f.read()
    lines = data.split("\n")

    for l in lines[1:]:
        items = l.split(",")
        url_complex = items[1]
        try:
            url = url_complex.split("(")[1].split(")")[0]
            ext = url_complex.split("(")[0].split(".")[1]
            name = items[0]
            path = name + "." + ext
            r = urllib2.urlopen(url)
            with open("profile_pictures/"+path, 'wb') as f:
                f.write(r.read())
        except Exception:
            print items

if __name__ == '__main__':
    main()