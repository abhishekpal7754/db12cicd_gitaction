from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Abhishek Pal</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 100px;">
        <h1>Welcome to Abhishek Pal's Website</h1>
        <h2>DevOps Engineer0</h2>
        <p>Python | AWS | Docker | Kubernetes | Jenkins</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
