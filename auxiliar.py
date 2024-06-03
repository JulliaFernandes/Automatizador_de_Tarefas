import pyautogui as pg
import time

pg.PAUSE = 0.5 ##Da um pause a cada comando rodando com pyautogui
# Abrir o navegador(chorme)
# pg.press("win") ## Abre a tecla do windows
# pg.write("chrome") ## Escreve chrome no campo de pesquisa
# pg.press("enter") ## Aperta a tecla enter

# time.sleep(1)
# pg.hotkey("ctrl", "t") ## Abre uma nova aba no navegador
# time.sleep(1)   
# link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# pg.write(link)
# pg.press("enter")


time.sleep(5) ## Da um tempo para o usuário posicionar o mouse onde deseja
print(pg.position()) ##Mostra a posição do mouse na tela

#Para saber a quantidade de scroll para subir na tela
pg.scroll(5000) ## Colocando um numero muito grande para subir o maximo possivel

