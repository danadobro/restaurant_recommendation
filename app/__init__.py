from flask import Flask, render_template, redirect, flash, url_for, session, request
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm, SearchForm
import random

app = Flask(__name__)

# secret key for CSRF Protection
app.config['SECRET_KEY'] = '123abcdddooowfmne'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'restaurants'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        return redirect(
            url_for('recommendations', cuisine=form.cuisine.data, budget=form.budget.data, vibe=form.vibe.data))
    return render_template('home.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data)
        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO users (username, email, password_hash) VALUES (%s,%s,%s)",
                        (username, email, password))
            mysql.connection.commit()
            flash('Successfully created account')
            return redirect(url_for('home'))
        except Exception as e:
            flash('Error creating an account')
        finally:
            cur.close()
    return render_template('register.html', form=form)


@app.route('/account')
def account():
    if 'username' in session:  # check if user is logged in to display their profile page
        username = session['username']
        return render_template('account.html', username=username)
    else:
        return redirect(url_for('login'))  # if not logged in, redirect to log in


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM users WHERE username = %s", [username])
        user = cur.fetchone()
        cur.close()

        if user and check_password_hash(user['password_hash'], password):
            session['username'] = username
            return redirect(url_for('account'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    flash('You have been logged out.', 'success')
    return redirect(url_for('home'))  # Redirect to the home page


@app.route('/restaurants')
def test_db():
    cur = mysql.connection.cursor()
    cur.execute('SELECT VERSION()')
    rv = cur.fetchone()
    return f"MySQL version: {rv[0]}"


def get_restaurant_recommendations(cuisine, budget, vibe):
    cur = mysql.connection.cursor()
    query = "SELECT * FROM my_restaurant_data WHERE 1=1"
    params = []

    # Apply filters only if not "surprise"
    if cuisine != 'surprise':
        query += " AND cuisine = %s"
        params.append(cuisine)
    if budget != 'surprise':
        if budget == 'under_150':
            query += " AND budget < %s"
            params.append(150)
        elif budget == '150_250':
            query += " AND budget BETWEEN %s AND %s"
            params.extend([150, 250])
        elif budget == 'over_250':
            query += " AND budget > %s"
            params.append(250)
    if vibe != 'surprise':
        query += " AND vibe = %s"
        params.append(vibe)

    cur.execute(query, params)
    all_matching_restaurants = cur.fetchall()

    # Randomly select one restaurant if there are any matches
    if all_matching_restaurants:
        recommendation = random.choice(all_matching_restaurants)
        recommendations = [recommendation]  # Wrap it in a list
    else:
        recommendations = []  # No matches found

    cur.close()
    return recommendations


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm(request.form)
    if request.method == 'POST' and form.validate():
        recommendations = get_restaurant_recommendations(
            form.cuisine.data,
            form.budget.data,
            form.vibe.data
        )

        # Pass recommendations to the template
        return render_template('recommendations.html', recommendations=recommendations)

    return render_template('home.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
