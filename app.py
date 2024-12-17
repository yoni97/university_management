from flask import Flask
from configs.postgres_url import connection_url
from routes.producer_route import student_profile_bp

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = connection_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(student_profile_bp)

@app.route('/')
def hello_world():
    return 'Welcome to my Flask App!'


if __name__ == '__main__':
    # with app.app_context():
        # init_db()
    # init_details_to_sql()
    # checks_connection()
    app.run(host='0.0.0.0',
            debug=True,
            port=5000
            )