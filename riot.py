import requests

API_KEY = "RGAPI-da5b6421-a330-45b1-b6d2-ee3f53c77d8e"
HEADER = {
    "Accept-Charset" : "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token" : API_KEY,
    "Accept-Language" : "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
}

def get_SummonerId(summonerName):
    url = f"https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonerName}"
    req = requests.get(url=url, headers=HEADER)
    print(req.status_code)
    if req.status_code == 200:
        leagues = req.json()
        if len(leagues) == 0:
            return None
        print(leagues["id"])
        return leagues["id"]
    else:
        print(req.status_code)


def get_RankInfo(summonerID):
    url = f"https://kr.api.riotgames.com/lol/league/v4/entries/by-summoner/{summonerID}"
    req = requests.get(url=url, headers=HEADER)
    if req.status_code == 200:
        leagues = req.json()
        if len(leagues) == 0:
            return None
        for league in leagues:
            if league["queueType"] == "RANKED_SOLO_5x5":
                    return league

    else:
        print(req.status_code)

print(get_RankInfo("TmJuG-D9jie2Bwla9jea52xBR2iOehTE-dTWnZaKm0qSHQ"))