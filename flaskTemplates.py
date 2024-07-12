'''
Использование шаблонов, шаблонов с параметрами, extend
Функция url_for и url адреса
'''


from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ["Установка", "Загрузка", "Поддержка"]


@app.route("/")
def index():
    print(url_for('index'))
    return render_template("index.html", title="О сайте", menu=menu)


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template("about.html", menu=menu)


@app.route("/base")
def base():
    return render_template("base.html")


# использование extend через html файл
@app.route("/exp")
def exp():
    return render_template("exp.html")


@app.route("/profile/<path:username>")
def profile(username):
    return f"Пользователь: {username}"


if __name__ == '__main__':
    app.run(debug=True)
