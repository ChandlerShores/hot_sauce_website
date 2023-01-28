from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hot_sauce.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    date = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<News {self.title}>'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about-us')
def about_us():
    return render_template('about-us.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/news')
def news():
    news_list = News.query.all()
    return render_template('news.html', news_list=news_list)

@app.route('/add-news', methods=['GET', 'POST'])
def add_news():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        date = request.form['date']

        new_news = News(title=title, body=body, date=date)
        db.session.add(new_news)
        db.session.commit()

        return redirect(url_for('news'))
    else:
        return render_template('add-news.html')

@app.route('/update-news/<int:id>', methods=['GET', 'POST'])
def update_news(id):
    news = News.query.get(id)
    if request.method == 'POST':
        news.title = request.form['title']
        news.body = request.form['body']
        news.date = request.form['date']

        db.session.commit()

        return redirect(url_for('news'))
    else:
        return render_template('update-news.html', news=news)

@app.route('/delete-news/<int:id>', methods=['GET', 'POST'])
def delete_news(id):
    news = News.query.get(id)
    db.session.delete(news)
    db.session.commit()
    return redirect(url_for('news'))

# Error handling
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    db.create_all()
