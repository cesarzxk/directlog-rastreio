import requests
import bs4
import time
from pygame import mixer

mixer.init()
mudanca = 0
finish = 's'
loop = 0
tempo = 0
Try = 1
rem = ''
tamanho = 0

while finish != 'n':
 if Try == 1:
  try:
     with open("remessas.txt",'r') as arq:
       for i in arq:
           tamanho += 1
       if tamanho != 0:
         print("Bem vindo de volta!")
         x = 0
         y = 0
         arq.seek(0)
         for i in arq:
             x += 1
             print(x,i,end="")
         y = int(input('Escolha uma remessa pelo número ou digite 0 para uma nova: '))
         if y == 0:
             rem = str(input("Entre com o número da remessa:"))
             with open("remessas.txt", "a") as arq:
                 arq.write(rem+'\n')
             Try = 0
         else:
             arq.seek(y-1)
             rem = arq.readline(14)
             Try = 0
       else:
           with open("remessas.txt", 'a') as arq:
               print('Seja bem vindo!')
               rem = str(input("Entre com o número da remessa:"))
               arq.write(rem+'\n')
  except:
     with open("remessas.txt", 'a') as arq:
         print('Seja bem vindo!')
         rem = str(input("Entre com o número da remessa:"))
         arq.write(rem+'\n')
         Try = 0

 else:
  if finish == 's':
      rem = str(input("Entre com o número da remessa:"))
      with open("remessas.txt", "a") as arq:
          arq.write(rem+'\n')
  else:
    time.sleep(tempo)
    print('________________________________________________________________________________________________________________________________________________________________')



 redditFile = requests.get("https://www.directlog.com.br/track_individual/index.asp?fase=&tipo=0&numtracking="+rem)

 soup = bs4.BeautifulSoup(redditFile.content, "html.parser")



 vet = []
 for i in soup:
    vet.append(str(i))

 vet2 = vet[1].split('<')
 vet3 = []
 for i in vet2:
    if i == 'b>DATA':
        x = vet2.index(i)
        while vet2[x] != '/table>':
            vet3.append(vet2[x])
            x+=1


 for i in range(30):
    del vet3[0]

 tamanho = len(vet3)
 i = 0
 while i < tamanho:
    if vet3[i] == ('br/>'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/b>\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/td>\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/tr>\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('tr>'):
        del vet3[i]
        i = 0
    if vet3[i] == ('td align="left" colspan="6">' ):
        del vet3[i]
        i = 0
    if vet3[i] == ('font face="Verdana" size="2">' ):
        del vet3[i]
        i = 0
    if vet3[i] == ('small>* Dados sujeitos à alteração até o final do dia.' ):
        del vet3[i]
        i = 0
    if vet3[i] == ('/small>'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/font>'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/tr>\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/b>\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/td>\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('td align="left" valign="top">\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/b>'):
        del vet3[i]
        i = 0
    if vet3[i] == ('br/>\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('td align="left" valign="top">\n'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/td>'):
        del vet3[i]
        i = 0
    if vet3[i] == ('/tr>'):
        del vet3[i]
        i = 0
    if vet3[i] == ('tr bgcolor="#FFEAEA" onmouseout="mOut(this,\'#FFEAEA\');this.style.color=\'black\';" onmouseover="mOvr(this,\'EF3A3E\');this.style.color=\'white\';" style="font-family:Verdana,Arial; font-size:10px; text-decoration:none; color:black;">\n'):
        del vet3[i]
        i = 0
    if len(vet3[i]) > 200 :
        del vet3[i]
        i = 0
    if vet3[i] == ('b>'):
        del vet3[i]
        i = 0

    tamanho = len(vet3)
    i+=1
 for i in range(len(vet3)):
     if vet3[4] == vet3[i] and 4 != i:
         del vet3[i]
         break
 horas = time.localtime()
 print('---------------------------------------|Última atualização:',str(horas[3])+':'+str(horas[4])+':'+str(horas[5]))
 print(vet3[4][12:])
 del vet3[4]
 tam = len(vet3)
 print('--------------------------------------------------------------------')
 x = 0
 while x < tam-1:

    print(vet3[x][2:],'|',vet3[x+1][2:],'|', vet3[x+2][2:],'|',vet3[x+3][2:])
    print('--------------------------------------------------------------------')
    x += 4

 if mudanca < len(vet3):
        if (vet3[len(vet3) - 2][2:-6] or vet3[len(vet3) - 1][2:-6]) == 'Remessa em Transferência':
            mixer.music.load('Transferencia.mp3')
            mixer.music.play()

        elif (vet3[len(vet3) - 2][2:-6] or vet3[len(vet3) - 1][2:-6]) == 'Em Transferencia':
                mixer.music.load('Transferencia.mp3')
                mixer.music.play()

        elif (vet3[len(vet3) - 2][2:] or vet3[len(vet3) - 1][2:]) == 'Remessa Transferida':
            mixer.music.load('Transferida.mp3')
            mixer.music.play()

        elif (vet3[len(vet3) - 2][2:-6] or vet3[len(vet3) - 1][2:-6]) == 'Geração da Remessa':
            mixer.music.load('Gerando.mp3')
            mixer.music.play()

        elif (vet3[len(vet3) - 2][2:-6] or vet3[len(vet3) - 1][2:-6]) == 'Remessa em Rota':
            mixer.music.load('Rota.mp3')
            mixer.music.play()
        else:
            mixer.music.load('Desconhecida.mp3')
            mixer.music.play()


        mudanca = len(vet3)

 if loop == 0:
     finish = 's'
 if finish == 's':
    finish = str(input('Deseja consultar outro número?[s/n}(ou r para racomeçar): '))
    if finish == 'r':

        loop = int(input('Reseja repetir quantas vezes? '))-1
        tempo = float(input('Tempo até o looping em minutos: '))*60
    else:
        Try = 1
        mudanca = 0
 else:
     loop -=1
