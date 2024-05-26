# Conformación del Hogar API

**Conformación del Hogar** es una aplicación web desarrollada para gestionar las personas que conforman un hogar. La aplicación permite agregar y visualizar información sobre los miembros del hogar.

### Características
- **Agregar Miembros: Permite añadir nuevas personas al hogar.
- **Listar Miembros: Visualización de todos los miembros del hogar en una lista clara y ordenada.

## Insignias

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## Tecnologías Utilizadas

- **Django**: Para el desarrollo del backend.
- **Django Rest Framework**: Para la creación de la API RESTful.
- **Base de datos Postgresql**: Almacenamiento de datos.

<p align="left">
  <img src="https://github.com/sebastiannarvaez23/event-anywhere/assets/88569352/d96abd89-7804-4fa5-816c-5ea41e8100ab" width="100" />
  <img src="https://user-images.githubusercontent.com/88569352/218375255-d9a28190-10e2-44ad-b13d-721292e46815.png" width="90">
  <img src="https://www.django-rest-framework.org/img/logo.png" width="180">
  <img src="https://user-images.githubusercontent.com/88569352/229976087-c6d3eba8-ef91-4ff4-8260-a8f38a88093e.png" width="auto" height="80">
  <img src="https://static-00.iconduck.com/assets.00/git-icon-1024x1024-pqp7u4hl.png" width="auto" height="90">
</p>

## Instalación

### Requisitos
- python >= 3.11

### Pasos
1. Instala las dependencias:
   ```bash
   $ pip install -r requiriments.txt
2. Crea la base de datos en tu motor de base de datos postgresql local:
   ```bash
   $ createdb chsprueba
3. Genera las migraciones de los modelos:
   ```bash
   $ python manage.py makemigrations
4. Aplica las migraciones en la base de datos:
   ```bash
   $ python manage.py migrate
5. Corre el servidor local:
   ```bash
   $ python manage.py runserver

## Apoyo

Para obtener ayuda, puedes utilizar las siguientes vías:

- [GitHub Issues](https://github.com/sebastiannarvaez23/conformation-home-api/issues)
- [Correo Electrónico](narvaezsebas8@gmail.com)

## Mapa vial

### Próximas Funcionalidades
- **Test Unitarios**: Implementación de pruebas unitarias.
- **Roles de Usuario**: Sistema de administración de roles.

## Contribuyendo

¡Contribuciones son bienvenidas! Para contribuir:

1. Realiza un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

### Configuración para Desarrollo

Para configurar el entorno de desarrollo:

1. Instala las dependencias del proyecto.
2. Configura las variables de entorno necesarias.
3. Ejecuta los scripts de inicio y prueba para asegurar la calidad del código.

## Autores y Reconocimientos

Desarrollado por [Sebastian Narvaez](https://github.com/sebastiannarvaez23).

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## Estado del proyecto

**Estado:** Activo. Estamos continuamente trabajando en mejoras y nuevas funcionalidades. Si deseas contribuir, no dudes en ponerte en contacto.
