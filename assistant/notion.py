
from . import secret
import json 
import requests
from .param_db import NotionSynthavoParamDB as synthavodb
from .param_db import NotionPrivateParamDB as privatedb


class NotionBase(object):
     
    def __init__(self, db_id, token) -> None:
        
        self.url = url = "https://api.notion.com/v1/pages"
        self.db_id = db_id
        self.token = token

        self.headers = headers = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json",
            "Notion-Version": "2021-05-13"
        }

     
class NotionPrivate(NotionBase):
     
    def __init__(self, db_id, token) -> None:
        super().__init__(db_id, token)

           
    def add_db_today(self, text):
        self.add_db_entry(text, privatedb.status_today)


    def add_db_default(self,text):
        self.add_db_entry(text, privatedb.STATUS_DEFAULT)

    def add_db_entry(self, text,status):
            data = {
                "parent": { "database_id": self.db_id},
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

            response = requests.request("POST", self.url, headers=self.headers, data=data)

            print(response)

class NotionSynthavo(NotionBase):
     
    def __init__(self, db_id, token) -> None:
          super().__init__(db_id, token)

    def standard_processing(self,text_in_Block):
    
        start_strings = text_in_Block.split(" ")[:2]

        status_mapping = {
            "hr": synthavodb.status_HR,
            "dev": synthavodb.status_Dev,
            "sales": synthavodb.status_Sales
        }
        prio_mapping = {
            "aa": synthavodb.PRIO_TODAY,
            "a" : synthavodb.PRIO_HIGH,
            "b": synthavodb.PRIO_MID,
            "c": synthavodb.PRIO_LOW
        }

        selected_status = None
        selected_prio = None

        for status in status_mapping:
            if status in start_strings:
                selected_status = status_mapping[status]

                #remove status from the string
                if status == start_strings[0]:
                    text_in_Block = text_in_Block[len(status) + 1:]
                elif status == start_strings[1]:
                    text_in_Block = text_in_Block[:len(start_strings[0]) + 1] +  text_in_Block[len(start_strings[0]) + 1 + len(status) + 1:]
                break

        

        start_strings = text_in_Block.split(" ")[:1]

        for prio in prio_mapping:
            if prio in start_strings:
                selected_prio = prio_mapping[prio]

                #remove prio from the string
                text_in_Block = text_in_Block[len(prio) + 1:]
                break
        
        #if not found, select defaults
        if selected_status is None:
            selected_status = synthavodb.STATUS_DEFAULT
        if selected_prio is None:
            selected_prio = synthavodb.PRIO_DEFAULT 

        data = {
            "parent": { "database_id": self.db_id},
            "properties": {
                "Name": {
                    "title": [
                        {
                            "text":{
                                "content": text_in_Block
                            }
                        }
                    ]
                },
                "Status": selected_status,
                "Prio": selected_prio
            }
        }


        data = json.dumps(data)

        response = requests.request("POST", self.url, headers=self.headers, data=data)

        if(response.status_code != 200):
            print(f"response: {response.status_code}")
            print(response.text)
            waiting = input()
        else:
            print("200")

        
