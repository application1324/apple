import requests


def getRank (targetDt):
    url = f'http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt={targetDt}'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            result =response.json()
            return result['boxOfficeResult']['dailyBoxOfficeList']
        except:
            return []
    else:
        return []

dt = input('날짜 yyyymmdd')
moives = getRank(dt)
if len(moives) == 0:
    print('값이 없습니다')
else:
    for moive in moives:
        print(moive['movieNm'])
