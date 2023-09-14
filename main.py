from assistant import Assistant

# 실행하는 예시를 쉽게 보여드리고자 파일 자체를 분리했는데,
# 클래스 파일에 main함수 형태로 아래 코드를 넣어놓고 sysarg 형태로 인자 값을 받게 만들어도 무방
instance = Assistant(name= '시리',
                      weather_api_key='s0qWCuA75VefKz89a1s0Vl7%2BViG0Jx6PJTYDGjVpwqqztNyKudmRCb3m25McS8VdyafThInzDcLMfjDXMa00xg%3D%3D',
                      game_api_key='CDBDE5D8FDE32E998911D97A58FAF6C6')
instance.start()