import sqlite3

def send_ex(command):
  connection = sqlite3.connect("baza.db")
  cursor = connection.cursor()
  cursor.execute(command)
  res = cursor.fetchall()
  connection.commit()
  cursor.close()
  connection.close()
  return res


