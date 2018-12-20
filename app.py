from flask import Flask, render_template, request, session, redirect, url_for, escape, flash, jsonify
from Forms import *
from DB import *
import pusher


app = Flask(__name__)
app.secret_key = 'something secretive' # secret key for session

pusher_client = pusher.Pusher(
  app_id='676025',
  key='5d81221ffcd304919c3e',
  secret='c7219da2871eed6020a2',
  cluster='us2',
  ssl=True
)
#home page that redirects user to login page if not currently logged in
@app.route('/')
def index():
    # create the database
    createDB()
    #if user is in session, they can use site
    if 'username' in session and session['username'] != 'Shredder':
        username_session = escape(session['username']).capitalize()
        return render_template('index.html', session_user_name=username_session)
    # if not, the user must log in
    return redirect(url_for('login'))
# login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    # create the database
    createDB()

    error = None
    if 'username' in session and session['username'] != 'Shredder':
        return redirect(url_for('index'))
    if request.method == 'POST':
        # get the user's login credentials from the fields in the login page
        username_form  = request.form['username']
        password_form  = request.form['password']
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        sqlUser = "SELECT COUNT(1) FROM CLIENTS WHERE userName = ?;"
        argUser = ([username_form])
        c.execute(sqlUser, argUser) # CHECKS IF USERNAME EXISTS
        if c.fetchone()[0]:
            sqlPass = "SELECT password FROM CLIENTS WHERE userName = ?;"
            argPass = ([username_form])
            c.execute(sqlPass, argPass) # Get password
            for row in c.fetchall():
                if password_form == row[0]: # if password in clients table matches the form, user is logged in...
                    session['username'] = request.form['username']
                    return redirect(url_for('index'))
                else:
                    error = "Invalid Credential" # otherwise, login denied
        elif 'username' in session and session['username'] == 'Shredder':
            return redirect(url_for('adminLogin'))
        else:
            error = "Invalid Credential"
    return render_template('login.html', error=error)

#logout link function
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))

# registration page for user
@app.route('/registration', methods=['POST', 'GET'])
def register():
    #create new registration form
    form = RegistrationForm()

    if request.method == 'POST':
        # store user inputs as variables for the clients table insert
        user = request.form['user']
        password = request.form['password']
        email = request.form['email']
        #call function to insert record and return insert status
        msg = registerUser(user, password, email)
        #present user feedback regarding user creation
        return render_template("result.html", msg=msg)
    elif request.method == 'GET':
        #send user to registration page with registration form
        return render_template('registration.html', form= form)


# admin page to view all clients
@app.route('/list')
def list():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session

        # call db method to return list of clients
        rows = displayClients()
        # display records in table on list page
        return render_template("list.html", rows=rows)
    else:
        return redirect(url_for('login'))
# admin home page
@app.route('/adminindex')
def adminIndex():
    if 'username' in session and session['username'] == 'Shredder':
        user = session['username']  # get username from session
        return render_template('adminindex.html')
    else:
        return redirect(url_for('login'))
# admin login page
@app.route('/adminlogin', methods=['GET', 'POST'])
def adminLogin():
    error = None
    if 'username' in session:
        return redirect(url_for('adminIndex'))
    if request.method == 'POST':
        # get the user's login credentials from the fields in the login page
        username_form = request.form['username']
        password_form = request.form['password']
        sqlite_file = 'Shredder.db'  # name of the sqlite database file
        # Connecting to the database
        conn = sqlite3.connect(sqlite_file)
        c = conn.cursor()

        sqlUser = "SELECT COUNT(1) FROM ADMIN WHERE userName = ?;"
        argUser = ([username_form])
        c.execute(sqlUser, argUser)  # CHECKS IF USERNAME EXISTS
        if c.fetchone()[0]:
            sqlPass = "SELECT password FROM ADMIN WHERE userName = ?;"
            argPass = ([username_form])
            c.execute(sqlPass, argPass)  # Get password
            for row in c.fetchall():
                if password_form == row[0]:  # if password in customers table matches the form, user is logged in...
                    session['username'] = request.form['username']
                    flash('You were successfully logged in')
                    return redirect(url_for('adminIndex'))
                else:
                    error = "Invalid Credentials"  # otherwise, login denied
        else:
            error = "Invalid Credential"
    return render_template('adminlogin.html', error=error)

# client page to view leg progress
@app.route('/viewlegprogress')
def viewlegprogress():
    if 'username' in session and session['username'] != 'Shredder':

        user = session['username']  # get username from session
        cid = getCID(user)  # function uses username to retrieve cid of the user
        rows = viewLegProgress(cid)
        return render_template("viewlegprogress.html", rows=rows)
    elif 'username' in session and session['username'] == 'Shredder':
        return redirect(url_for('adminLogin'))
    else:
        return redirect(url_for('login'))

