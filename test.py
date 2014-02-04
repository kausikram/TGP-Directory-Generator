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

NAME_COLOR = "#2BB673"
BODY_COLOR = "#000000"

class ProfilePage(object):
    def __init__(self):
        self.img = Image.open("a5.png")
        self.draw = ImageDraw.Draw(self.img)
        self.font = ImageFont.truetype("AbrilFatface-Regular.ttf", 18 * 300 / 72 )
        self.font_body = ImageFont.truetype("Quicksand-Regular.otf", 12 * 300 / 72 )

    def run(self, list_of_three):
        self.draw_first(list_of_three[0])
        self.draw_second(list_of_three[1])
        self.draw_third(list_of_three[2])

    def draw_first(self,item):
        self.draw.rectangle([(236,236),(591,591)], fill="#efefef")
        self.draw_image("profile_pictures/1.JPG",236,236)
        self.draw.text((708, 236), item[0], fill=NAME_COLOR, font=self.font)
        self.draw.text((708, 352), item[1], fill=BODY_COLOR, font=self.font_body)
        self.draw.text((708, 420), item[2], fill=BODY_COLOR, font=self.font_body)
        self.draw_multi_line(708,520,item[3])

    def draw_second(self,item):
        self.draw.rectangle([(236,1001),(591,1356)], fill="#efefef")
        self.draw_image("profile_pictures/2.png",236,1001)
        self.draw.text((708, 1001), item[0], fill=NAME_COLOR, font=self.font)
        self.draw.text((708, 1117), item[1], fill=BODY_COLOR, font=self.font_body)
        self.draw.text((708, 1185), item[2], fill=BODY_COLOR, font=self.font_body)
        self.draw_multi_line(708,1285,item[3])

    def draw_third(self,item):
        self.draw.rectangle([(236,1713),(591,2068)], fill="#efefef")
        self.draw_image("profile_pictures/3.jpg",236,1713)
        self.draw.text((708, 1713), item[0], fill=NAME_COLOR, font=self.font)
        self.draw.text((708, 1829), item[1], fill=BODY_COLOR, font=self.font_body)
        self.draw.text((708, 1897), item[2], fill=BODY_COLOR, font=self.font_body)
        self.draw_multi_line(708,1997,item[3])


    def save(self, page_number):
        self.img.save("output/%s.png"%(page_number,))

    def draw_image(self,image,pos_x,pos_y):
        profile_picture = Image.open(image)
        profile_picture = profile_picture.resize((355,355))
        self.img.paste(profile_picture, (pos_x, pos_y))

    def draw_multi_line(self,start_x,start_y,text):
        margin = start_x
        offset = start_y
        for line in textwrap.wrap(text, width=40):
            self.draw.text((margin, offset), line, font=self.font_body, fill=BODY_COLOR)
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