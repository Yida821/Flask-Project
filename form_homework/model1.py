import datetime
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Profile(db.Model):
    __tablename__ = 'profile'

    # primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # full_name
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    
    #password & email
    email = db.Column(db.String(80), nullable=True)
    password = db.Column(db.String(80), nullable=True)


    # attachment
    file_photo_filename = db.Column(db.String(80), nullable=True)
    file_photo_code = db.Column(db.String(80), nullable=True)

    #check_box and radio
    check_box =  db.Column(db.String(80), nullable=True)
    radio = db.Column(db.String(80), nullable=True)

    #date, city, state, zipcode
    date = db.Column(db.String(80), nullable=True)
    city = db.Column(db.String(80), nullable=True)
    state = db.Column(db.String(80), nullable=True)
    zipcode = db.Column(db.String(80), nullable=True)
    address = db.Column(db.String(80), nullable=True)

    #date_range, time_picker, slider_value
    date_range = db.Column(db.String(80), nullable=True)
    time = db.Column(db.String(80), nullable=True)
    slider_value = db.Column(db.String(80), nullable=True)

    #multiselect
    multiselect = db.Column(db.String(80), nullable=True)

    #Like level
    like_level = db.Column(db.String(80), nullable=True)


    def remove_none_values(self):
        self.first_name = self.first_name if self.first_name else ""
        self.last_name = self.last_name if self.last_name else ""
        self.file_photo_filename = self.file_photo_filename if self.file_photo_filename else ""
        self.file_photo_code = self.file_photo_code if self.file_photo_code else ""
        self.check_box = self.check_box if self.check_box else ""
        self.radio = self.radio if self.radio else ""
        self.date_range = self.date_range if self.date_range else ""
        self.time = self.time if self.time else ""
        self.slider_value = self.slider_value if self.slider_value else ""
        self.multiselect = self.multiselect if self.multiselect else ""
        self.like_level = self.like_level if self.like_level else ""

    def list_to_string(self,my_list, delim = ","):
        my_string = ""
        for i in my_list:
            my_string += i + delim
        self.multiselect = my_string    

    def string_to_list(self,my_string):
        return self.multiselect.split(',')


class Tables(db.Model):
    __tablename__ = 'tables'

    # primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # full_name
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    
    #password & email
    email = db.Column(db.String(80), nullable=True)
    dob = db.Column(db.String(80), nullable=True)


    # attachment
    file_photo_filename = db.Column(db.String(80), nullable=True)
    file_photo_code = db.Column(db.String(80), nullable=True)


    #excel
    file_data_filename  = db.Column(db.String(80), nullable=True)
    file_data_code = db.Column(db.String(80), nullable=True)

    def remove_none_values(self):
        self.first_name = self.first_name if self.first_name else ""
        self.last_name = self.last_name if self.last_name else ""
        self.file_photo_filename = self.file_photo_filename if self.file_photo_filename else ""
        self.file_photo_code = self.file_photo_code if self.file_photo_code else ""
        self.email = self.email if self.email else ""
        self.dob = self.dob if self.dob else ""



 
class Employee(db.Model):
    __tablename__ = 'employee'   
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    employee_id = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone_number = db.Column(db.String(100))
    hire_date = db.Column(db.Date)
    job_id = db.Column(db.String(100))
    salary = db.Column(db.Float)
    commission_pct   = db.Column(db.Float)
    department_id = db.Column(db.Integer)
    department_name = db.Column(db.String(100))

    @classmethod
    def from_dict(cls,in_dict):
        cls = Employee()
        cls.employee_id = in_dict['EMPLOYEE_ID']
        cls.first_name = in_dict['FIRST_NAME']
        cls.last_name = in_dict['LAST_NAME']
        cls.email = in_dict['EMAIL']
        cls.phone_number = in_dict['PHONE_NUMBER']
        if in_dict['HIRE_DATE']:
            cls.hire_date = datetime.datetime.strptime(
                str(in_dict['HIRE_DATE']), "%m/%d/%Y")

        cls.job_id = in_dict['JOB_ID']
        cls.salary = in_dict['SALARY']
        cls.commission_pct = in_dict['COMMISSION_PCT']
        cls.department_id = in_dict['DEPARTMENT_ID']
        cls.department_name = in_dict['DEPARTMENT_NAME']

        return cls


