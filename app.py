from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/ping')
def main():
    return render_template(
        'ping.html',
        datestr = datetime.datetime.utcnow()
        )

# if __name__ == '__main__':
#     app.run(debug=True, port=23457)