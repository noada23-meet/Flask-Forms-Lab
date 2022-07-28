from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "llo2ay"
password = "123"
facebook_friends=["yeal","ido","omri", "sagiv", "laika", "noa"]


@app.route('/', methods=['GET','POST'])  # '/' for the default page
def login():
	if request.method=='POST':
		username1= request.form["username"]
		password1= request.form["password"]
		if username1==username and password1==password:
 			return render_template ('home.html',facebook_friends=facebook_friends)
	else: 
  		return render_template('login.html')

@app.route('/facebook_friends/<string:name>', methods= ['GET','POST'])  # '/' for the default page
def friends(name):
	flag = False
	if name in facebook_friends:
		flag = True
	return render_template('friend_exists.html',facebook_friends=facebook_friends,N=name, flag = flag)



@app.route('/home')  # '/' for the default page
def home():
  return render_template('home.html')
  return redirect('friend_exists')


  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)