# DESAFIO 021

from pygame import mixer

# Inicializar o mixer
mixer.init()

# Carregar a música em mp3
mixer.music.load('wildflower.mp3')

# Dar play para a música tocar
mixer.music.play()

# Comando para o usuário parar a música
input('Aperte ENTER para parar a música')
