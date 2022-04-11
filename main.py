# /Library/Frameworks/Python.framework/Versions/3.9/bin
import pymysql

class data_base:
    def __init__(self):
        self.connection = pymysql.connect(
            #si la base esta en un servidor web, el host es la ip del servidor
            host='localhost',
            user='root',
            password='m2a0t0i2&',
            db='platzi_operation'
        )

        self.cursor = self.connection.cursor()
        print('conexion establecida')
        # print(db)

    def select_user(self, id):
        sql = 'SELECT id, username, email FROM users WHERE id = {}'.format(id)
        try:
            self.cursor.execute(sql)
            authors = self.cursor.fetchone()

            print('id:', authors[0])
            print('username:', authors[1])
            print('email:', authors[2])

        except Exception as e:
            raise

database = data_base()
database.select_user(1)