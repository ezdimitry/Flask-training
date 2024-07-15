from flask import Flask, redirect, make_response, abort


app = Flask(__name__)


@app.route("/")
def index():
    return "<h1>Hello World!<h1>"


# Следующая страница по адресу http://127.0.0.1:5000/user/<name>, приветствует пользователя
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name


# Переадресация на внешний сайт
@app.route('/ur')
def adres():
    return redirect('http://www.example.com')


# Создание объекта ответа и установка cookie
@app.route('/respon')
def make_respon():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


# Обработка загрузки пользователя и возможной ошибки 404
@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, %s</h1>' % user['name']


# Вспомогательная функция для загрузки пользователя (демонстрационная реализация)
def load_user(user_id):
    # Пример пользователей
    users = {
        '1': {'name': 'Dima'},
        '2': {'name': 'Bob'},
        '3': {'name': 'Charlie'}
    }
    return users.get(user_id)


if __name__ == '__main__':
    app.run(debug=True)
