import requests
from datetime import datetime
from env import PIXEL_TOKEN, PIXEL_USERNAME, PIXEL_GRAPH_ID

'''
    goes to pixel sight and then enters your number of km u ran.
'''

pixela_ep = 'https://pixe.la/v1/users'
my_token = PIXEL_TOKEN
USERNAME = PIXEL_USERNAME
GRAPH_ID = PIXEL_GRAPH_ID
# ----------------------- FIRST STEP ----------------------- #
# creating a new profile
'''user_param = {
  'token': my_token,
  'username': USERNAME,
  'agreeTermsOfService': 'yes',
  'notMinor': 'yes'
}

# after first run comment this out
response1 = requests.post(url=pixela_ep, json=user_param)
print(response1.text)'''
# up to hear

# ----------------------- SECOND STEP ----------------------- #
# creating a new gragh
headers = {'X-USER-TOKEN': my_token}
gragh_ep = f'{pixela_ep}/{USERNAME}/graphs'
'''graph_param = {
  'id': GRAPH_ID,
  'name': 'First Habit',
  'unit': 'Km',
  'type': 'float',
  'color': 'kuro'
}


# comment this out when finsh running
response2 = requests.post(url=gragh_ep, json=graph_param, headers=headers)
print(response2.text)
'''

# ----------------------- THIRD STEP ----------------------- #
# creating pixels on the gragh (post)

pixel_ep = f'{gragh_ep}/{GRAPH_ID}'

inp_pixel = input('how meny km did you run today? ')
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response3 = requests.post(url=pixel_ep, json=pixel_data, headers=headers)
print(response3.text)

# ----------------------- FOURTH STEP ----------------------- #
# changing a pixel in the graph (put)
'''yesterday = datetime(year=2024, month=4, day=26)

update_ep = f'{pixel_ep}/{USERNAME}/graghs/{GRAPH_ID}/{yesterday.strftime("%Y%m%d")}'

new_pixel = {'quantity': '30'}

response4 = requests.put(url=update_ep, json=new_pixel, headers=headers)
print(response4.text)

# ----------------------- FIFTH STEP ----------------------- #
# delete pixel (delete)

delete_ep = f'{pixel_ep}/{USERNAME}/graghs/{GRAPH_ID}/{yesterday.strftime("%Y%m%d")}'

response5 = requests.delete(url=delete_ep, headers=headers)
print(response5.text)
'''