class Banking(db.Model):
    __tablename__ = 'banking'

    # primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    Row_Number= db.Column(db.String(100))
    Customer_Id= db.Column(db.String(100))
    Sur_name= db.Column(db.String(100))
    Credit_Score= db.Column(db.String(100))
    Geography= db.Column(db.String(100))
    Gender= db.Column(db.String(100))
    Age= db.Column(db.String(100))
    Tenure= db.Column(db.String(100))
    Balance= db.Column(db.Float)
    Num_Of_Products= db.Column(db.String(100))
    Has_CrCard= db.Column(db.String(100))
    Is_Active_Member= db.Column(db.String(100))
    Estimated_Salary= db.Column(db.Float)
    Exited= db.Column(db.String(100))

    def to_dict(self):
        return {"Row_Number": self.Row_Number, "Customer_Id": self.Customer_Id, "Sur_name": self.Sur_name, 
        "Credit_Score": self.Credit_Score, "Geography": self.Geography, "Gender": self.Gender,
        "Age": self.Age, "Tenure": self.Tenure, "Balance": self.Balance, "Num_Of_Products": self.Num_Of_Products,
        "Has_CrCard": self.Has_CrCard, "Is_Active_Member": self.Is_Active_Member, "Estimated_Salary": self.Estimated_Salary, "Exited": self.Exited}

    @classmethod
    def from_dict(cls, in_dict):
        cls = Banking()
        cls.Row_Number = in_dict['Row_Number']
        cls.Customer_Id = in_dict['Customer_Id']
        cls.Sur_name = in_dict['Sur_name']
        cls.Credit_Score = in_dict['Credit_Score']
        cls.Geography = in_dict['Geography']
        cls.Gender = in_dict['Gender']
        cls.Age = in_dict['Age']
        cls.Tenure = in_dict['Tenure']
        cls.Balance = in_dict['Balance']
        cls.Num_Of_Products = in_dict['Num_Of_Products']
        cls.Has_CrCard = in_dict['Has_CrCard']
        cls.Is_Active_Member = in_dict['Is_Active_Member']
        cls.Estimated_Salary = in_dict['Estimated_Salary']
        cls.Exited = in_dict['Exited']

        return cls

class Bank(db.Model):
    __tablename__ = 'bank'
     # primary key
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    customer_id  = db.Column(db.String(100))
    sur_name = db.Column(db.String(100))
    credit_score = db.Column(db.Integer)
    geography = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    age = db.Column(db.Integer)
    tenure = db.Column(db.Integer)
    balance = db.Column(db.Float)
    num_of_products = db.Column(db.Integer)
    has_cr_card = db.Column(db.Integer)
    is_activate_member = db.Column(db.Integer)
    estimated_salary = db.Column(db.Float)
    exited = db.Column(db.Integer)

    # excel/csv attachment
    file_data_filename = db.Column(db.String(80), nullable=True)
    file_data_code = db.Column(db.String(80), nullable=True)

    def remove_none_values(self):
        self.customer_id = self.customer_id if self.customer_id else ""
        self.sur_name = self.sur_name if self.sur_name else ""
        self.credit_score = self.credit_score if self.credit_score else ""
        self.geography = self.geography if self.geography else ""

        self.age = self.age if self.age else ""
        self.tenure = self.tenure if self.tenure else ""
        self.balance = self.balance if self.balance else ""
        self.num_of_products = self.num_of_products if self.num_of_products else ""

        self.has_cr_card = self.has_cr_card if self.has_cr_card else ""
        self.is_activate_member = self.is_activate_member if self.is_activate_member else ""
        self.estimated_salary = self.estimated_salary if self.estimated_salary else ""
        self.exited = self.exited if self.exited else ""


        self.file_data_filename = self.file_data_filename if self.file_data_filename else ""
        self.file_data_code = self.file_data_code if self.file_data_code else ""

    def to_dict(self):
        return {"id": self.customer_id, "name": self.sur_name, "credit_score":self.credit_score, "geography":self.geography, "gender":self.gender, "age":self.age, "tenure":self.tenure, "balance":self.balance, "product":self.num_of_products, "credit_card":self.has_cr_card, "activate":self.is_activate_member, "salary":self.estimated_salary, "exited":self.exited}
    def to_x_y(self):
        return {'x': self.age, 'y': self.credit_score}

    def __str__(self):  
        
        return "Tenure: " + str(self.tenure) + "  "+"Exited: " + str(self.exited)
    
    
    @classmethod
    def from_dict(cls, in_dict):
        cls = Bank()
        cls.customer_id = in_dict['Customer_Id']
        cls.sur_name = in_dict['Sur_name']
        cls.credit_score  = in_dict['Credit_Score']
        cls.geography  = in_dict['Geography']
        cls.gender  = in_dict['Gender']
        cls.age  = in_dict['Age']
        cls.tenure  = in_dict['Tenure']
        cls.balance  = in_dict['Balance']
        cls.num_of_products  = in_dict['Num_Of_Products']
        cls.has_cr_card  = in_dict['Has_CrCard']
        cls.is_activate_member  = in_dict['Is_Active_Member']
        cls.estimated_salary   = in_dict['Estimated_Salary']
        cls.exited   = in_dict['Exited']

        return cls
