if [[ `command -v termux-chroot` ]]; then
   termux-chroot ./server/cloudflared tunnel -url localhost:8080 --logfile server/.cld.log > /dev/null 2>&1 &
else
   ./server/cloudflared tunnel -url localhost:8080 --logfile server/.cld.log > /dev/null 2>&1 &
fi

sleep 4
link=$(grep -o 'https://[-0-9a-z]*\.trycloudflare.com' "server/.cld.log")
echo -e "\n\033[32m[~] Link : $link"
