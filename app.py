from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql+psycopg2://postgres:West7th7@localhost/quotes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False


db = SQLAlchemy(app)


class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(300))
    quote = db.Column(db.String(5000))
      
@app.route('/')
def index():
    result = Favquotes.query.all()
    return render_template('index.html',result=result)




@app.route('/quotes')
def my_quotes():
    return render_template('quotes.html')



@app.route('/process',methods= ['GET','POST' ])
def process():
    
    author = request.form.get('author')
    quote = request.form.get('quote')
    quotedata =Favquotes(author=author,quote=quote)
    db.session.add(quotedata)
    db.session.commit()
    
    return redirect(url_for('index')) 


if __name__ == "__main__":
    app.run(debug=True)