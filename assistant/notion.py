
from . import secret
import json 
import requests

url = "https://api.notion.com/v1/pages"

headers = {
    "Authorization": "Bearer " + secret.token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


status_todo = {
                "id":"^OE@",
                "type":"select",
                "select":{
                    "id":"1"
                    ,"name":"To Do",
                    "color":"red"}
            }

status_today = {
      "id": "^OE@",
      "type": "select",
      "select": {
        "id": "9b329245-fc7d-4257-97d4-0cda03c24dda",
        "name": "TODAY",
        "color": "blue"
      }
    }

status = {
            'id': '%5EOE%40', 
            'type': 'select', 
            'select': {
                'id': '1',
                'name': 'To Do', 
                'color': 'green'
            }
        }

def add_db_entry(text):
        data = {
            "parent": { "database_id": secret.db_id},
            "properties": {
                "Task": {
                    "title": [
                        {
                            "text":{
                                "content": text
                            }
                        }
                    ]
                },
                "Kategorie": status
            }

        }


        data = json.dumps(data)

        response = requests.request("POST", url, headers=headers, data=data)

        #if(response.status_code != 200):
            #print(f"response: {response.status_code}")
            #print(response.text)
            #waiting = input()

        print(response)