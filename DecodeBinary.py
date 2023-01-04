from ReportLog import Log

import os
import base64
import random
import string
import imghdr
import Configuracao


class Decode():

    def RandomText(size = 10):

        """ Gera String Aleatorio

        Args:
            size  (int) : Quantidade de Digitos da String Gerada

        Returns:
            text : Valor Gerado

        """

        text = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

        return text


    def DecodeBinary(file, extencao):

        """ Converte Binario para Arquivo

        Args:
            file (str)     : Código Binario
            extencao (str) : Extenção Original do Arquivo

        Returns:
            status    : True -> Proceeso OK | False -> Processo com Falha
            file_dir  : Caminho Absoluto do Arquivo
            errorDesc : Detalhes do Erro, se tiver

        """
        
        # Gera nome aleatorio para o arquivo
        nome = Decode.RandomText()

        try:

            # Cria o diretorio raiz
            dirRaiz = f'{Configuracao.dir_raiz}/temp/'

            # Valida se o diretorio existe
            if not os.path.exists(dirRaiz):
                os.makedirs(dirRaiz)

            Log(event = 'CONVERTENDO BINARIO', eventLog = 'INICIANDO CONVERSAO DE BINARIO PARA ARQUIVO', terminal = False)  # Gera Log de Execução

            # Valida se a extenção está preenchida
            if extencao.replace(" ", "")  == '':
                
                # Pega extenção do arquivo - None = PDF
                extencao = imghdr.what(None, h = base64.b64decode(file))

            # Valida a extenção
            if extencao == None or extencao.upper() == '.PDF':

                # Decodifica o binaro
                decoded_file = base64.b64decode(file)

                # Monta o diretorio do arquivo
                file_dir = f'{dirRaiz}{nome}.PDF'

                # Escreve o arquivo no diretorio apontado
                file = open(file_dir, 'wb')
                file.write(decoded_file)
                file.close

            else:

                # Decodifica o binaro
                decoded_file = base64.b64decode(file)

                # Monta o diretorio do arquivo
                file_dir = f'{dirRaiz}{nome}.JPG'

                # Escreve o arquivo no diretorio apontado
                file = open(file_dir, 'wb')
                file.write(decoded_file)
                file.close


            Log(event = 'CONVERTENDO BINARIO', eventLog = 'CONVERSAO REALIZADA COM SUCESSO', terminal = False)  # Gera Log de Execução

            status = True

            return status, file_dir, ''


        except Exception as errorDesc:

            status = False
            Log(event = 'CONVERTENDO IMAGEM', error = errorDesc, terminal = False) # Gera Log de Execução

            return status, '', errorDesc
