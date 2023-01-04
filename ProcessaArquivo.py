from PIL import Image
from ReportLog import Log
from datetime import datetime
from pdf2image import convert_from_path

import os
import Configuracao


#----------------------------------------------------------
#   CONVERTE IMAGEM PARA JPG
#----------------------------------------------------------
def ProcessaArquivo(dirProvisorio, extArquivo, integracao, cnpjCliente, numeroNf, dtEmissao):

    """ Converte Imagens para o Formato JPG

        Args:
            dirProvisorio (str) : Caminho do nomArquivo que sera Convertido
            extArquivo    (str) : Extenção do Arquivo
            integracao    (str) : Nome da Integração 
            cnpjCliente   (str) : CNPJ do cliente responsavel
            numeroNf      (str) : Número da nota fiscal
            dtEmissao     (str) : Data de emissão do CTe
        
        Returns:
            status     : True -> Proceeso OK | False -> Processo com Falha
            dirArquivo : Link Compartilhado
            errorDesc  : Detalhes do Erro, se tiver

    """
     
    # Carrega informações de configuração
    host = Configuracao.dir_host          # Retorna o host
    raiz = Configuracao.dir_processado    # Retorna o dir raiz
       
    Log(event = 'PROCESSANDO ARQUIVO', eventLog = 'INICIANDO CONVERSAO DE IMAGEM PARA JPG', terminal = False)  # Gera Log de Execução
    Log(event = 'PROCESSANDO ARQUIVO', eventLog = f'Arquivo: {dirProvisorio}', terminal = False)               # Gera Log de Execução
    
    # Lista com os meses do ano
    listMes = ['OUTROS','JAN','FEV','MAR','ABR','MAI','JUN','JUL','AGO','SET','OUT','NOV','DEZ']

    # Converte data de string para date
    data = datetime.strptime(dtEmissao, '%Y-%m-%d')

    # Estrutura da pasta
    estruturaPasta = f'{integracao}/{str(data.year)}/{listMes[data.month]}/{str("%02d" % data.day)}/'

    # Diretorio raiz
    dirArquivo = f'{raiz}/{estruturaPasta}'

    # Nome do arquivo
    nomeArquivo = f'{cnpjCliente}_{numeroNf}.jpg'
    
    # Valida se o diretorio existe
    if not os.path.exists(dirArquivo):
        os.makedirs(dirArquivo)

    # Diretorio absoluto
    dirArquivo = f'{dirArquivo}/{nomeArquivo}'

    try:

        # Valida se a extenção está preenchida
        if extArquivo.replace(" ", "") == '':

            # Pega extenção do arquivo
            extArquivo = f'.{dirProvisorio.split(".")[1]}'

        # Valida extenção da imagem
        if extArquivo.upper() == '.PDF':

            filePath = dirProvisorio
            popplerPath = f'{os.path.dirname(os.path.realpath(__file__))}/system/extra/poppler-0.68.0/bin'

            # Valida SO
            if os.name == 'nt':

                # Abre arquivo e salva no novo diretorio como imagem
                for rgbImg in convert_from_path(filePath, poppler_path = popplerPath):
                    rgbImg.save(dirArquivo, 'JPEG')

            else:

                # Abre arquivo e salva no novo diretorio como imagem
                for rgbImg in convert_from_path(filePath):
                    rgbImg.save(dirArquivo, 'JPEG')

        else:

            # Abre arquivo da imagem
            imagem = Image.open(dirProvisorio)

            # Converte imagem para binario
            rgbImg = imagem.convert('RGB')

            # Salva binario
            rgbImg.save(dirArquivo)

        Log(event = 'PROCESSANDO ARQUIVO', eventLog = 'CONVERSAO REALIZADA COM SUCESSO', terminal = False)        # Gera Log de Execução

        # Remove arquivo provisorio
        os.remove(dirProvisorio)

        status = True
        url = host + estruturaPasta + nomeArquivo# estruturaPasta.replace('\\', '/') + nomeArquivo

        return status, url, ''

    except Exception as errorDesc:
    
        status = False

        Log(event = 'PROCESSANDO ARQUIVO', error = errorDesc, terminal = False) # Gera Log de Execução

        # Remove arquivo provisorio
        os.remove(dirProvisorio)

        return status, '', errorDesc


if __name__ == '__main__':
    ProcessaArquivo(dirProvisorio = '', extArquivo = '', integracao = '', cnpjCliente = '', numeroNf = '', dtEmissao = '')