from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = '1234'


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
    print(request.method)
    current_method = request.method
    if 'username' in session:
        user_name, name, lastname, email = session['username'], '', '', ''
    if request.method == 'GET':
        print('get')
        if 'name' in request.args:
            name = request.args['name']
            lastname = request.args['lastname']
            email = request.args['email']
        else:
            name, lastname, email = '', '', ''
    if request.method == 'GET':
        print('post')
        if 'username' in request.args:
            user_name = request.args['username']
            session['username'] = request.args['username']
            password = request.args['password']
            email = request.args['email']
        else:
            user_name, email = '', ''
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


if __name__ == '__main__':
    app.run(debug=True)
