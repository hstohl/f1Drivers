from bs4 import BeautifulSoup
import requests
from collections import defaultdict

scoring = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]  # Points for positions 1-10
year = 1950

driver_points = defaultdict(int)

while year <= 2024:
    url = f'https://www.formula1.com/en/results/{year}/drivers'  # Replace with your target URL
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    driver_first_names = soup.find_all('span', class_='max-lg:hidden')
    driver_last_name = soup.find_all('span', class_='max-md:hidden')

    # Print each matching span
    i = 0
    for first, last in zip(driver_first_names, driver_last_name):
        name = f"{first.text.strip()} {last.text.strip()}"

        if i >= len(scoring):
            points_earned = 0
        else:
            points_earned = scoring[i]
        i += 1

        driver_points[name] += points_earned
    year += 1


# Print results
for item in sorted(driver_points.items(), key=lambda x: x[1], reverse=True):
    print(item)