# client page to view core progress
@app.route('/viewcoreprogress')
def viewcoreprogress():
    if 'username' in session and session['username'] != 'Shredder':

        user = session['username']  # get username from session
        cid = getCID(user)  # function uses username to retrieve cid of the user
        rows = viewCoreProgress(cid)
        return render_template("viewcoreprogress.html", rows=rows)
    elif 'username' in session and session['username'] == 'Shredder':
        return redirect(url_for('adminLogin'))
    else:
        return redirect(url_for('login'))

# client page to view arm progress
@app.route('/viewarmsprogress')
def viewarmprogress():
    if 'username' in session and session['username'] != 'Shredder':

        user = session['username']  # get username from session
        cid = getCID(user)  # function uses username to retrieve cid of the user
        rows = viewArmsProgress(cid)
        return render_template("viewarmsprogress.html", rows=rows)
    elif 'username' in session and session['username'] == 'Shredder':
        return redirect(url_for('adminLogin'))
    else:
        return redirect(url_for('login'))

# client page to chest/back leg progress
@app.route('/viewchestbackprogress')
def viewchestbackprogress():
    if 'username' in session and session['username'] != 'Shredder':

        user = session['username']  # get username from session
        cid = getCID(user)  # function uses username to retrieve cid of the user
        rows = viewChestBackProgress(cid)
        return render_template("viewchestbackprogress.html", rows=rows)
    elif 'username' in session and session['username'] == 'Shredder':
        return redirect(url_for('adminLogin'))
    else:
        return redirect(url_for('login'))
# admin page to view chest/back day
@app.route('/viewchestback')
def viewchestback():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session

        rows =displayChestBack()
        return render_template("viewchestback.html", rows=rows)
    elif 'username' in session and session['username'] == 'Shredder':
        return redirect(url_for('adminLogin'))
    else:
        return redirect(url_for('login'))
# admin page to view arms day
@app.route('/viewarms')
def viewarms():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session

        rows =displayArms()
        return render_template("viewarms.html", rows=rows)
    else:
        return redirect(url_for('login'))

# admin page to view core day
@app.route('/viewcore')
def viewcore():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session

        rows =displayCore()
        return render_template("viewcore.html", rows=rows)
    else:
        return redirect(url_for('login'))
# admin page to leg day
@app.route('/viewleg')
def viewleg():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session

        rows =displayLeg()
        return render_template("viewleg.html", rows=rows)
    else:
        return redirect(url_for('login'))

# admin page to updatechestback
@app.route('/updatechestback', methods=['POST', 'GET'])
def updatechestback():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session

        # call the progression form
        form = ProgressionForm()

        if request.method == 'POST':
            # get the progression from user input
            cid = request.form['cid']
            pVal = request.form['pVal']
            # db method to update the chestback table
            msg = updateChestBack(cid,pVal)
            return render_template('adminsuccess.html', msg=msg)
        elif request.method == 'GET':
            return render_template('updatechestback.html', form=form)
    else:
        return redirect(url_for('login'))

@app.route('/updatearms', methods=['POST', 'GET'])
def updatearms():
    if 'username' in session and session['username'] == 'Shredder':

        # call the progression form
        form = ProgressionForm()

        if request.method == 'POST':
            # get the progression from user input
            cid = request.form['cid']
            pVal = request.form['pVal']
            # db method to update the arms table
            msg = updateArms(cid,pVal)
            return render_template('adminsuccess.html', msg=msg)
        elif request.method == 'GET':
            return render_template('updatearms.html', form=form)
    else:
        return redirect(url_for('login'))

@app.route('/updatecore', methods=['POST', 'GET'])
def updatecore():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session

        # call the progression form
        form = ProgressionForm()

        if request.method == 'POST':
            # get the progression from user input
            cid = request.form['cid']
            pVal = request.form['pVal']
            # db method to update the core table
            msg = updateCore(cid,pVal)
            return render_template('adminsuccess.html', msg=msg)
        elif request.method == 'GET':
            return render_template('updatecore.html', form=form)
    else:
        return redirect(url_for('login'))

@app.route('/updateleg', methods=['POST', 'GET'])
def updateleg():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session

        # call the progression form
        form = ProgressionForm()

        if request.method == 'POST':
            # get the progression from user input
            cid = request.form['cid']
            pVal = request.form['pVal']
            # db method to update the leg table
            msg = updateLeg(cid,pVal)
            return render_template('adminsuccess.html', msg=msg)
        elif request.method == 'GET':
            return render_template('updateleg.html', form=form)
    else:
        return redirect(url_for('login'))

