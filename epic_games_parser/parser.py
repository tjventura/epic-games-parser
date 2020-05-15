import urllib.request, json 

gamesInfo = {
    'title': 'title',
    'startDate': 'startDate',
    'endDate': 'endDate'
}

def fetcher():
    with urllib.request.urlopen("https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions") as url:
        data = json.loads(url.read().decode())

        freeGamesData = data['data']['Catalog']['searchStore']['elements']

        for freeGameInfo in freeGamesData:
            gamesInfo['title'] = freeGameInfo['title']
            if freeGameInfo['title'] == 'Mystery Game':
                AvailableTime = freeGameInfo['promotions']['upcomingPromotionalOffers'][0]['promotionalOffers'][0]
                #gamesInfo[]
                gamesInfo['startDate'] = AvailableTime['startDate']
                gamesInfo['endDate'] = AvailableTime['endDate']
            else:
                AvailableTime = freeGameInfo['promotions']['promotionalOffers'][0]['promotionalOffers'][0]
                gamesInfo['startDate'] = AvailableTime['startDate']
                gamesInfo['endDate'] = AvailableTime['endDate']

        return json.dumps(gamesInfo)

fetcher()