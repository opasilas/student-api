from app import db

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __repr__(self):
        return f"<Student {self.name}>"

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }

# db.create_all()