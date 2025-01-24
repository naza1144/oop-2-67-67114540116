from thai import Thaicitizen
import requests

url = "https://dummyjson.com/users"
data = requests.get(url).json()
users = data['users']
thai = []
for user in users:
    u = Thaicitizen(
        first_name = user['firstName'],
        last_name = user['lastName'],
        image = user['image'],
        country = user['address']['country']
    )
    thai.append(u)
for t in thai:
    print(t.first_name, t.last_name,t.image , t.country)