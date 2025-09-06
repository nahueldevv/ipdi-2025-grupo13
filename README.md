# Proyectos de Procesamiento Digital de Imágenes

> [!IMPORTANT]
> Antes de ejecutar este proyecto, asegúrate de tener **Pipenv** instalado en tu computadora.  
> Puedes instalarlo con `pip install pipenv` si aún no lo tienes.

Este proyecto contiene ejercicios de procesamiento de imágenes, organizados en distintos trabajos prácticos (`tp00`, `tp01`). Cada TP se ejecuta mediante un script definido en el `Pipfile`.

## Requisitos

- Python 3.13
- Pipenv

## Instalación de dependencias

Clonar el repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```

Crear el entorno virtual e instalar dependencias:
```bash
pipenv install
```

Activar el entorno virtual (opcional, pero recomendado):
```bash
pipenv shell
```

## Ejecucion de los Programas

Los scripts están definidos en el Pipfile bajo [scripts].
Dependiendo del trabajo práctico que quieras ejecutar, usarás el nombre correspondiente:

Ejecuta el script tp00:
```bash
pipenv run tp00
```

Ejecuta el script tp01:
```bash
pipenv run tp01
```

> [!Note] 
> También puedes ejecutar directamente usando Python dentro del entorno virtual:
```bash
python -m tp01.main
```