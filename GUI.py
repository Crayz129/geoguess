from tkinter import *
from tkinter import ttk
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import tkintermapview
import random
from geopy.geocoders import Nominatim
import math 

class GeoGuessApp:
    def __init__(self, root):
        self.root = root
        self.start_menu()
        self.latitude1 = None
        self.longtitude1 = None
        self.latitude = None
        self.longtitude = None
        self.distance = None
        self.is_city = None

    def start_menu(self):
        self.root.title("Geoguess menu")
        self.root.geometry('600x500')

        KeyEnterLabel = tb.Label(text="Введите ключ:", font=("Helvetica", 18), bootstyle="LIGHT")
        KeyEnterLabel.pack(pady=40)

        KeyEntry = tb.Entry(self.root, width=25)
        KeyEntry.pack(pady=10)

        OkButton = tb.Button(self.root, text="OK", bootstyle=SUCCESS, width=10)
        OkButton.pack(pady=40)

        StartButton = tb.Button(self.root, text="Начать без ключа", bootstyle=SUCCESS, width=25, command=self.start_game)
        StartButton.pack(pady=70)

    def map_game(self):
        self.random_geocoordinates()
        self.root.destroy()
        map_game_window = tb.Window(themename="superhero")
        map_game_window.title("Geoguess game")
        map_game_window.geometry("1500x900")

        self.markers = [] # Список понадобится ниже
        self.map_widget = tkintermapview.TkinterMapView(map_game_window, width=1200, height=600)
        self.map_widget.set_zoom(1)
        self.map_widget.add_right_click_menu_command(label="Выбрать точку",
                                                    command=self.add_marker_event,
                                                    pass_coords=True)
        self.map_widget.pack(pady=40)

        self.tip = tb.Label(text="Вы должны угадать загаданную точку на карте, для выбора точки нажмите ПКМ",
                            font=("Helvetica", 18), bootstyle="LIGHT")
        self.tip.pack(pady=10)

        self.tip = tb.Label(text="Пока смотри на вывод в консоли",
                            font=("Helvetica", 18), bootstyle="LIGHT")
        self.tip.pack(pady=10)

        map_game_window.mainloop()

    def add_marker_event(self, coords):
        print("Add marker:", coords)
        self.marker_1 = self.map_widget.set_marker(coords[0], coords[1], text="Ваш выбор")
        
        self.latitude1 = coords[0]
        self.longtitude1 = coords[1]

        self.markers.append(self.marker_1)
        
        # Проверяем, чтобы в списке маркеров элементов было меньше 1, очищаем список, удаляем прошлый маркер

        if len(self.markers) > 1:
            last_marker = self.markers.pop(0)
            self.map_widget.delete(last_marker)

        self.haversine()

    def start_game(self):
        self.map_game()

    def haversine(self):
        # Радиус Земли в километрах
        radius = 6371.0

        if self.latitude1 is not None and self.longtitude1 is not None and self.latitude is not None and self.longtitude is not None:

            # Переводим градусы в радианы
            lat1 = math.radians(self.latitude1)
            lon1 = math.radians(self.longtitude1)
            lat2 = math.radians(self.latitude)
            lon2 = math.radians(self.longtitude)

            # Разница между широтами и долготами
            dlat = lat2 - lat1
            dlon = lon2 - lon1

            # Вычисляем расстояние с использованием формулы Haversine
            a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

            # Расстояние в километрах
            self.distance = radius * c

            if self.distance > 1:
                print("До загаданной точки ", self.distance, " км")
            else: print("ПОБЕДААААА")    
        
        else: 
            print(self.latitude1, self.longtitude1, self.latitude, self.longtitude) 
            print("Pizdec")    

    def random_geocoordinates(self):
        
        self.geolocator = Nominatim(user_agent="random_geocoordinates")

        while True:
        # Генерируем случайные координаты
            
            self.latitude = random.uniform(-90, 90)
            self.longtitude = random.uniform(-180, 180)

            self.is_city = tkintermapview.convert_coordinates_to_city(self.latitude, self.longtitude)

            if self.is_city is not None: 
                print ("Успех!")
                

         # Преобразуем координаты в адрес

            #location = self.geolocator.reverse(f"{self.latitude}, {self.longitude}") 
                print(self.latitude, self.longtitude)
                break
            else:
                print("Загрузка...")

            
"""
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
    #latitude, longitude = app.random_geocoordinates()
    root.mainloop()