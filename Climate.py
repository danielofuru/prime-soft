import requests
import matplotlib.pyplot as plt

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# Function to analyze weather data
def analyze_weather(weather_data):
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    weather_desc = weather_data['weather'][0]['description']

    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
    print(f"Weather Description: {weather_desc}")

    # Visualize the data (e.g., temperature)
    plt.bar(['Temperature'], [temperature], color='skyblue')
    plt.ylabel('Temperature (°C)')
    plt.title('Current Temperature')
    plt.show()

# Main function
def main():
    # Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
    api_key = 'YOUR_API_KEY'
    city = input("Enter city name: ")
    weather_data = fetch_weather_data(api_key, city)

    if weather_data['cod'] == 200:
        analyze_weather(weather_data)
    else:
        print("City not found. Please enter a valid city name.")

if __name__ == "__main__":
    main()
