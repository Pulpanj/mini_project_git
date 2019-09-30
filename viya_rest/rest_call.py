# curl - X GET "https://server.example.com/folders/folders/@myFolder" \
# - H "Accept: application/json" \
# - H "Authorization: Bearer <TOKEN-STRING>"



import requests
import os
import json
import sys

server= 'viyacdh01.ita.sas.com'
clientId= 'jptst.client'
clientSecret='jptst'
token='eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiJiYWFlYTVkZGZkYWI0ZDQ1YTE1M2U5M2NlMTY1NzFkNCIsInN1YiI6ImQzODUyYmRlLWJjMTUtNDBjMS1hOTdmLTcwM2E5YTQ3YmYzMSIsInNjb3BlIjpbIm9wZW5pZCJdLCJjbGllbnRfaWQiOiJqcHRzdC5jbGllbnQiLCJjaWQiOiJqcHRzdC5jbGllbnQiLCJhenAiOiJqcHRzdC5jbGllbnQiLCJncmFudF90eXBlIjoicGFzc3dvcmQiLCJ1c2VyX2lkIjoiZDM4NTJiZGUtYmMxNS00MGMxLWE5N2YtNzAzYTlhNDdiZjMxIiwiZXh0X2lkIjoiY249SmFyb3NsYXYgUHVscGFuLG91PXVzZXJzLG91PVByYWd1ZSxvdT1DemVjaCBSZXB1YmxpYyxkYz1lbWVhLGRjPVNBUyxkYz1jb20iLCJvcmlnaW4iOiJsZGFwIiwidXNlcl9uYW1lIjoiY3plamFwIiwiZW1haWwiOiJKYXJvc2xhdi5QdWxwYW5Ac2FzLmNvbSIsImF1dGhfdGltZSI6MTU1MDIyMDIwMywicmV2X3NpZyI6ImJkN2JlZWI1IiwiaWF0IjoxNTUwMjIwMjAzLCJleHAiOjE1NTAyNjM0MDMsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvU0FTTG9nb24vb2F1dGgvdG9rZW4iLCJ6aWQiOiJ1YWEiLCJhdWQiOlsianB0c3QuKiIsImpwdHN0LmNsaWVudCIsIm9wZW5pZCJdfQ.QmuCUq4vYh4FeFbWUukFDveyeCoFTRDcTNk6EhFGUJ7LgEnXlEMXHF5cBzMXRM1HQnWwThZgaNRho9q5OYeSqh4FcisWpfNSocs_Z6Z_zP_Ts58dtvK1tw8KjoAymBFhG_41S35wk5s6Bqk6vsQMCim_0obIofqZfFpi7fxnBgg'
# prepare URL - setting the server

# url = "http://viyacdh01.ita.sas.com/casManagement"
# headers = {"Accept": "application/json",'Authorization':'Bearer'+token }

url = "http://viyacdh01.ita.sas.com/casManagement/servers"
headers = {"Accept": "application/json",'Authorization':'Bearer'+token }


response = requests.get(url, headers=headers)
print(response)
#except:
    # print("Could not connect to server.")
    # print("Check if server ip address is correct.")
    # sys.exit()
myjson= response.json()
print(type(myjson))
print(myjson)
# my=json.loads(json)
print(json.dumps(response.json(), indent=4)) #, sort_keys=True))