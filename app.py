from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Abhishek Pal | DevOps Engineer</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                text-align: center;
                padding: 50px;
            }
            .container {
                background: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                max-width: 900px;
                margin: auto;
            }
            h1 {
                color: #333;
            }
            h2 {
                color: #0077b6;
            }
            p {
                font-size: 18px;
                line-height: 1.6;
            }
            .skills {
                margin-top: 20px;
                font-weight: bold;
                color: #444;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Abhishek Pal's Portfolio</h1>
            <h2>DevOps Engineer IT</h2>

            <p>
                Hi, I'm <b>Abhishek Pal</b>, a passionate DevOps Engineer
                focused on automating software delivery, managing cloud
                infrastructure, and building scalable CI/CD pipelines.
            </p>

            <p>
                I work with Git, GitHub, Jenkins, Docker, Kubernetes,
                AWS, Linux, and GitHub Actions to create reliable,
                efficient, and cloud-native solutions.
            </p>

            <div class="skills">
                Skills: AWS | Docker | Kubernetes | Jenkins | GitHub Actions | Linux | Python
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

