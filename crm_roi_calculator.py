from flask import Flask, render_template_string, request

app = Flask(__name__)

html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Teeshirt Delivery Form</title>
    <script>
        window.onload = function() {
            if (localStorage.getItem("contactDetails")) {
                document.getElementById("contact").value = localStorage.getItem("contactDetails");
                document.getElementById("remember").checked = true;
            }
        };

        function saveDetails() {
            const contact = document.getElementById("contact").value;
            const remember = document.getElementById("remember").checked;
            if (remember) {
                localStorage.setItem("contactDetails", contact);
            } else {
                localStorage.removeItem("contactDetails");
            }
        }
    </script>
</head>
<body>
    <h2>Teeshirt Delivery Request</h2>
    <form method="POST" action="/" onsubmit="saveDetails()">
        <label for="size">Select Teeshirt Size:</label>
        <select name="size" id="size" required>
            <option value="">--Select--</option>
            <option value="Small">Small</option>
            <option value="Medium">Medium</option>
            <option value="Large">Large</option>
            <option value="XL">XL</option>
            <option value="XXL">XXL</option>
        </select>
        <br><br>
        <label for="contact">Contact Details and Address:</label><br>
        <textarea id="contact" name="contact" rows="4" cols="50" required></textarea>
        <br><br>
        <input type="checkbox" id="remember"> Remember my details
        <br><br>
        <input type="submit" value="Submit">
    </form>
    {% if submitted %}
        <h3>Thank you! Your request has been received.</h3>
        <p><strong>Size:</strong> {{ size }}</p>
        <p><strong>Contact Details:</strong> {{ contact }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        size = request.form.get("size")
        contact = request.form.get("contact")
        return render_template_string(html_template, submitted=True, size=size, contact=contact)
    return render_template_string(html_template, submitted=False)

if __name__ == "__main__":
    app.run(debug=True)
