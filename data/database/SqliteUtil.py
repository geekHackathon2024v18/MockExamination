import sqlite3

class SqliteUtil:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

    def execute(self, sql:str, params:tuple=None):
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        self.conn.commit()

    def execute_many(self, sql:str, params:tuple=None):
        if params is None:
            self.cursor.executemany(sql)
        else:
            self.cursor.executemany(sql, params)
        self.conn.commit()

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()