from flask import Flask, render_template, request
import json
from dream_analyzer import analyze_dream


app = Flask(__name__)

from flask import session 
@app.route("/", methods=["GET", "POST"])
def index():
    analysis = None
    if request.method == "POST":
        dream_text = request.form.get("dream_text")
        if dream_text:
            result = analyze_dream(dream_text)  # this returns a JSON string
            try:
                analysis = json.loads(result)   # parse string -> dict
            except json.JSONDecodeError:
                 analysis = {
                    "fluid_interpretation": result,
                    "tags": {},
                    "reflective_questions": []
                }
                
    return render_template("index.html", analysis=analysis)



if __name__ == "__main__":
    app.run(debug=True, port=5000)
    

