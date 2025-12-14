import requests
import pandas as pd

url = "https://stats.wnba.com/stats/leaguedashplayerstats?College=&Conference=&Country=&DateFrom=&DateTo=&Division=&DraftPick=&DraftYear=&GameScope=&GameSegment=&Height=&LastNGames=0&LeagueID=10&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlayerExperience=&PlayerPosition=&PlusMinus=N&Rank=N&Season=2025&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&StarterBench=&TeamID=0&TwoWay=0&VsConference=&VsDivision=&Weight="

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Referer": "https://stats.wnba.com/players/traditional/?PerMode=Totals&sort=PTS&dir=-1"
}

response = requests.get(url, headers=headers)
response.raise_for_status()
data = response.json()

headers_cols = data["resultSets"][0]["headers"]
rows = data["resultSets"][0]["rowSet"]

df = pd.DataFrame(rows, columns=headers_cols)
df.to_csv("../data/raw/wnba_2025_totals.csv", index=False)

print(df)
