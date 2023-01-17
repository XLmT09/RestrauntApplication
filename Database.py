import bitdotio

class Database:
    def __init__(self):
        self.dbName = "zkac226/restaurantDB"
        self.dbPassword = "v2_3y4bx_ctTL5vz3jLyK3ytQvA5dZD7"

    def connect(self):
        b = bitdotio.bitdotio(self.dbPassword)
        return b.get_connection(self.dbName)

    def executeQuery(self, connection, query):
        with connection as conn:
            conn.cursor().execute(query)
            
    def createTable(self, connection, tableName, tableDescription):
        self.executeQuery(connection, "DROP TABLE IF EXISTS " + tableName)
        self.executeQuery(connection, tableDescription)
        print("Table " + tableName + " successfully created")

if __name__ == "__main__":
    try:
        myDatabase = Database()
        dbConnection = myDatabase.connect()
        print("successfully connected to database!")

        loginTableSql = "CREATE TABLE loginInfo(username varchar(10), password varchar(10) NOT NULL, role varchar(15), primary key(username))"
        myDatabase.createTable(dbConnection, "loginInfo", loginTableSql)

    except Exception:
        print("Error connecting to database")