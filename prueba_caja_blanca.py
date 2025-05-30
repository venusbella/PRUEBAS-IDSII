import sqlite3
from backend import DATABASE

def test_insert_logica():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO productos (nombre, precio, descripcion) VALUES (?, ?, ?)", ("WhiteBox", 123, "Tipo1"))
    conn.commit()
    cursor.execute("SELECT * FROM productos WHERE nombre = ?", ("WhiteBox",))
    row = cursor.fetchone()
    assert row is not None
    assert row[1] == "WhiteBox"
    conn.close()

if __name__ == '__main__':
    test_insert_logica()
    print("Prueba completada correctamente")
