text_in_Block = input()

from assistant.Anki import anki
from assistant.notion import add_db_entry




"""
Ýou need to have a file called "secret.py" in the tools folder:

jo
"""




if __name__ =="__main__":


    text_in_Block = text_in_Block.lower()
    
    if text_in_Block.startswith("anki"): #anki mode
        anki()
    else: #notion mode, default 
        
        add_db_entry(text_in_Block)

