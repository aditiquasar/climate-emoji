weather = input("Enter any weather: ").lower()

match weather:
    case "sunny":
        print("☀️") 
    case "rainy":
        print("🌧️") 
    case "cloudy":
        print("☁️")
    case _:
        print("🤷")