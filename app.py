from flask import Flask, request, render_template_string

app = Flask(__name__)

html = """
<h2>Simple Calculator</h2>
<form method="post">
  Number 1: <input name="num1"><br>
  Number 2: <input name="num2"><br>
  Operation:
  <select name="operation">
    <option value="add">Add</option>
    <option value="sub">Subtract</option>
    <option value="mul">Multiply</option>
    <option value="div">Divide</option>
  </select><br><br>
  <input type="submit" value="Calculate">
</form>

{% if result %}
<h3>Result: {{ result }}</h3>
{% endif %}
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        op = request.form["operation"]

        if op == "add":
            result = num1 + num2
        elif op == "sub":
            result = num1 - num2
        elif op == "mul":
            result = num1 * num2
        elif op == "div":
            result = num1 / num2

    return render_template_string(html, result=result)

app.run(host="0.0.0.0", port=5000)