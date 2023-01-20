import sqlite3

#Creates a connection to a given database 
connection = sqlite3.connect("example.db")

#Creates a 'cursor' which is used to execute statements 
c = connection.cursor()

#Checks if the table already exists 
c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='menu' """)

#fetches the result of the execute above
results = c.fetchone()

#If table exists (true) print the message else create the table menu
if results:
    print("The table already exists")
else:
    c.execute("""CREATE TABLE menu (productName TEXT, price REAL)""")


def updateItem(productName,price):

    connection = sqlite3.connect("example.db")
    c = connection.cursor()

    c.execute("UPDATE menu SET price = ? WHERE productName = ?", (price, productName))

    connection.commit()

#Function to add an item into the menu table 
def addItem(productName, price):

    connection = sqlite3.connect("example.db")
    c = connection.cursor()

    #Inserts the item into table menu
    c.execute('INSERT INTO menu (ProductName, Price) VALUES (?, ?)', (productName, price))

    #Commits the changes into the table
    connection.commit()

def deleteItem(productName):

    connection = sqlite3.connect("example.db")
    c = connection.cursor()
    
    #Deletes all instances of that item if the productName matches 
    c.execute("DELETE FROM menu WHERE productName = ?", (productName,))

    connection.commit()

#Example of the function addItem being used, an item "Milk" is being added that has productName = 'Milk' and price = 12.99 
addItem("Milk", 12.99)

#Example of the function deleteItem being used, any instance of where productName = 'Pizza' will be deleted from the table
deleteItem("Burrito")

#Example of the function updateItem being used, items with name "Milk" have their price updated to 20.00
updateItem("Milk", 20.00)


#Simple check to see if an item exists, if productName exists in table a message with the item (ProductName, Price) is displayed
c.execute("SELECT * FROM menu WHERE ProductName = ?", ('Milk',))
item = c.fetchone()

if item:
    print("Item exists in the table: ", item)
else:
    print("Item does not exist in the table")


#Prints out the entire menu table 
c.execute("SELECT * FROM menu")
rows = c.fetchall()
for row in rows:
    print(row)

#closes all of the open connections at the end of the program 
c.close()
connection.close()

#Note:
#This implementation allows for multiple instances of the same item being added to the list, will be updating it so that it
#restricts the same item being added soon