import os
import hashlib

from flask import Flask

app = Flask(__name__)
API_KEY = os.environ.get("API_KEY", "")


@app.get("/digest")
def digest():
    return hashlib.sha256(b"demo").hexdigest()


if __name__ == "__main__":
    app.run(debug=False)
