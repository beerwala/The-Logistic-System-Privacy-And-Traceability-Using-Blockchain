from flask import Flask,request,flash,url_for,redirect,render_template,session
import pandas as pd
import mysql.connector
import random
from datetime import datetime
import smtplib
import hashlib
import binascii
import secrets
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
app=Flask(__name__)
app.config['SECRET_KEY'] = "Lakshmi"
mydb = mysql.connector.connect(host="localhost", user="root", passwd="",port=3307, database="research_on_logistics_information")
cursor = mydb.cursor()
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/reg")
def reg():
    return render_template("reg.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/regback',methods=['POST', 'GET'])
def regback():
    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        pwd = request.form['pwd']
        cpwd = request.form['cpwd']
        pno = request.form['pno']
        addr = request.form['addr']

        sql = "select * from sender"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("Email already exists", "danger")
            return render_template('reg.html', msg="email existed")
        if (pwd == cpwd):
            sql = "INSERT INTO sender (name,email,pwd,pno,addr) VALUES (%s,%s,%s,%s,%s)"
            val = (name, email, pwd, pno, addr)
            cursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered", "success")
            return render_template('reg.html')
        else:
            flash("Password and Confirm Password not same","primary")
        return render_template('reg.html')

    return render_template('reg.html')


@app.route("/login")
def login():
    return render_template("login.html")
@app.route('/logback',methods=['POST', 'GET'])
def logback():
    if request.method == "POST":

        email = request.form['email']
        password1 = request.form['pwd']

        sql = "select * from sender where email='%s' and pwd='%s' " % (email, password1)
        print('q')
        x = cursor.execute(sql)
        print(x)
        results = cursor.fetchall()
        print(results)
        global name
        name = results[0][1]
        print(name)
        session['name'] = results[0][1]
        session['email'] = email
        if len(results) > 0:
            flash("Welcome to website", "primary")
            return render_template('senderhome.html', msg=results[0][1])
        else:
            flash("Login failed", "warning")
            return render_template('login.html', msg="Login Failure!!!")

    return render_template('login.html')


@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route('/upback',methods=['POST','GET'])
def upback():
    print("gekjhiuth")
    if request.method=='POST':
        fname=request.form['fname']
        file=request.form['file']

        dd="text_files/"+file
        print(dd)
        f = open(dd, "r")
        data = f.read()
        keyPair = RSA.generate(3072)

        pubKey = keyPair.publickey()
        print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
        pubKeyPEM = pubKey.exportKey()
        pukey=pubKeyPEM.decode('ascii')
        print(pubKeyPEM.decode('ascii'))

        print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
        privKeyPEM = keyPair.exportKey()
        prkey=privKeyPEM.decode('ascii')
        print(privKeyPEM.decode('ascii'))
        f = open("text_files/plaintext.txt", "rb")
        f = f.read()
        # encryption
        # msg = 'A message for encryption'
        encryptor = PKCS1_OAEP.new(pubKey)
        encrypted = encryptor.encrypt(f)
        enc=binascii.hexlify(encrypted)
        print("Encrypted:", binascii.hexlify(encrypted))
        now = datetime.now()
        a = random.randint(500, 50000)
        email = session.get('email')
        name = session.get('name')

        datalen = int(len(data) / 2)
        print(datalen, len(data))
        g = 0
        a = ''
        b = ''
        c = ''
        for i in range(0, 2):
            if i == 0:
                a = data[g: datalen:1]
                # a=a.decode('utf-8')
                print(a)
                result = hashlib.sha1(a.encode())
                hash1 = result.hexdigest()

                print(hash1)
                print("===================================")
                # result = hashlib.sha1(a.encode())
                # hash1 = result.hexdigest()
                # print(hash1)
                print("++++++++++++++++++++++++++")
                # print(g)
                # print(len(data))
                # b = data[g: len(data):1]
                # print(c)

        print(g)
        print(len(data))
        c = data[datalen: len(data):1]
        # c = c.decode('utf-8')
        print(c)
        print("===================================")
        print("*****************************")
        result = hashlib.sha1(c.encode())
        hash2 = result.hexdigest()
        print(hash2)
        currentDay = datetime.now().strftime('%Y-%m-%d')
        t1 = datetime.now().strftime('%H:%M:%S')

        sql = "INSERT INTO uploaded_files (name,email,fname,file,hash1,hash2,date,time1) VALUES (%s,%s,%s,AES_ENCRYPT(%s,'lakshmi'),%s,%s,%s,%s)"
        val = (name,email,fname, data, hash1, hash2, currentDay, t1)
        cursor.execute(sql, val)
        mydb.commit()
        sql = "select * from uploaded_files where time1='%s' " % (t1)
        x = pd.read_sql_query(sql, mydb)
        print("^^^^^^^^^^^^^")
        print(type(x))
        print(x)
        # x = x.drop(['demail'], axis=1)
        x = x.drop(['name'], axis=1)
        x = x.drop(['email'], axis=1)
        x = x.drop(['file'], axis=1)
        flash("File stored in the cloud server", "success")
        return render_template("upback.html", col_name=x.columns.values, row_val=x.values.tolist())

    flash("File not uploaded please try again","danger")
    return render_template('upload.html')
@app.route('/vfile')
def vfile():
    email=session.get('email')

    sql ="select * from uploaded_files where email='%s'" %(email)
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['email'], axis=1)
    x = x.drop(['file'], axis=1)
    x = x.drop(['name'], axis=1)
    return render_template("vfile.html", cal_name=x.columns.values, row_val=x.values.tolist())

