import logging
from datetime import datetime


# Niveles personalizados
SUCCESS = 25
EVENT = 35
SECURITY = 45

logging.addLevelName(SUCCESS, "SUCCESS")
logging.addLevelName(EVENT, "EVENT")
logging.addLevelName(SECURITY, "SECURITY")


class Logger:
    def __init__(self, nombre="App", archivo="app.log"):
        self.nombre = nombre
        self.archivo = archivo

        self.logger = logging.getLogger(nombre)
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            handler = logging.FileHandler(
                archivo,
                encoding="utf-8"
            )

            formato = logging.Formatter(
                "[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S"
            )

            handler.setFormatter(formato)
            self.logger.addHandler(handler)


    def info(self, texto):
        self.logger.info(texto)


    def warning(self, texto):
        self.logger.warning(texto)


    def error(self, texto):
        self.logger.error(texto)


    def debug(self, texto):
        self.logger.debug(texto)


    def success(self, texto):
        self.logger.log(SUCCESS, texto)


    def evento(self, texto):
        self.logger.log(EVENT, texto)


    def seguridad(self, texto):
        self.logger.log(SECURITY, texto)


    def custom(self, nivel, texto):
        self.logger.log(nivel, texto)


def crear_logger(nombre="App", archivo="app.log"):
    return Logger(nombre, archivo)