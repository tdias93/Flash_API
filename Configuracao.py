import os
import configparser


class Configuracao():

    global dir_host 
    global dir_raiz

    config = configparser.ConfigParser()
    config.read(f"{os.path.dirname(os.path.realpath(__file__))}/system/config.ini")

    dir_host = config.get('DIR', 'host')        # Le Arquivo .ini e retorna o host
    dir_raiz = config.get('DIR', 'raiz')        # Le Arquivo .ini e retorna o dir raiz
 