# InflacionCanastaBasica

## Descripción del Proyecto

InflacionCanastaBasica es un proyecto desarrollado para la materia de
Herramientas de Productividad de la Escuela de Sistemas Informáticos de la
Facultad de Ingeniería y Arquitectura de la Universidad de El Salvador.

El objetivo principal de este proyecto es realizar un análisis detallado del
efecto de la inflación en los productos incluidos en la canasta básica en El
Salvador durante los últimos 5 años. A través de la recopilación y el análisis
de datos, se busca comprender cómo la inflación ha afectado los precios de los
productos esenciales en el país.

El proyecto utiliza el framework Django para la implementación de la aplicación
web, donde los usuarios podrán explorar los datos y visualizar información
relevante sobre la inflación y los precios de la canasta básica. Se espera que
esta herramienta proporcione insights valiosos y contribuya al estudio y la
comprensión de la economía y la situación socioeconómica del país.

## Requisitos Previos

- Python (versión 3.11.X o mayor) 🐍
- Pip (versión 22.3.X o mayor) 📦
- Git (versión 2.40.X o mayor) 🗄️

## Configuración del Entorno de Desarrollo

1. Clona el repositorio: 📥

```shell
git clone https://github.com/ado1203/ExAulaHDP115Grupo11.git
```

2. Crea y activa un entorno virtual: ⚙️

```shell
python -m venv venv
```

- En Windows:
  ```shell
  .\venv\Scripts\activate
  ```

- En macOS/Linux:
  ```shell
  source venv/bin/activate
  ```

3. Instala las dependencias del proyecto: ⚡

```shell
pip install -r requirements.txt
```

## Puesta en Marcha del Proyecto

1. Realiza las migraciones de la base de datos: 🗃️

```shell
python manage.py migrate
```

2. Inicia el servidor de desarrollo: 🚀

```shell
python manage.py runserver
```

3. Accede a la aplicación en tu navegador web: 🌐 http://localhost:8000

## Contribución

Si deseas contribuir al proyecto, sigue los siguientes pasos: 🤝

1. Crea una rama nueva desde la rama `develop`: 🌿

```shell
git checkout develop
git pull
git checkout -b feature/nombre_de_la_rama
```

2. Realiza los cambios y realiza commits con mensajes descriptivos: ✏️

```shell
git add .
git commit -m "Mensaje descriptivo"
```

3. Sincroniza tu rama con la rama `develop`: 🔄

```shell
git checkout develop
git pull
git merge nombre_de_la_rama
```

4. Soluciona cualquier conflicto de fusión (si los hay). 🛠️
5. Realiza un push de tus cambios a la rama remota: 📤

```shell
git push origin develop
```

<p align="center"><img src="https://raw.githubusercontent.com/catppuccin/catppuccin/main/assets/footers/gray0_ctp_on_line.svg?sanitize=true" /></p>
