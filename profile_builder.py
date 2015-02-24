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
from PIL import Image, ImageDraw, ImageFont
import textwrap
import config


PIX_CONVERTER = 12 #12dpmm
MARGIN = 15 #15 10
BOX = 50  #50 30

class ProfilePage(object):
    def __init__(self):
        self.img = Image.open(config.BACKGROUND_IMAGE_PATH)
        self.draw = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype(config.NAME_FONT, 14 * 300 / 72 )
        self.font_body = ImageFont.truetype(config.BODY_FONT, 10 * 300 / 72 )

    def run(self, lst):
        for i in enumerate(lst):
            self.draw_first(i[1],i[0])

    def get_pix(self,mm):
        return mm * PIX_CONVERTER

    def draw_first(self,item, box_number):
        print item[0]
        offset = box_number* BOX + (box_number+1) * MARGIN
        self.draw_image(item[4],self.get_pix(10),self.get_pix(offset))
        self.draw.text((self.get_pix(40),self.get_pix(offset)), item[0], fill=config.NAME_COLOR, font=self.font)
        self.draw.text((self.get_pix(40),self.get_pix(offset + 10)), item[1], fill=config.BODY_COLOR, font=self.font_body)
        self.draw.text((self.get_pix(40),self.get_pix(offset + 15)), item[2], fill=config.BODY_COLOR, font=self.font_body)
        self.draw_multi_line(self.get_pix(40),self.get_pix(offset + 20),item[3])

    def save(self, page_number):
        self.img.save(config.OUTPUT_FOLDER + "/%s.png"%(page_number,))

    def draw_image(self,image,pos_x,pos_y):
        try:
            profile_picture = Image.open(config.PROFILE_PICTURE_FOLDER + "/%s"%(image,))
        except Exception, e:
            print image
            print e
            return
        basewidth = 240
        wpercent = (basewidth/float(profile_picture.size[0]))
        hsize = int((float(profile_picture.size[1])*float(wpercent)))
        profile_picture = profile_picture.resize((basewidth,hsize), Image.ANTIALIAS)
##        profile_picture.thumbnail((355,355), Image.ANTIALIAS)
        self.img.paste(profile_picture, (pos_x, pos_y))

    def draw_multi_line(self,start_x,start_y,text):
        margin = start_x
        offset = start_y
        for line in textwrap.wrap(text, width=50):
            self.draw.text((margin, offset), line, font=self.font_body, fill=config.BODY_COLOR)
            offset += self.font_body.getsize(line)[1]

def main():
    p = ProfilePage()
    p.run([
        ["Kausikram Krishnasayee","kausikram@gmail.com","@kausikram","Udhay's primary passion is collecting interesting people, and putting them together in interesting ways. He pursues this passion tirelessly - as an investor, consultant, and emerging markets product expert; and also as the main man behind the vaunted silklist, one of the oldest active email lists on the net."],
        ["Vijay Anand","vijay@vijayanand.name","@vijayanand","Udhay's primary passion is collecting interesting people, and putting them together in interesting ways. He pursues this passion tirelessly - as an investor, consultant, and emerging markets product expert; and also as the main man behind the vaunted silklist, one of the oldest active email lists on the net."],
        ["Sumit Anand","sumit@gmail.com","@sumit","Udhay's primary passion is collecting interesting people, and putting them together in interesting ways. He pursues this passion tirelessly - as an investor, consultant, and emerging markets product expert; and also as the main man behind the vaunted silklist, one of the oldest active email lists on the net."]
    ])
    p.save(1)

if __name__ == '__main__':
    main()