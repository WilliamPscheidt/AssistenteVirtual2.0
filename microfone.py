import speech_recognition as sr  
from mensagens import Mensagens
from pesquisar import Pesquisar
from pesquisarYoutube import PesquisarYoutube
import webbrowser
class Microfone:
	path = "Audios/"
	global comando
	comando = (path+'Abrir.mp3',path+'BemVindo.mp3',path+'DesejaPesquisar.mp3')
	def __init__():
		global falou
		r = sr.Recognizer() 
		with sr.Microphone() as source:                                                                       
			print("Pronta para comandar")                                                                                   
			audio = r.listen(source) 
		try:
			print("Você disse " + r.recognize_google(audio, language="pt-BR"))
			falou = r.recognize_google(audio, language="pt-BR")
		except sr.UnknownValueError:
			print("Não entendi")
		except sr.RequestError as e:
			print("Sem requests; {0}".format(e))

		if falou == "Google":
			Mensagens.comandos(comando[0])
			Mensagens.comandos(comando[2])
			Pesquisar.__init__()
		elif falou == "Facebook":
			Mensagens.comandos(comando[0])
			webbrowser.open("https://www.facebook.com/")
		elif falou == "YouTube":
			Mensagens.comandos(comando[0])
			Mensagens.comandos(comando[2])
			PesquisarYoutube.__init__()
		elif falou == "WhatsApp":
			Mensagens.comandos(comando[0])
			webbrowser.open("https://web.whatsapp.com/")
		else:
			print("Não entendi")
		
			