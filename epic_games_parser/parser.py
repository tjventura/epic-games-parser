import urllib.request, json 

gamesInfo = [{
    'title': 'title',
    'startDate': 'startDate',
    'endDate': 'endDate'
},
{
    'title': 'title',
    'startDate': 'startDate',
    'endDate': 'endDate'
},]

def fetcher():
    with urllib.request.urlopen("https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions") as url:
        data = json.loads(url.read().decode())

        freeGamesData = data['data']['Catalog']['searchStore']['elements']

        i = 0
        for freeGameInfo in freeGamesData:
            gamesInfo[i]['title'] = freeGameInfo['title']
            if freeGameInfo['title'] == 'Mystery Game':
                AvailableTime = freeGameInfo['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]
                #gamesInfo[]
                gamesInfo[i]['startDate'] = AvailableTime['startDate']
                gamesInfo[i]['endDate'] = AvailableTime['endDate']
            else:
                AvailableTime = freeGameInfo['promotions']['promotionalOffers'][0]['promotionalOffers'][0]
                gamesInfo[i]['startDate'] = AvailableTime['startDate']
                gamesInfo[i]['endDate'] = AvailableTime['endDate']
            i+=1
        i = 0            
        return json.dumps(gamesInfo)

fetcher()