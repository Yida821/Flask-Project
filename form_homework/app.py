import os
from flask import Flask, render_template, request, flash, url_for, redirect,abort, send_file, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, case, and_, or_
import json
import requests
import uuid
import pandas as pd
#internal modules
from model import User, FormHomework, Photo
from model1  import db, Profile, Tables, Employee, Banking, Bank
from regression import LinearRegression
from forms import RegisterForm,LoginForm,FormCollection, UploadForm, ProfileForm, TablesForm, EmployeeForm, GroupUploadForm, BankForm
import sqlite3
from werkzeug.utils import secure_filename
from flask_login import login_user, current_user, logout_user, login_required




#instantiate flask
app = Flask(__name__)

#configure
app.config['SECRET_KEY'] = 'b5fe0584dd8bb2c792c920dff3d82295'
app.config['UPLOAD_FOLDER'] = './static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
#db = SQLAlchemy(app)


# initalize app with database
db.init_app(app)

#decorator addes other functionality to this function
@app.before_first_request
def before_first_request_func():
    db.create_all()




#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#db = SQLAlchemy(app)

#UPLOAD_FOLDER = 'UPLOAD_FOLDER'
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#ALLOWED_EXTENSIONS = {'csv','xlsx'}


DATABASE = 'yichun.db'
@app.route("/")
@app.route("/yichun", methods = ['GET','POST'])
def yichun():

    return render_template('yichun.html', title = 'Yichun') # customize the title


@app.route("/swap_2_numbers", methods = ['GET','POST'])
def swap_2_numbers():
    if request.method == "POST":
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        #value that is already swaped
        #print(num1) 
        #print(num2)
        #pass swaped num1 and num2 as prameters to render_template assign to value = {num}
        return render_template('swap_2_numbers.html', title = 'Swap Numbers', num1 = num1, num2= num2)
    
    return render_template('swap_2_numbers.html', title = 'Swap Numbers') # customize the title


@app.route("/forum", methods = ['GET','POST'])
def forum():

    return render_template('about.html', title = 'About Us') # customize the title

'''
@app.route("/register", methods = ['GET','POST'])
def register():
    #print(request.args) Immutable dictionary
    #name = request.args.get("name")
    #email = request.args.get("email")
    #password = request.args.get("password")
    user = None
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        #make the model 
        user = User(name, email, password)
    #print("name", name)
    #print("email", email)
    #print("password", password)
    
    return render_template('register.html', title = 'My Flask', user = user) # customize the title
'''

