from flask import Blueprint, render_template, request, redirect
import mysql

assignment10_blueprint = Blueprint(
    'assignment10',
    __name__,
    static_folder='static',
    static_url_path='/assignment10',
    template_folder='templates'
)


@assignment10_blueprint.route('/assignment10')
def users():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', users=query_result)


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         passwd='1993',
                                         database='users')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


@assignment10_blueprint.route('/insert_user', methods=['GET', 'POST'])
def insert_user():
    if request.method == 'GET' and request.args['email'] and request.args['password']:
        username = request.args['username']
        firstname = request.args['firstname']
        lastname = request.args['lastname']
        email = request.args['email']
        password = request.args['password']
        query = "INSERT INTO users(user_name,first_name, last_name, email, password) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
            username, firstname, lastname, email, password)
        interact_db(query=query, query_type='commit')
    return redirect('/assignment10')


@assignment10_blueprint.route('/delete_user', methods=['GET', 'POST'])
def delete_user():
    if request.args['password'] == '1234':
        id = request.args['id']
        query = "DELETE FROM users WHERE id='%s';" % id
        interact_db(query, query_type='commit')
    return redirect('/assignment10')


@assignment10_blueprint.route('/update_user', methods=['GET', 'POST'])
def update_user():
    id = request.args['id']
    username = request.args['username']
    firstname = request.args['firstname']
    lastname = request.args['lastname']
    email = request.args['email']
    password = request.args['password']
    query = "UPDATE users SET user_name = '%s', first_name = '%s',last_name = '%s',email = '%s',password = '%s' WHERE id='%s'; " % (
    username, firstname, lastname, email, password, id)
    interact_db(query=query, query_type='commit')
    return redirect('/assignment10')
