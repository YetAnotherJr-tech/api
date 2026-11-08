import requests
from datetime import datetime

def retrieve_epic_photos(api_key, date_str):
    endpoint_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date_str}"
    params = {"api_key": api_key}

    response = requests.get(endpoint_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Data not received. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    user_date = input("pick a date, any date \n(actually scratch that be reasonable)\n just use the format YYYY-MM-DD (anything past july, 2015): ").strip()

    try:
        parsed_date = datetime.strptime(user_date, "%Y-%m-%d")
    except ValueError:
        print("c'mon man, like an actual date, in the format i specified, stop playing in my face.")
        exit()

    api_key = "DEMO_KEY"
    photos = retrieve_epic_photos(api_key, user_date)

    if photos and len(photos) > 0:
        print(f"\nFound {len(photos)} photos on {user_date}.")

        first_photo = photos[0]
        image_name = first_photo.get("image")
        date_time_str = first_photo.get("date")

        year, month, day = user_date.split("-")
        
        image_url = f"https://epic.gsfc.nasa.gov/archive/natural/{year}/{month}/{day}/png/{image_name}.png"
        
        print(f"\n--- Photo Details ---")
        print(f"Image Title/Name: {image_name}")
        print(f"Capture Timestamp: {date_time_str}")
        print(f"Direct Link to Earth Photo:\n{image_url}")
    else:
        print(f"No photos found for {user_date}. Try a different date.")