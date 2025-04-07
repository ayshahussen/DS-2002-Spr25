# -*- coding: utf-8 -*-
""".ds2002-lab5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UYtwC1emt8qb3DkpzUhmEacOZBBqDEnJ
"""

import json
import pandas as pd

with open('schacon.repos.json', 'r') as file:
    data = json.load(file)

# extracting the four fields
rows = []
for repo in data[:5]:
    name = repo.get('name', '')
    html_url = repo.get('html_url', '')
    updated_at = repo.get('updated_at', '')
    visibility = repo.get('visibility', '')

    row = f"{name},{html_url},{updated_at},{visibility}"
    rows.append(row)


with open('chacon.csv', 'w') as out_file:
    for row in rows:
        out_file.write(row + '\n')