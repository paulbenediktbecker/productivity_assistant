text_in_Block = input()

from assistant.Anki import anki
from assistant.notion import add_db_default, add_db_today
from assistant.spotify import spotify


"""
Ýou need to have a file called "secret.py" in the assistant folder:

token = ""
db_id = ""
"""


def handle_spotify_list(text):
    second_word = text.split(" ")[0]

    inner_trigger_dict={
    "bb":spotify.play_beckersbeste, 
    "study":spotify.play_studdybuddy,
    "adhd": spotify.play_adhd
    }
    
    if second_word in inner_trigger_dict:
        inner_trigger_dict[second_word]()
    else:
        spotify.choose_playlist()



def help(text):
    for x in trigger_action_dict:print(x)

trigger_action_dict = {
    "anki": anki,
    "aa": add_db_today,
    "a":add_db_default,
    "next":spotify.next_track,
    "previous":spotify.prev_track,
    "prev": spotify.prev_track,
    "list":handle_spotify_list,
    "shuffle":spotify.shuffle,
    "shuffle off":spotify.shuffle_off,
    "appointment":None,
    "help":help,

}



default_action = add_db_default




if __name__ =="__main__":


    text = text_in_Block.lower()
    startword = text.split(" ")[0]
    
    if startword in trigger_action_dict:
        trigger_action_dict[startword](text)
    else:
        default_action(text)

