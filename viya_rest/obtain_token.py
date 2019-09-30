import requests
import os
import json
import sys

server= 'viyacdh01.ita.sas.com'
clientId= 'jptst.client'
clientSecret='jptst'
user="czejap"
password="Jpssro159\\"

# prepare URL - setting the server
url = "http://viyacdh01.ita.sas.com/SASLogon/oauth/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
#mydata={"?grant_type=password&"}
payload = {'grant_type':'password','username':'czejap','password':'Jpssro159\\'}
#try:
response = requests.post(url, headers=headers,data=payload,auth=(clientId, clientSecret))
print(response)
#except:
    # print("Could not connect to server.")
    # print("Check if server ip address is correct.")
    # sys.exit()
token= response.json()['access_token']
print(token)

#curl -X POST "https://server.example.com/SASLogon/oauth/token" \
#      -H "Content-Type: application/x-www-form-urlencoded" \
#       -d "grant_type=password&username=<user-id>&password=<password>" \
#       -u "app:mysecret"

 # curl -X POST "http://viyacdh01.ita.sas.com/SASLogon/oauth/token"       -H "Content-Type: application/x-www-form-urlencoded"       -d "grant_type=password&username=sas&password=Orion123"       -u "jptst.client:jptst"
