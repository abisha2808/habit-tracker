import requests
from datetime import datetime

user_name ="janeabisha"
token = "ghikalzlsmjdsojdi"
End_point = "https://pixe.la/v1/users"
grap_endpoint = f"{End_point}/{user_name}/graphs"
post_endpoint = f"{grap_endpoint}/graph2"

parameter = {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(End_point, json=parameter)
# print(response.text)

parameter1 = {
    "id": "graph2",
    "name": "walking graph",
    "unit": "km",
    "type": "float",
    "color": "ichou"
}

header = {
    "X-USER-TOKEN": token
}
today = datetime.now()
parameter2 = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1.5"
}
response = requests.post(post_endpoint, json=parameter2, headers=header)
print(response.text)