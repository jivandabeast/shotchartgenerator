#!/usr/bin/env python3

# A basketball shot chart generator
# Created by Jivan RamjiSingh

from PIL import Image, ImageDraw, ImageFont
import pandas as pd

def df_create(table):
    df = pd.DataFrame.from_dict(table)
    new_header = df.iloc[0]
    df = df[1:]
    df.columns = new_header
    df = df.astype({new_header[1] : 'int32'})
    df = df.astype({new_header[2] : 'int32'})
    df["percent"] = (df[new_header[1]] / df[new_header[2]]).fillna(0)
    df["percent"] = df["percent"] * 100
    return df

def left2(val, filename):
    filename = filename + ".jpg"
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    (x, y) = (184, 404)
    color = 'rgb(0, 0, 0)'                                   
#    val = round(val)
    val = str(val)
    draw.text((x,y), val, fill=color, font=font)
    image.save(filename)                                   

def left3(val, filename):
    filename = filename + ".jpg"
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    (x, y) = (184, 1040)
    color = 'rgb(0, 0, 0)'                                   
#    val = round(val)
    val = str(val)
    draw.text((x,y), val, fill=color, font=font)
    image.save(filename)                                   

def right2(val, filename):
    filename = filename + ".jpg"
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    (x, y) = (1270, 404)
    color = 'rgb(0, 0, 0)'                                   
#    val = round(val)
    val = str(val)
    draw.text((x,y), val, fill=color, font=font)
    image.save(filename)                                   

def right3(val, filename):
    filename = filename + ".jpg"
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    (x, y) = (1270, 1040)
    color = 'rgb(0, 0, 0)'                                   
#    val = round(val)
    val = str(val)
    draw.text((x,y), val, fill=color, font=font)
    image.save(filename)                                   

def top2(val, filename):
    filename = filename + ".jpg"
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    (x, y) = (724, 590)
    color = 'rgb(0, 0, 0)'                                   
#    val = round(val)
    val = str(val)
    draw.text((x,y), val, fill=color, font=font)
    image.save(filename)                                   

def top3(val, filename):
    filename = filename + ".jpg"
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    (x, y) = (724, 1040)
    color = 'rgb(0, 0, 0)'                                   
#    val = round(val)
    val = str(val)
    draw.text((x,y), val, fill=color, font=font)
    image.save(filename)                                   

def totalclose(val, filename):
    filename = filename + ".jpg"
    image = Image.open(filename)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    (x, y) = (724, 295)
    color = 'rgb(0, 0, 0)'                                   
#    val = round(val)
    val = str(val)
    draw.text((x,y), val, fill=color, font=font)
    image.save(filename)                                   

def appendname(val):
    image = Image.open('template.jpg')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=45)
    (x, y) = (1040, 1300)
    color = 'rgb(0, 0, 0)'                                   
    draw.text((x,y), val, fill=color, font=font)
    filename = val + ".jpg"
    image.save(filename)                                   

def getfrac(df, i):
    topval = df.iloc[i, 1]
    bottomval = df.iloc[i, 2]
    return topval, bottomval

df = pd.read_csv("testData.csv", header=None, names=range(3))
table_names = ["Left 2", "Total Close", "Top 2", "Right 2", "Top 3", "Left 3", "Right 3"]
groups = df[0].isin(table_names).cumsum()
tables = {g.iloc[0,0]: g.iloc[1:] for k,g in df.groupby(groups)}

left2_df = df_create(tables["Left 2"])
right2_df = df_create(tables["Right 2"])
left3_df = df_create(tables["Left 3"])
right3_df = df_create(tables["Right 3"])
top2_df = df_create(tables["Top 2"])
top3_df = df_create(tables["Top 3"])
totalc_df = df_create(tables["Total Close"])

length = len(left2_df.index)

#print(left2_df.iloc[6])
#print()
#print(left2_df['percent'].iloc[6])
#print()
#print(left2_df.iloc[6, 3])

#val1, val2 = getfrac(left2_df, 6)
#print(val1, val2)

for i in range (0, length):
    name = left2_df['Player Name'].iloc[i]
    appendname(name)

    val1, val2 = getfrac(left2_df, i)
    left2_val = str(val1) + "/" + str(val2)

    val1, val2 = getfrac(left3_df, i)
    left3_val = str(val1) + "/" + str(val2)

    val1, val2 = getfrac(top3_df, i)
    top3_val = str(val1) + "/" + str(val2)

    val1, val2 = getfrac(top2_df, i)
    top2_val = str(val1) + "/" + str(val2)

    val1, val2 = getfrac(right2_df, i)
    right2_val = str(val1) + "/" + str(val2)

    val1, val2 = getfrac(right3_df, i)
    right3_val = str(val1) + "/" + str(val2)

    val1, val2 = getfrac(totalc_df, i)
    totalc_val = str(val1) + "/" + str(val2)

    
    left2(left2_val, name)
    left3(left3_val, name)
    top3(top3_val, name)
    top2(top2_val, name)
    right2(right2_val, name)
    right3(right3_val, name)
    totalclose(totalc_val, name)




#    left2(left2_df['percent'].iloc[i], name)
#    left3(left3_df['percent'].iloc[i], name)
#    top3(top3_df['percent'].iloc[i], name)
#    top2(top2_df['percent'].iloc[i], name)
#    right2(right2_df['percent'].iloc[i], name)
#    right3(right3_df['percent'].iloc[i], name)
#    totalclose(totalc_df['percent'].iloc[i], name)




