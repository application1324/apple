import requests

def get_meals(dt):
    p = {
        'Type' : 'json',
        'ATPT_OFCDC_SC_CODE' : 'J10',
        'SD_SCHUL_CODE' : '7530167',
        'MLSV_YMD': dt
    }
    url = f'https://open.neis.go.kr/hub/mealServiceDietInfo'
    result = requests.get(url, params=p)

    try:
        if result.status_code == 200:
            meals = result.json()  # 결과를 json => dictionary(파일) 로 변환인식
            return meals['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
        else:
            return ''
    except:
        return ''

date = input("급식일자 입력: 20000101 형태")
meal = get_meals(dt=date)
if meal == '':
    print('주말입니다')
else:
    meals = str(meal).split('<br/>')
    for i in meals:
        print(i)
