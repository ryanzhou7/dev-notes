from flaskr import db


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long = db.Column(db.String(128))

    def __repr__(self):
        return f'<Url id:{self.id}, long:{self.long}>'
