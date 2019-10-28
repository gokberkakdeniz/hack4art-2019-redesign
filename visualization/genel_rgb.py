#!/usr/bin/env python3

from pandas import DataFrame, read_csv
import pandas as pd

df = pd.read_csv(r"data.csv", delimiter=";")
df.columns = ["servis_adi", "servis_turu", "tarih", "meslek", "cinsiyet", "temas_oncesi", "temas_sonrasi", "aseptik_oncesi", "sivi_sonrasi", "temas_cevresi"]
#print(df.query("meslek == 'Hemşire'")["temas_oncesi"].value_counts())
df = df.sort_values('tarih')
# from tkinter import *
from PIL import Image, ImageDraw
edge = 100
row = int(len(df.values) ** 0.5)
column = row

canvas_height = row * edge
canvas_width = column * edge

#master = Tk()
#
#w = Canvas(master, 
#           width=canvas_width, 
#           height=canvas_height)
#w.pack()
i = 0
k = 0

image1 = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))
draw = ImageDraw.Draw(image1)
temp = df.values[0][2]
for ci in range(row):
    for ri in range(column):
        r, g, b = 255, 255, 255
        data = df.values[i]
        if data[5] in ["Yok"]:
            r = r - 125
        if data[6] in ["Yok"]:
            r = r - 125
        if data[7] in ["Yok"]:
            g = g - 125
        if data[8] in ["Yok"]:
            g = g - 125
        if data[9] in ["Yok"]:
            b = b - 200
#       beyaz --> birey her durumda el hijyenine dikkat ediyor
#       açık mavi ve turkuaz --> hasta ile temas öncesi ve sonrası ellerini temizlemiyor diğer durumlarda temizliyor
#       lacivert --> normalde elini temizlemeyenler ama hasta çevresi ile temastan sonra da temizleyenler(sayısı bir hayli az)
#       kırmızı ve turuncu - hasta ile temasta elini temizliyor ama onun haricinde temizlemiyor
#       sarı --> normalde elini temizliyor ama hasta çevresi ile temastan sonra elini temizlemiyor (diğer verilere göre fazla bir oranda)
#       koyulaşan yeşil --> aseptik işlemler ve vücut sıvılarına dikkat ediyor fakat hasta ve çevresinin hijyenine dikkat etmiyor
#       kahverengi ve siyah --> neredeyse hiç bir durumda el hijyenine dikkat etmiyor
        color = "#%02x%02x%02x" % (int(r) % 256, int(g) % 256, int(b) % 256)
        i+=1
        #w.create_polygon([ri*edge, ci*edge, (ri+1)*edge, ci*edge, (ri+1)*edge, (ci+1)*edge, ri*edge, (ci+1)*edge], fill=color, width=0)
        draw.polygon([ri*edge, ci*edge, (ri+1)*edge, ci*edge, (ri+1)*edge, (ci+1)*edge, ri*edge, (ci+1)*edge], color)
        k = 0

filename = "genel_rgb.jpg"
image1.save(filename)
# mainloop()