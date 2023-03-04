import requests
from bs4 import BeautifulSoup
import csv

# Fetch the web page
url = "https://www.pro-football-reference.com/years/1948/games.htm"
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table
table = soup.find('table', {'id': 'games'})

# Create a list to hold the data
data = []
rows=table.find_all('tr')

# Find the table rows
for row in rows[1:]:
    #print(row)
    # Skip header rows 
    #if 'thead' in row.get('class', []):
    #    continue
    
    # Get the cells in the row
    wk_cell = row.find('th')
    other_cells = row.find_all('td')
    #print(cells)
    if len(other_cells) == 0:
        continue
    # Extract the data from the cells
    week = wk_cell.text.strip()
    date = other_cells[1].text.strip()
    if date == 'Playoffs':
        continue
    year = date[:4]
    time = other_cells[2].text.strip()
    href = other_cells[6].find('a')['href']
    
    # Add the data to the list
    data.append([year, week, date, time, href])
    
# Write the data to a CSV file
with open('games.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Year', 'Week', 'Date', 'Time', 'href'])
    writer.writerows(data)
