from flask import Blueprint
import pandas as pd
import re

# Url of my google sheet file
url = "https://docs.google.com/spreadsheets/d/1J6cpmYgPiFpqX7IGZR4T_WOxrz6l8-yJKFJsozXA7Ng/edit#gid=0"

# url_before = "https://docs.google.com/spreadsheets/d/1J6cpmYgPiFpqX7IGZR4T_WOxrz6l8-yJKFJsozXA7Ng/export?format=csv&gid=0"

# # Pattern to obtain the spreadsheet_id and the sheet_id
# pattern = r"^.+/d/([\w|-]+)/edit#gid=([\d]+)$"

# # Get the spreadsheet_id and sheet_id
# if matches := re.search(pattern, url):
#     spreadsheet_id = matches.group(1)
#     sheet_id = matches.group(2)

pattern = r"(edit#)"

new_url = re.sub(pattern, "export?format=csv&", url)

# Creacion del Data frame
df = pd.read_csv(new_url)

# Cambiar el indice por el nombre
df.index = df["code"]
