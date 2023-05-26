import requests

def get_football_news(api_key):
    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': 'football',
        'apiKey': api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        articles = data['articles']
        return articles
    else:
        return None

