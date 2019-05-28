from flask import *
from flask.ext.sqlalchemy import SQLAlchemy

# configure app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)


@app.route('/test', methods=['GET'])
def test():
    return 'This is working!'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
