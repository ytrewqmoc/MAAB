from bs4 import BeautifulSoup

with open("weather.html", "r") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")

table_body = soup.find("tbody")
rows = table_body.find_all("tr")

weather_data = []
for row in rows:
    columns = row.find_all("td")
    day = columns[0].text.strip()
    temperature = ''.join(filter(str.isdigit, columns[1].text))  # Extract only numeric characters
    temperature = int(temperature)
    condition = columns[2].text.strip()

    weather_data.append({"day": day, "temperature": temperature, "condition": condition})

print("Weather Data:")
for entry in weather_data:
    print(f"Day: {entry['day']}, Temperature: {entry['temperature']}°C, Condition: {entry['condition']}")

max_temp = max(entry["temperature"] for entry in weather_data)
hottest_days = [entry["day"] for entry in weather_data if entry["temperature"] == max_temp]
print(f"\nHottest Day(s): {', '.join(hottest_days)} ({max_temp}°C)")

sunny_days = [entry["day"] for entry in weather_data if entry["condition"].lower() == "sunny"]
print(f"Sunny Days: {', '.join(sunny_days)}")

total_temperature = sum(entry["temperature"] for entry in weather_data)
average_temperature = total_temperature / len(weather_data)
print(f"\nAverage Temperature for the Week: {average_temperature:.2f}°C")
