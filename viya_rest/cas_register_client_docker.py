#does not work...
import requests
import os
import json
import sys

server= '10.0.75.1:32769'
clientId= 'jptst.docker'
consulToken='781a7bec-cd36-4827-8579-25fec807be0f'
clientSecret='jptst'

# prepare URL - setting the server
#url= "http://%s//SASLogon/oauth/clients/consul?callback=false&serviceId=%s" % (server, clientId)
url= "http://%s/SASLogon/oauth/clients/consul?callback=false&serviceId=%s" % (server, clientId)
# preparing the URL header
headers = {"X-Consul-Token":consulToken}
# calling the URL as POST request
try:
    response = requests.post(url, headers=headers)
except:
    print("Could not connect to server.")
    print("Check if server ip address is correct.")
    sys.exit()

# check if URL call was successful
if response.status_code < 200 or response.status_code >= 300:
    print(response)
    print(response.json()['error'])
    print(response.json()['error_description'])
    print('Error receiving access token!')
    sys.exit()

# grap the user token from the URL response. The token is used when calling the next URL
token= response.json()['access_token']
print(token)

# prepare URL - setting the server
url = "http://%s///SASLogon/oauth/clients" % (server)
# preparing the URL header
headers = {"Content-Type": "application/json", "Authorization": ""}
headers["Authorization"] = "Bearer " + token
body = {
    "client_id": clientId,
    "client_secret": clientSecret,
    "scope": ["openid"],
    "authorized_grant_types": ["password"],
    "access_token_validity": 43200
}
# convert dictionary to json
bodyJSON = json.dumps(body)
# calling the URL as POST request
response = requests.post(url, headers=headers, data=bodyJSON)
# check if URL call was successful
if response.status_code < 200 or response.status_code >= 300:
    print(response)
    print(response.json()['error'])
    print(response.json()['error_description'])
    print('Could not register client!')
    sys.exit()

# output success
print("Client Id: '" +  clientId + "' with Secret: '" + clientSecret + "' successfully registered.")

