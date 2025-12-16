import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.unrivaled.basketball/stats/team'

response=requests.get(url)
response.encoding='utf-8'

if response.status_code==200:
    html=response.text

soup=BeautifulSoup(html, 'html.parser')
table=soup.find('table')
rows=[]
for row in table.find_all('tr'):
    cells=[]
    cells_a_row=row.find_all(['th', 'td'])
    for td in cells_a_row:
        text=td.get_text(strip=True)
        cells.append(text)
    if cells:
        rows.append(cells)

df=pd.DataFrame(rows[1:], columns=rows[0])
stats_columns=['GP', 'PTS', 'OR', 'DR', 'REB', 'AST', 'STL', 'BLK', 'TO', 'PF']
for column in stats_columns:
    df[column]=pd.to_numeric(df[column], errors='coerce')

df.to_csv('unrivaled_2025_team_stats.csv', index=False)

print(df.head())