from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>DevOps in Training</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(120deg, #1f1c2c, #928dab);
                    color: white;
                    text-align: center;
                    padding: 50px;
                }

                .container {
                    background: rgba(0, 0, 0, 0.4);
                    padding: 30px;
                    border-radius: 15px;
                    max-width: 600px;
                    margin: auto;
                    box-shadow: 0 0 20px rgba(0,0,0,0.5);
                }

                h1 {
                    font-size: 2.5rem;
                    margin-bottom: 20px;
                    color: #00ffe7;
                }

                p {
                    font-size: 1.2rem;
                    line-height: 1.6;
                }

                .btn {
                    margin: 15px 10px;
                    padding: 12px 25px;
                    border: none;
                    border-radius: 8px;
                    font-size: 1rem;
                    cursor: pointer;
                    transition: 0.3s;
                }

                .btn-devops {
                    background-color: #007bff;
                    color: white;
                }

                .btn-security {
                    background-color: #28a745;
                    color: white;
                }

                .btn:hover {
                    transform: scale(1.05);
                    opacity: 0.9;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>#Wow I am Officially a DevOps in Training</h1>
                <p>
                    Here I'm just learning Development Operations basics<br>
                    as I am developing an interest in this field as well<br>
                    as becoming a Security Application Engineer.
                </p>
                <button class="btn btn-devops">Learn DevOps</button>
                <button class="btn btn-security">Explore Security</button>
            </div>
        </body>
        </html>
    """)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