@app.route("/cs")
def cs():
    return render_template("cs.html")

@app.route('/csback',methods=['POST', 'GET'])
def csback():

    if request.method == 'POST':
        username = request.form['name']
        password1 = request.form['pwd']
        if username == 'cloud' and password1 == 'cloud' :
            flash("Welcome to website cloud", "primary")
            return render_template('cshome.html')
        else:

            flash("Invalid Credentials Please Try Again","warning")
            return render_template('cs.html')

    return render_template('cs.html')
@app.route("/vsender")
def vsender():
    sql = "select * from sender "
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['pwd'], axis=1)
    return render_template("vsender.html", cal_name=x.columns.values, row_val=x.values.tolist())

@app.route("/vreceiver")
def vreceiver():
    sql = "select * from receiver "
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['pwd'], axis=1)
    return render_template("vreceiver.html", cal_name=x.columns.values, row_val=x.values.tolist())
@app.route('/viewfiles')
def viewfiles():

    sql ="select * from uploaded_files "
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['file'], axis=1)
    x = x.drop(['hash1'], axis=1)
    x = x.drop(['hash2'], axis=1)
    return render_template("viewfiles.html", cal_name=x.columns.values, row_val=x.values.tolist())

@app.route("/signup")
def signup():
    return render_template("signup.html")

@app.route('/signupback',methods=['POST', 'GET'])
def signupback():
    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        pwd = request.form['pwd']
        cpwd = request.form['cpwd']
        pno = request.form['pno']
        addr = request.form['addr']

        sql = "select * from receiver"
        result = pd.read_sql_query(sql, mydb)
        email1 = result['email'].values
        print(email1)
        if email in email1:
            flash("Email already exists", "danger")
            return render_template('signup.html', msg="email existed")
        if (pwd == cpwd):
            sql = "INSERT INTO receiver (name,email,pwd,pno,addr) VALUES (%s,%s,%s,%s,%s)"
            val = (name, email, pwd, pno, addr)
            cursor.execute(sql, val)
            mydb.commit()
            flash("Successfully Registered", "success")
            return render_template('signup.html')
        else:
            flash("Password and Confirm Password not same","primary")
        return render_template('signup.html')

    return render_template('signup.html')

@app.route("/signin")
def signin():
    return render_template("signin.html")
@app.route('/signinback',methods=['POST', 'GET'])
def signinback():
    if request.method == "POST":

        email = request.form['email']
        password1 = request.form['pwd']

        sql = "select * from receiver where email='%s' and pwd='%s' " % (email, password1)
        print('q')
        x = cursor.execute(sql)
        print(x)
        results = cursor.fetchall()
        print(results)
        global name
        name = results[0][1]
        print(name)
        session['name'] = results[0][1]
        session['email'] = email
        if len(results) > 0:
            flash("Welcome to website", "primary")
            return render_template('receiverhome.html', msg=results[0][1])
        else:
            flash("Login failed", "warning")
            return render_template('signin.html', msg="Login Failure!!!")

    return render_template('signin.html')



