import os
import json
from watson_developer_cloud import ConversationV1
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

conversation_client = ConversationV1(
    username=os.environ.get("CONVERSATION_USERNAME"),
    password=os.environ.get("CONVERSATION_PASSWORD"),
    version='2016-07-11')

workspace_id = '93054028-2b0b-4b21-9bc1-ec8c48970dbb'

context = {
  'conversation_id': '1b7b67c0-90ed-45dc-8508-9488bc483d5b',
  'system': {
    'dialog_stack': ['root'],
    'dialog_turn_counter': 1,
    'dialog_request_counter': 1
  }
}

response = conversation_client.message(
  workspace_id=workspace_id, 
  message_input={'text': 'i want to cook'}, 
)

print(json.dumps(response, indent=2))
print
print
print response['output']['text'][0]