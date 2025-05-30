document.addEventListener('DOMContentLoaded', cargarProductos);

let productoEditandoId = null;

function cargarProductos() {
    fetch('/productos')
        .then(response => response.json())
        .then(data => {
            const tbody = document.querySelector('#tabla-productos tbody');
            tbody.innerHTML = '';
            data.forEach(producto => {
                tbody.innerHTML += `
                    <tr>
                        <td>${producto.id}</td>
                        <td>${producto.nombre}</td>
                        <td>${producto.precio}</td>
                        <td>${producto.descripcion}</td>
                        <td>
                            <button onclick="editarProducto(${producto.id})">Editar</button>
                            <button onclick="eliminarProducto(${producto.id})">Eliminar</button>
                        </td>
                    </tr>
                `;
            });
        });
}

function guardarProducto() {
    const nombre = document.getElementById('nombre').value.trim();
    const precio = parseFloat(document.getElementById('precio').value);
    const descripcion = document.getElementById('descripcion').value.trim();

    if (!nombre || isNaN(precio) || !descripcion) {
        alert("⚠️ Todos los campos deben estar correctamente completados.");
        return;
    }

    const producto = {
        nombre: nombre,
        precio: precio,
        descripcion: descripcion
    };

    const url = productoEditandoId ? `/productos/${productoEditandoId}` : '/productos';
    const method = productoEditandoId ? 'PUT' : 'POST';

    fetch(url, {
        method: method,
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(producto)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('message').textContent = data.mensaje;
        cargarProductos();
        limpiarFormulario();
        productoEditandoId = null;
    });
}


function editarProducto(id) {
    fetch(`/productos/${id}`)
        .then(response => response.json())
        .then(producto => {
            productoEditandoId = id;
            document.getElementById('nombre').value = producto.nombre;
            document.getElementById('precio').value = producto.precio;
            document.getElementById('descripcion').value = producto.descripcion;
            window.scrollTo(0, 0);
        });
}

function eliminarProducto(id) {
    const fila = document.querySelector(`button[onclick="eliminarProducto(${id})"]`).closest("tr");
    const nombre = fila.children[1].textContent;

    if (confirm(`¿Estás seguro de que deseas eliminar el producto "${nombre}"?`)) {
        fetch(`/productos/${id}`, { method: 'DELETE' })
            .then(response => response.json())
            .then(data => {
                document.getElementById('message').textContent = data.mensaje;
                cargarProductos();
            });
    }
}


function limpiarFormulario() {
    document.getElementById('nombre').value = '';
    document.getElementById('precio').value = '';
    document.getElementById('descripcion').value = '';
    productoEditandoId = null;
}

function filtrarProductos() {
    const filtro = document.getElementById('busqueda').value.toLowerCase();
    const filas = document.querySelectorAll('#tabla-productos tbody tr');

    filas.forEach(fila => {
        const nombre = fila.children[1].textContent.toLowerCase();
        fila.style.display = nombre.includes(filtro) ? '' : 'none';
    });
}

function ordenarProductos() {
    const criterio = document.getElementById("orden").value;
    const filas = Array.from(document.querySelectorAll("#tabla-productos tbody tr"));

    filas.sort((a, b) => {
        if (criterio === "nombre") {
            return a.children[1].textContent.localeCompare(b.children[1].textContent);
        } else if (criterio === "precio-asc") {
            return parseFloat(a.children[2].textContent) - parseFloat(b.children[2].textContent);
        } else if (criterio === "precio-desc") {
            return parseFloat(b.children[2].textContent) - parseFloat(a.children[2].textContent);
        } else {
            return 0;
        }
    });

    const tbody = document.querySelector("#tabla-productos tbody");
    tbody.innerHTML = "";
    filas.forEach(fila => tbody.appendChild(fila));
}

function eliminarTodos() {
    if (confirm("⚠️ ¿Estás seguro de que deseas eliminar TODOS los productos? Esta acción no se puede deshacer.")) {
        fetch('/productos', { method: 'DELETE' })
            .then(response => response.json())
            .then(data => {
                document.getElementById('message').textContent = data.mensaje;
                cargarProductos();
            });
    }
}
