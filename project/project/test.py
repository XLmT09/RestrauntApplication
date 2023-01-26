import Database

database = Database.Database()

x = database.executeQueryGet(database.connect(),"SELECT * From MenuItem")
