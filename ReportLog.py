import os

from datetime import datetime

#----------------------------------------------------------
#   LOG DE EXECUÇÃO
#----------------------------------------------------------
def Log(event, eventLog = '---', error = '---', line = False, terminal = True, writeLog = True):

    """ Gela Logs em Tempo de Execução

        Args:
            event (str)     : Evento Executado
            eventLog (str)  : Descrição do Evento
            error (str)     : Descrição do Erro, se Houver
            line (bool)     : Define se Pula ou não de Linha
            terminal (bool) : Define se Aparece ou Não no Terminal
            writeLog (bool) : Define se Deve ou não Escrever o log

    """

    # Registra Data e Hora do Evento
    registry = datetime.now()
    registry = registry.strftime('%d/%m/%Y - %H:%M:%S')
    
    # Coverte Valores para String em Maiúsculo
    event    = str(event).upper()
    eventLog = str(eventLog).upper()
    error    = str(error).upper()


    if writeLog:

        # Abre Arquivo De Texto
        doc = open(f'{os.path.dirname(os.path.realpath(__file__))}/system/Log.txt', 'a')

        # Registro O Evento No Arquivo
        doc.writelines(f'Event      : {event}    \n'
                       f'Event Log  : {eventLog} \n' + 
                       f'Registry   : {registry} \n' +
                       f'Error      : {error}    \n\n' + 
                       f'-----------------------------------------------------------------------\n\n')

        doc.close()


    if terminal:

        if eventLog != '---' and eventLog != '':
            print(f'############### Event: {event} -> Event Log: {eventLog} - {registry}.')
        else:
            print(f'############### Event: {event} -> Error: {error} - {registry}.')

        if line == True: 
            print('\n')