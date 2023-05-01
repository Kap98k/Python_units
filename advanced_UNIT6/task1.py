#todo:
# Организовать подключение к DB Postgres на базе паттерна Singleton
# Использовать библиотеку https://www.psycopg.org/psycopg3/docs/basic/index.html
# Пароли спросить у админа.

class SettingsDB:
    name = ''
    address = ''
    port = 0
    user = ''
    password = ''
    
    def toString(self) -> str:
        template = "dbname={dbname} host={address} port={port} user={user} password={password}"
        return template.format(
            dbname = self.name,
            address = self.address,
            port = self.port,
            user = self.user,
            password = self.password
        )

class ConnectionDB:
    import psycopg
    from psycopg import sql
    
    __instanse__ = None;
    connection = None;
    cursor = None;
    SqlQuery = sql;
    
    def __init__(self) -> None:
        if ConnectionDB.__instanse__ == None:
            ConnectionDB.__instanse__ = self;
        else:
            raise Exception("Класс уже инициализирован");
            
    def __del__(self) -> None:
        print("~ConnectionDB");
        self.connection.close();
        self.cursor.close()
        
    @staticmethod
    def instance(self):
        if ConnectionDB.__instanse__ == None:
            ConnectionDB();
        else:
            return ConnectionDB.__instanse__;
        
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

query = ConnectionDB.SqlQuery.SQL("CREATE TABLE IF NOT EXISTS films ( \
    code        char(5) CONSTRAINT firstkey PRIMARY KEY, \
    title       varchar(40) NOT NULL, \
    did         integer NOT NULL, \
    date_prod   date, \
    kind        varchar(10), \
    len         interval hour to minute \
);")

connection.createTable(query);