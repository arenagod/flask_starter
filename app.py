from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(20), nullable=False)
#     data_create = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<User %r>' % self.id








@app.route('/', methods=['GET', 'POST'])
def home():

    return render_template('index.html')







if __name__ == '__main__':
    app.run(port=80, debug=True)