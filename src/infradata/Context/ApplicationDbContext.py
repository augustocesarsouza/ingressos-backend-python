from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class ApplicationDbContext:
    def __init__(self) -> None:
        self.__connection_string = "{}://{}:{}@{}:{}/{}".format(
            'mysql+pymysql',
            'root',
            '123456',
            'localhost',
            '3307',
            'Ingresso'
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        # esse metodo ativa quando 'with' é chamado lá no repositorio
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # esse método é chamado quando o bloco 'with' é encerrado.
        self.session.close()
