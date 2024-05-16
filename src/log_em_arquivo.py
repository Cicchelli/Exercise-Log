from .manipulador_de_log import ManipuladorDeLog

class LogEmArquivo():
    @classmethod
    def log(cls, message):
        with open('data/log.txt', 'a') as file:
            print(message, file=file)
