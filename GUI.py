from tkinter import *
from tkinter import ttk
from typing import Self
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkintermapview
import random
from geopy.geocoders import Nominatim

class GeoGuessApp:
    def __init__(self, root):
        self.root = root
        self.start_menu()

    def start_menu(self):
        self.root.title("Geoguess menu")
        self.root.geometry('600x500')

        KeyEnterLabel = tb.Label(text="Введите ключ:", font=("Helvetica", 18), bootstyle="LIGHT")
        KeyEnterLabel.pack(pady=40)

        KeyEntry = tb.Entry(self.root, width=25)
        KeyEntry.pack(pady=10)

        OkButton = tb.Button(self.root, text="OK", bootstyle=SUCCESS, width=10)
        OkButton.pack(pady=40)

        StartButton = tb.Button(self.root, text="Начать без ключа", bootstyle=SUCCESS, width=25, command=self.map_game)
        StartButton.pack(pady=70)

    def map_game(self):
        self.root.destroy()
        map_game_window = tb.Window(themename="superhero")
        map_game_window.title("Geoguess game")
        map_game_window.geometry("1500x800")

        self.markers = [] # Список понадобится ниже
        self.map_widget = tkintermapview.TkinterMapView(map_game_window, width=1200, height=600)
        self.map_widget.set_zoom(1)
        self.map_widget.add_right_click_menu_command(label="Выбрать точку",
                                                    command=self.add_marker_event,
                                                    pass_coords=True)
        self.map_widget.pack()

        self.tip = tb.Label(text="Вы должны угадать загаданную точку на карте, для выбора точки нажмите ПКМ",
                            font=("Helvetica", 18), bootstyle="LIGHT")
        self.tip.pack(pady=50)

        map_game_window.mainloop()

    def add_marker_event(self, coords):
        print("Add marker:", coords)
        self.marker_1 = self.map_widget.set_marker(coords[0], coords[1], text="Ваш выбор")
        self.markers.append(self.marker_1)
        
        # Проверяем, чтобы в списке маркеров элементов было меньше 1, очищаем список, удаляем прошлый маркер

        if len(self.markers) > 1:
            last_marker = self.markers.pop(0)
            self.map_widget.delete(last_marker)
            

        

"""
    def random_geocoordinates(self):

        self.geolocator = Nominatim(user_agent="random_geocoordinates")

        while True:
        # Генерируем случайные координаты
            latitude = random.uniform(-90, 90)
            longitude = random.uniform(-180, 180)

         # Преобразуем координаты в адрес
            location = self.geolocator.reverse(f"{latitude}, {longitude}")

        # Полная инфа 
            if location is not None:
                adress = location.address
                building_keywords = ["amenity", "building", "geological", "historic", "millitary", "tourism"]

        # Проверяем, находятся ли координаты на суше
            if hasattr(location, 'raw') and "type" in location.raw:
                if "land" in location.raw["type"]:
                    for keyword in building_keywords: # Проверяем здание ли это
                        if keyword in adress:
                            print(f"Latitude: {latitude}, Longitude: {longitude}")
                            return latitude, longitude
"""                        
        
if __name__ == "__main__":
    root = tb.Window(themename="superhero")
    app = GeoGuessApp(root)
   # latitude, longitude = app.random_geocoordinates()
    root.mainloop()