@app.route("/search")
def search():
    return render_template("search.html")

@app.route('/searchback', methods=['POST','GET'])
def searchback():
    if request.method=='POST':
        fname=request.form['fname']
        sql = "select * from uploaded_files where fname LIke '%"+fname+"%'"
        x = pd.read_sql_query(sql, mydb)
        print("^^^^^^^^^^^^^")
        print(type(x))
        print(x)
        x = x.drop(['file'], axis=1)
        x = x.drop(['hash1'], axis=1)
        x = x.drop(['hash2'], axis=1)
        x = x.drop(['email'], axis=1)
        x = x.drop(['time1'], axis=1)

        # x["View Data"] = " "
        # x["Send Request"] = ""

        return render_template("searchback.html", col_name=x.columns.values, row_val=x.values.tolist())

@app.route('/req/<s>/<s1>/<s2>')
def req(s=0,s1='',s2=''):
    global fname,demail,sname,fid
    fname=s2
    name=s1
    fid=s


    email = session.get('email')
    sql = "insert into request_files(fid,name,fname,email) values(%s,%s,%s,%s)"
    val=(fid,name,fname,email)
    cursor.execute(sql,val)
    mydb.commit()
    flash("Request sended to the cloud server","sucess")
    return redirect(url_for('search'))

@app.route('/viewreq')
def viewreq():

    sql ="select * from request_files where status='Request' "
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['status'], axis=1)
    x = x.drop(['pkey'], axis=1)
    return render_template("viewreq.html", cal_name=x.columns.values, row_val=x.values.tolist())

@app.route("/acceptreq/<s>/<s1>")
def acceptreq(s=0, s1=''):
    otp1="Your private key is:"
    otp = random.randint(000000, 999999)
    skey = secrets.token_hex(4)
    print(skey)
    mail_content = otp1 + ' '+str(skey)
    sender_address = '107sushant@gmail.com'
    sender_pass = 'lbstvjiovzwwjmbh'
    receiver_address = s1
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Oceanic logistic Solutions'
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()

    sql = "update request_files set status='Accepted',pkey='%s' where id='%s'   "%(skey,s)
    cursor.execute(sql)
    mydb.commit()
    flash("Key sent to Receiver ", "success")
    return redirect(url_for('viewreq'))

@app.route('/down')
def down():
    email=session.get('email')

    sql ="select * from request_files where status='Accepted' and email='%s' " %(email)
    x = pd.read_sql_query(sql, mydb)
    x = x.drop(['status'], axis=1)
    x = x.drop(['pkey'], axis=1)
    x = x.drop(['email'], axis=1)
    return render_template("down.html", cal_name=x.columns.values, row_val=x.values.tolist())
@app.route("/download/<s>/<s1>")
def download(s=0,s1=0):
    global g,f1,a1
    g=s
    f1=s1

    return render_template("download.html",g=g,f1=f1)

@app.route("/downfile",methods=['POST','GET'])
def downfile():
    print("dfhlksokhso")
    if request.method == 'POST':
        print("gekjhiuth")
        fid = request.form['fid']
        id = request.form['id']
        skey = request.form['pkey']

        sql = "select count(*), aes_decrypt(file, 'lakshmi') from uploaded_files,request_files where request_files.fid = '"+fid+"' and uploaded_files.id = '"+fid+"' and request_files.id='"+id+"' and request_files.pkey='"+skey+"' "
        x = pd.read_sql_query(sql, mydb)
        count=x.values[0][0]
        print(count)
        asss=x.values[0][1]
        # asss=asss.decode('utf-8')

        print("^^^^^^^^^^^^^")
        if count==0:
            flash("Enter Valid Key","danger")
            return redirect(url_for('download'))
        if count==1:
            return render_template("downfile.html", msg=asss)

        return render_template("downfile.html")



if __name__=='__main__':
    app.run(debug=True)