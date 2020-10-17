from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tweets.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  content = db.Column(db.Text, nullable=False)
  author = db.Column(db.String(20), nullable=False, default="N/A")
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

  def __repr__(self):
    return 'Blogpost ' + str(self.id)
all_posts = [
  {
    'title': 'post 1',
    'content': 'Tis is the content of the post 1.',
    'author': 'sahil'
  },
  {
    'title': 'post 2',
    'content': 'Tis is the content of the post 2.'
  }
]

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/posts')
def posts():
  return render_template('posts.html', posts=all_posts)

@app.route('/home/<name>')
def hello(name):
  return "Hello " + name

@app.route('/onlyget', methods=['GET'])
def get_req():
  return 'you will only get this webpage'

if __name__ == "__main__":
  app.run(debug=True)