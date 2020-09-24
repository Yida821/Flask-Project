class User():
    def __init__(self, name, email,password):
        self.name = name
        self.email = email
        self.password = password

class FormHomework():
    def __init__(self, first_name, last_name, email, password, gender, order_type,
    address1, address2, city, state, zipcode, checkbox, message, photo): #photo
        self.first_name = first_name
        self.last_name =  last_name
        self.email = email
        self.password =  password
        self.gender = gender
        self.order_type =  order_type
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.checkbox = checkbox
        self.message = message
        self.photo = photo

class Photo():
    def __init__(self, photo):
        self.photo =  photo
