
from . import secret
import json 
import requests

url = "https://api.notion.com/v1/pages"

headers = {
    "Authorization": "Bearer " + secret.token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


           
def add_db_today(text):
    status_today = {
        "id": "^OE@",
        "type": "select",
        "select": {
            "id": "9b329245-fc7d-4257-97d4-0cda03c24dda",
            "name": "TODAY",
            "color": "blue"
        }
    }
    add_db_entry(text, status_today)


def add_db_default(text):

    status = {
                'id': '%5EOE%40', 
                'type': 'select', 
                'select': {
                    'id': '1',
                    'name': 'To Do', 
                    'color': 'green'
                }
            }
    
    add_db_entry(text, status)

def add_db_entry(text,status):
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