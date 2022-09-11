from erp_manager import db


class User(db.Model):  # parent
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    birthdate = db.Column(db.String(100))
    departament = db.Column(db.String(150))
    started_date = db.Column(db.String(150))
    role = db.Column(db.String(100))
    img = db.Column(db.String(100))
    address = db.Column(db.PickleType)
    documents = db.Column(db.PickleType)
    passport_details = db.Column(db.PickleType)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    patronymic = db.Column(db.String(100))
    fullname = db.Column(db.String(100))
    birthdate = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    address = db.Column(db.String(100))
    avatar = db.Column(db.String(250))
    phone1 = db.Column(db.String(100))
    phone2 = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    role = db.Column(db.String(100))
    subjects = db.Column(db.PickleType)
    branches = db.Column(db.PickleType)
    documents = db.Column(db.PickleType)

    def to_dict(self):  # automatic calling the dict (creating a func)
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return '<Teacher {}>'.format(self.fullname)


# db.create_all()

