# Chistes
Es un pequeño proyecto de muestra realizado con Django y Django REST Framework.

---
## Puesta en funcionamiento
Tras clonar el repositorio hay una serie de comandos a ejecutar para su funcionamiento (con django runserver).

- `$ make docker-build-dev` crea la imagen de Docker
- `$ make docker-start` inicia el contenedor y expone el servicio

Para correr los test hay que ejecutar:
- `$ make docker-test`

Ejecutar `$ make` para ver el resto de las opciones.

## EndPoints
### Swagger
- Documentación: `http://localhost:8000/swagger/`

### Apartado de chistes
- Chistes Random: `http://localhost:8000/api/v1/jokes/random/`
- Chistes de Chuck: `http://localhost:8000/api/v1/jokes/random/Chuck/`
- Chistes de Dad: `http://localhost:8000/api/v1/jokes/random/Dad/`

### Apartado matemático
- Mínimo común múltiplo: `http://localhost:8000/api/v1/maths/?numbers=2,4,10`
- N+1: `http://localhost:8000/api/v1/maths/?number=2`

## Detalles constructivos

El projecto está armado para ser ejecutado con Docker, tanto para probarlo como para continuar su desarollo (el Dockerfile.dev que adjunto no está pensado para producción). Por otro lado utilizo un esquema modular en el projecto Django propiamente dicho, con requerimientos en cascada según dónde se vaya a utilizar (producción, testing o desarrollo local).
