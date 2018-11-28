from microfone import Microfone
from mensagens import Mensagens
from pesquisar import Pesquisar
import speech_recognition as sr  
import os
import webbrowser
path = "Audios/"
comando = (path+'Abrir.mp3',path+'BemVindo.mp3',path+'DesejaPesquisar.mp3')
Mensagens.comandos(comando[1])
Funcionar = False
variavel = None

while(True):
	r = sr.Recognizer() 
	with sr.Microphone() as source:                                                                       
		print("[#] [#] [#] [#] PODE ME COMANDAR [#] [#] [#] [#]")                                                                                   
		audio = r.listen(source) 
	try:
		print("Você disse " + r.recognize_google(audio, language="pt-BR"))
		variavel = r.recognize_google(audio, language="pt-BR")
	except sr.UnknownValueError:
		print("Não entendi")
	except sr.RequestError as e:
		print("Sem requests")
	if(r.recognize_google(audio, language="pt-BR") == "Jarvis"):
		Funcionar = True
	else:
		Funcionar = False
	if(Funcionar == True):
		Microfone.__init__()
		Funcionar = False
	else:
		print("Em espera, fale 'Jarvis' Para me chamar")
		Funcionar = False
