import os
import subprocess
import colorama
from colorama import Fore
import time

def server():
  print(f'\n{Fore.RED}[!] Si pregunta sobre la clave RSA, escribe yes')
  print(f'\n{Fore.LIGHTBLUE_EX}[?] La IP de los usuarios que entren al link se guardara en un archivo llamado ip.txt')
  print(f'\n{Fore.GREEN}[!] Para salir presiona CTRL + C ')
  print(f'\n{Fore.LIGHTYELLOW_EX}[~] Iniciando servidor...')
  cmd_line = "php -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
  p = subprocess.Popen(cmd_line, shell=True)
  out = p.communicate()[0]
  

def menu():
  os.system("killall php")
  os.system("clear")
  print(f'''{Fore.LIGHTYELLOW_EX}
  _____ _____  _      ____   _____  _____ ______ _____  
 |_   _|  __ \| |    / __ \ / ____|/ ____|  ____|  __ \ 
   | | | |__) | |   | |  | | |  __| |  __| |__  | |__) |
   | | |  ___/| |   | |  | | | |_ | | |_ |  __| |  _  / 
  _| |_| |    | |___| |__| | |__| | |__| | |____| | \ \ 
 |_____|_|    |______\____/ \_____|\_____|______|_|  \_\
   ''')
  print(f'\n{Fore.GREEN}[~] Elije una opcion')
  print('[1] Iniciar link iplogger')
  print('[99] Salir')
  var = int(input('root@user: >> '))
  if var == 1:
    server()
  elif var == 99:
    print(f'{Fore.RED}[~] Saliendo del programa...')
    time.sleep(1)
  else:
    print(f'{Fore.RED}[!] Error opcion invalida intenta de nuevo')
    time.sleep(2)
    menu()

menu()
