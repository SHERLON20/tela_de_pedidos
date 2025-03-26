import psycopg2

conn = psycopg2.connect(
    database= 'pedidos',
    user= 'postgres',
    password='lelobarril2014',
    host= 'localhost',
    port = '1234',
)