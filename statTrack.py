import requests
from bs4 import BeautifulSoup
import json

#stat scrape parameters
url = "https://www.nihlnational.com/stats/teams?id_season=4&id_stage=1#main-section"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

#find the table
table = soup.find("table" , class_="styled align-middle")

#get table headers
header_tags = table.find("th").find_all("tr")
keys = [th.get_text(strip=True) for th in header_tags]

thead = table.find("thead")
if thead:
    keys = [th.get_text(strip=True) for th in thead.find_all("th")]
else:
    keys = [th.get_text(strip=True) for th in table.find_all("th")]

#iterate through table rows and extract data
standings = []
rows = table.find("tbody").find_all("tr")

for index, row in enumerate(rows, start=1): 
    cells = row.find_all("td")
    if not cells:
        continue

    #get text from cells
    row_data = [cell.get_text(strip=True) for cell in cells]

    #dictionary for each row
    stats_entry = dict(zip(keys, row_data))

    #Fix for rank in league not coming through. 
    if "Rank" not in stats_entry:
        stats_entry["Rank"] = index
    standings.append(stats_entry)

#write to json
with open("stats.json", 'w') as f:
    json.dump(standings, f, indent=4)

#success message
print(f"Done! Scraped stats for {len(standings)} teams.")
