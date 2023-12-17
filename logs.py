import logging

def setLogging(name, type, msg):
    # FORMAT = '{levelname:<8} - {asctime}. В модуле "{name}" в строке {lineno:03d} функция "{funcName}()" в {created} секунд записала сообщение: {msg}'
    FORMAT = f'%(asctime)s - %(levelname)s: Модуль %(name)s: %(message)s'

    logging.basicConfig(
                        format = FORMAT
                        # , style = '{'
                        # , datefmt="%F %A %T"
                        , handlers=[logging.FileHandler(filename='./logs.log', encoding='utf-8', mode='a+')]
                        , level=logging.INFO)
    logger = logging.getLogger(name)

    if type == 'info':
        logger.info(msg)
    elif type == 'error':
        # logger.error(msg)
        logging.exception(msg)
    # logger.info(f'{datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S.%f")}: {msg}')


