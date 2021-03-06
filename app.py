from flask import Flask, render_template, json, request,redirect,session
from werkzeug import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'

conn = sqlite3.connect('setup/database.db')
cursor = conn.cursor()


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp(emailInUse=""):
    conn = sqlite3.connect("setup/database.db")
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute("select * from district")

    rows = cursor.fetchall();
    return render_template("signup.html",rows = rows,emailInUse=emailInUse)
    #return render_template('signup.html')

@app.route('/showLogin')
def showLogin():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('login.html')

@app.route('/showAddNewAddress')
def showAddNewAddress():
    if session.get('user'):
        return render_template('addNewAddress.html')
    else:
        return render_template('login.html')

@app.route('/userHome')
def userHome():
    if session.get('user'):
        return render_template('userHome.html')
    else:
        return render_template('error.html',error = 'Unauthorized Access')


@app.route('/logout')
def logout():
    session.pop('user',None)
    return redirect('/')

@app.route('/showRestaurantLogin')
def showRestaurantLogin():
    return render_template('restaurant_login.html')


@app.route('/validateRestaurantLogin')
def validateRestaurantLogin():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        conn = sqlite3.connect('setup/database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM restaurant WHERE email = ?;",(_email,))
        data = cursor.fetchall()

        if len(data) > 0:
            if check_password_hash(str(data[0][2]),_password):
                session['user'] = data[0][0]
                return redirect('/restaurantHome')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')


    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()

@app.route('/validateLogin',methods=['POST'])
def validateLogin():
    try:
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        conn = sqlite3.connect('setup/database.db')
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM customer WHERE email = ?;",(_email,))
        data = cursor.fetchall()

        if len(data) > 0:
            if check_password_hash(str(data[0][2]),_password):
                session['user'] = data[0][0]
                return redirect('/userHome')
            else:
                return render_template('error.html',error = 'Wrong Email address or Password.')
        else:
            return render_template('error.html',error = 'Wrong Email address or Password.')


    except Exception as e:
        return render_template('error.html',error = str(e))
    finally:
        cursor.close()
        conn.close()

@app.route('/addNewAddress',methods=['POST','GET'])
def addNewAddress():
    try:
        print("here")
        _address_title = request.form['addressTitle']
        _phone_num = request.form['phoneNumber']
        _street_name = request.form['streetName']
        _street_num = request.form['streetNumber']

        # _city = request.form['city']
        # _district = request.form['district']
        _zipcode=request.form['zipcode']
        _address_description=request.form['addressDescription']

        print("here2")
        # validate the received values
        if _address_title and _phone_num and _street_name and _street_num and _zipcode and _address_description:
            conn = sqlite3.connect('setup/database.db')
            cursor = conn.cursor()
            print(1)
            cursor.execute("INSERT INTO customer_address (address_type,phone_number,street_name,street_number,city,zipcode,adress_desc,d_id) \
                        VALUES (?,?,?,?,'Ankara',?,?,2);",(_address_title,_phone_num,_street_name,_street_num,_zipcode,_address_description))
            print(2)
            conn.commit()
            print(3)
            return render_template("userHome.html")

        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        print("error "+ str(e))
        return json.dumps({'error':str(e)})

    finally:
        cursor.close()
        conn.close()

@app.route('/signUp',methods=['POST','GET'])
def signUp():
    try:
        print("a")
        _name = request.form['inputName']
        print("name")
        _surname = request.form['inputSurname']
        #_surname = "Bekend"
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']

        print("here")
        # validate the received values
        if _name and _email and _password:
            conn = sqlite3.connect('setup/database.db')
            cursor = conn.cursor()
            _hashed_password = generate_password_hash(_password)
            cursor.execute("SELECT * FROM customer WHERE email = ?;",(_email,))
            data=cursor.fetchall()
            if len(data) > 0:

                return showSignUp("Email is in use")  ####buraya return ekle
            else:
                print("else")
                cursor.execute("INSERT INTO customer (email,password,name,surname) \
                            VALUES (?,?,?,?);",(_email,_hashed_password,_name,_surname))
                conn.commit()
                return render_template("login.html",loggedIn="<p>You have successfully signed up. Time to login!</p>") #####burayı değiştir

        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    except Exception as e:
        print("error "+ str(e))
        return json.dumps({'error':str(e)})

    finally:
        print("finally")
        cursor.close()
        conn.close()



if __name__ == "__main__":
    app.run(port=5002)
