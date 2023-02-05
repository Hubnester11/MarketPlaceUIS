import psycopg2

try: 
    conecction=psycopg2.connect(
        host="localhost",
        user="postgres",
        password="12345",
        database="MarketPlaceUIS"
    )
    print("conexion exitosa")
    cursor=conecction.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print("error")

finally:
    conecction.close()
    print("conexion finalizada")