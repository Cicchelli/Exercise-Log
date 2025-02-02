from datetime import datetime


class Log:
    def __init__(self, manipuladores=None):
        self.__manipuladores = set(manipuladores or [])

    def adicionar_manipulador(self, manipulador):
        self.__manipuladores.add(manipulador)

    def info(self, msg):
        self.__log("INFO", msg)

    def alerta(self, msg):
        self.__log("ALERTA", msg)

    def erro(self, msg):
        self.__log("ERRO", msg)

    def debug(self, msg):
        self.__log("DEBUG", msg)

    def __log(self, nivel, msg):
        formatted_msg = self.__formatar(nivel, msg)
        for manipulador in self.__manipuladores:
            manipulador.log(formatted_msg)

    def __formatar(self, nivel, msg):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return f"[{nivel} - {data}]: {msg}"
