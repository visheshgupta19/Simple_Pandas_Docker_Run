from flask import Flask, request, render_template_string
import pandas as pd
import io

app = Flask(__name__)


# Home route with file upload form
@app.route("/")
def home():
    return """
    <h1>Upload Your CSV File</h1>
    <form method="POST" action="/analyze" enctype="multipart/form-data">
        <label for="file">CSV File:</label>
        <input type="file" id="file" name="file" accept=".csv">
        <button type="submit">Upload & Analyze</button>
    </form>
    """


# Analyze uploaded CSV
@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return '<h1>No file uploaded!</h1><a href="/">Back</a>'

    file = request.files["file"]

    if file.filename == "":
        return '<h1>No file selected!</h1><a href="/">Back</a>'

    try:
        # Read CSV into pandas DataFrame
        df = pd.read_csv(file)

        # Basic numeric statistics
        summary = df.describe().to_html()

        return render_template_string(
            """
        <h1>Data Analysis Results</h1>
        {{ summary | safe }}
        <a href="/">Back</a>
        """,
            summary=summary,
        )

    except Exception as e:
        return f'<h1>Error processing file: {e}</h1><a href="/">Back</a>'


if __name__ == "__main__":
    app.run(debug=True)
