from abc import ABC, abstractmethod

#Etape 1:
#Définitions d'interface 
class IDataSource(ABC):

    @abstractmethod
    def find_all(self) -> str: pass

    @abstractmethod
    def find_one(self) -> str: pass

    @abstractmethod
    def find_by_id(self) -> str: pass

#Etape 2:

#implémentation d'interface par MongodbDataSource
class MongodbDataSource(IDataSource):

    def find_all(self):
        return "MongoDBDataSource : find_all"

    def find_one(self):
        return "MongoDBDataSource : find_one"

    def find_by_id(self):
        return "MongoDBDataSource : find_by_id"

#implémentation d'interface par postgresql
class PostgresqlDataSource(IDataSource):

    def find_all(self):
        return "PostgresSQLDataSource : find_all"

    def find_one(self):
        return "PostgresSQLDataSource : find_one"

    def find_by_id(self):
        return "PostgresSQLDataSource : find_by_id"

#  classe qui sera exposée aux endroits où ton code en a besoin
class DataSourceHandler():
    def __init__(self, data_source: IDataSource) -> None:
        self.__data_source = data_source

    def find_all(self) -> None:
        print(self.__data_source.find_all())

    def find_one(self) -> None:
        print(self.__data_source.find_one())

    def find_by_id(self) -> None:
        print(self.__data_source.find_by_id())

# Injection de la dépendance externe: (MongodbDataSource)
data_source_handler = DataSourceHandler(MongodbDataSource())

# Utilisation
data_source_handler.find_all()
data_source_handler.find_one()
data_source_handler.find_by_id()