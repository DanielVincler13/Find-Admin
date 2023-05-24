import sys
import requests as req
import colorama 
from colorama import Fore, Back, Style 


print(Fore.RED,'''    #####  ######   # ####  ######   
   ##   #  #    #  #  ## #  #    ##  
  ##  ###  ##  ##  #   # #  #  #  ## 
  #     #   #  #   #     #  #  ##  # 
  ##  ###   #  #   #  #  #  #  ##  # 
   #  #    ##  ##  #  ## #  #  #  ## 
   #  #    #    #  #  ## #  #    ##  
   ####    ######  #######  ######   

 ####     ####      #######  ######  ########          ######## ######## 
 #  #     #  #      #  #  # ##    ## #  ##  #  ######  #  ##  # #      # 
 #  ####  #  #     ##  #  # #  ##  # #  #  ## ##    ## #  ##  # #  ##### 
       ## #  #     #  ##  # #  ##### #    ##  #  ##  # ##    ## #    #   
 #  ##  # #  #     #        #  ##### #    ##  #      #  ##  ##  #  ###   
 #  ##  # #  ##### #####  # #  ##  # #  #  ## #  #####   #  #   #  ##### 
 #     ## #      #     #  # ##    ## #  ##  # ##    #    #  #   #      # 
  # ####  ########     ####  ######  ########  ######    ####   ######## 

''')

url = input("Coloque a URL: ")

with open("wordlist.txt", "r") as dir:
    find = dir.readlines()

    for word in find:
        word = word.strip()  # Remove espaços em branco no início e no final da palavra
        full_url = f"https://{url}{word}"  # Adiciona o esquema "https://" à URL
        
        try:
            a = req.head(full_url)
            code = a.status_code
            
            if code == 200:
                print(Fore.GREEN, "[ + ] FIND DIR ADMIN ->", full_url)
            if code == 301:
                ru = a.headers.get('Location')
                print(Fore.BLUE, full_url, ">> {}".format(ru))
            if code == 404:
                pass
            
        except req.exceptions.ConnectionError:
            pass
         