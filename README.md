# CISA - Conferencia de Institutos Seculares de Argentina

Plataforma web oficial desarrollada en **Django** y **MySQL** para la **Conferencia de Institutos Seculares de Argentina (CISA)**. El portal centraliza la difusión institucional, noticias, eventos y el catálogo general de los distintos institutos seculares con presencia en el país.

---

## 📋 Tabla de Contenidos

- [Descripción](#-descripción)
- [Características Principales](#-características-principales)
- [Stack Tecnológico](#-stack-tecnológico)
- [Requisitos](#-requisitos)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Modelos de Datos](#-modelos-de-datos)
- [Instalación y Puesta en Marcha](#-instalación-y-puesta-en-marcha)
  - [Opción 1: Docker & Docker Compose](#opción-1-docker--docker-compose-recomendado)
  - [Opción 2: Instalación Local Tradicional](#opción-2-instalación-local-tradicional)
- [Variables de Entorno](#-variables-de-entorno)
- [Usuarios y Permisos](#-usuarios-y-permisos)
- [Rutas y Endpoints](#-rutas-y-endpoints)
- [Archivos Estáticos y Media](#-archivos-estáticos-y-media)
- [Desarrollo y Mantenimiento](#-desarrollo-y-mantenimiento)
- [Tests](#-tests)
- [Despliegue y Producción](#-despliegue-y-producción)
- [Backups y Restauración](#-backups-y-restauración)
- [Troubleshooting](#-troubleshooting)
- [Seguridad](#-seguridad)
- [Roadmap](#-roadmap)
- [Contribución](#-contribución)
- [Licencia](#-licencia)
- [Autor y Contacto](#-autor-y-contacto)

---

## 📌 Descripción

CISA es una plataforma institucional orientada a publicar información sobre la Conferencia de Institutos Seculares de Argentina y mantener un directorio de los institutos seculares presentes en el país.

El sistema combina un sitio público con herramientas de gestión para usuarios administradores/staff.

> **Nota:** este README documenta las funcionalidades y configuraciones indicadas por el proyecto. Cualquier comportamiento no descrito aquí debe verificarse directamente en el código fuente.

---

## ✨ Características Principales

- **Portal Institucional:** presentación de la identidad, historia y misión canónica de los Institutos Seculares en Argentina.
- **Directorio de Institutos Seculares:** catálogo detallado de institutos masculinos, femeninos, sacerdotales y laicales con información de fundación, carisma, miembros, presencia geográfica y vías de contacto.
- **Gestión de Novedades y Eventos:** publicación y administración de noticias con soporte para imágenes, fechas y horarios de eventos.
- **Panel de Autenticación y Administración:** control de acceso y operaciones CRUD restringidas para usuarios administradores mediante `@staff_member_required`.
- **Soporte PWA:** service worker integrado (`serviceworker.js`) y assets adaptados para dispositivos móviles.
- **Optimización de Estáticos:** WhiteNoise con compresión y manifest hashes para la entrega de archivos estáticos en producción.
- **Contenerización:** configuración mediante Docker y Docker Compose con MySQL 8.0.

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

## 📋 Requisitos

### Para Docker

- Docker
- Docker Compose

No es necesario instalar Python ni MySQL directamente en el host para utilizar el entorno Docker documentado por el proyecto.

### Para instalación local

- Python 3.12+
- MySQL Server 8.0+
- `pip`
- Entorno virtual recomendado
- Paquetes del sistema necesarios para compilar `mysqlclient`

En Linux/Debian pueden ser necesarios:

```bash
gcc
default-libmysqlclient-dev
pkg-config
```

---

## 📂 Estructura del Proyecto

```text
project_CISA/
├── core/                    # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py          # Ajustes generales, base de datos y seguridad
│   ├── urls.py              # Enrutador global del proyecto
│   └── wsgi.py
├── news/                    # Noticias, inicio y contacto
│   ├── forms.py             # Formularios de carga y edición de noticias
│   ├── models.py            # Modelo de noticias y eventos
│   ├── templates/news/      # Plantillas HTML
│   ├── urls.py              # Rutas de la aplicación news
│   └── views.py             # Lógica de vistas
├── institutos/              # Directorio y gestión de institutos seculares
│   ├── forms.py             # Formularios para creación/edición
│   ├── models.py            # Modelo Instituto y tipos de instituto
│   ├── templates/institutos/ # Plantillas del catálogo y CRUD
│   ├── urls.py              # Rutas de institutos
│   └── views.py             # Vistas de catálogo y administración
├── users/                   # Autenticación y sesiones
│   ├── templates/users/     # Plantillas de autenticación
│   ├── urls.py              # Rutas de login/logout
│   └── views.py             # Vistas de autenticación
├── static/                  # Archivos estáticos fuente
├── staticfiles/             # Archivos estáticos compilados
├── templates/               # Plantillas globales
│   └── layouts/
│       ├── base.html
│       ├── logo_svg.html
│       └── serviceworker.js
├── media/                   # Archivos multimedia cargados por usuarios
├── docker-compose.yml       # Orquestación de Django + MySQL
├── Dockerfile               # Imagen Docker de la aplicación
├── requirements.txt         # Dependencias Python
├── .env.example             # Plantilla de variables de entorno
├── .gitignore
└── manage.py                # Utilitario de gestión de Django
```

---

## 🗄 Modelos de Datos

### 1. `news` — App `news`

Almacena publicaciones, noticias institucionales y convocatorias:

- `titulo`: título de la publicación (`max_length=50`).
- `resumen`: síntesis o copete.
- `cuerpo`: contenido completo.
- `fecha`: fecha y hora de creación automática (`auto_now_add=True`).
- `imagen`: imagen de cabecera (`upload_to='noticias/'`).
- `ubicacion`: lugar del evento, opcional.
- `fecha_evento`: fecha programada del evento, opcional.
- `hora_evento`: hora programada del evento, opcional.

### 2. `Instituto` — App `institutos`

Representa cada instituto secular registrado:

- **Identificación:** `nombre`, `sigla`, `logo`, `tipo_instituto`.
- **Identidad y Carisma:** `breve_descripcion`, `historia`, `carisma`.
- **Fundación:** `anio_fundacion`, `fundador`, `foto_fundador`, `pais_origen`.
- **Gobierno y Miembros:** `responsable`, `consejo_gobierno`, `numero_miembros`, `paises_presencia`.
- **Presencia en Argentina:** `anio_llegada_argentina`, `provincias_diocesis`, `casas_comunidades`, `tipo_presencia`.
- **Canales de Contacto:** `direccion`, `telefono`, `email`, `website`, `redes_sociales`.

---

## 🚀 Instalación y Puesta en Marcha

### Opción 1: Docker & Docker Compose (Recomendado)

Es la opción recomendada para levantar el entorno sin instalar MySQL ni Python directamente en el host.

#### 1. Clonar el repositorio

```bash
git clone https://github.com/rjsoloaga/CISA.git
cd CISA
```

#### 2. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto.

Utilizar `.env.example` como referencia y **no subir el archivo `.env` al repositorio**.

#### 3. Construir e iniciar los contenedores

```bash
docker-compose up -d --build
```

El servicio `web`, según la configuración documentada, realiza el siguiente flujo:

1. Espera a que MySQL esté disponible.
2. Ejecuta las migraciones mediante `python manage.py migrate`.
3. Crea el superusuario inicial si todavía no existe.
4. Inicia la aplicación en `http://localhost:8000`.

#### 4. Verificar los contenedores

```bash
docker-compose ps
```

Ver logs:

```bash
docker-compose logs -f web
```

Ver logs de MySQL:

```bash
docker-compose logs -f db
```

#### 5. Acceder a la aplicación

- **Sitio web:** `http://localhost:8000`
- **Panel administrativo:** `http://localhost:8000/admin/`
- **Login de gestión:** `http://localhost:8000/login/`

### Detener el entorno

```bash
docker-compose down
```

Para detener y eliminar también los volúmenes del entorno:

```bash
docker-compose down -v
```

> ⚠️ `docker-compose down -v` elimina los volúmenes asociados y puede provocar pérdida de datos locales de MySQL. Utilizarlo solamente cuando corresponda.

---

### Opción 2: Instalación Local Tradicional

#### 1. Crear entorno virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

#### 3. Crear la base de datos MySQL

Ejemplo:

```sql
CREATE DATABASE cisa_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Crear un usuario dedicado para la aplicación:

```sql
CREATE USER 'cisa_user'@'localhost'
IDENTIFIED BY 'TU_PASSWORD_SEGURA';

GRANT ALL PRIVILEGES ON cisa_db.*
TO 'cisa_user'@'localhost';

FLUSH PRIVILEGES;
```

> 🔐 Nunca colocar contraseñas reales en este README, en el repositorio ni en archivos versionados.

#### 4. Configurar variables de entorno

**Windows PowerShell:**

```powershell
$env:DJANGO_DEBUG="True"
$env:DB_HOST="127.0.0.1"
$env:DB_PORT="3306"
$env:DB_NAME="cisa_db"
$env:DB_USER="cisa_user"
$env:DB_PASSWORD="TU_PASSWORD"
```

**Linux / macOS:**

```bash
export DJANGO_DEBUG=True
export DB_HOST=127.0.0.1
export DB_PORT=3306
export DB_NAME=cisa_db
export DB_USER=cisa_user
export DB_PASSWORD=TU_PASSWORD
```

#### 5. Ejecutar migraciones

```bash
python manage.py migrate
```

#### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

#### 7. Iniciar el servidor

```bash
python manage.py runserver
```

---

## 🔐 Variables de Entorno

| Variable | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `DJANGO_DEBUG` | Activa/desactiva el modo debug | `False` |
| `SECRET_KEY` | Clave criptográfica de Django | `clave-segura` |
| `DB_NAME` | Nombre de la base MySQL | `cisa_db` |
| `DB_USER` | Usuario MySQL | `cisa_user` |
| `DB_PASSWORD` | Contraseña MySQL | `********` |
| `DB_HOST` | Host MySQL (`db` en Docker) | `db` |
| `DB_PORT` | Puerto MySQL | `3306` |

### `.env.example`

Se recomienda mantener un archivo de referencia:

```env
DJANGO_DEBUG=False
SECRET_KEY=change-this-secret-key
DB_NAME=cisa_db
DB_USER=cisa_user
DB_PASSWORD=change-this-password
DB_HOST=db
DB_PORT=3306
```

El archivo `.env` real debe permanecer fuera del control de versiones.

---

## 👥 Usuarios y Permisos

El proyecto utiliza el sistema de autenticación y autorización de Django.

Las operaciones de gestión descritas utilizan `@staff_member_required`.

| Rol | Sitio público | Gestión | `/admin/` |
| :--- | :---: | :---: | :---: |
| Visitante | ✅ | ❌ | ❌ |
| Staff | ✅ | ✅* | Según permisos |
| Superusuario | ✅ | ✅ | ✅ |

\* El acceso efectivo depende de las restricciones implementadas en las vistas y permisos de Django.

### Crear un superusuario

```bash
python manage.py createsuperuser
```

---

## 🗺 Rutas y Endpoints

### Públicas

| Ruta | Función |
| :--- | :--- |
| `/` | Portada principal |
| `/news/` | Listado de noticias y eventos |
| `/news/<int:pk>/` | Detalle de una noticia |
| `/cisa/` | Información institucional |
| `/contacto/` | Formulario y datos de contacto |
| `/documentos/` | Repositorio de documentos |
| `/institutos/` | Directorio de institutos |
| `/institutos/<int:pk>/` | Detalle de un instituto |

### Gestión y Administración

| Ruta | Función | Acceso |
| :--- | :--- | :--- |
| `/login/` | Inicio de sesión | Público |
| `/login/logout/` | Cierre de sesión | Autenticado |
| `/admin/` | Administración Django | Según permisos |
| `/noticias/crear/` | Crear noticia | Staff |
| `/noticias/<int:pk>/editar/` | Editar noticia | Staff |
| `/noticias/<int:pk>/eliminar/` | Eliminar noticia | Staff |
| `/institutos/crear/` | Crear instituto | Staff |
| `/institutos/<int:pk>/editar/` | Editar instituto | Staff |
| `/institutos/<int:pk>/eliminar/` | Eliminar instituto | Staff |

---

## 🖼 Archivos Estáticos y Media

El proyecto diferencia entre:

- `static/`: archivos estáticos fuente.
- `staticfiles/`: archivos procesados para producción.
- `media/`: imágenes y otros archivos multimedia cargados por la aplicación.

### Desarrollo

Django puede servir los archivos estáticos durante el desarrollo.

### Producción

Los archivos estáticos deben procesarse mediante:

```bash
python manage.py collectstatic
```

WhiteNoise se utiliza para servir los archivos estáticos procesados.

> ⚠️ La carpeta `media/` contiene datos generados por la aplicación y debe contar con almacenamiento persistente en producción.

---

## 🔧 Desarrollo y Mantenimiento

### Crear migraciones

Después de modificar modelos:

```bash
python manage.py makemigrations
```

### Aplicar migraciones

```bash
python manage.py migrate
```

### Verificar el proyecto

```bash
python manage.py check
```

### Abrir shell de Django

```bash
python manage.py shell
```

### Recolectar archivos estáticos

```bash
python manage.py collectstatic
```

### Actualizar dependencias

Antes de actualizar paquetes en producción, probar los cambios en un entorno separado.

```bash
pip install -r requirements.txt
```

Después de realizar cambios, verificar:

```bash
python manage.py check
python manage.py test
```

---

## 🧪 Tests

Ejecutar la suite de pruebas:

```bash
python manage.py test
```

En Docker:

```bash
docker-compose exec web python manage.py test
```

> Si el proyecto todavía no dispone de una cobertura de tests completa, se recomienda incorporar pruebas para modelos, formularios, autenticación, permisos y vistas CRUD antes de realizar cambios importantes en producción.

---

## 🐳 Docker

El proyecto utiliza Docker Compose para orquestar al menos los servicios de aplicación Django y base de datos MySQL.

### Servicios

```text
Docker Compose
│
├── web
│   └── Django
│
└── db
    └── MySQL 8.0
```

### Comandos principales

```bash
# Construir y arrancar
docker-compose up -d --build

# Ver estado
docker-compose ps

# Ver logs
docker-compose logs -f

# Detener
docker-compose down

# Entrar al contenedor web
docker-compose exec web bash

# Ejecutar comandos Django
docker-compose exec web python manage.py check
docker-compose exec web python manage.py migrate
```

> Los nombres exactos de servicios y comandos internos deben coincidir con `docker-compose.yml`.

---

## 🛡 Despliegue y Producción

El proyecto incluye configuraciones orientadas a entornos productivos:

### WhiteNoise

Se utiliza `CompressedManifestStaticFilesStorage` para procesar y servir archivos estáticos con compresión y manifest.

### Proxy inverso y SSL

La configuración contempla:

```python
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
```

para operar detrás de proxies inversos o túneles de Cloudflare.

También se contemplan dominios de confianza mediante `CSRF_TRUSTED_ORIGINS` y `ALLOWED_HOSTS`.

### Persistencia

En Docker:

- La base de datos persiste mediante el volumen `mysql_data`.
- `media/` debe mapearse a almacenamiento persistente en producción.

### Recomendaciones antes de producción

Verificar:

```text
[ ] DEBUG=False
[ ] SECRET_KEY segura y externa al repositorio
[ ] ALLOWED_HOSTS correctamente configurado
[ ] CSRF_TRUSTED_ORIGINS correctamente configurado
[ ] HTTPS habilitado
[ ] Base de datos con credenciales seguras
[ ] Backups funcionando
[ ] Media persistente
[ ] Staticfiles recolectados
[ ] Logs disponibles
[ ] Tests ejecutados
```

---

## 💾 Backups y Restauración

La estrategia de backup debe contemplar **base de datos y archivos multimedia**.

### Backup de MySQL

Ejemplo:

```bash
mysqldump -u cisa_user -p cisa_db > cisa_backup.sql
```

### Restauración

```bash
mysql -u cisa_user -p cisa_db < cisa_backup.sql
```

### Archivos multimedia

Realizar además una copia de la carpeta:

```text
media/
```

> El backup de la base de datos por sí solo no reemplaza el backup de los archivos multimedia.

Se recomienda establecer una política de backup acorde a la criticidad del servicio y verificar periódicamente que los respaldos puedan restaurarse.

---

## 🐛 Troubleshooting

### La aplicación no conecta con MySQL

Verificar:

```text
DB_HOST
DB_PORT
DB_NAME
DB_USER
DB_PASSWORD
```

y confirmar que MySQL esté ejecutándose.

### Docker no inicia correctamente

Consultar:

```bash
docker-compose ps
docker-compose logs
```

Para revisar específicamente Django:

```bash
docker-compose logs -f web
```

Para MySQL:

```bash
docker-compose logs -f db
```

### Faltan tablas

Ejecutar:

```bash
python manage.py migrate
```

En Docker:

```bash
docker-compose exec web python manage.py migrate
```

### Los archivos estáticos no aparecen

Ejecutar:

```bash
python manage.py collectstatic
```

y verificar la configuración de `STATIC_URL`, `STATIC_ROOT` y WhiteNoise.

### Las imágenes cargadas desaparecieron

Verificar que `media/` tenga almacenamiento persistente y que no se haya eliminado el volumen correspondiente.

---

## 🔒 Seguridad

### Credenciales

**Nunca almacenar en el repositorio:**

- Contraseñas reales.
- `SECRET_KEY` real.
- Credenciales de producción.
- Tokens o claves API.

Utilizar variables de entorno o un sistema seguro de gestión de secretos.

### Archivos sensibles

El `.gitignore` debería excluir, como mínimo, archivos de entorno y secretos que no deban versionarse.

### Producción

Antes de publicar el sistema:

```bash
python manage.py check --deploy
```

Corregir las advertencias de seguridad relevantes antes del despliegue.

---

## 🗺 Roadmap

Posibles mejoras futuras:

- [ ] Ampliar cobertura de tests.
- [ ] Incorporar monitoreo y alertas.
- [ ] Automatizar backups.
- [ ] Documentar completamente el procedimiento de deployment.
- [ ] Incorporar procedimiento de rollback.
- [ ] Mejorar documentación de API si se incorporan endpoints REST.
- [ ] Automatizar CI/CD.

---

## 🤝 Contribución

Para realizar cambios:

1. Crear una rama específica para la modificación.
2. Realizar los cambios.
3. Ejecutar verificaciones y tests.
4. Revisar migraciones.
5. Verificar Docker si el cambio afecta al entorno de despliegue.
6. Crear un Pull Request describiendo los cambios.

Ejemplo:

```bash
git checkout -b feature/nueva-funcionalidad
git add .
git commit -m "feat: agrega nueva funcionalidad"
git push origin feature/nueva-funcionalidad
```

---

## 📄 Licencia

La licencia debe definirse explícitamente para el proyecto.

> **Pendiente de confirmar:** este README no permite determinar qué licencia legal utiliza actualmente el repositorio. Agregar aquí la licencia correspondiente una vez definida.

---

## 👨‍💻 Autor y Contacto

**Proyecto:** CISA — Conferencia de Institutos Seculares de Argentina

**Repositorio:**  
https://github.com/rjsoloaga/CISA

Para soporte o mantenimiento, utilizar los canales definidos por el equipo responsable del proyecto.

---

## 📚 Resumen de comandos

| Acción | Comando |
| :--- | :--- |
| Crear entorno virtual | `python -m venv venv` |
| Activar Windows | `venv\Scripts\activate` |
| Instalar dependencias | `pip install -r requirements.txt` |
| Verificar proyecto | `python manage.py check` |
| Crear migraciones | `python manage.py makemigrations` |
| Aplicar migraciones | `python manage.py migrate` |
| Crear superusuario | `python manage.py createsuperuser` |
| Ejecutar tests | `python manage.py test` |
| Recolectar estáticos | `python manage.py collectstatic` |
| Ejecutar servidor | `python manage.py runserver` |
| Docker build/up | `docker-compose up -d --build` |
| Docker logs | `docker-compose logs -f` |
| Docker stop | `docker-compose down` |

---
