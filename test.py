from time import sleep

import xlwings as xw
import os

def rgbToInt(rgb):
    colorInt:int = rgb[0] + (rgb[1] * 256) + (rgb[2] * 256 * 256)
    return colorInt

filepath = os.getcwd()+'\\test.xlsx'
wb = xw.Book(filepath)
sheet = wb.sheets[0]

TEXT = 'text'
CELL_FILL_COLOR = 'fillcolor'
FONT_STYLE = 'fontstyle'
FONT_COLOR = 'fontcolor'
FONT_SIZE = 'fontsize'

red = rgbToInt((230,0,0))
green = rgbToInt((0,230,0))
yellow = rgbToInt((204,204,0))
print("got values")
print("clearing values")
#wb.app.screen_updating = False
print("updating color green")
sheet.range('A1').api.Cells.interior.Color = red
d = [{TEXT:'hello',CELL_FILL_COLOR:red,FONT_COLOR:yellow,FONT_STYLE:"Bold Italic",FONT_SIZE:14},
     {TEXT:'this',CELL_FILL_COLOR:yellow,FONT_COLOR:red,FONT_STYLE:"Bold",FONT_SIZE:12},
     {TEXT:'test',CELL_FILL_COLOR:None,FONT_COLOR:red,FONT_STYLE:"Regular",FONT_SIZE:11}]

l = ('C7','D7','E7')
for i in range(3):
    t = sheet.range(l[i])
    if d[i][CELL_FILL_COLOR] == None:
        t.api.Cells.interior.ColorIndex = 0
    else:
        t.api.Cells.interior.Color = d[i][CELL_FILL_COLOR]
    t.api.Font.Color = d[i][FONT_COLOR]
    t.api.Font.FontStyle = d[i][FONT_STYLE]
    t.api.Font.Size = d[i][FONT_SIZE]
    t.value = d[i][TEXT]


print("finised yello")
#wb.app.screen_updating = True
wb.save(filepath)
print
