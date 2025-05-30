
import requests
import time

def test_estabilidad():
    url = "http://127.0.0.1:5000/productos"
    errores = 0
    total = 50

    print("🚀 Iniciando prueba de estabilidad...")

    for i in range(total):
        producto = {
            "nombre": f"ProductoStress{i}",
            "precio": i * 10.5,
            "descripcion": f"Tipo{i}"
        }

        try:
            res = requests.post(url, json=producto)
            if res.status_code != 200:
                errores += 1
                print(f"❌ Error en iteración {i} → Status: {res.status_code}, Respuesta: {res.text}")
            else:
                print(f"✅ Iteración {i} completada correctamente.")
        except Exception as e:
            errores += 1
            print(f"❌ Excepción en iteración {i}: {e}")
        
        # Puedes descomentar esto si deseas ralentizar la prueba un poco
        # time.sleep(0.1)

    print("\n🎯 Resultado final:")
    if errores == 0:
        print(f"✅ Todas las {total} peticiones se realizaron con éxito.")
    else:
        print(f"⚠️ Se detectaron {errores} errores de {total} intentos.")

if __name__ == "__main__":
    test_estabilidad()
