
import os
import sqlite3
from backend import DATABASE

def test_caja_gris_sin_backend():
    print("📦 Probando acceso directo a:", DATABASE)

    if not os.path.exists(DATABASE):
        print("❌ La base de datos no existe. Ejecuta 'python backend.py' una vez para crearla.")
        return

    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        # Insertar
        cursor.execute("INSERT INTO productos (nombre, precio, descripcion) VALUES (?, ?, ?)",
                       ("Caja Gris", 88.8, "Prueba Interna"))
        conn.commit()
        print("✅ Producto insertado directamente.")

        # Verificar
        cursor.execute("SELECT * FROM productos WHERE nombre = ?", ("Caja Gris",))
        producto = cursor.fetchone()
        conn.close()

        if producto:
            print("✅ Producto encontrado:")
            print(f"  ➤ ID: {producto[0]}")
            print(f"  ➤ Nombre: {producto[1]}")
            print(f"  ➤ Precio: {producto[2]}")
            print(f"  ➤ Descripción: {producto[3]}")
        else:
            print("❌ Producto no encontrado.")

    except Exception as e:
        print("❌ Error accediendo a la base de datos:", e)

test_caja_gris_sin_backend()
