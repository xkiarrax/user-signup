from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def sign_up():
    return render_template("user-signup.html")                     #this is the first page of the program, we are rendering the form from the templates that was written in html

@app.route("/register", methods=['POST'])                   # this second page is a registration page, using the "POST" method so info doesn't appear in URL
def register():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""                                         # here you're creating an empty string for the username error to make it a variable
    password_error = ""
    verify_error = ""
    email_error = ""



#THIS IS FOR THE USERNAME ERROR
    if not 20 >= len(username) >= 3 or " " in username:         # if the username is greater than 20 characters or less than three, or there is a space                
        username_error = "Please enter a valid username. Username should be between 3-20 characters and cannot contain any spaces or periods."       # it will produce an error message

#THIS IS FOR THE PASSWORD ERROR
    if not 20 >= len(password) >= 3 or " " in password:
        password_error = "Please enter a valid password. Password should be between 3-20 characters and cannot contain any spaces or periods."       

#THIS IS FOR VERIFYING THE PASSWORD
    if verify != password:                                  
        verify_error = "Password does not match."

#THIS IS FOR EMAIL
    if email != "":                                                                         #if the email field is not left blank...do the following
        if not 2 < len(email) < 20 or " " in email or not email.count("@") == 1 or not email.count(".") == 1:
            email_error = "Please enter a vaild email address. Email address should be between 3-20 characters and cannot contain any spaces. Must only have 1 '@' and 1 period."
    
    if not username_error and not password_error and not verify_error and not email_error:                      #if there is no error in the username send them to the correct page                                                                    
        return redirect("/welcome?username={0}".format(username))                               
    else:
        return render_template('user-signup.html', username=username, username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, email =email)   #otherwise, give the user the form with the username in tact



@app.route("/welcome")                                                                          #the page is being directed to the welcome page
def valid_signup():                                                                             # here we are requesting the program to retrieve the username that was entered
    username = request.args.get("username")
    return render_template("welcome.html", username=username)                                   # here we are rendering the template "welcome.html" and returning the page to the user

app.run()