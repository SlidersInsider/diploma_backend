import pymysql

host = "80.87.104.185"
user = "test"
password = "test"
database = "diploma"

try:
    conn = pymysql.connect(host=host, user=user, password=password, database=database)
    print("✅ Подключение успешно!")
    conn.close()
except Exception as e:
    print("❌ Ошибка подключения:", e)
