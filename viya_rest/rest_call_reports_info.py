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
token='eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI4YTA0YmMzOWE4Y2U0YjJkOTE5ODNlODhhZTY5MTIwNSIsInN1YiI6ImQzODUyYmRlLWJjMTUtNDBjMS1hOTdmLTcwM2E5YTQ3YmYzMSIsInNjb3BlIjpbIm9wZW5pZCJdLCJjbGllbnRfaWQiOiJqcHRzdC5jbGllbnQiLCJjaWQiOiJqcHRzdC5jbGllbnQiLCJhenAiOiJqcHRzdC5jbGllbnQiLCJncmFudF90eXBlIjoicGFzc3dvcmQiLCJ1c2VyX2lkIjoiZDM4NTJiZGUtYmMxNS00MGMxLWE5N2YtNzAzYTlhNDdiZjMxIiwiZXh0X2lkIjoiY249SmFyb3NsYXYgUHVscGFuLG91PXVzZXJzLG91PVByYWd1ZSxvdT1DemVjaCBSZXB1YmxpYyxkYz1lbWVhLGRjPVNBUyxkYz1jb20iLCJvcmlnaW4iOiJsZGFwIiwidXNlcl9uYW1lIjoiY3plamFwIiwiZW1haWwiOiJKYXJvc2xhdi5QdWxwYW5Ac2FzLmNvbSIsImF1dGhfdGltZSI6MTU1MjQ4NjI5NywicmV2X3NpZyI6ImJkN2JlZWI1IiwiaWF0IjoxNTUyNDg2Mjk3LCJleHAiOjE1NTI1Mjk0OTcsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvU0FTTG9nb24vb2F1dGgvdG9rZW4iLCJ6aWQiOiJ1YWEiLCJhdWQiOlsianB0c3QuKiIsImpwdHN0LmNsaWVudCIsIm9wZW5pZCJdfQ.KccHF4NkPfDZaG7CH4-AVud7jY50kAuy3q7eZAeWqS6_nOPyav2GlXb7w8DqXlX_22Sa_K-6YU1jP8a922v8OIOo5CWHS-nyJi446-Tz-OKWlV30OGfYSRDh7FCMfYMD-A2wvi-q552x-v896uvFmQDtQCLiariRZrzJnyoWcck'
# prepare URL - setting the server
url = "http://viyacdh01.ita.sas.com/reports/reports"
headers = {"Accept": "application/vnd.sas.collection+json",'Authorization':'Bearer'+token }
#mydata={"?grant_type=password&"}
#payload = {'grant_type':'password','username':'czejap','password':'Jpssro369\\'}
#try:
response = requests.get(url, headers=headers)
print(response)
print(json.dumps(response.json(), indent=4)) #, sort_keys=True))
# #except:
    # print("Could not connect to server.")
    # print("Check if server ip address is correct.")
    # sys.exit()
# folder= response.content
# print(folder)

#print(json.dumps(response.json(), indent=4)) #, sort_keys=True))

#url = "http://viyacdh01.ita.sas.com/reports/reports/cbf97b0a-457d-4b4f-8913-547e0cdf390c"
url = "http://viyacdh01.ita.sas.com/casManagement/process"
headers = {"Accept": "application/json",'Authorization':'Bearer'+token }
response = requests.get(url, headers=headers)
print(type(response))
print(response)
#print(json.dumps(response.json(), indent=4)) #, sort_keys=True))
