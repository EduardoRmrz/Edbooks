# Edbooks - Entrega final de Coder - PYTHON 31080
## Nombre: Ramirez Arenas, José Eduardo 

Instalacion del proyecto en pc 
Instalación de Django

`$ python3 -m pip install Django`

Para correr el proyecto

`$ python3 ./manage.py runserver

Para realizar las migraciones

`$ python3 manage.py makemigrations`

`$ python3 manage.py migrate`

Para crear superusuario

`$ python3 manage.py createsuperuser`

##### VISTAS
- **Pagina de inicio** -
Para acceder al sitio se dirige a la siguiente URL `"http://127.0.0.1:8000"`

![Inicio](https://user-images.githubusercontent.com/106790128/180829141-4c12917c-8af7-48aa-81e8-08572aeb4bd6.PNG)

- **Panel de Administrador** -
![panel admin](https://user-images.githubusercontent.com/106790128/180830218-da9aab84-10a6-487b-889d-6cf4cef1371d.PNG)

- **Pagina con contenido en tipo de lista** -
![libros](https://user-images.githubusercontent.com/106790128/180830420-12960a6f-ef2c-4509-8f52-3f16cf47ad49.PNG)

##### CRUD
Dentro de este proyecto se pueden crear usuarios que tienen permitido crear y editar libros y autores, ademas, pueden visualizar a detalle cada libro con su respectiva informacion, sin embargo, solo los usuarios staff pueden eliminar elementos de la base de datos 

Los usuarios pueden:
- Agregar, editar y eliminar su avatar en el apartado de editar perfil
- Crear, editar, visualizar los libros
- Crear, editar y eliminar autores

Los usuarios pueden:
- Agregar, editar y eliminar su avatar en el apartado de editar perfil
- Crear, editar, visualizar y eliminar los libros
- Crear, editar y eliminar autores
- Tienen acceso al panel de administrador 
- Pueden observar la pagina de BD de lectores 

##### UNIT TEST
Dentro de este archivo se pueden observar los casos de prueba para el sitio

