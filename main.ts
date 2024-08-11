// Etape 1:
// Définitions d'interface 
interface IDataSource {
    findAll(): string
    findOne(): string
    findById(): string
}

// Etape 2:

// implémentation d'interface par MongodbDataSource
class MongodbDataSource implements IDataSource {
    findAll(): string {
        return "MongoDBDataSource : find_all"
    }
    findOne(): string {
        return "MongoDBDataSource : find_one"
    }
    findById(): string {
        return "MongoDBDataSource : find_by_id"
    }
}

// implémentation d'interface par postgresql
class PostgresqlDataSource implements IDataSource {
    findAll(): string {
        return "PostgresSQLDataSource : find_all"
    }
    findOne(): string {
        return "PostgresSQLDataSource : find_one"
    }
    findById(): string {
        return "PostgresSQLDataSource : find_by_id"
    }

}

//  classe qui sera exposée aux endroits où ton code en a besoin
class DataSourceHandler {

    constructor(private dataSource: IDataSource) { }

    findAll(): void {
        console.log(this.dataSource.findAll())
    }
    findOne(): void {
        console.log(this.dataSource.findOne())
    }
    findById(): void {
        console.log(this.dataSource.findById())
    }
}

//  Injection de la dépendance externe: (PostgresqlDataSource)
const dataSourceHandler = new DataSourceHandler(new PostgresqlDataSource())

//  Utilisation
dataSourceHandler.findAll()
dataSourceHandler.findOne()
dataSourceHandler.findById()