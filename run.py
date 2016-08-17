import json
import os
import time
from dotenv import load_dotenv
from slackclient import SlackClient
from watson_developer_cloud import ConversationV1

from recipe import RecipeClient
from souschef.souschef import SousChef

if __name__ == "__main__":
  load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

  bot_id = os.environ.get("BOT_ID")

  slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

  conversation_client = ConversationV1(
    username=os.environ.get("CONVERSATION_USERNAME"),
    password=os.environ.get("CONVERSATION_PASSWORD"),
    version='2016-07-11')

  recipe_client = RecipeClient(os.environ.get("SPOONACULAR_KEY"))

  souschef = SousChef(bot_id, 
                      slack_client, 
                      conversation_client,
                      recipe_client)
  souschef.run()