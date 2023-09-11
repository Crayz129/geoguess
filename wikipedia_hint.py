import tkinter as tk
from tkinter import ttk
import ttkbootstrap.constants
import ttkbootstrap as tb
import tkintermapview
import random
from geopy.geocoders import Nominatim
import math 
import base64
import wikipediaapi
import translators as ts

class WikiHintWindow:
    def __init__(self, root) -> None:
        wiki_hint_window = tk.Tk()
        wiki_hint_window.title("Подсказка")
        wiki_hint_window.geometry("200x150")
        self.marker_is_city = "Kerch"
        self.is_city = True
        self.wiki_agent_ru = wikipediaapi.Wikipedia("geoguess (arsenii.solovev12@gmail.com)",'ru')
        self.wiki_agent_en = wikipediaapi.Wikipedia("geoguess (arsenii.solovev12@gmail.com)",'en')
        self.root = root
        self.is_city = None
        self.wiki_hint_window_init()
        
    def wiki_hint_window_init(self):
        hintLabel = tb.Label(text="Подсказка:", font=("Helvetica", 18), bootstyle="LIGHT")
        hintLabel.pack(pady=40)
        
        while self.marker_is_city != self.is_city:
            self.ru_wiki_hint = self.wiki_agent_ru.page(self.marker_is_city)
            if self.ru_wiki_hint.exists():
                hint = self.format_hint_text(self.ru_wiki_hint.summary)
                hintText = tb.Label(text=hint, font=("Helvetica", 18), bootstyle="LIGHT")
                hintText.pack(pady=10)
                
                print(hint)
                break
            else:
                self.en_wiki_hint = self.wiki_agent_en.page(self.marker_is_city)
                if self.en_wiki_hint.exists():
                    hint_text = ts.translate_text(query_text=self.en_wiki_hint.summary, to_language='ru', from_language='en')
                    hint = self.format_hint_text(hint_text)
                    print(hint)
                else:
                    print("Page does not exist")
                break
        else: 
            print("ERROR")
            
    def format_hint_text(self, hint_text):
        city_name = ts.translate_text(query_text=self.marker_is_city, to_language='ru', from_language='en')
        formated_hint = hint_text.split(' ', 7)[7]
        formated_hint = formated_hint[:208]
        formated_hint = formated_hint.replace(city_name, '***')
        formated_hint = formated_hint.replace(self.marker_is_city, '***')
        return formated_hint
            

if __name__ == "__main__":
    root = tb.Window(themename="superhero")
    app = WikiHintWindow(root)
    root.mainloop()
