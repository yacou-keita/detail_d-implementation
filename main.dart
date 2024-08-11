// Etape 1:
// Définitions d'interface
abstract interface class IDataSource {
  String findAll();
  String findOne();
  String findById();
}

// Etape 2:

// implémentation d'interface par MongodbDataSource
class MongodbDataSource implements IDataSource {
  String findAll() {
    return "MongoDBDataSource : find_all";
  }

  String findOne() {
    return "MongoDBDataSource : find_one";
  }

  String findById() {
    return "MongoDBDataSource : find_by_id";
  }
}

// implémentation d'interface par postgresql
class PostgresqlDataSource implements IDataSource {
  String findAll() {
    return "PostgresSQLDataSource : find_all";
  }

  String findOne() {
    return "PostgresSQLDataSource : find_one";
  }

  String findById() {
    return "PostgresSQLDataSource : find_by_id";
  }
}

//  classe qui sera exposée aux endroits où ton code en a besoin
class DataSourceHandler {
  late IDataSource _dataSource;

  DataSourceHandler(IDataSource dataSource) {
    this._dataSource = dataSource;
  }

  void findAll() {
    print(this._dataSource.findAll());
  }

  void findOne() {
    print(this._dataSource.findOne());
  }

  void findById() {
    print(this._dataSource.findById());
  }
}

//  Injection de la dépendance externe: (PostgresqlDataSource)
DataSourceHandler dataSourceHandler = DataSourceHandler(PostgresqlDataSource());

void main() {
  //  Utilisation
  dataSourceHandler.findAll();
  dataSourceHandler.findOne();
  dataSourceHandler.findById();
}
