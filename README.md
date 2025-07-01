# Generador de Códigos QR 📱

Una aplicación web simple y elegante para generar códigos QR a partir de URLs, construida con Flask y Python.

## 🌟 Características

- ✨ **Interfaz moderna y responsive**: Diseño atractivo que funciona en desktop y móvil
- 🔗 **Generación de QR desde URLs**: Convierte cualquier URL en un código QR
- 📁 **Múltiples formatos**: Soporta PNG y JPG
- 💾 **Descarga directa**: Descarga los códigos QR generados
- 🖼️ **Galería integrada**: Ve todos tus códigos QR generados
- 🚀 **Fácil de usar**: Interfaz intuitiva y amigable

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Flask** - Framework web
- **qrcode** - Generación de códigos QR
- **Pillow (PIL)** - Procesamiento de imágenes
- **HTML5/CSS3** - Frontend moderno

## 📋 Requisitos Previos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

## 🚀 Instalación y Configuración

### 1. Clonar o descargar el proyecto
```bash
# Si tienes git instalado
git clone <URL_DEL_REPOSITORIO>
cd qr_generator_app

# O simplemente descargar y extraer el archivo ZIP
```

### 2. Crear y activar el entorno virtual
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Linux/Mac:
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🎮 Uso de la Aplicación

### Ejecutar la aplicación
```bash
python app.py
```

La aplicación estará disponible en: `http://127.0.0.1:5000`

### Características principales:

1. **Página Principal**:
   - Ingresa cualquier URL válida
   - Selecciona el formato de imagen (PNG o JPG)
   - Haz clic en "Generar Código QR"

2. **Página de Resultados**:
   - Visualiza el código QR generado
   - Descarga la imagen
   - Accede a la galería
   - Genera otro código QR

3. **Galería**:
   - Ve todos los códigos QR generados
   - Descarga cualquier código QR anterior
   - Navegación fácil entre páginas

## 📁 Estructura del Proyecto

```
qr_generator_app/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Este archivo
├── templates/            # Plantillas HTML
│   ├── index.html        # Página principal
│   ├── result.html       # Página de resultados
│   └── gallery.html      # Galería de códigos QR
├── static/               # Archivos estáticos
│   └── qr_codes/         # Códigos QR generados
└── venv/                 # Entorno virtual (generado)
```

## 🎨 Capturas de Pantalla

La aplicación cuenta con un diseño moderno con:
- Gradientes atractivos
- Iconos emoji para mejor UX
- Diseño responsive
- Animaciones suaves
- Interfaz intuitiva

## 🔧 Configuración Avanzada

### Personalizar configuraciones en `app.py`:

```python
# Cambiar puerto y host
app.run(debug=True, host='0.0.0.0', port=8000)

# Cambiar directorio de códigos QR
QR_CODES_DIR = os.path.join('mi_carpeta', 'qr_codes')

# Modificar configuración de QR
qr = qrcode.QRCode(
    version=1,                    # Tamaño del QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección
    box_size=10,                  # Tamaño de cada cuadro
    border=4,                     # Tamaño del borde
)
```

## 📖 API Endpoints

- `GET /` - Página principal
- `POST /generate` - Generar código QR
- `GET /download/<filename>` - Descargar código QR
- `GET /gallery` - Ver galería de códigos QR

## 🐛 Solución de Problemas

### Error: "No module named 'flask'"
```bash
# Asegúrate de que el entorno virtual esté activado
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Reinstala las dependencias
pip install -r requirements.txt
```

### Error: "Address already in use"
```bash
# El puerto 5000 está ocupado, cambia el puerto en app.py:
app.run(debug=True, host='127.0.0.1', port=5001)
```

### Los códigos QR no se generan
- Verifica que la URL sea válida (debe incluir http:// o https://)
- Asegúrate de que la carpeta `static/qr_codes/` tenga permisos de escritura

## 🚀 Despliegue en Producción

Para desplegar en producción:

1. **Desactivar modo debug**:
```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

2. **Usar un servidor WSGI** como Gunicorn:
```bash
pip install gunicorn
gunicorn app:app -b 0.0.0.0:5000
```

3. **Configurar un proxy reverso** con Nginx (opcional)

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Creado con ❤️ por [Tu Nombre]

## 🆘 Soporte

Si tienes problemas o preguntas:
1. Revisa la sección de solución de problemas
2. Crea un issue en el repository
3. Contacta al desarrollador

---

¡Disfruta generando códigos QR! 🎉 # qr_generator_app
