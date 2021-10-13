# redis-python
* Joham Sebastian Medina Corredor  [![Git-JohamSMC](https://img.shields.io/badge/GitHub-JohamSMC-red?style=plastic&logo=github&link=https://github.com/JohamSMC)](https://github.com/JohamSMC)
* Hernan Alirio Cadena Gonzalez  [![Git-HernanChain](https://img.shields.io/badge/GitHub-HernanChain-red?style=plastic&logo=github&link=https://github.com/hernanChain)](https://github.com/hernanChain)


![GitHub last commit](https://img.shields.io/github/last-commit/JohamSMC/redis-python)

### 1 paso:
> Se sugiere crear un entorno virtual, para lo cual se debe tener instalado ***python*** y el gestor de paquetes ***PIP***

### 2 paso:
> Crear entorno virtual con  **venv**

```
python -m venv env
```

### 3 paso:
> Activar  **venv**

```
source /env/bin/activate
```

### 4 paso:
> Nos ubicamos en la carpeta raiz del proyecto y verificamos que existe el archivo
***``requirements.txt``***

> y ejecutamos el comando:

```
pip install -r requirements.txt
```

> Con este comando se instalara todas las librerias necesarias para el proyecto.

### 5 paso:
> Despues procedemos a correr el proyecto ("Estando Ubicados en la raiz del proyecto") con el comando:

```
uvicorn main:app --reload
```
