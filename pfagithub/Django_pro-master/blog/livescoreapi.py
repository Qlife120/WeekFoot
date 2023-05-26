import requests

def fetch_live_scores():
    url = "https://v3.football.api-sports.io/"  # Replace with the actual API endpoint
    api_key = "67372e25d2a670aee9fa8de68afe630b"  # Replace with your API key
    api_secret = ""  # Replace with your API secret

    headers = {
        "Authorization": f"APIKey {api_key}:{api_secret}"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            live_scores = response.json()
            return live_scores
        else:
            print("Failed to fetch live scores. Status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error occurred while fetching live scores:", e)
    
    return None

# Call the function to fetch live scores
scores = fetch_live_scores()

if scores:
    # Process the live scores data
    for score in scores:
        print(score)
else:
    print("Failed to fetch live scores.")