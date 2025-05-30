Espejos del Alma

 Descripción breve
“Espejos del Alma” es una aplicación web creada para un emprendimiento de accesorios. Permite registrar, listar, buscar, ordenar y eliminar productos (nombre, precio, descripción) a través de una interfaz sencilla y visualmente agradable. La app utiliza Flask como backend y SQLite como base de datos. Fue desarrollada aplicando principios de arquitectura por capas y un enfoque centrado en pruebas.

---

 Objetivo del ejercicio

El objetivo principal fue aplicar **pruebas de software** sobre un sistema funcional, validando su comportamiento interno, externo, estabilidad y experiencia de usuario. Se buscó asegurar la calidad del sistema mediante pruebas automatizadas y manuales desde distintas perspectivas.

---

 Pruebas aplicadas

 Prueba de Humo
- **Objetivo:** Verificar que el servidor Flask arranca correctamente.
- **Resultado:** El servidor se inicia sin errores y permite acceder a la app.

 Prueba Unitaria
- **Objetivo:** Validar que se puede crear un producto mediante la API.
- **Resultado:** Código 200 y mensaje de éxito recibido correctamente.

 Prueba de Caja Blanca
- **Objetivo:** Probar directamente la lógica interna accediendo a la base de datos.
- **Resultado:** Inserción directa del producto y recuperación exitosa.

 Prueba de Caja Negra
- **Objetivo:** Verificar el comportamiento externo de la API sin conocer su lógica interna.
- **Resultado:** Inserción correcta simulando un cliente externo.

 Prueba de Caja Gris
- **Objetivo:** Acceso intermedio con conocimiento parcial del sistema y manipulación directa de la base.
- **Resultado:** Inserción y recuperación del producto desde consola, correctamente.

 Prueba de Estabilidad
- **Objetivo:** Enviar 50 solicitudes POST consecutivas para verificar la resistencia del sistema.
- **Resultado:** Todas las peticiones fueron exitosas, sin errores ni caídas.

 Prueba UI/UX Manual
- **Objetivo:** Verificar manualmente que la interfaz funcione correctamente.
- **Acciones verificadas:**
  -  Guardar productos desde el formulario.
  -  Buscar productos por nombre.
  -  Ordenar productos por nombre y precio.
  -  Eliminar todos los productos con confirmación.

---

Mejoras aplicadas

-  Barra de búsqueda por nombre de producto.
-  Validación de campos vacíos en el formulario.
-  Confirmación previa al eliminar productos.
-  Botón para eliminar todos los productos.
-  Menú desplegable para ordenar productos.
-  Estilo visual con CSS personalizado y diseño claro.
-  Mensajes dinámicos de estado tras operaciones.

---
 Herramientas y tecnologías usadas

- **Backend:** Flask (Python)
- **Base de datos:** SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Pruebas:** `unittest`, `pytest`, `requests`, `sqlite3`
- **Editor:** Visual Studio Code
- **Navegador usado:** Google Chrome (DevTools)

---

Cómo clonar y ejecutar el proyecto

Sigue estos pasos para clonar el repositorio, ejecutar el sistema y probarlo:

1. **Clona este repositorio desde GitHub:**

   bash
   git clone https://github.com/tu_usuario/espejos-del-alma.git
   cd espejos-del-alma
Instala Flask (si aún no lo tienes):


pip install flask
Ejecuta el servidor:


python backend.py
Abre tu navegador en:


http://127.0.0.1:5000
(Opcional) Ejecuta las pruebas:

Prueba de humo:
python prueba_humo.py
Prueba unitaria:
python prueba_unitaria.py
Prueba de estabilidad:
python prueba_estabilidad.py
Otras: prueba_caja_negra.py, prueba_caja_blanca.py, prueba_caja_gris.py

Créditos del autor
Nombre del estudiante: Isabella Mejia Salinas
Asignatura: Ingenieria de software
Fecha: 30/05/2025
