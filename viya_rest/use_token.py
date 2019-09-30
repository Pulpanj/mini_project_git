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
token='eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiIwNDM1ODM1N2JmMDU0OWM4ODA5ZTU4ZDc2ZWEyNmU3OCIsInN1YiI6ImQzODUyYmRlLWJjMTUtNDBjMS1hOTdmLTcwM2E5YTQ3YmYzMSIsInNjb3BlIjpbIm9wZW5pZCJdLCJjbGllbnRfaWQiOiJqcHRzdC5jbGllbnQiLCJjaWQiOiJqcHRzdC5jbGllbnQiLCJhenAiOiJqcHRzdC5jbGllbnQiLCJncmFudF90eXBlIjoicGFzc3dvcmQiLCJ1c2VyX2lkIjoiZDM4NTJiZGUtYmMxNS00MGMxLWE5N2YtNzAzYTlhNDdiZjMxIiwiZXh0X2lkIjoiY249SmFyb3NsYXYgUHVscGFuLG91PXVzZXJzLG91PVByYWd1ZSxvdT1DemVjaCBSZXB1YmxpYyxkYz1lbWVhLGRjPVNBUyxkYz1jb20iLCJvcmlnaW4iOiJsZGFwIiwidXNlcl9uYW1lIjoiY3plamFwIiwiZW1haWwiOiJKYXJvc2xhdi5QdWxwYW5Ac2FzLmNvbSIsImF1dGhfdGltZSI6MTU1MDE2MjEwOCwicmV2X3NpZyI6ImJkN2JlZWI1IiwiaWF0IjoxNTUwMTYyMTA4LCJleHAiOjE1NTAyMDUzMDgsImlzcyI6Imh0dHA6Ly9sb2NhbGhvc3QvU0FTTG9nb24vb2F1dGgvdG9rZW4iLCJ6aWQiOiJ1YWEiLCJhdWQiOlsianB0c3QuKiIsImpwdHN0LmNsaWVudCIsIm9wZW5pZCJdfQ.I1DvfITEWn1OmrRa-_fyMSU5wcdBYO5ao480NKYQ3E_FAHtnk8r4C3RhH0IoD6PP9sFcrqcYnYKh29tV3R0OO5tzB2MnV0xVO8TGprOitossLHjS0bkyjzxFvPF2PFW9lm6OBhznfCQPFMssfkm6FOLgyZkf8erpzLcXhCW53nQ'
# prepare URL - setting the server
url = "http://viyacdh01.ita.sas.com/folders/folders/@myFolder"
headers = {"Accept": "application/json",'Authorization':'Bearer'+token }
#mydata={"?grant_type=password&"}
#payload = {'grant_type':'password','username':'czejap','password':'Jpssro369\\'}
#try:
response = requests.get(url, headers=headers)
print(response)
#except:
    # print("Could not connect to server.")
    # print("Check if server ip address is correct.")
    # sys.exit()
folder= response.content
print(folder)