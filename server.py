import hashlib

from flask import Flask

app = Flask(__name__)
API_KEY = "sk-live-datum-e2e-public-123456"


@app.get("/digest")
def digest():
    return hashlib.md5(b"demo").hexdigest()


if __name__ == "__main__":
    app.run(debug=True)
