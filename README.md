# chinook

Para correr ejecutar:

export FLASK_APP=flask_app.py;flask run

Registro de horas:

[planilla](https://docs.google.com/spreadsheets/d/18PCmaGaa5jwOVpQroU0FV6IK6_393f36VlKLHTYOjwY/edit#gid=0)


# Features
* Alta, baja, modificacion, detalle y listado de clientes
* Alta, baja, modificacion, detalle y listado de empleados

Dado un cliente se muestran sus favoritos:
* generos / artistas y albums

Dado un empleado se muestra:
* a quien reporta
* cuales son sus clientes

Autenticacion
* los clientes podran registrarse un usuario / contrasenia para realizar compras

Compra de canciones:
* los clientes que iniciaron sesion podran agregar canciones a su carrito
* al finalizar el carrito se muestra y guarda la factura en la base de datos

# API

GET /customers

GET /customer/:id

POST /customers

# Diagrama de tablas

https://www.sqlitetutorial.net/sqlite-sample-database/