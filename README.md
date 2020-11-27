# python101

### Requisitos:
-Python 3
-Docker

Este es un proyecto de ejemplo para Rockstars G5

###Instrucciones:

-Clonar este repo
-Crear imagen de docker:
```
dockerbuild =t "phyton101" .
```
-Correr imagen en modo developer (salir con [CTRL] + [C])
```
docker run -it -p 5000:5000 --rm --name "python101-volatil" python101
```
-Correr imagen en modo servicio
```
docker run -it -p 5000:5000 --d --name "python101-volatil" python101
```