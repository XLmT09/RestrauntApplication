import bitdotio

class Database:
    def __init__(self):
        self.dbName = "zkac226/restaurantDB"
        self.dbPassword = "v2_3y4bx_ctTL5vz3jLyK3ytQvA5dZD7"

    def connect(self):
        b = bitdotio.bitdotio(self.dbPassword)
        return b.get_connection(self.dbName)

    def executeQuery(self, connection, query, retrieveData = False):
        with connection as conn:
            cursor = conn.cursor()
            cursor.execute(query)
        
        if retrieveData:
            return cursor.fetchall() #returns all the rows returned by a query result as a list. (useful for SELECT queries)

    def createTable(self, connection, tableName, tableDescription):
        self.executeQuery(connection, "DROP TABLE IF EXISTS " + tableName)
        self.executeQuery(connection, tableDescription)
        print("Table " + tableName + " successfully created")


if __name__ == "__main__":
    try:
        myDatabase = Database()
        dbConnection = myDatabase.connect()
        print("successfully connected to database!")

        #Create a table for storing login information about staff and customers
        userTableSql = "CREATE TABLE User(username varchar(10), password varchar(10) NOT NULL, role varchar(15), primary key(username))"
        myDatabase.createTable(dbConnection, "User", userTableSql)

        #Create a table for storing information about each dish on the menu
        dishTableSql = "CREATE TABLE Dish(dishID int, name varchar(20), price float, calories int, ingredients varchar(50), primary key(dishID))"
        myDatabase.createTable(dbConnection, "Dish", dishTableSql)

    except Exception:
        print("Error connecting to database")