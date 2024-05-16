from .manipulador_de_log import ManipuladorDeLog

class LogEmTela(ManipuladorDeLog):
    def log(self, message):
        print(message)

