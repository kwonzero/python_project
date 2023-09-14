import speech_recognition as sr

# speak to text
class SttEngine:
    def __init__(self):
        self.r = sr.Recognizer()
        self.mic = sr.Microphone()

    def recognize(self): # 음성 인식하고 변환
        try:
            with self.mic as source:
                audio = self.r.listen(source, timeout=5, phrase_time_limit=5)
            user = self.r.recognize_google(audio, language = "ko-KR")   # 음성 텍스트로 변환
            print('당신이 말한 단어는 '+ user)
            return user
        except sr.UnknownValueError:
            print('Unknown Value Error')
        except sr.RequestError:
            print('Request Error')
        except sr.WaitTimeoutError:
            print('Timeout Error')
