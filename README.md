# Chistes
Es un pequeño proyecto de muestra realizado con Django y Django REST Framework.

---
## Puesta en funcionamiento
Tras clonar el repositorio hay una serie de comandos a ejecutar para su funcionamiento (con django runserver).

- `$ make docker-build-dev` crea la imagen de Docker
- `$ make docker-start` inicia el contenedor y expone el servicio

Para correr los test hay que ejecutar:
- `$ make docker-test`

## EndPoints
### Swagger
- Documetación: `http://localhost:8000/swagger/`

### Apartado de chistes
-COMPLETAR-

### Apartado matemático
- Mínimo común múltiplo: `http://localhost:8000/api/v1/maths/?numbers=2,4,10`
- N+1: `http://localhost:8000/api/v1/maths/?number=2`

## Detalles constructivos

Realicé tests de los endpoint pytest parametrizados.
Por cuestiones de tiempo realicé la validación dentro de las views en lugar de usar Sarializers de DRF.
