from app.db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), unique=True)
    phone = db.Column(db.String(255))
    address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime())
    updated_at = db.Column(db.DateTime())

    def __ini__(self, name, lastname, username, email, password, phone, address):
        self.name = name
        self.lastname = lastname
        self.username = username
        self.email = email
        self.password = password
        self.phone = phone
        self.address = address

    def to_json(self):
        return{
            'id' : self.id,
            'full_name' : f"{self.name} {self.address}",
            'email' : self.email,
            'phone' : self.phone,
            'address': self.address
        }