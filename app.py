from flask import Flask, render_template
import datetime

app = Flask(__name__)

doomsday = datetime.datetime(2038, 1, 19, 3, 14, 7)
now = datetime.datetime.now()

clock = {
    "Year": (doomsday.year - now.year) - 1,
    "Month": ((doomsday.month - now.month) % 12),
    "Day": (doomsday.day - now.day),
    "Hour": ((doomsday.hour - now.hour) % 24),
    "Minute": ((doomsday.minute - now.minute) % 60),
    "Second": ((doomsday.second - now.second) % 60),
}

@app.route("/")
def home():
    return render_template("index.html", clock=clock)

if __name__ == "__main__":
    app.run(debug=True)