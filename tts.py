from gtts import gTTS 
import playsound
import os
# text to speak

# 이 부분은 간단한 코드라서 따로 클래스화하지 않았음
def speak(text): 
	tts = gTTS(text=text, lang='ko') # 음성으로 변환
	tts.save('voice.mp3') # 사운드 저장
	playsound.playsound('voice.mp3') # 사운드 재생
	os.remove('voice.mp3') # 음성 파일을 재생한 후에 해당 파일을 삭제