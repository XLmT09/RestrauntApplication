import bitdotio

class Database:
    def __init__(self):
        self.dbName = "zkac226/restaurantDB"
        self.dbPassword = "v2_3y4bx_ctTL5vz3jLyK3ytQvA5dZD7"

    def connect(self):
        b = bitdotio.bitdotio(self.dbPassword)
        with b.get_connection(self.dbName) as conn:
            return conn

if __name__ == "__main__":
    try:
        dbConnection = Database().connect()
        print("successfully connected to database!")
    except Exception:
        print("Error connecting to database")