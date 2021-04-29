from sqlalchemy.orm import backref
from extensions import db
from datetime import datetime
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(55), nullable=False)
    short_description = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(20), default='default.jpg', nullable=False)
    date_posted = db.Column(db.DateTime, str(default=datetime.utcnow))
    category = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

    def __repr__(self):
        return self.title


class Category(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    posts = db.relationship(Post, backref='categories', lazy=True)
    title = db.Column(db.String(55), nullable=False)



