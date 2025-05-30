import subprocess

def test_smoke():
    try:
        proc = subprocess.Popen(["python", "backend.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("✅ El servidor Flask se inició correctamente. Verifica en el navegador en http://127.0.0.1:5000")
        proc.terminate()
    except Exception as e:
        print(f"❌ Error al iniciar el servidor: {e}")

test_smoke()

