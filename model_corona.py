import view_corona
import json
import requests


def CoronaDetail(CountryName):
    url  = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"
    querystring = {"country":CountryName}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "31d74b416amshbd44b0c872c069dp18c47ejsn9e63af5f0486"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    corona_data = json.loads(response.text)
    with open('corona.txt','w') as output:
        json.dump(corona_data,output)


