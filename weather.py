import requests
import json

# 날씨/대기상태라는 하나의 큰 목적을 공유하고 있어서 클래스로 만들어보았는데,
# 지금 정도의 함수만 있다면 굳이 하나의 클래스로 만들 필요는 없어보임
class WeatherApi:
    def __init__(self, api_key):
        self.locations = {'서울':{'latitude': 37.56, 'longitude': 126.97},
                    '부산':{'latitude': 35.10, 'longitude': 129.03}}
        self.service_key = api_key

    def get_weather(self, location):
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={self.locations[location]['latitude']}&longitude={self.locations[location]['latitude']}&current_weather=true&timezone=auto"
            response = requests.get(url)
            json_data = json.loads(response.text)
            return f"{json_data['current_weather']['temperature']}°C"
        except KeyError:
            return '없는 지역'

    def get_airinfo(self, location):
        try: 
            params = {
                'serviceKey': self.service_key,
                'returnType': 'json',
                'numOfRows': '100',
                'pageNo': '1',
                'sidoName': location,
                'ver': '1.0',
            }
            response = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty', params=params)
            json_data = json.loads(response.text)
            airinfo_list = json_data['response']['body']['items']

            return airinfo_list[0]['pm25Value']
        except IndexError:
            return '없는 지역'
        except KeyError:
            return '없는 지역'