#!/usr/bin/env python3

from pandas import DataFrame, read_csv
import pandas as pd
# from tkinter import *
from PIL import Image, ImageDraw

df = pd.read_csv(r"data.csv", delimiter=";")
df.columns = ["servis_adi", "servis_turu", "tarih", "meslek", "cinsiyet", "temas_oncesi", "temas_sonrasi", "aseptik_oncesi", "sivi_sonrasi", "temas_cevresi"]
df = df.sort_values('tarih').query("meslek == 'Hasta Bakıcı'")

edge = 50
row = int(len(df.values) ** 0.5)
column = row

canvas_height  = row * edge
canvas_width = column * edge

# master = Tk()

# w = Canvas(master, 
#            width=canvas_width, 
#            height=canvas_height)
# w.pack()
i = 0
k = 0

image1 = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))
draw = ImageDraw.Draw(image1)

for ci in range(row):
    for ri in range(column):
        r, g, b = 255, 255, 255
        data = df.values[i]

        if data[5] in ["Yok"]:
            k = k + 1 
        if data[6] in ["Yok"]:
            k = k + 1
        if data[7] in ["Yok"]:
            k = k + 1
        if data[8] in ["Yok"]:
            k = k + 1
        if data[9] in ["Yok"]:
            k = k + 1

        color = {"0": "#e5cdd4", "1": "#c18a9b", "2": "#b0697f", "3": "#753e4f", "4": "#542c38", "5": "#321a22"}        # r, g, b = r + 5, g + 5, b + 5

        # w.create_polygon([ri*edge, ci*edge, (ri+1)*edge, ci*edge, (ri+1)*edge, (ci+1)*edge, ri*edge, (ci+1)*edge], fill=color[str(k)], width=0)
        draw.polygon([ri*edge, ci*edge, (ri+1)*edge, ci*edge, (ri+1)*edge, (ci+1)*edge, ri*edge, (ci+1)*edge], fill=color[str(k)])
        k = 0
        i+=1

filename = "meslek_hbakici.jpg"
image1.save(filename)

# mainloop()