from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    height = ""
    weight = ""

    if request.method == "POST":
        try:
            height = request.form.get("height", "").strip()
            weight = request.form.get("weight", "").strip()

            if height and weight:
                height_m = float(height) / 100  # cm → meters
                bmi = round(float(weight) / (height_m ** 2), 2)

                if bmi < 18.5:
                    category = "underweight"
                elif 18.5 <= bmi < 24.9:
                    category = "normal"
                elif 25 <= bmi < 29.9:
                    category = "overweight"
                else:
                    category = "obese"
            else:
                category = "error"
        except:
            category = "error"

    return render_template("index.html", bmi=bmi, category=category, height=height, weight=weight)

if __name__ == "__main__":
    app.run(debug=True)
