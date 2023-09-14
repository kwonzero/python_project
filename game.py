import requests
import json
from tts import speak
from stt import SttEngine

class RelayGame:
    def __init__(self, api_key, turn=1, default_word='사과'):
        self.api_key = api_key
        self.turn = turn
        self.default_word = default_word
        self.previous_words = [] # 이전 단어 리스트
        self.stt_engine = SttEngine()

    # Api로 단어 검색하는 메소드 , query = 검색어
    def get_words(self, query, method): 
        headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
        response = requests.get(f'http://opendict.korean.go.kr/api/search?key={self.api_key}&req_type=json&q={query}&advanced=y&sort=popular&type1=word&method={method}&num=100&pos=1&type3=general', headers=headers)
        json_data = json.loads(response.text) # 검색어 저장
        return json_data['channel']['item'] # 검색어 반환
    
    # query 단어가 유효한 한국어인지 검증 (Api 검색), T/F로 반환
    def validate_word(self, query): 
        result = self.get_words(query, 'exact') # exact로 정확한 단어 검색
        return result != [] # 검색된 단어가 있으면(빈 리스트가 아니면) 반환
    
    # 사용자의 음성 입력을 받아들이고, 이 입력을 유효성을 검사하면서 처리하는 메소드
    def input_with_validation(self):
        while True:
            my_word = self.stt_engine.recognize() # my_word -> text로 변환된 데이터
            if my_word is None: # 아무 말도 안했으면, 따로 조건검사없이 다시 인식하도록
                continue # 다음 루프로
            elif len(my_word) < 2: # 각 조건문 마다 함수 형태로 만든 후에, 딕셔너리 형태로 만들어서 elif 문의 중첩을 제거할 수는 있음
                speak('2자 이상 말해주세요.')
            elif self.previous_words != [] and my_word[0] != self.previous_words[-1][-1]: # 이전 단어가 존재하고, 말한 단어의 마지막 글자가 이전단어의 마지막 글자가 아니면:
                speak('끝말을 잇지 않았습니다.')
            elif my_word in self.previous_words: # 말한 단어가 이전 단어에 있으면:
                speak('이미 나온 단어입니다.')
            elif not self.validate_word(my_word): # 검증된 단어가 아니면:
                speak('없는 단어입니다.')
            else:
                return my_word
             
    # 다음 단어 반환하는 메소드(컴퓨터 차례에서)
    def get_next_word(self, query): 
        words = self.get_words(query, 'start') # 'start'로 헤당 단어로 시작하는 단어 검색
        for word in words:
            if len(word['word']) < 2: # 검색한 단어가 2글자 미만인 경우:
                continue # 건너뛰고 다음 단어 검토
            if word['word'] not in self.previous_words: # 검색 단어 중 이전 단어 리스트에 없는 경우:
                return word['word'] # 해당 단어 반환
        return None # 위에서 return 되지 않았다면 더 이상 조건에 맞는 단어가 없다는 뜻이므로 None 반환
    
    # 끝말잇기 게임 시작
    def start(self):
        while True:
            if self.turn == 1: # 내 차례
                current_word = self.input_with_validation() 
            else: # 컴퓨터 차례
                previous_word = self.previous_words[-1] if self.previous_words else self.default_word
                current_word = self.get_next_word(previous_word[-1])
                speak(current_word) 
            self.previous_words.append(current_word) # 지금까지 나온 단어 리스트에 추가
            self.turn = not self.turn # 다음 턴