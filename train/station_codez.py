import requests
from bs4 import BeautifulSoup
import json

def scrape_station_data():
	url_template = "http://www.railwaycodes.org.uk/stations/station{}.shtm"
	letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
	station_dict = {}

	for letter in letters:
		url = url_template.format(letter)
		try:
		#if 1==1:
			response = requests.get(url, timeout=10)
			if response.status_code != 200:
				print(f"Skipping {url} (status code {response.status_code})")
				continue

			soup = BeautifulSoup(response.text, "html.parser")
			table = soup.find("table")
			if not table or not table.find("tbody"):
				print(f"No valid table found on {url}")
				continue

			for row in table.find("tbody").find_all("tr"):
				cells = row.find_all("td")
				if len(cells) >= 5:
					station_cell = cells[0].get_text(strip=True)
					station_name1 = str(cells[0]).split('<div ')[0].split('>')[-1]

					if "(" in station_cell and ")" in station_cell:
						crs_code = station_cell.split("(")[1].split(")")[0]
						station_name_raw = station_cell.split(")")[-1].strip()
						station_name = station_name_raw.split("\n")[0].strip()
						if len(station_name) >= 2*len(station_name1) and len(station_name1)>1:
							station_name = station_name1
					else:
						continue

					operator_cell = cells[4]
					operator_summary = operator_cell.find("summary")
					operator = operator_summary.get_text(strip=True) if operator_summary else operator_cell.get_text(strip=True)

					station_dict[crs_code] = {
						"station_name": station_name,
						"operator": operator
					}
		except Exception as e:
			print(f"Error processing {url}: {e}")

	return station_dict

# Scrape and save to JSON
stations = scrape_station_data()
print(f"Total stations scraped: {len(stations)}")

with open("stations.json", "w", encoding="utf-8") as f:
	json.dump(stations, f, ensure_ascii=False, indent=4)

print("Data saved to stations.json")
