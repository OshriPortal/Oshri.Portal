from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/main', methods=['PUT', 'POST', 'GET'])
@app.route('/', methods=['PUT', 'POST', 'GET'])
def main():
    return render_template('cv.html')


@app.route('/contact%20list.html')
def contact():
    return render_template('contact list.html')


@app.route('/assignment8', methods=['PUT', 'POST', 'GET'])
def assignment8():
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
                           contact_user=contact_user)


@app.route('/games', methods=['PUT', 'POST', 'GET'])
def games():
    games = ['FIFA', 'billiard', 'Beer Pong']
    return render_template('games.html',
                           games=games)


if __name__ == '__main__':
    app.run(debug=True)
