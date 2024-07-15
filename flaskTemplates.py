from flask import Flask, render_template, request, flash

app = Flask(__name__)

menu = [{"name": "Установка", "url": "/install-flask"},
        {"name": "Первое приложение", "url": "/first-app"},
        {"name": "Обратная связь", "url": "/contact"}]


@app.route("/")
def index():
    return render_template('index.html', menu=menu)


@app.route("/about")
def about():
    return render_template('about.html', title='О сайте', menu=menu)


@app.route("/install-flask")
def install_flask():
    return render_template('install.html', title='Установка Flask', menu=menu)


@app.route("/first-app")
def first_app():
    return render_template('first_app.html', title='Первое приложение', menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено')
        else:
            flash('Ошибка отправки')
    return render_template('contact.html', title='Обратная связь', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)