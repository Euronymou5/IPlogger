# IPlogger
**Creador de un link IPlogger con una pagina falsa 404 error codigo de html**

# ¿Que es un IPlogger?
**• Un IPlogger es una herramienta que loggea la IP por medio de la conexion del usuario y con esta IP podemos obtener datos como su ciudad,estado,isp,codigo postal,etc.**

**• Existen 2 tipos de IP 1.- La ipv4 y la ipv6 esta herramienta loggea la ipv4 la cual siempre va a ser ejemplo: 199.19.224.6**

# Uso y instalacion
**• La IP de las personas que entren se guardaran en un archivo llamado ip.txt junto a su user-agent**

```
apt install wget -y
```
```
apt install python -y
```
```
apt install python3 -y
```
```
apt install git -y
```
```
apt install php -y
```
```
git clone https://github.com/Euronymou5/IPlogger.git
```
```
cd IPlogger
```
```
python3 run.py
```

# ¿Como usar?

**Una vez dentro del menu elegiremos la opcion 1**


![image.png](https://github.com/Euronymou5/IPlogger/blob/main/.imagenes/Screenshot_20220312-1628012.png?raw=true)


**Despues podemos editar el puerto o dejarlo en el puerto por default (8080)**
![image.png](https://github.com/Euronymou5/IPlogger/blob/main/.imagenes/Screenshot_20220312-1628112.png?raw=true)


**Las IP de las victimas llegaran en la terminal de esta forma**

![image.png](https://github.com/Euronymou5/IPlogger/blob/main/.imagenes/Screenshot_20220312-1632482.png?raw=true)


# Actualizacion 

**Se agregó la generación de un link con cloudflare, por lo que ya no será necesario usar otra opción de tunelización**

**Alternativas a cloudflare:**

**• Podemos usar varios tuneles en este caso el mas facil de usar es localhost.run**

```
ssh -R 80:localhost:8080 nokey@localhost.run
```

# Contacto
**• Discord: Euronymou5#3155**
