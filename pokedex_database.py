import sqlite3

class PokedexDatabase:
    def __init__(self):
        self.db = sqlite3.connect("pokedex.db")
        self.cursor = self.db.cursor()

    def create_table(self, table_name:str) -> None:
        '''Creates a new table in the database'''
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS {}(NUM INTEGER PRIMARY KEY, NAME TEXT,
        ENTRY TEXT)
        '''.format(table_name))

        self.db.commit()

    def get_entry(self, dexnum: int) -> [str]:
        '''Gets the entry'''
        command = "SELECT * FROM POKEMON WHERE NUM=?"
        self.cursor.execute(command, (dexnum,))
        return self.cursor.fetchone()
        
    def close_connection(self):
        '''Closes the connection to the database'''
        self.db.commit()
        self.db.close()
        