from flask import render_template, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from yourapp import app, mysql  # Import your Flask app and mysql instance
from forms import RegistrationForm  # Import the form you defined

# The functions for application routes


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password_hash = generate_password_hash(form.password.data)

        cur = mysql.connection.cursor()
        try:
            cur.execute("INSERT INTO users (username, email, password_hash) VALUES (%s, %s, %s)", (username, email, password_hash))
            mysql.connection.commit()
            flash('Account created successfully! Please log in.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            flash(f'Error creating account: {e}', 'danger')
        finally:
            cur.close()

    return render_template('register.templates', title='Register', form=form)