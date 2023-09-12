# Ejemplo de **SENTRY** con *Flask* y *Loguru*
[Sentry]('https://sentry.io/welcome/'). 

## Creación de *entorno virtual*

```bash
python3.8 -m venv venv
```
### Activación en Linux

```bash
source venv/bin/activate
```

## Instalación de dependencias

```bash
python -m pip install -r requirements.txt
```

## Instalación SENTRY 
Para usar con Flask, ejecución realizada desde *requirements.txt*

```bash
pip install --upgrade 'sentry-sdk[flask]'
```


## Ejecución de script
Ejecute en la línea de comandos

```bash
gunicorn app:app -b 0.0.0.0:8052
```

Esto permitirá levantar http://0.0.0.0:8052 asignado en app.py, una vez allí,
vaya a la dirección:

```html
http://0.0.0.0:8052/debug-sentry
```

Esto ejecutará la excepción del código y registrará en Sentry el issue.

