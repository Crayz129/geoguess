import json
from requests import get, post

YOUR_KEY = 'd7e3945b-81c4-4562-83de-c49f4ed4a47b'
DISTANCE_MATRIX = 'http://routing.api.2gis.com/routing/7.0.0/global?key=d7e3945b-81c4-4562-83de-c49f4ed4a47b'

InputException = Exception('Wrong input! Try again')

# Проверка, содержит ли ввод буквы
def find_letters(list):
    for i in list:
        try: 
            float(i)
            return False
        except:
            return True
        
        # JOPA
 
# Создание и обработка координат          
def create_coords():
    # Ввод координат
    coords = input('Input adress na russkom or coordinats: ')
    
    # Разбиваем координаты на широту и долготу
    if ',' in coords:
        coords = coords.split(',')
        print(coords)
    else: 
        try:
            coords = coords.split(' ')
            print(coords)
        except InputException:
            print('Program ended with code -1')

    # Если массив пустой, просим ввести ещё раз        
    if len(coords) == 2 and not find_letters(coords):
        return coords
    else:
        print('Wrong input! Try again.')
        create_coords()
        
def api_get_request(coords):
    lon = float(coords[0])
    lat = float(coords[1])
    """ print('https://catalog.api.2gis.com/3.0/items/geocode?lon={lon}&lat={lat}&fields=items.point&key={YOUR_KEY}'.format(lat = lat, lon = lon, YOUR_KEY = YOUR_KEY))
    get_response = get('https://catalog.api.2gis.com/3.0/items/geocode?lon={lon}&lat={lat}&fields=items.point&key={YOUR_KEY}'.format(lon = lon, lat = lat, YOUR_KEY = YOUR_KEY))
    with open('geo.json','w') as f:
        json.dump(get_response.json(), f, ensure_ascii=False) """
    with open('geo.json','r') as f:
        adress = json.load(f)
    """ adress = get_response.json() """
    print(adress['result']['items'][0]['full_name'], adress['result']['items'][3]['full_name'])
    
def api_post_request(coords):
    lon = float(coords[0])
    lat = float(coords[1])
    data = {
    "points": [
        {
            "lat": 36.45671576713001,
            "lon": 45.340016732485225,
            'type': 'stop'
        },
        {
            'lon': 35.04993610565122,
            'lat': 48.46841133624937,
            'type': 'stop'
        }
    ],
    "type": "shortest",
    "sources": [0], # Начальные точки
    "targets": [1] # Конечные точки
    }

    # Преобразуйте данные в JSON формат
    data_json = json.dumps(data)
    print(data_json)
    # Установите заголовки
    headers = {'Content-Type': 'application/json'}
    post_response = post(url = DISTANCE_MATRIX, data=data_json, headers=headers)
    print(post_response)
    with open('distance.json','w') as f:
        json.dump(post_response.json(), f, ensure_ascii=False)

if __name__ == '__main__':
    coords = create_coords()
    print('Вызов create_coords завершён. ', coords)
    api_get_request(coords)
    print('Вызов api_request завершён. ')
    api_post_request(coords)
    print("Вызов api_post_request завершён. ")
    
    