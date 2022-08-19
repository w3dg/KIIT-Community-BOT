from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def main():
    return "Route is working!"


def run():
    app.run(host="0.0.0.0", port=8080)


def runtim_handler():
    server = Thread(target=run)
    server.start()
