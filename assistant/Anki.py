from . import picture_fetcher
import json

import urllib.request
from urllib.error import URLError

import copy
import clipboard
from progress.bar import IncrementalBar

class Card:
    def __init__(self, head):
        self.head = head
        self.content = ""
        self.picture_links = []
    def __str__(self):
        return(self.head + "\n" + self.content + "\n" + self.picture_links)



def parse_cards(data, pic_fetcher):
    cards = []
    start_of_picture_row = "![Untitled]"
    
    for counter, row in enumerate(data) :
        if row != '    \r' and row != '\r': # filter empty lines
            #print(repr(row))
            #print("------------------------------------")


            if row.startswith("-"): #these are the headings of the cards
                row = row[1:]
                if counter != 0:
                    cards.append(current_card)
                current_card = Card(row)
            
            else:
                if start_of_picture_row in row:
                    pic_url = pic_fetcher.get_picture_url_of_block(row,current_card.head)
                    current_card.picture_links.append(pic_url)
                else:
                    current_card.content = current_card.content + "<div>" + row + "</div>"
    cards.append(current_card)
    return cards





    
    



def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    try:
        response = json.load(urllib.request.urlopen(urllib.request.Request('http://localhost:8765', requestJson)))

        if len(response) != 2:
            raise Exception('response has an unexpected number of fields')
        if 'error' not in response:
            raise Exception('response is missing required error field')
        if 'result' not in response:
            raise Exception('response is missing required result field')
        if response['error'] is not None:
            raise Exception(response['error'])
        return response['result']
    except URLError:
        print("ANKI NOT ONLINE !")

def choose_deck(decks):
    
    print("Choose ANKI deck:")
    for index, deck in enumerate(decks): print(f"{index}: {deck}")
    chosen_one = input()
    try:
        ret = int(chosen_one)
        if ret >= len(decks) or ret < 0 :
            return choose_deck(decks)
        else: 
            return ret 
    except: 
        return choose_deck(decks)

def send_card_to_anki(deckname, front, back, pic_urls):
    pictures = []
    picture_base = {
                "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/A_black_cat_named_Tilly.jpg/220px-A_black_cat_named_Tilly.jpg",
                "filename": "some_thing.jpg",
                "fields": [
                    "Back"
                ]
            }
    
        
    for pic_url in pic_urls:
        base = copy.deepcopy(picture_base)
        base["url"] = pic_url
        base["filename"] = str(hash(pic_url)) + ".jpg"
        pictures.append(base)

    
        
    
    API_base = {
        "action": "addNote",
        "version": 6,
        "params": {
            "note": {
                "deckName": deckname,
                "modelName": "Basic-7b116",
                "fields": {
                    "Front": front,
                    "Back": back
                },
                "options": {
                    "allowDuplicate": False,
                    "duplicateScope": "deck",
                    "duplicateScopeOptions": {
                        "deckName": deckname,
                        "checkChildren": False,
                        "checkAllModels": False
                    }
                },
                "picture" : pictures
            }
        }
    }
    result = invoke(API_base["action"],  **API_base["params"])

def create_all_cards(cards,decks,chosen_deck):
    bar = IncrementalBar('Creating Cards...', max=len(cards))
    for card in cards:
        send_card_to_anki(decks[chosen_deck], card.head, card.content,card.picture_links)
        bar.next()
    bar.finish()

def get_clipboard():
    return clipboard.paste()

def anki(text):
    data = get_clipboard()
    data = data.split("\n") # split by line

    pic_fetcher = picture_fetcher()
    cards = parse_cards(data,pic_fetcher)

    decks = invoke('deckNames') 
    chosen_deck = choose_deck(decks)

    create_all_cards(cards,decks,chosen_deck)

    

    while(True):
        input("Press Enter to paste Clipboard again.")
        data = get_clipboard()
        data = data.split("\n")  # split by line
        cards = parse_cards(data,pic_fetcher)
        create_all_cards(cards, decks, chosen_deck)