from conexao_pg import conn
cursor = conn.cursor()
class consulta_bd:
    def __init__(self,sql:str,valores:tuple):
        self.sql = sql
        self.valores = valores
        cursor = conn.cursor()
        cursor.execute(
            self.sql,self.valores
            
            )
        conn.commit()

