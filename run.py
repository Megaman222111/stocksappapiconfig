import json
import requests

response = requests.get('https://dashboard.nbshare.io/api/v1/apps/reddit')

arrays = json.loads(response.text)
for array in arrays:
    print(array['ticker'], "|", array['sentiment'], "|", array['sentiment_score'], "|", array['no_of_comments'])