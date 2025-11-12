from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    color = None

    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"]) / 100  # convert cm → meters
            bmi = round(weight / (height ** 2), 2)

            if bmi < 18.5:
                category = "Underweight"
                color = "underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
                color = "normal"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
                color = "overweight"
            else:
                category = "Obese"
                color = "obese"

        except (ValueError, ZeroDivisionError):
            bmi = "Invalid input"
            category = ""
            color = "error"

    return render_template("index.html", bmi=bmi, category=category, color=color)

if __name__ == "__main__":
    app.run(debug=True)
