import speech_recognition as sr  
import webbrowser
class Pesquisar:
	def __init__():
		global falou2
		r = sr.Recognizer() 
		with sr.Microphone() as source:                                                                       
			print("Fale sua pesquisa")                                                                                   
			audio = r.listen(source) 
		try:
			falou2 = r.recognize_google(audio, language="pt-BR")
		except sr.UnknownValueError:
			print("Não entendi")
		except sr.RequestError as e:
			print("Sem requests; {0}".format(e))
		webbrowser.open('https://www.google.com/search?q='+falou2)