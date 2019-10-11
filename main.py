from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/signup", methods=['GET', 'POST'])
def index():
    return render_template('user-signup.html')

@app.route("/welcome", methods=['POST'])
def signed_in():
    username = request.form['username']
    errname = ""
    password = request.form['password']
    errpass = ""
    confirm_password = request.form['confirm_password']
    errconfirm = ""
    email = request.form['email']
    errmail = ""

    if len(username) < 3 or len(username) > 20:
        errname = "Please enter a username between 3 and 20 characters."
        username = ""
        return render_template('user-signup.html', errname=errname, email=email)
    elif " " in username:
        errname = "Usename may not contain any spaces."
        username = ""
        return render_template('user-signup.html', errname=errname, email=email)
    
    if len(password) < 3 or len(password) > 20:
        errpass = "Please enter a password beween 3 and 20 characters."
        password = ""
        confirm_password = ""
        return render_template('user-signup.html', errpass=errpass, username=username, email=email)
    elif " " in password:
        errpass = "Password may not contain any spaces."
        password = ""
        confirm_password = ""
        return render_template('user-signup.html', errpass=errpass, username=username, email=email)
    
    if password != confirm_password:
        errconfirm = "Passwords must match."
        password = ""
        confirm_password = ""
        return render_template('user-signup.html', errconfirm=errconfirm, username=username, email=email)

    if email:
        if '@' not in email or "." not in email:
            errmail = "Please enter a valid email."
            email = ""
            return render_template('user-signup.html', username=username, errmail=errmail)
        elif len(email) < 3 or len(email) > 20:
            errmail = "Email must be between 3 and 20 characters."
            email = ""
            return render_template('user-signup.html', username=username, errmail=errmail)
        elif " " in email:
            errmail = "Email may not contain spaces.."
            email = ""
            return render_template('user-signup.html', username=username, errmail=errmail)

    if len(secretquestion) < 3 or len(secretquestion) > 20:
        errsecret = "Please enter an answer at between 3 - 20 characters."
        secretquestion = ""
        return render_template('user-signup.html', errsecret=errsecret, secretquestion=secretquestion)

    return render_template('welcome.html', username=username)



app.run()