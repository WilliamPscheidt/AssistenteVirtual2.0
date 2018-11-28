import pygame as pg
import time
class Mensagens:
	def __init__(self, comando):
		self.comando = comando
	def comandos(comando):
		pg.mixer.init()
		pg.mixer.music.load(comando)
		pg.mixer.music.play()
		while pg.mixer.music.get_busy():  # Tempo entre as mensagens
			time.sleep(0.5)