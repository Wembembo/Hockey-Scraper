import requests
from bs4 import BeautifulSoup
import json

# Scrape parameters
url = "https://www.nihlnational.com/schedule?id_season=4&id_team=&id_month=999"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

#empty games list for initialization
game_list = []
#placeholder date until date is found in scrape
current_date = "Unknown Date"


for element in soup.find_all(['h3', 'li']):
    #date finder    
    if element.name == 'h3':
        current_date = element.get_text(strip=True)
        continue

        #game finder
    if element.name == 'li' and 'grid' in str(element.get('class', [])):
        try:
            time_tag = element.find('time')
            game_time = time_tag.get_text(strip=True) if time_tag else "N/A"

            teams = element.find_all('img')
            home_team = teams[0]['alt'] if len(teams) > 0 else "Unknown"
            away_team = teams[1]['alt'] if len(teams) > 1 else "Unknown"

            score_tag = element.find('a', class_=lambda x: x and 'font-bold' in x)
            score = score_tag.get_text(strip=True) if score_tag else "-:-"

            #json structure
            game_list.append({
                "date": current_date,
                "time": game_time,
                "home": home_team,
                "away": away_team,
                "score": score
            })
        except Exception:
            continue

#write to json
with open('games.json', 'w') as f:
    json.dump(game_list, f, indent=4)

#success message
print(f"Done! Scraped {len(game_list)} games.")