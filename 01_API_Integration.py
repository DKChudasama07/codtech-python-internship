# CODTECH INTERNSHIP - TASK 1
# Simple Weather Data Fetcher and Visualizer


import requests
import matplotlib.pyplot as plt

print("=== WEATHER DATA DASHBOARD ===")
print("Welcome! Let's fetch some weather data and make cool charts!")

# Your API key from OpenWeatherMap (get it free from openweathermap.org)
api_key = "add546b3547cb5f359e26fbc92a544f4"  # Your OpenWeatherMap API key

def get_weather(city):
    """Get weather data for a city"""
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200:
            return {
                'city': city,
                'temp': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description']
            }
        else:
            print(f"Error getting data for {city}")
            return None
    except:
        print(f"Failed to get data for {city}")
        return None

# Let user choose cities or use default ones
print("\nChoose cities to compare:")
print("1. Use default cities (New York, London, Tokyo, Mumbai)")
print("2. Enter your own cities")

choice = input("Enter 1 or 2: ")

if choice == "2":
    cities = []
    print("Enter city names (press Enter after each city, type 'done' to finish):")
    while True:
        city = input("City name: ")
        if city.lower() == 'done':
            break
        if city:
            cities.append(city)
else:
    cities = ["New York", "London", "Tokyo", "Mumbai"]

print(f"\nFetching weather data for: {', '.join(cities)}")

# Get weather data for all cities
weather_data = []
for city in cities:
    print(f"Getting data for {city}...")
    data = get_weather(city)
    if data:
        weather_data.append(data)
        print(f"✓ {city}: {data['temp']}°C, {data['description']}")

if not weather_data:
    print("No weather data found! Check your API key.")
    exit()

print(f"\n=== Got data for {len(weather_data)} cities! ===")

# Show what we found
print("\nCURRENT WEATHER:")
for data in weather_data:
    print(f"{data['city']}: {data['temp']}°C, {data['humidity']}% humidity, {data['description']}")

# Create simple charts
print("\nCreating charts...")

# Chart 1: Temperature comparison
plt.figure(figsize=(10, 6))
cities_list = [data['city'] for data in weather_data]
temps = [data['temp'] for data in weather_data]

bars = plt.bar(cities_list, temps, color=['red', 'blue', 'green', 'orange', 'purple'])
plt.title('Temperature Comparison', size=16)
plt.ylabel('Temperature (°C)')
plt.xlabel('Cities')

# Add temperature numbers on top of bars
for i, temp in enumerate(temps):
    plt.text(i, temp + 0.5, f'{temp}°C', ha='center')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 2: Humidity comparison
plt.figure(figsize=(10, 6))
humidity = [data['humidity'] for data in weather_data]

plt.bar(cities_list, humidity, color=['lightblue', 'lightgreen', 'lightcoral', 'lightyellow', 'lightpink'])
plt.title('Humidity Comparison', size=16)
plt.ylabel('Humidity (%)')
plt.xlabel('Cities')

# Add humidity numbers on bars
for i, hum in enumerate(humidity):
    plt.text(i, hum + 1, f'{hum}%', ha='center')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Chart 3: Temperature vs Humidity scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(temps, humidity, s=100, c=['red', 'blue', 'green', 'orange', 'purple'])

# Add city names next to points
for i, city in enumerate(cities_list):
    plt.text(temps[i], humidity[i] + 1, city, ha='center')

plt.title('Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Show summary
print("\n=== SUMMARY ===")
hottest = max(weather_data, key=lambda x: x['temp'])
most_humid = max(weather_data, key=lambda x: x['humidity'])

print(f"🌡️  Hottest city: {hottest['city']} ({hottest['temp']}°C)")
print(f"💧 Most humid city: {most_humid['city']} ({most_humid['humidity']}%)")

print("\n✅ Task 1 Complete!")
print("You successfully:")
print("- Fetched data from OpenWeatherMap API")
print("- Created 3 different charts using matplotlib")
print("- Made an interactive weather dashboard")

# Save data to file (bonus)
try:
    with open('weather_data.txt', 'w') as f:
        f.write("WEATHER DATA REPORT\n")
        f.write("===================\n\n")
        for data in weather_data:
            f.write(f"{data['city']}: {data['temp']}°C, {data['humidity']}% humidity\n")
    print("\n💾 Data saved to 'weather_data.txt'")
except:
    print("Could not save file")

print("\nThanks for using the weather dashboard! 🌤️")