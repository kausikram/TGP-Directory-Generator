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
from fetch import fetch_data
import config
import urllib2

def get_file_name_for_entry(e):
    try:
        url_complex = e[config.IMAGE_FIELD]
        ext = url_complex.split("(")[0].split(".")[1]
        name = e["EntryId"]
        path = name + "." + ext
        return path
    except Exception:
        return "blank.png"

def main():
    data = fetch_data()
    for d in data:
        print "Getting image for", d["EntryId"]
        url_complex = d[config.IMAGE_FIELD]
        try:
            url = url_complex.split("(")[1].split(")")[0]
            ext = url_complex.split("(")[0].split(".")[1]
            name = d["EntryId"]
            path = name + "." + ext
            r = urllib2.urlopen(url)
            with open(config.PROFILE_PICTURE_FOLDER+"/"+path, 'wb') as f:
                f.write(r.read())
        except Exception:
            print "***** No Image Found *****", d["EntryId"]

if __name__ == '__main__':
    main()