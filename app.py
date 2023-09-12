import sys
from flask import Flask
from loguru import logger
from sentry_sdk import capture_exception
import tracker_sentry_flask


config = {
    "handlers": [
        {"sink": sys.stdout, "format": "{time} - {message}"},
        # {"sink": "test_flask.log", "serialize": True}, # formato: {"text": "2023-09-12 16:58:09.493 | ERROR    | app:trigger_error:24 - Error al dividir por 0\n", ...
        {"sink": "test_flask.log", "serialize": False},  # formato: 2023-09-12 18:58:48.937 | ERROR    | app:trigger_error:25 - Error al dividir por 0
    ]
}

app = Flask(__name__)
logger.configure(**config)


@app.route('/debug-sentry')
def trigger_error():
    try:
        division_by_zero = 1 / 0
    except Exception as e:
        logger.error('Error al dividir por 0')
        capture_exception(e) 


if __name__ == "__main__":
    app.run(app, host="0.0.0.0", port=8052)