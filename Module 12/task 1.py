import requests

def fetch_joke():
    try:
        response = requests.get("https://api.chucknorris.io/jokes/random")
        response.raise_for_status()
        joke = response.get("value").json()
        if joke:
            print(joke)
        else:
            print("Failed to retrieve joke.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

fetch_joke()
