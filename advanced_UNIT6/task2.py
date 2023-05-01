#todo: Реализовать класс враппер PgDataBase над библиотекой psycopg3.
# предусмотреть методы
# __connect()
# create_database
# insert(sql, data)
# select(sql)
# delete(sql)
# update(sql, data)
# close_database()

from task1 import SettingsDB

class ConnectionDB:
    import psycopg
    from psycopg import sql
    
    connection = None;
    cursor = None;
    SqlQuery = sql.SQL;
    
    def __init__(self) -> None:
        print("ConnectionDB")
            
    def __del__(self) -> None:
        print("~ConnectionDB");
        self.connection.close();
        self.cursor.close()
        
    def connect(self, settings : SettingsDB):
        connection = ConnectionDB.psycopg.connect(settings.toString())
        self.connection = connection
        self.connection.autocommit = True
        self.cursor = connection.cursor()
    
    def createDatabase(self, settings : SettingsDB):
        try:
            self.connect(settings)
            self.cursor.execute(
                self.sql.SQL("CREATE DATABASE {} ENCODING 'UTF-8'; ").format(
                    self.sql.Identifier(self.dbname)
                )
            )
        except Exception as e:
            print("Ошибка при создании базы данных: " + str(e))
            #self.closeDatabase()

    def createTable(self, sql: SqlQuery):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("Ошибка при создании таблицы: " + str(e));

    def insert(self, sql : SqlQuery):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("Ошибка при вставке в БД: " + str(e));
    
    def select(self, sql : SqlQuery):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("Ошибка при выборке из БД: " + str(e));
    
    def update(self, sql : SqlQuery):
        try:
            self.cursor.execute(sql)
        except Exception as e:
            print("Ошибка при обновлении БД: " + str(e));
    
    def closeDatabase(self) -> None:
        try:
            self.cursor.close();
        except Exception as e:
            print("Ошибка при закрытии БД: " + str(e));


settings = SettingsDB()
settings.name = "python"
settings.address = "172.18.3.222"
settings.port = 5433
settings.user = "postgres"
settings.password = "postgres"

connection = ConnectionDB()
connection.connect(settings)
#connection.createDatabase(settings);

query = ConnectionDB.SqlQuery("CREATE TABLE IF NOT EXISTS films ( \
    code        char(5) CONSTRAINT firstkey PRIMARY KEY, \
    title       varchar(40) NOT NULL, \
    did         integer NOT NULL, \
    date_prod   date, \
    kind        varchar(10), \
    len         interval hour to minute \
);")

connection.createTable(query);

query = ConnectionDB.SqlQuery("INSERT INTO films VALUES (25, 'Deep Deep Blue Sea', 2010);");