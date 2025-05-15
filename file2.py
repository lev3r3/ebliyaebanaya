im


class App: 
    def database(self):
        try: 
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='0000',
                database='polarflowers51'
            )
            cursor = connection.cursor()
            
            cursor.execute("SELECT * FROM клиент")
            result = cursor.fetchall()
            
            print(result)
            
            cursor.close()
            connection.close()
        except mysql.connector.Error as err:
            print("Zalupa")


if __name__ == "__main__":
    app = App()
    
    app.database()





