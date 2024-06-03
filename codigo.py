## PASSO A PASSO DO PROJETO
## Passo 1: Entrar no sistema da empresa, link: https://dlp.hashtagtreinamentos.com/python/intensivao/login 
import pyautogui as pg
import time
pg.PAUSE = 0.5 ##Da um pause a cada comando rodando com pyautogui

# pyautogui.click -> clicar em algum ugar da tela
# pyautogui.write -> escrever algo
# pyautogui.press -> apertar alguma tecla do teclado

# Abrir o navegador(chorme)
pg.press("win") ## Abre a tecla do windows
pg.write("chrome") ## Escreve chrome no campo de pesquisa
pg.press("enter") ## Aperta a tecla enter

# time.sleep(1.5)
time.sleep(1)
pg.hotkey("ctrl", "t") ## Abre uma nova aba no navegadorjullia@email.com    

##Selecionando o espaço em que sera apertado para entrar em alguma conta de login
# perfil_desejado_position = (600, 300)
# pg.click(perfil_desejado_position)

time.sleep(1)
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pg.write(link)
pg.press("enter")


## Passo 2: Fazer o login no sistema

time.sleep(1)
##Para clicar no campo de email, precisa clicar onde esta o campo e depois clicar no campo de email
email_position = (960,400)
pg.click(email_position)
pg.write("jullia@email.com")

## Para ir para o campo da senha, podemos ou pegar a posição do compo de senha ou podemos apertar a tecla tab do teclado
## 1º maneira de escrever a senha
# senha_position = (197, 390)
# pg.click(senha_position)
# pg.write("123456")

##2º maneira de escrever a senha
# pg.click(x=197, y=390)
# pg.write("123456")

##3º maneira de escrever a senha
pg.press("tab")
pg.write("123456")

time.sleep(0.5)
enter_position = (995,565)
pg.click(enter_position)

time.sleep(2)

## Passo 3: Importar a base de dados para fazer o cadastro
## Precisamos importar a base de dados para o sistema, para isso, vamos usar o Pandas, uma das melhores ferramentas para trabalhar com base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela.head())

## Passo 4: Cadastrar um produto
##Comentei depois pois isso abaixo é um exemplo de como cadastrar um produto
# pg.click(x=164, y=218) ## CLicando no primeiro campo para cadastrar um produto
# ##Codigo do produto
# pg.write("Codigo do produto")

# ## Passando para o proximo campo que é a marca do produto
# pg.press("tab")
# pg.write("Marca")

# ## Passando para o proximo campo que é o tipo do produto
# pg.press("tab")
# pg.write("Tipo do produto")

# ## Passando para o proximo campo que é a categoria do produto
# pg.press("tab")
# pg.write("Categoria")

# ## Passando para o proximo campo que é a preço do produto
# pg.press("tab")
# pg.write("Preco.00")

# ## Passando para o proximo campo que é o custo do produto
# pg.press("tab")
# pg.write("custo")

# ## Passando para o proximo campo que é as obs do produto
# pg.press("tab")
# pg.write("obs")

# ## Passando para o proximo campo que é o enter para cadastrar o produto
# pg.press("tab")
# pg.press("enter") 


## Passo 5: Ir cadastrando os produtos ate acabar
for linha in tabela.index:
    codigo = tabela.loc[linha, 'codigo']
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    preco = tabela.loc[linha, 'preco_unitario']
    custo = tabela.loc[linha, 'custo']
    obs = tabela.loc[linha, 'obs']

    pg.click(x=762, y=288) ## CLicando no primeiro campo para cadastrar um produto
    ##Codigo do produto
    pg.write(codigo)

    ## Passando para o proximo campo que é a marca do produto
    pg.press("tab")
    pg.write(marca)

    ## Passando para o proximo campo que é o tipo do produto
    pg.press("tab")
    pg.write(tipo)

    ## Passando para o proximo campo que é a categoria do produto
    pg.press("tab")
    pg.write(str(categoria))
    ## Uma maneira para passar valores que são int,flaot etc é fazer ou com str(), ou do jeito que esta abaixo

    ## Passando para o proximo campo que é a preço do produto
    pg.press("tab")
    pg.write(f"{preco}")

    ## Passando para o proximo campo que é o custo do produto
    pg.press("tab")
    pg.write(f"{custo}")

    ## Passando para o proximo campo que é as obs do produto
    pg.press("tab")
    if not pd.isna(obs):
        pg.write(obs)        

    ## Passando para o proximo campo que é o enter para cadastrar o produto
    pg.press("tab")
    pg.press("enter")

    pg.scroll(10000) ## Para subir para o inicio da tela
