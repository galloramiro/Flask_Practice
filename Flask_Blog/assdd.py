from flaskblog import app, db, bcrypt
from flaskblog.models import  User, Post

db.create_all()
"""
user_1 = User(username='Corey', email='c@demo.com', password='password')
db.session.add(user_1)
user_2 = User(username='JohnDOe', email='j@demo.com', password='password')
db.session.add(user_2)
db.session.commit()


user_1 = User.query.first()

post_1 = Post(title='Blog 1', content='First Post Content!', user_id=user_1.id)
post_2 = Post(title='Blog 2', content='Second Post Content!', user_id=user_1.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()

print(User.query.all())
print(User.query.first())
print(User.query.filter_by(username='Corey').all())
print(user_1.post)
"""
user_1 = User.query.first()

#db.drop_all()
#db.create_all()
print(User.query.all())
print(user_1.password)
print(Post.query.all())