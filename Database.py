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

    def addItem(self, connection, name, price, calories):
        query = "INSERT INTO Dish (dishName, price, calories) VALUES ('{}', '{}', '{}')".format(name, price, calories)
        self.executeQuery(connection, query)
        print(name + " Added to the menu")
        connection.commit()

    def deleteItem(self, connection, productName):
        #Deletes all instances of that item if the productName matches 
        self.executeQuery(connection, "DELETE FROM Dish WHERE dishName = '" + productName +"'")
        connection.commit()
        print(productName + " deleted from menu")

    def updateItem(self, connection, productName, newPrice = None, newCalories = None):
        itemsToUpdate = ""
        if newPrice != None:
            itemsToUpdate += "price = '" + str(newPrice) + "',"
        if newCalories != None:
            itemsToUpdate += "calories = '" + str(newCalories) + "',"
        itemsToUpdate = itemsToUpdate[:len(itemsToUpdate)-1] #removes trailing comma
        
        self.executeQuery(dbConnection, "UPDATE Dish SET " + itemsToUpdate + " WHERE dishName = '" + productName + "'")
        connection.commit()

if __name__ == "__main__":
    try:
        myDatabase = Database()
        dbConnection = myDatabase.connect()
        print("successfully connected to database!")

        #Create a table for storing login information about staff and customers
        userTableSql = "CREATE TABLE Users(username varchar(30), password varchar(30) NOT NULL, role varchar(15), primary key(username))"
        myDatabase.createTable(dbConnection, "Users", userTableSql)

        #Create a table for storing information about each dish on the menu
        dishTableSql = "CREATE TABLE Dish(dishName varchar(30), price float, calories int, primary key(dishName))"
        myDatabase.createTable(dbConnection, "Dish", dishTableSql)

        myDatabase.addItem(dbConnection, 'Pizza', 12.99, 1000)

        myDatabase.updateItem(dbConnection, 'Pizza', newPrice = 15.99, newCalories = 2000)

        items = myDatabase.executeQuery(dbConnection, "SELECT * FROM Dish", True)
        print(items)

        myDatabase.deleteItem(dbConnection, "Pizza")
        items = myDatabase.executeQuery(dbConnection, "SELECT * FROM Dish", True)
        print(items)

    except Exception as e:
        print("Error connecting to database")
        print(e)
    
    