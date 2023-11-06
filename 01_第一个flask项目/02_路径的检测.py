from flask import Flask, render_template

app = Flask(__name__, template_folder='aaaa1')


@app.route('/123')
def home():
    return render_template('yigexiaoceshi.html')


if __name__ == '__main__':


    app.run()
