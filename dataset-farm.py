import schedule
import time
import urllib.request, json 
import os.path
from random import randint
from fake_useragent import UserAgent

MAX_REQUESTS = 60
maxRequests = MAX_REQUESTS
OD_MATCH_URL = 'https://api.opendota.com/api/matches/'
OD_PARSED_MATCH_URL = 'https://api.opendota.com/api/parsedMatches'
JSON_FILE_PATH = 'datasets/'

def clamp(n, minn, maxn):
    if n < minn:
        return minn
    elif n > maxn:
        return maxn
    else:
        return n

def getData():
    global maxRequests
    queryRandomizer= randint(600000000, 999999999)
    paresedMatchUrl = OD_PARSED_MATCH_URL + '?less_than_match_id='+str(queryRandomizer)
    matches = set()
    headers = {
        'authority': 'api.opendota.com',
        'User-Agent': UserAgent().chrome,
    }
    
    url = urllib.request.Request(paresedMatchUrl, headers=headers)
    with urllib.request.urlopen(url) as url:
        maxRequests-= 1
        data = json.load(url)
    for i in range(len(data)):
        matches.add(data[i]['match_id'])
    print("Got match IDs: "+str(matches))
    matches = list(matches)
    
    requestsToSend = clamp(len(matches), 0, maxRequests) #max 59 requests, minimum is the len() of matches
    
    for i in range(requestsToSend):
        path = JSON_FILE_PATH + str(matches[i]) + '.json'
        if not os.path.exists(path):
            url = OD_MATCH_URL+str(matches[i])
            url = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(url) as url:
                maxRequests-= 1
                data = json.load(url)
                with open(path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    print("Dumped matchID: "+ str(matches[i]))
        else:
            print("matchID: "+ str(matches[i]) + " already exists, skipping...")
    print("Finished")

def execute():
    while maxRequests > 0:
        getData()
        time.sleep(3)

def reset():
    global maxRequests
    maxRequests = MAX_REQUESTS
    

schedule.every(1).minutes.do(reset)

while True:
    execute()
    print("Waiting to loop again")
    schedule.run_pending()

    