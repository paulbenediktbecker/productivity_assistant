
"""
Ýou need to have a file called "secret.py" in the assistant folder:

token = ""
db_id = ""
"""

class Assistant(object):
    
    def __init__(self) -> None:
        self.trigger_action_dict = {
            # works_isolated -> does the function need further input?
            # if True: is run directly in subprocess
            #if False: preaction with input will be handled
            "anki": {
                "action":self.run_anki,
                "works_isolated": True
            },
            "next": {
                "action":self.run_next_track,
                "works_isolated": True
            },
            "n":{
                "action":self.run_next_track,
                "works_isolated": True
            },
            "previous":{
                "action":self.run_prev_track,
                "works_isolated": True
            },
            "prev": {
                "action":self.run_prev_track,
                "works_isolated": True
            },
            "list":{
                "action":self.run_spotify_inner,
                "works_isolated": False,
                "pre_action":None,
            },
            "shuffle":{
                "action":self.run_shuffle,
                "works_isolated": True
            },
            "shuffleoff":{
                "action":self.run_shuffle_off,
                "works_isolated": True
            },
            "appointment":{
                "action":None,
                "works_isolated": True
            },
            "help":{
                "action":self.run_help,
                "works_isolated": False
            },
            "launch":{
                "action":None, # launch apps, if already open, open that window,
                "works_isolated": True
            },
            "priv":{
                "action":self.run_notion_private_inner,
                "works_isolated": True
            },
            "playlistname":{
                "action": self.run_play_playlist_by_keyword,
                "works_isolated": True,
            },
            "playlistindex":{
                "action": self.run_play_playlist_by_id,
                "works_isolated": True,
            },
        } 
        self.default_action = self.run_notion_synthavo_standard_processing
    
    def run(self,text_in_Block):
        text = text_in_Block.lower()
        startword = text.split(" ")[0]
        
        Assistant.run_function_dict(text, self.trigger_action_dict, startword, self.default_action)
        
    def works_input_isolated(self, text):
        text = text.lower()
        startword = text.split(" ")[0]
        if startword in self.trigger_action_dict:
            is_isolated =  self.trigger_action_dict[startword]["works_isolated"]
            
            if is_isolated:
                action = None
            else:
                action = self.trigger_action_dict[startword]["action"]
        else:
            is_isolated = True#standard action works isolated
            action = None
        return  is_isolated, action

    def return_action(self,keyword):
        return self.trigger_action_dict[keyword]["action"]()
    
    def run_function_dict(text,dic, keyword, default_action):
        if keyword in dic:
            return dic[keyword]["action"](text)
        else:
            return default_action(text)
        
    def run_anki(self, text):
        from assistant.Anki import anki
        return anki(text)
    
    def run_next_track(self,text):
        from assistant.spotify import spotify
        return spotify.next_track(text)
    
    def run_prev_track(self,text):
        from assistant.spotify import spotify
        return spotify.prev_track(text)
    
    def run_spotify_inner(self,text):
        from assistant.spotify import spotify
        return spotify._spotify_inner(text)
    
    def run_shuffle(self,text):
        from assistant.spotify import spotify
        return spotify.shuffle(text)
    
    def run_shuffle_off(self,text):
        from assistant.spotify import spotify
        return spotify.shuffle_off(text)
    
    def run_play_playlist_by_id(self,text):
        from assistant.spotify import spotify
        return spotify.play_playlist_by_index(text)
    
    def run_play_playlist_by_keyword(self,text):
        from assistant.spotify import spotify
        return spotify.play_playlist_by_keyword(text)
    
    def run_notion_synthavo_standard_processing(self,text):
        from assistant.notion import NotionSynthavo
        return NotionSynthavo().standard_processing(text)
    
    def run_notion_private_inner(self,text):
        from assistant.notion import NotionPrivate
        return NotionPrivate()._privateNotion_inner(text)
    
    def run_help(self,text):
        print("_________________________________________________")
        for x in self.trigger_action_dict:
            print(x)
        print("_________________________________________________")
        input("Enter to exit.")
        
    
    
    
        
        

if __name__ =="__main__":
    DEBUG = False
    
    if not DEBUG:
        import argparse
        parser = argparse.ArgumentParser("simple_example")
        parser.add_argument("input", help="An integer will be increased by 1 and printed.", type=str)
        args = parser.parse_args()
        text = args.input
        Assistant().run(text)
    else:
        query = "priv holaa"
    
        Assistant().run(query)

    
   
   

