import requests
import json, os
from dotenv import load_dotenv


load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

spoonacular_key=os.environ.get("SPOONACULAR_KEY")
endpoint = 'https://spoonacular-recipe-food-nutrition-v1.p.mashape.com/'
url = endpoint + 'recipes/findByIngredients'

params = {
  'fillIngredients': False,
  'ingredients': 'apples, beef, flour, sugar',
  'limitLicense': False,
  'number': 5,
  'ranking': 1
}

headers={
  "X-Mashape-Key": spoonacular_key,
  "Accept": "application/json"
}

response = requests.get(url, params=params, headers=headers)

for r in response.json():
  print r
  print