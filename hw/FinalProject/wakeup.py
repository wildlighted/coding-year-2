from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """<b>Доброе утро! Сейчас оживу.</b>"""

if __name__ == '__main__':
    import os
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)