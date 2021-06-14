from flask import Flask, redirect, url_for, render_template, request, session, jsonify
import mysql.connector

app = Flask(__name__)
app.secret_key = '1234'

from assignment10.assignment10 import assignment10_blueprint, interact_db

app.register_blueprint(assignment10_blueprint)


@app.route('/main', methods=['PUT', 'POST', 'GET', 'DELETE'])
@app.route('/', methods=['PUT', 'POST', 'GET', 'DELETE'])
def main():
    return render_template('cv.html')


@app.route('/contact%20list.html')
def contact():
    return render_template('contact list.html')


@app.route('/assignment8', methods=['PUT', 'POST', 'GET'])
def assignment8():
    assignment = 'assignment8'
    contact_user = {'firstname': 'Michael', 'lastname': 'Lawson'}
    hobbies = ['Scuba diving', 'football', 'movies']
    divingSites = ['Red sea', 'Mexico', 'Galapagos']
    movies = ['fight club', 'the godfather', 'the dark knight']
    footballClubs = ['FC Ashdod', 'FC Barcelona']
    return render_template('assignment8.html',
                           hobbies=hobbies,
                           divingSites=divingSites,
                           movies=movies,
                           footballClubs=footballClubs,
                           contact_user=contact_user,
                           assignment=assignment)


@app.route('/games')
def games():
    games = ['FIFA', 'billiard', 'Beer Pong']
    return render_template('games.html',
                           games=games)


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():
    assignment = 'assignment9'
    users = [{'firstname': 'Michael', 'lastname': 'Lawson', 'email': "Lawson@gmail.com"},
             {'firstname': 'Dana', 'lastname': 'Dvorin', 'email': "Dana@gmail.com"},
             {'firstname': 'Dani', 'lastname': 'Din', 'email': "Dani@gmail.com"}]
    current_method = request.method
    if 'username' in session:
        user_name, name, lastname, email = session['username'], '', '', ''
    if request.method == 'POST':
        if 'username' in request.form:
            user_name = request.form['username']
            session['username'] = request.form['username']
            password = request.form['password']
        else:
            user_name = ''
    else:
        user_name = ''
    if request.method == 'GET':
        if 'name' in request.args:
            name = request.args['name']
            lastname = request.args['lastname']
            email = request.args['email']
        else:
            name, lastname, email = '', '', ''
    else:
        name, lastname, email = '', '', ''
    return render_template('assignment9.html',
                           user_name=user_name,
                           name=name,
                           lastname=lastname,
                           email=email,
                           users=users,
                           assignment=assignment,
                           current_method=current_method)


@app.route('/logout')
def log_out():
    session['username'] = ''
    return redirect(url_for('assignment9'))


@app.route('/assignment11/users', methods=['GET'])
@app.route('/assignment11/users/', methods=['GET'])
def assignment11():
    query = "SELECT * FROM users";
    query_result = interact_db(query=query, query_type='fetch')
    response = {}
    if len(query_result) != 0:
        response = query_result
    response = jsonify(response)
    return response

@app.route('/assignment11/users/selected/', defaults={'id': -1})
@app.route('/assignment11/users/selected/<int:id>', methods=['GET'])
def assignment11_1(id):
    if id == -1:
        id =1;
    query = "SELECT * FROM users WHERE id='%s';" % id
    query_result = interact_db(query=query, query_type='fetch')
    response = {}
    if len(query_result) != 0:
        response = query_result[0]
    else:
        response = "-------user does not exist!-------"
    response = jsonify(response)
    return response


if __name__ == '__main__':
    app.run(debug=True)
