from flask import Blueprint, jsonify, request
from erp_manager import db
from erp_manager.models import Teacher

# if we need append
# from flask import current_app

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
teacher = Blueprint('teacher_folder', __name__, static_folder='static', template_folder='templates')


@teacher.route('/home')
@teacher.route('/')
def home():
    text = "Welcome dear teacher"
    return f"<h1>{text}</h1>"


@teacher.route('/all', methods=['GET'])  # Return all teachers with GET method
def all_teachers():
    teachers = db.session.query(Teacher).all()
    every_teacher = [every_teacher.to_dict() for every_teacher in teachers]
    return jsonify(teachers=every_teacher)


@teacher.route('/add', methods=["POST"])
def post():
    try:
        new_teacher = Teacher(
            firstname=request.args.get("firstname"),
            surname=request.args.get("surname"),
            patronymic=request.args.get("patronymic"),
            fullname=f'{request.args.get("firstname")} {request.args.get("surname")} {request.args.get("patronymic")}',
            birthdate=request.args.get("birthdate"),
            gender=request.args.get("gender"),
            address=request.args.get("address"),
            avatar=request.args.get("avatar"),
            phone1=request.args.get("phone1"),
            phone2=request.args.get("phone2"),
            subjects=request.args.getlist("subjects"),
            branches=request.args.getlist("branches"),
            email=request.args.get("email"),
            password=request.args.get("password"),
            role=request.args.get("role"),
            documents=request.args.getlist("documents"),
        )

    except Exception as e:
        print(e)
        new_teacher = Teacher(
            firstname=request.form.get("firstname"),
            surname=request.form.get("surname"),
            patronymic=request.form.get("patronymic"),
            fullname=f'{request.form.get("firstname")} {request.form.get("surname")} {request.form.get("patronymic")}',
            birthdate=request.form.get("birthdate"),
            gender=request.form.get("gender"),
            address=request.form.get("address"),
            avatar=request.form.get("avatar"),
            phone1=request.form.get("phone1"),
            phone2=request.form.get("phone2"),
            subjects=request.form.getlist("subjects"),
            branches=request.form.getlist("branches"),
            email=request.form.get("email"),
            password=request.form.get("password"),
            role=request.form.get("role"),
            documents=request.form.getlist("documents"),
        )

    db.session.add(new_teacher)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new teacher."})


@teacher.route('/edit/<int:teacher_id>', methods=["PUT"])
def edit(teacher_id):
    selected_teacher = db.session.query(Teacher).get(teacher_id)
    if selected_teacher:
        selected_teacher.firstname = request.args.get("firstname")
        selected_teacher.surname = request.args.get("surname")
        selected_teacher.patronymic = request.args.get("patronymic")
        selected_teacher.fullname = request.args.get("fullname")
        selected_teacher.birthdate = request.args.get("birthdate")
        selected_teacher.gender = request.args.get("gender")
        selected_teacher.address = request.args.get("address")
        selected_teacher.avatar = request.args.get("avatar")
        selected_teacher.phone1 = request.args.get("phone1")
        selected_teacher.phone2 = request.args.get("phone2")
        selected_teacher.subjects = request.args.getlist("subjects")
        selected_teacher.branches = request.args.getlist("branches")
        selected_teacher.email = request.args.get("email")
        selected_teacher.password = request.args.get("password")
        selected_teacher.role = request.args.get("role")

        return jsonify(response={"success": "Successfully updated the teacher."}), 200
    else:
        return jsonify(error={"Not Found": "Sorry a teacher with that id was not found in the database."}), 404


@teacher.route("/delete/<int:teacher_id>", methods=["DELETE"])
def delete(teacher_id):
    delete_teacher = Teacher.query.get(teacher_id)
    api_key = request.args.get("api-key")
    if api_key == "Teacher":
        db.session.delete(delete_teacher)
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the teacher from the API."}), 200

    elif not delete_teacher:
        return jsonify(error={"Not Found": "Sorry a teacher with that id was not found in the database."}), 404

    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403


@teacher.route("/search")
def search_teacher():
    query_name = request.args.get("name")

    teachers = Teacher.query.all()
    searched_teachers = []
    for each_teacher in teachers:
        if query_name.lower() in each_teacher.fullname.lower():
            searched_teachers.append(each_teacher.to_dict())
    if len(searched_teachers) >= 1:
        return jsonify(teachers=searched_teachers)
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a teacher with that name"})


@teacher.route('/test')
def test():
    text = "This is a test page!"
    return f"<h1>{text}</h1>"
