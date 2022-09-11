from erp_manager import create_app

app = create_app()

# RUN THESE BEFORE RUNNING THE APP

# $ python
# >>> from erp_manager import create_app
# >>> app = create_app()
# >>> app.app_context().push()

# >>> from erp_manager import db
# >>> db.create_all(app=create_app())

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
