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
    val = round(val)
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
    val = round(val)
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
    val = round(val)
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
    val = round(val)
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
    val = round(val)
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
    val = round(val)
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
    val = round(val)
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

for i in range (0, length):
    name = left2_df['Player Name'].iloc[i]
    appendname(name)
    left2(left2_df['percent'].iloc[i], name)
    left3(left3_df['percent'].iloc[i], name)
    top3(top3_df['percent'].iloc[i], name)
    top2(top2_df['percent'].iloc[i], name)
    right2(right2_df['percent'].iloc[i], name)
    right3(right3_df['percent'].iloc[i], name)
    totalclose(totalc_df['percent'].iloc[i], name)
