# Flask Blog

Why am using `application` instead of `app`?

look at StackOverFlow post [here](https://stackoverflow.com/questions/64236840/500-internal-server-error-elastic-beanstalk-flask/64236867?noredirect=1#comment114685109_64236867).


## Video 3

```py
import secrets
secrets.token_hex(16)

>>> 5791628bb0b13ce0c676dfde280ba245
```




## Video 4 - Creating the Database

`pip install flask-sqlalchemy`


run these lines in puython in terminal:

```py
from flaskblog import db
db.create_all()   #this will create a file called site.db as in flaskblog.py

from flaskblog import User, Post
# add users to db
user_1 = User(username='Mahmoud', email='mahmoud@demo.com', password='password')
db.session.add(user_1)    # add user_1 to db
user_2 = User(username='Reda', email='reda@demo.com', password='password')
db.session.add(user_2)
db.session.commit()   # commit changes

# return all users stored in db
User.query.all()
# return first users stored in db
User.query.first()

## Filter results
User.query.filter_by(username='Reda').all()

## Access attributes
User.query.get(2)    # get specific user by its ID
user_2.id

### Do the same with Post
post_1 = Post(title='Bost 1', content='first blog post', user_id=user_1.id)
post_2 = Post(title='Bost 2', content='second blog post', user_id=user_2.id)
db.session.add(post_1)
db.session.add(post_2)
db.session.commit()
post_1
post_1.author

## Delete all Tables & Rows
db.drop_all()
## Recreate db structure again:     ### very important
db.create_all()
```


---
## 06-Login-Auth

`pip install flask-bcrypt`


```py
import flask_bcrypt
bcrypt = flask_bcrypt.Bcrypt()

bcrypt.generate_password_hash('testing')                    # bytes
>>> b'$2b$12$4/VBoDIBBd41t87K1bEod.IaRkz8AGzmQaLuAqHDTx/Kt2bDbjRFK'
bcrypt.generate_password_hash('testing').decode('utf-8')    # String
>>> '$2b$12$Djx6UEHD/3DHuoGycLPEUuyOdd1FoSsw7M9AZr5fnTdU93BYJ45JG'
bcrypt.generate_password_hash('testing').decode('utf-8')    # will give us another hashed password
>>> '$2b$12$8tWalGJB6ZweWgXQdrQr8Oy.wEn.NDPQG/xgwijMcP1HLZA48mDXe'
bcrypt.generate_password_hash('testing').decode('utf-8')    # will give us another hashed password
>>> '$2b$12$pH97Eiwny.jz151KBpk60.O1G9lzUMMwExWDxllTpSryEsTlmxEfi'

hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
bcrypt.check_password_hash(hashed_pw, 'password')
>>> False
bcrypt.check_password_hash(hashed_pw, 'testing')
>>> True
```

`pip install flask-login`

---
## 7 - User Account and Profile

`pip install Pillow`
---
