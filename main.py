import requests
base_url = "https://www.themealdb.com/api/json/v1/1"

def get_meal_info(meal):
    url = f"{base_url}/search.php?s={meal}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return -1
    

get_meal_info ('Arrabiata')
get_meal_info('Samuel')
