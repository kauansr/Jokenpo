import random
import os
from time import sleep



    


while True:
    try:
        item = ('pedra','papel','tesoura')
        pc = random.randint(0,2)
        print(''' suas opções
        [0] pedra
        [1] papel
        [2] tesoura
        para parar aperte qualquer numero acima de 2 ''')
        jg = int(input('>'))


        

        
        if jg > 2 :
            print("Até...")
            break
            
            
          
       

        print('JO')
        sleep(1)
        print('                          KEN')
        sleep(1)
        print('                                                            PO!!!')

        print('-=' *10)
        print(f'O computador jogou> {item[pc]}')
        print(f'O jogador jogou> {item[jg]}')
        print('-=' *10)


       
    

        if pc == 0:
            if jg == 0:
                print('empate')

                sleep(5)
                os.system('cls')

            elif jg == 1:
                print('Jogador venceu!')

                sleep(5)
                os.system('cls')

            elif jg == 2:
                print('Computador venceu')

                sleep(5)
                os.system('cls')

            else:
                print('Jogada invalida!!')

                sleep(5)
                os.system('cls')
        
        elif pc == 1:
            if jg == 0:
                print('Computador venceu')

                sleep(5)
                os.system('cls')

            elif jg == 1:
                print('empate')

                sleep(5)
                os.system('cls')
            
            elif jg == 2:
                print('Jogador venceu!')

                sleep(5)
                os.system('cls')

            else:
                print('jogada invalida!!')

                sleep(5)
                os.system('cls')
        
        elif pc == 2:
            if jg == 0:
                print('Jogador venceu')

                sleep(5)
                os.system('cls')

            elif jg == 1:
                print('Computador venceu')

                sleep(5)
                os.system('cls')
            
            elif jg == 2:
                print('empate')

                sleep(5)
                os.system('cls')

            else:
                print('jogada invalida!!')

                sleep(5)
                os.system('cls')
        else:
            print('Entre 0 e 2')
        
               
    
    except ValueError as v:
        print("Erro de valor",v)