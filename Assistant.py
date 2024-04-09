text_in_Block = input()

from assistant.Anki import anki
from assistant.notion import NotionPrivate, NotionSynthavo
from assistant.spotify import spotify

from assistant import secret
"""
Ýou need to have a file called "secret.py" in the assistant folder:

token = ""
db_id = ""
"""

class Assistant(object):
    
    def __init__(self) -> None:
        self.notion_priv = NotionPrivate(
            secret.notion_private_db_id,
            secret.notion_private_token
        )
        self.notion_synthavo = NotionSynthavo(
            secret.notion_synthavo_db_id,
            secret.notion_synthavo_token
        )
        
        self.trigger_action_dict = {
            "anki": anki,
            "next":spotify.next_track,
            "n":spotify.next_track,
            "previous":spotify.prev_track,
            "prev": spotify.prev_track,
            "list":self._spotify_inner,
            "shuffle":spotify.shuffle,
            "shuffle off":spotify.shuffle_off,
            "appointment":None,
            "help":help,
            "priv":self._privateNotion_inner

        }
        self.default_action = self.notion_synthavo.standard_processing
    
    def run(self):
        text = text_in_Block.lower()
        startword = text.split(" ")[0]
        
        self._run_function_dict(text, self.trigger_action_dict, startword, self.default_action)
    
    def _run_function_dict(self, text,dic, keyword, default_action):
        if keyword in dic:
            dic[keyword](text)
        else:
            default_action(text)
    
    def _spotify_inner(self,text):
        second_word = text.split(" ")[1]

        inner_trigger_dict={
        "bb":spotify.play_beckersbeste, 
        "study":spotify.play_studdybuddy,
        "adhd": spotify.play_adhd
        }
            
        self._run_function_dict(text, inner_trigger_dict, second_word,spotify.choose_playlist)

    def _privateNotion_inner(self,text):
        text = text[len(text.split(" ")[0]) +1:] # remove first word 
        second_word = text.split(" ")[1]
        inner_trigger_dict = {
            "aa":self.notion_priv.add_db_today,
            "a":self.notion_priv.add_db_default,
        }
        
        self._run_function_dict(text,inner_trigger_dict, second_word,self.notion_priv.add_db_default)
        

    def _help(self,text):
        for x in self.trigger_action_dict:
            print(x)

if __name__ =="__main__":
    Assistant().run()

