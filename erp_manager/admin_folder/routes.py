from flask import Blueprint

admin = Blueprint('admin_folder', __name__, static_folder='static', template_folder='templates')


@admin.route('/home')
@admin.route('/')
def home():
    text = "Welcome dear admin"
    return f"<h1>{text}</h1>"


@admin.route('/test')
def test():
    text = "This is a test page of admin_folder!"
    return f"<h1>{text}</h1>"