# admin page to delete a client
@app.route('/deleteclient', methods=['POST', 'GET'])
def deleteclient():
    if 'username' in session and session['username'] == 'Shredder':
        user = session['username']  # get username from session

        # display all customers
        rows = displayClients()
        form = DeleteCustomerForm()

        if request.method == 'POST':
            # get customer id from delete customer form
            cid = request.form['cid']
            # call db method to delete the customer
            msg = deleteClient(cid)
            return render_template('adminsuccess.html', msg=msg)
        elif request.method == 'GET':
            return render_template('deleteclient.html', form=form, rows = rows)
    else:
        return redirect(url_for('login'))
# admin page to search for one customer
@app.route('/searchcustomer', methods=['POST', 'GET'])
def searchcustomer():
    if 'username' in session and session['username'] == 'Shredder':

        user = session['username']  # get username from session
        # create the search customer form
        form = SearchCustomerForm()

        if request.method == 'POST':
            # get the customer id from user input in the form
            cid = request.form['cid']
            # call db method to search for customer via cid
            rows = searchCustomer(cid)
            return render_template('list.html', rows= rows)
        elif request.method == 'GET':
            return render_template('searchcustomer.html', form=form)
    else:
        return redirect(url_for('login'))

@app.route('/setstart', methods=['POST', 'GET'])
def setstart():
    if 'username' in session and session['username']== 'Shredder':

        user = session['username']  # get username from session
        #create new Starting weight form
        form = StartForm()

        if request.method == 'POST':
            # store user inputs as variables for the table inserts
            cid = request.form['cid']
            bench = request.form['bench']
            seatedDip = request.form['seatedDip']
            unilateralRow = request.form['unilateralRow']
            frontPulldown = request.form['frontPulldown']
            latPulldown = request.form['latPulldown']
            curl = request.form['curl']
            seatedHammer = request.form['seatedHammer']
            lateralRaise = request.form['lateralRaise']
            tricepExtension = request.form['tricepExtension']
            shoulderRaise = request.form['shoulderRaise']
            rearFly = request.form['rearFly']
            obliqueActivation = request.form['obliqueActivation']
            lowerBackActivation = request.form['lowerBackActivation']
            abActivation = request.form['abActivation']
            medicineBall = request.form['medicineBall']
            lowerBackPlank = request.form['lowerBackPlank']
            sideSpin = request.form['sideSpin']
            lunges = request.form['lunges']
            horizontalCalf = request.form['horizontalCalf']
            mtsLegExtension = request.form['mtsLegExtension']
            legCurl = request.form['legCurl']
            hipAbduction = request.form['hipAbduction']
            legPress = request.form['legPress']
            #call function to insert record and return insert status
            chestBackmsg = setStartingChestBackWeight(cid, bench, seatedDip, unilateralRow, frontPulldown, latPulldown, rearFly)
            armMsg = setStartingArmWeight(cid, curl, seatedHammer, lateralRaise, tricepExtension, shoulderRaise)
            coreMsg = setStartingCoreWeight(cid, obliqueActivation, lowerBackActivation, abActivation, medicineBall,lowerBackPlank, sideSpin)
            legMsg = setStartingLegWeight(cid, lunges, horizontalCalf, mtsLegExtension,legCurl, hipAbduction, legPress)
            #present user feedback regarding user creation
            return render_template("result.html", msg=(chestBackmsg + '\n' + armMsg + '\n' +coreMsg + '\n' +legMsg))
        elif request.method == 'GET':
            #send admin to admin page with starting weight form
            return render_template('setstart.html', form= form)
    else:
        return redirect(url_for('login'))

# resources page
@app.route('/resources')
def resources():
    #if user is in session, they can use site
    if 'username' in session and session['username'] != 'Shredder':
        username_session = escape(session['username']).capitalize()
        return render_template('resources.html', session_user_name=username_session)
    # if not, the user must log in
    elif 'username' in session and session['username'] == 'Shredder':
        return redirect(url_for('adminLogin'))
    else:
        return redirect(url_for('login'))
# chat page
@app.route('/chat')

def chat():
    if 'username' in session:
        return render_template('chat.html')
    elif 'username' not in session:
        return redirect(url_for('login'))

@app.route('/message', methods=['POST'])
def message():
    try:

        username = session['username']
        message = request.form.get('message')

        pusher_client.trigger('chat-channel', 'new-message', {'username': username, 'message': message})

        return jsonify({'result': 'success'})

    except:

        return jsonify({'result': 'failure'})




# run the application
if __name__ == '__main__':
    app.run(debug= True)
