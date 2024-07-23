from . import secret

import json 
import requests
from .param_db import NotionSynthavoParamDB as synthavodb
from .param_db import NotionPrivateParamDB as privatedb
from .param_db import NotionTorrParamDB as torrdb




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
     
    def __init__(self) -> None:
        db_id = secret.notion_private_db_id
        token = secret.notion_private_token
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

            #print(response)
            
    def _privateNotion_inner(self,text):
        from Assistant import Assistant
        
        text = text[len(text.split(" ")[0]) +1:] # remove first word 
        split = text.split(" ")
        if len(split) > 1:
            second_word = split[1]
            inner_trigger_dict = {
                "aa":self.add_db_today,
                "a":self.add_db_default,
            }
            
            return Assistant.run_function_dict(text,inner_trigger_dict, second_word,self.add_db_default)
        return self.add_db_default(text)

class NotionTorr(NotionBase):
    def __init__(self) -> None:
        db_id = secret.notion_torr_db_id
        token = secret.notion_torr_token
        super().__init__(db_id, token)

    def standard_processing(self,text_in_Block):

        prio_mapping = {
            "aa": torrdb.PRIO_TODAY,
            "a" : torrdb.PRIO_HIGH,
            "b": torrdb.PRIO_MID,
            "c": torrdb.PRIO_LOW,
            "now":torrdb.PRIO_NOW,
            "fast":torrdb.PRIO_FAST

        }
        selected_prio = None



        start_strings = text_in_Block.split(" ")[:1]

        for prio in prio_mapping:
            if prio in start_strings:
                selected_prio = prio_mapping[prio]

                #remove prio from the string
                text_in_Block = text_in_Block[len(prio) + 1:]
                break
        
 
        if selected_prio is None:
            selected_prio = torrdb.PRIO_DEFAULT 

        data = {
            "parent": { "database_id": self.db_id},
            "properties": {
                "Description":{
                    'id': 'title', 'type': 'title', 'title': [{'type': 'text', 'text': {'content': text_in_Block, 'link': None}, 'annotations': {'bold': False, 'italic': False, 'strikethrough': False, 'underline': False, 'code': False, 'color': 'default'}, 'plain_text': text_in_Block, 'href': None}]},
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
            #print("200")
            return

        

    

    
class NotionSynthavo(NotionBase):
     
    def __init__(self) -> None:
        db_id = secret.notion_synthavo_db_id
        token = secret.notion_synthavo_token
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

            
        
