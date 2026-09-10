# CISA - Conferencia de Institutos Seculares de Argentina

Plataforma web oficial desarrollada en **Django** y **MySQL** para la **Conferencia de Institutos Seculares de Argentina (CISA)**. Este portal centraliza la difusión institucional, noticias, eventos y el catálogo general de los distintos institutos seculares con presencia en el país.

---

## 📋 Tabla de Contenidos
- [Características Principales](#-características-principales)
- [Stack Tecnológico](#-stack-tecnológico)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Modelos de Datos](#-modelos-de-datos)
- [Instalación y Puesta en Marcha](#-instalación-y-puesta-en-marcha)
  - [Opción 1: Con Docker & Docker Compose (Recomendado)](#opción-1-con-docker--docker-compose-recomendado)
  - [Opción 2: Instalación Local Tradicional](#opción-2-instalación-local-tradicional)
- [Variables de Entorno](#-variables-de-entorno)
- [Rutas y Endpoints](#-rutas-y-endpoints)
- [Despliegue y Producción](#-despliegue-y-producción)

---

## ✨ Características Principales

- **Portal Institucional**: Presentación de la identidad, historia y misión canónica de los Institutos Seculares en Argentina.
- **Directorio de Institutos Seculares**: Catálogo detallado de institutos masculinos, femeninos, sacerdotales y laicales con información de fundación, carisma, miembros, presencia geográfica y vías de contacto.
- **Gestión de Novedades y Eventos**: Publicación y administración de noticias con soporte para imágenes, fechas y horarios de eventos.
- **Panel de Autenticación y Administración**: Control de acceso y operaciones CRUD restringidas para usuarios administradores (`@staff_member_required`).
- **Soporte PWA (Progressive Web App)**: Service worker integrado (`serviceworker.js`) y assets adaptados para dispositivos móviles.
- **Optimización de Estáticos**: Implementación de **WhiteNoise** con compresión y manifest hashes para un rendimiento óptimo en producción.
- **Contenerización Completa**: Configuración lista para despliegue con Docker y MySQL 8.0.

---

## 🛠 Stack Tecnológico

| Capa | Tecnología |
| :--- | :--- |
| **Backend** | Python 3.12, Django 5.x |
| **Base de Datos** | MySQL 8.0 (`mysqlclient`) |
| **Manejo de Imágenes** | Pillow 10.4.0 |
| **Archivos Estáticos** | WhiteNoise 6.6+ |
| **Frontend** | HTML5, CSS3, JavaScript, Bootstrap 5, Bootstrap Icons |
| **Contenedores** | Docker, Docker Compose |
| **Servidor Web / Proxy** | Compatible con Nginx, Cloudflare Tunnels |

---

## 📂 Estructura del Proyecto

```text
project_CISA/
├── core/                    # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Ajustes generales, bases de datos y seguridad
│   ├── urls.py              # Enrutador global del proyecto
│   └── wsgi.py
├── news/                    # Aplicación de noticias, inicio y contacto
│   ├── forms.py             # Formularios de carga y edición de noticias
│   ├── models.py            # Modelo 'news' (noticias y eventos)
│   ├── templates/news/      # Vistas HTML (home, cisa, noticias, detalle, contacto)
│   ├── urls.py              # Rutas de la app news
│   └── views.py             # Lógica de controladores y vistas
├── institutos/              # Directorio y gestión de institutos seculares
│   ├── forms.py             # Formularios para creación/edición de institutos
│   ├── models.py            # Modelo 'Instituto' y enumeración 'OpcionesTipoInstituto'
│   ├── templates/institutos/# Plantillas para listado, detalle y CRUD
│   ├── urls.py              # Rutas de institutos
│   └── views.py             # Vistas de catálogo y administración
├── users/                   # Autenticación y sesiones
│   ├── templates/users/     # Plantilla de inicio de sesión
│   ├── urls.py              # Rutas de login / logout
│   └── views.py             # Vistas de autenticación
├── static/                  # Archivos estáticos fuente (CSS, JS, logos, iconos PWA)
├── staticfiles/             # Archivos estáticos compilados para producción (WhiteNoise)
├── templates/               # Plantillas base y layouts globales
│   └── layouts/
│       ├── base.html        # Layout principal (Navbar, Footer, CSS, JS)
│       ├── logo_svg.html    # Logotipo vectorial embebible
│       └── serviceworker.js # Service worker para soporte PWA
├── docker-compose.yml       # Orquestación de servicios Django + MySQL
├── Dockerfile               # Construcción de la imagen Docker de la aplicación
├── requirements.txt         # Dependencias Python
└── manage.py                # Utilitario de gestión de Django
```

---

## 🗄 Modelos de Datos

### 1. `news` (App `news`)
Almacena las publicaciones, noticias institucionales y convocatorias:
- `titulo`: Título de la publicación (`max_length=50`).
- `resumen`: Síntesis o copete de la noticia.
- `cuerpo`: Contenido completo de la nota.
- `fecha`: Fecha y hora de creación automática (`auto_now_add=True`).
- `imagen`: Imagen de cabecera (`upload_to='noticias/'`).
- `ubicacion`: Lugar de realización del evento (opcional).
- `fecha_evento`: Fecha programada del evento (opcional).
- `hora_evento`: Hora programada del evento (opcional).

### 2. `Instituto` (App `institutos`)
Representa cada instituto secular registrado:
- **Identificación:** `nombre`, `sigla`, `logo`, `tipo_instituto` (Masculino, Femenino, Ambas, Sacerdotal, Laical).
- **Identidad y Carisma:** `breve_descripcion`, `historia`, `carisma`.
- **Fundación:** `anio_fundacion`, `fundador`, `foto_fundador`, `pais_origen`.
- **Gobierno y Miembros:** `responsable`, `consejo_gobierno`, `numero_miembros`, `paises_presencia`.
- **Presencia en Argentina:** `anio_llegada_argentina`, `provincias_diocesis`, `casas_comunidades`, `tipo_presencia`.
- **Canales de Contacto:** `direccion`, `telefono`, `email`, `website`, `redes_sociales`.

---

## 🚀 Instalación y Puesta en Marcha

### Opción 1: Con Docker & Docker Compose (Recomendado)

Esta es la forma más rápida y estándar para levantar el entorno sin necesidad de instalar MySQL ni Python en el host.

#### 1. Clonar el repositorio
```bash
git clone https://github.com/rjsoloaga/CISA.git
cd CISA
```

#### 2. Configurar variables de entorno (opcional)
Crea un archivo `.env` en la raíz si deseas personalizar las credenciales (o utiliza los valores preconfigurados en `docker-compose.yml` para desarrollo local).

#### 3. Construir e iniciar los contenedores
```bash
docker-compose up -d --build
```

El servicio `web`:
1. Esperará activamente a que el contenedor de base de datos (`mysql:8.0`) esté listo en el puerto 3306.
2. Aplicará automáticamente las migraciones (`python manage.py migrate`).
3. Creará el superusuario inicial (`rsoloaga`) si aún no existe.
4. Iniciará el servidor de desarrollo en `http://localhost:8000`.

#### 4. Acceder a la aplicación
- **Sitio Web:** [http://localhost:8000](http://localhost:8000)
- **Panel Administrativo:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Login de Gestión:** [http://localhost:8000/login/](http://localhost:8000/login/)

---

### Opción 2: Instalación Local Tradicional

#### 1. Requisitos Previos
- **Python 3.12+**
- **MySQL Server 8.0+** corriendo en local o accesible por red
- Paquetes del sistema para compilar `mysqlclient` (en Linux/Debian: `gcc`, `default-libmysqlclient-dev`, `pkg-config`)

#### 2. Crear y activar un entorno virtual
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

#### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 4. Configurar Base de Datos en MySQL
Crea la base de datos y usuario correspondiente en tu servidor MySQL:
```sql
CREATE DATABASE cisa_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'javier_admin'@'localhost' IDENTIFIED BY 'Ciro2014';
GRANT ALL PRIVILEGES ON cisa_db.* TO 'javier_admin'@'localhost';
FLUSH PRIVILEGES;
```

#### 5. Configurar Variables de Entorno
En Windows (PowerShell):
```powershell
$env:DJANGO_DEBUG="True"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
$env:DB_NAME="cisa_db"
$env:DB_USER="javier_admin"
$env:DB_PASSWORD="TuPassword"
```

#### 6. Ejecutar migraciones y crear superusuario
```bash
python manage.py migrate
python manage.py createsuperuser
```

#### 7. Iniciar el servidor
```bash
python manage.py runserver
```

---

## 🔐 Variables de Entorno

| Variable | Descripción | Valor por defecto |
| :--- | :--- | :--- |
| `DJANGO_DEBUG` | Activa/desactiva modo depuración (`True` / `False`) | `False` |
| `SECRET_KEY` | Clave secreta criptográfica de Django (Obligatoria si `DEBUG=False`) | Clave insegura en local |
| `DB_NAME` | Nombre de la base de datos MySQL | `cisa_db` |
| `DB_USER` | Usuario de la base de datos | `javier_admin` |
| `DB_PASSWORD` | Contraseña del usuario de base de datos | - |
| `DB_HOST` | Host del servidor MySQL (`db` en Docker o `127.0.0.1` en local) | `db` |
| `DB_PORT` | Puerto de conexión MySQL | `3306` |

---

## 🗺 Rutas y Endpoints

### Públicas
- `/`: Portada principal con últimas noticias y bienvenida.
- `/news/`: Listado completo de noticias y eventos.
- `/news/<int:pk>/`: Detalle individual de una noticia.
- `/cisa/`: Información institucional sobre la identidad de los Institutos Seculares.
- `/contacto/`: Formulario de consulta y datos de contacto.
- `/documentos/`: Repositorio de documentos descargables.
- `/institutos/`: Directorio de Institutos Seculares.
- `/institutos/<int:pk>/`: Ficha técnica y detallada de un instituto.

### Gestión y Administración
- `/login/`: Inicio de sesión para administradores/staff.
- `/login/logout/`: Cierre de sesión seguro.
- `/admin/`: Panel de administración nativo de Django.
- `/noticias/crear/`: Formulario para redactar noticias (`@staff_member_required`).
- `/noticias/<int:pk>/editar/`: Modificar noticia existente (`@staff_member_required`).
- `/noticias/<int:pk>/eliminar/`: Baja de noticia (`@staff_member_required`).
- `/institutos/crear/`: Alta de instituto secular (`@staff_member_required`).
- `/institutos/<int:pk>/editar/`: Actualización de ficha de instituto (`@staff_member_required`).
- `/institutos/<int:pk>/eliminar/`: Baja de instituto (`@staff_member_required`).

---

## 🛡 Despliegue y Producción

El proyecto incluye configuraciones listas para entornos productivos:
1. **WhiteNoise**: Los archivos estáticos se procesan automáticamente mediante `CompressedManifestStaticFilesStorage`, optimizando su entrega y cacheo mediante encabezados HTTP eficientes.
2. **Proxy Inverso y SSL**:
   - `SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')` está activo para operar correctamente detrás de proxies inversos o túneles de Cloudflare.
   - Dominios de confianza configurados en `CSRF_TRUSTED_ORIGINS` y `ALLOWED_HOSTS`.
3. **Persistencia de Media y Base de Datos**:
   - En Docker, la base de datos persiste en el volumen `mysql_data`.
   - La carpeta `media/` debe mapearse como volumen persistente en producción para evitar la pérdida de imágenes cargadas en el servidor.
