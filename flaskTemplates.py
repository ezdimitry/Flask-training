from flask import Flask, render_template, request, flash, session, redirect, url_for, abort

app = Flask(__name__)


app.config['SECRET_KEY'] = 'fdgszrgr485734578hsHEfjfbjze'


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


@app.errorhandler(404)
def pageNotFount(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu), 404


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f"Профиль пользователя: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "Dima" and request.form['psw'] == "123":
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    
    return render_template('login.html', title="Авторизация", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)

    