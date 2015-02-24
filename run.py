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
from fetch import fetch_data
from profile_builder import ProfilePage
from get_images import get_file_name_for_entry

def main():
    data = fetch_data()
    counter = 1
    dumper = []
    page = 1
    for d in data:
        profile_photo_file = get_file_name_for_entry(d) #extension
        dumper.append([d[config.NAME_FIELD],d[config.EMAIL_FIELD],d[config.TWITTER_FIELD],d[config.DESCRIPTION_FIELD],profile_photo_file])
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