@app.route("/register", methods=['Get', 'Post'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            user = User(form.name.data, form.email.data, form.password.data)
            if request.method == "POST":
                name = request.form.get('name')
                email = request.form.get('email')
                password = request.form.get('password')
                print(name)
                print(password)
                print(email)
            with sqlite3.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user (name,email,password) VALUES (?,?,?)",
                            (user.name, user.email, user.password))
                con.commit()
                flash('Registered Successfully!', 'success')
                return redirect(url_for('login'))
        except Exception as e:
            con.rollback()
            flash(f'Unknow error!\n{str(e)}', 'danger')

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['Get', 'Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            with sqlite3.connect(DATABASE) as con:
                cur = con.cursor()
                cur.execute("SELECT * FROM user WHERE email = ? and password = ?", [form.email.data, form.password.data])
                rows = cur.fetchall()
                print(rows)
                row = rows[0]
                if row:
                    flash('Login Successfully!', 'success')
                    return redirect(url_for('shop'))
                else:
                    flash('Login Unsuccessfully. Please check email and password', 'danger')
        except Exception as e:
            con.rollback()
            flash(f'Unknow error!\n{str(e)}', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/form", methods=['Get', 'Post'])
def form():
    form = FormCollection()
    if form.validate_on_submit():
         if form.photo.data:
            #if the post form request has a file data
            file  = form.photo.data
            print(file.filename)
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'],filename)
            print(file_path)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            try:
                model = FormHomework(form.first_name.data, form.last_name.data, form.email.data, form.password.data, form.gender.data, form.order_type.data, form.address1.data, form.address2.data, form.city.data, form.state.data, form.zipcode.data, form.checkbox.data,form.message.data, file_path)
                with sqlite3.connect(DATABASE) as con:
                    cur = con.cursor()

                    cur.execute("INSERT INTO form_collection6 (first_name,last_name, email,password, gender, order_type, address1, address2, city, state, zipcode, checkbox, message, photo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                                (model.first_name, model.last_name, model.email, model.password, model.gender, model.order_type, model.address1, model.address2, model.city, model.state, model.zipcode, model.checkbox, model.message, model.photo))
                    con.commit()
                    flash('Capture data and store in database Successfully!', 'success')
                    return redirect(url_for('form_display')) 
            except Exception as e:
                con.rollback()
                flash(f'Unknow error!\n{str(e)}', 'danger')    

    return render_template('form.html', title='Form', form = form)


@app.route("/form_display", methods = ['GET','POST'])
def form_display():
    rows = None
    try:
        #instantiate model FormHomeowrk
        #model = FormHomework(form.first_name.data, form.last_name.data, form.email.data, form.password.data, form.gender.data, form.order_type.data, form.address1.data, form.address2.data, form.city.data, form.state.data, form.zipcode.data, form.message.data)
        #user = User(form.name.data, form.email.data, form.password.data)
        with sqlite3.connect(DATABASE) as con:
            cur = con.cursor()
            cur.execute("SELECT * FROM form_collection6  " ) #WHERE message = 'hello'
            rows = cur.fetchall()
            con.commit()
            flash('Retrieve all information from Database', 'success')
            return render_template('form_display.html', title = 'Form Display', rows = rows)
    except Exception as e:
        con.rollback()
        flash(f'Unknow error!\n{str(e)}', 'danger')

    return render_template('form_display.html', title = 'Form Display') # customize the title

@app.route('/download/<path:filename>')
def downloadFile(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(path, as_attachment=True)



@app.route("/profile", methods = ['GET','POST'])
def profile():
    #form instance
    form = ProfileForm()
    #model instance
    data = Profile()
    #print("sucess")
 
    if form.validate_on_submit():
        data.first_name = request.form.get('first_name')
        data.last_name = request.form.get('last_name')
        data.email =  request.form.get('email')
        data.password = request.form.get('password')
        data.check_box = request.form.get('check_list')
        data.radio = request.form.get('radio1')
        data.city = request.form.get('city')
        data.state = request.form.get('state')
        data.zipcode = request.form.get('zipcode')
        data.date = request.form.get('choose_date')
        data.address = request.form.get('address')
        data.date_range = request.form.get('my_date_range')
        data.time =  request.form.get('time_picker')
        data.slider_value =  request.form.get('slider_value')
        data.list_to_string(request.form.getlist('multiple_states'))
        data.like_level = request.form.get('multiple_options')
        #print("data.check_box", data.check_box)
        #print("data.date_range", data.date_range) 
        #print("data.time", data.time)
        #print("data.slider_value", data.slider_value)
        #print("data.multiselect", data.multiselect)
        #print("data.like_level", data.like_level)
        #test fetch data from the form successfully

        # process file
        file = request.files.get('file_photo')
        #print("filename", file.filename)
        if file:
            orig_filename = secure_filename(file.filename)
            new_filename = str(uuid.uuid1())
            data.file_photo_filename = orig_filename
            data.file_photo_code = new_filename
            #rint("data.file_photo_filename", data.file_photo_filename)
            #print("data.file_photo_code", data.file_photo_code)
            


            #save the local file system
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))

            # save to database
            db.session.add(data)
            db.session.commit()
            #print("data", data.id)
            return redirect('/profile/' + str(data.id)) 
    
    return render_template('profile.html', title = 'Profile', form = form) # customize the title


@app.route("/profile/<int:id>", methods=['Get'])
def profile_by_id(id):
    data = Profile.query.filter_by(id=id).first()
    if data == None:
        abort(404)
    # print(my_data)
    return render_template('profile_view.html', data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/shop")
def shop():
    #create a dictionary stores {product - items} key-value pair
    shoppingDict = {'product1' : {'image' : 'static/pics/1.jfif' , 'name' : 'name1', 'price' : 'price1', 'description' : "This is the description for product1"},
                    'product2' : {'image' : 'static/pics/2.jfif' , 'name' : 'name2', 'price' : 'price2', 'description' : "This is the description for product2"},
                    'product3' : {'image' : 'static/pics/3.jfif' , 'name' : 'name3', 'price' : 'price3', 'description' : "This is the description for product3"},
                    'product4' : {'image' : 'static/pics/4.jfif' , 'name' : 'name4', 'price' : 'price4', 'description' : "This is the description for product4"},
                    'product5' : {'image' : 'static/pics/5.jfif' , 'name' : 'name5', 'price' : 'price5', 'description' : "This is the description for product5"},
                    'product6' : {'image' : 'static/pics/6.jfif' , 'name' : 'name6', 'price' : 'price6', 'description' : "This is the description for product6"},
                    'product7' : {'image' : 'static/pics/7.jfif' , 'name' : 'name7', 'price' : 'price7', 'description' : "This is the description for product7"},
                    'product8' : {'image' : 'static/pics/8.jfif' , 'name' : 'name8', 'price' : 'price8', 'description' : "This is the description for product8"},
                    'product9' : {'image' : 'static/pics/9.jfif' , 'name' : 'name9', 'price' : 'price9', 'description' : "This is the description for product9"},
                    'product10' : {'image' : 'static/pics/10.jfif' , 'name' : 'name10', 'price' : 'price10', 'description' : "This is the description for product10"}
                    }  
    return  render_template('shop.html', title = 'shop', dic_items = shoppingDict.items())

@app.route("/tables", methods= ['Get', 'Post'])
def tables():
    my_form = TablesForm()
    my_data = Tables()
    my_data.remove_none_values()
    print("get")

    if my_form.validate_on_submit():
    
        my_form.first_name = request.form.get('first_name')
        
        my_form.last_name = request.form.get('last_name')
        my_form.email = request.form.get('email')
        my_form.dob = request.form.get('choose_date')
        print("my_form.first_name",my_form.first_name)
        print("my_form.last_name",my_form.last_name)
        print("my_form.email",my_form.email)
        print("my_form.dob",my_form.dob)
        db.session.add(my_data)
        db.session.commit()
        print(my_data.id)

        #return redirect("/tables/" + str(my_data.id))

    return  render_template('tables.html', my_form = my_form, my_data = my_data)

@app.route("/display", methods = ['GET','POST'])
def display():

    return render_template('display.html', title = 'My Flask') # customize the title

@app.route("/test", methods = ['GET','POST'])
def test():

    return render_template('test.html', title = 'My Flask') # customize the title

@app.route("/regression", methods = ['GET','POST'])
def regression():
    #LinearRegression
    resultString = ''
    input1 = ''
    input2 = ''
    output1 = ''

    liner_regression = LinearRegression()
    print("okay")
    if request.method == "POST":
        input1 = request.form.get('input1')
        print("input1", input1)
        input_x_list = liner_regression.regression_string_2_list(input1)
        print("input_x_list", input_x_list)

        input2 = request.form.get('input2')
        print("input2", input2)
        input_y_list = liner_regression.regression_string_2_list(input2)
        print("input_y_list", input_y_list)

        liner_regression.model(input_x_list, input_y_list)


        output1 = request.form.get('output1')
        print("output1", output1)
        predict_x_list = liner_regression.regression_string_2_list(output1)
        print("predict_x_list", predict_x_list)


        predict_y_list = liner_regression.predict(predict_x_list)
        print("predict_y_list", predict_y_list)
        
        resultString = ''
        for i in range(len(predict_y_list)):
            resultString += str(predict_y_list[i]) + ', '
        print("resultString", resultString)    
        return render_template('regression.html', title = 'Regression', resultString = resultString, input1 = input1,input2 = input2, output1 =output1) # customize the title


    return render_template('regression.html', title = 'Regression', resultString = resultString, input1 = input1,input2 = input2, output1 =output1) # customize the title




@app.route("/employee", methods = ['GET','POST'])
def employee():
    my_form = EmployeeForm()
    print("sucess")
    if my_form.validate_on_submit():
        # fetch the uploaded file
        file_csv = request.files.get('file_csv')
        print("valid")
        if file_csv:
            # get the file full path
            file_full_path = os.path.join(app.config['UPLOAD_FOLDER'], file_csv.filename)
            # save it in the server file system
            file_csv.save(file_full_path)
            # read that file in dataframe 
            df = pd.read_csv(file_full_path)
            #print(df)
            employee_list_raw = df.to_dict('records')
            #create a list for bulk insert later on
            employee_list = []
            for curr_employee in employee_list_raw:
                emp = Employee.from_dict(curr_employee)
                employee_list.append(emp)
            print("employee_list_count", len(employee_list)) 

            # save t0 DB
            db.session.bulk_save_objects(employee_list)
            db.session.commit()

            # test query
            e_list = Employee.query.limit(5).all()
            print("*******")
            print(e_list)
            print("*******")  


    return render_template('employee.html', title = 'Employee', my_form = my_form) # customize the title



@app.route("/bank", methods=['Get', 'Post'])
def bank():
    my_form = BankForm()
    my_data = Bank()
    my_data.remove_none_values()
    if my_form.validate_on_submit():
        file_csv = request.files.get('file_csv')
        if file_csv:
            if file_csv:
                file_full_path = os.path.join(
                    app.config['UPLOAD_FOLDER'], file_csv.filename)
                # print("file_full_path", file_full_path)

                # save to upload folder
                file_csv.save(file_full_path)
            #print("save file")
         

            # read file using pandas
            df = pd.read_csv(file_full_path)
            #print(df)
            bank_list_dic = df.to_dict('record')
            #print(bank_list_dic)
            #load data to bank table
            bank_list = []
            for cur_bank_list_dic in bank_list_dic:
                bank = Bank.from_dict(cur_bank_list_dic)
                bank_list.append(bank)
            #print("bank_list", len(bank_list))

            # save t0 DB
            db.session.bulk_save_objects(bank_list)
            db.session.commit()
            print("save to db")
            #return render_template("query_bank.html", title="Bank", my_form = my_form)
            # redirect to display page
            #return redirect('/bank/' + str(my_data.id))  # profile/5

    return render_template("bank.html", title="Bank", my_form = my_form)

@app.route("/query_bank", methods=['Get'])
def query_bank():
    bank_list = Bank.query.limit(100).all()
    scatter_list = []
    for bank in bank_list:
        scatter_list.append(bank.to_x_y())

    return render_template('query_bank.html', bank_list = bank_list, scatter_list=scatter_list )



@app.route("/bankjson", methods=['Get'])
def bankjson():
    bank_list = []

    banks_count = Bank.query.count()
    banks = Bank.query.all()
    for bank in banks:
        bank_list.append(bank.to_dict())
    # print(bank_list)
    return jsonify({"draw": 1, "recordsTotal": banks_count, "recordsFiltered": banks_count, "data": bank_list})


@app.route("/chart", methods=['Get'])
def chart():
    leave = func.count(case([((Bank.exited) == 1,1)]).label('leave'))

    stay =func.count(case([((Bank.exited) == 0,1)]).label('stay'))

    testing=db.session.query(Bank.tenure,leave,stay).group_by(Bank.tenure)
    new_list1 = []
    new_list2 = []
    for test in testing:
        new_list1.append(test[1])
        new_list2.append(test[2])

    print(testing)

    return render_template('chart.html', new_list1=new_list1, new_list2 =new_list2)

@app.route("/upload", methods=['Get', 'Post'])
def upload():
    my_form = GroupUploadForm()

    if my_form.validate_on_submit():  # my_form.submitted()
            # file we are importing
            file_csv = request.files.get('file_csv')

            if file_csv:
                file_full_path = os.path.join(
                    app.config['UPLOAD_FOLDER'], file_csv.filename)
                # print("file_full_path", file_full_path)

                # save to upload folder
                file_csv.save(file_full_path)
            # read the csv using pandas
            df = pd.read_csv(file_full_path)
            dataset =  df.to_dict('records')

            new_list = []
            for data in dataset:
                lis = Banking.from_dict(data)
                #print(lis)
                new_list.append(lis)

            #print("lis_count", len(new_list))

            # save to DB
            db.session.bulk_save_objects(new_list)
            db.session.commit()

            # test query
            e_list = Banking.query.limit(5).all()
            print("*******")
            print(e_list)
            print("*******")   
            return redirect(url_for('banking'))

    return render_template('groupupload.html', my_form = my_form)


@app.route("/banking")
def banking():
    my_data = Banking.query.all()
    sample_data2=Banking.query.limit(1000).all()

    return render_template('banking.html', my_data=my_data,sample_data2=sample_data2)



@app.route("/banking.json", methods=['Get'])
def banking_api():
    b_list = []

    b_count = Banking.query.count()
    data_all = Banking.query.all()

    for data in data_all:
        b_list.append(data.to_dict())
    
    return jsonify({"draw": 1, "recordsTotal": b_count, "recordsFiltered": b_count, "data": b_list})

@app.route("/group_dashboard")
def group_dashboard():
    #The general data--Contrbuted by Siqi Xu
    sum_cus=db.session.query(
        func.count(Banking.Customer_Id),
        func.round(func.avg(Banking.Credit_Score),0),
        func.round(func.max(Banking.Credit_Score),0),
        func.round(func.min(Banking.Credit_Score),0),
        func.round(func.avg(Banking.Estimated_Salary),2),
        func.round(func.max(Banking.Estimated_Salary),2),
        func.round(func.min(Banking.Estimated_Salary),2),
        func.count(case([((Banking.Exited)==0,1)]).label('stay')),
        func.count(case([(or_((Banking.Exited)==1,(Banking.Exited)==0),1)]).label('Total'))
        ).all()

    count_cus=[a for a,b,c,d,e,f,g,h,i in sum_cus]
    avg_cre=[b for a,b,c,d,e,f,g,h,i in sum_cus]
    max_cre=[c for a,b,c,d,e,f,g,h,i in sum_cus]
    min_cre=[d for a,b,c,d,e,f,g,h,i in sum_cus]
    avg_sal=[e for a,b,c,d,e,f,g,h,i in sum_cus]
    max_sal=[f for a,b,c,d,e,f,g,h,i in sum_cus]
    min_sal=[g for a,b,c,d,e,f,g,h,i in sum_cus]
    stay_exi=[h for a,b,c,d,e,f,g,h,i in sum_cus]
    total_exi=[i for a,b,c,d,e,f,g,h,i in sum_cus]

    
    #First Line Graph--contributed by Alicia (Qing Lan Zheng)
    low_risk=func.count(case
        ([
            ((Banking.Estimated_Salary-Banking.Balance)>0,1)
            ]).label('low risk'))


    high_risk=func.count(case
        ([
            ((Banking.Estimated_Salary-Banking.Balance)<0,1)
            ]).label('high risk'))

    testing=db.session.query(Banking.Geography,low_risk,high_risk).group_by(Banking.Geography)
    print("testing",testing)
    geography=[i for i,j,k in testing]
    low_risk_num=[j for i,j,k in testing]
    high_risk_num=[k for i,j,k in testing]
    print("geography",geography)

    #Second bar graph--contributed by Yichun Liu
    leave=func.count(case
        ([
            ((Banking.Exited)==1,1)
            ]).label('leave'))

    stay=func.count(case
        ([
            ((Banking.Exited)==0,1)
            ]).label('stay'))

    testing2=db.session.query(Banking.Tenure,leave,stay).group_by(Banking.Tenure).all()

    Leave=[i for i,j,k in testing2]
    Stay=[j for i,j,k in testing2]

    #Third doughnut graph--contributed by Siqi Xu
    high_cr=db.session.query(Banking.Geography,func.count(case([((Banking.Credit_Score)>700,1)]).label('high_credit'))).group_by(Banking.Geography).all()
    cr_geo_la=[a for a,b in high_cr]
    cr_geo_am=[b for a,b in high_cr]

    return render_template('group_dashboard.html', geography=geography, low_risk_num=low_risk_num, high_risk_num=high_risk_num,Leave=Leave,
    Stay=Stay,sum_cus=sum_cus,count_cus=count_cus,avg_cre=avg_cre,max_cre=max_cre,min_cre=min_cre,avg_sal=avg_sal,max_sal=max_sal,min_sal=min_sal,
    stay_exi=stay_exi,total_exi=total_exi,cr_geo_la=cr_geo_la,cr_geo_am=cr_geo_am)




@app.route("/tableau")
def tableau():
    

    return render_template('tableau.html')


#debug deals with hot change
#what is the debug pin? How can we use it ?
#redeploy the server
if __name__=='__main__':
    app.run(debug = True)
