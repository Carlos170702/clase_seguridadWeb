## Instrucciones de Configuración

Sigue estos pasos para configurar tu entorno de desarrollo:

### 1. Crear el Entorno Virtual

Estando dentro del directorio de tu proyecto, ejecuta el siguiente comando para crear un entorno virtual:

py -m venv env

### 2. Activar el Entorno Virtual

Activa el entorno virtual. El comando para activar el entorno virtual varía según el sistema operativo:

.\env\Scripts\activate

### 3. Instalar Dependencias
Con el entorno virtual activado, instala todas las dependencias requeridas ejecutando:

pip install -r requirements.txt

### 4. Levantar el Servidor

Una vez que las dependencias estén instaladas, puedes levantar el servidor con el siguiente comando:

py manage.py runserver


