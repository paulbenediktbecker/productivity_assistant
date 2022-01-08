from .secret import secret
import json
from PIL import Image
import requests
from io import BytesIO
class picture_fetcher:

    


    def __init__(self):
        self.has_loaded_semester = False
        self.page_id =secret.semester_page_id
        self.token = secret.token
        self.headers = {
            "Authorization": "Bearer " + self.token,
            "Notion-Version": "2021-08-16"
        }

        self.loaded_subpage = None
    
    def get_picture_of_block(self,row,head_of_toggle):
        if self.has_loaded_semester:
            low = row.find("(") +1
            high = row.find(")")
            pic_url = row[low:high]
            toggles = [y for y in self.loaded_subpage["results"] if(y["type"] =="toggle")]
            
            head_of_toggle_replaced = head_of_toggle.replace(" ","")
            chosen_toggle = None #TODO add exception 
            for toggle in toggles: 
                if toggle["toggle"]["text"][0]["plain_text"].replace(" ","") in head_of_toggle_replaced: #does one of the toggles we iterate through has the head of the toggle we search ? 
                    chosen_toggle = toggle
                    break

            #now we have the toggle we were searching for. 
            chosen_toggle_id = chosen_toggle["id"]
            chosen_toggle_children = self.fetch_block(chosen_toggle_id) #this is whats inside the searched toggle. Here we have to search for the picture.
            print("hi")
            images_in_toggle = [y for y in chosen_toggle_children["results"] if(y["type"] == "image")] #all images in the toggle


            # now we want to search for the given "pic_url" in the images of the toggle, to find the searched one. 
            # we cut this url, because the beginning of the 2 url does not match each other. We will do the same operation on the other url. 
            pic_url_cutted = pic_url[pic_url.find(".com"):] 
            
            found_url = None #TODO add exception 
            for image in images_in_toggle: 
                temp_url = image["image"]["file"]["url"]
                temp_url_cutted = temp_url[temp_url.find(".com"):]#cut url, see comments below 

                if pic_url_cutted in temp_url_cutted: 
                    found_url = temp_url
                    break

            # now we have the url of the picture which we can really fetch. Look in the anki API, this can directly fetch the picture. 
            #CONTINUE HERE 
            

            


        else:
            self.load_semester()
            self.get_picture_of_block(row,head_of_toggle)

    # returns a json object, fetched from the notion api with the block id 
    def fetch_block(self, block_id):
        url = f"https://api.notion.com/v1/blocks/{block_id}/children"
        response = requests.request("GET", url, headers=self.headers)
        return json.loads(response.text)
        

    #returns an int corresponding to the index of the chosen subpage 
    def choose_subpage(self,names_of_subpages):
        print("Choose Notion Subpage:")

        for index, subpage_name in enumerate(names_of_subpages): print(f"{index}: {subpage_name}")
        chosen_one = input()
        try:
            ret = int(chosen_one)
            if ret >= len(names_of_subpages) or ret < 0 :
                return self.choose_subpage(names_of_subpages)
            else: 
                return ret 
        except: 
            return self.choose_subpage(names_of_subpages)
    
    def load_semester(self):
        json_semester = self.fetch_block(self.page_id)
        print("Hi")

        semester_page = json_semester["results"]
        ids_of_subpages = [result["id"] for result in semester_page if (result["type"] =="child_page" )] #get all ids ob the subpages
        names_of_subpages = [result["child_page"]["title"] for result in semester_page if (result["type"] =="child_page" )] #get all ids ob the subpages 

        choosen_subpage_index = self.choose_subpage(names_of_subpages)        
        self.loaded_subpage = self.fetch_block(ids_of_subpages[choosen_subpage_index]) #here we now have the real subpage we want. 
        

        self.has_loaded_semester = True
