#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/maomao'
db = SQLAlchemy(app)
app.debug = True

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(80),unique=True)
    created_time = db.Column(db.DateTime)
    category_id = db.Column(db.Integer,db.ForeignKey('CATEGORY.id'))
    content = db.Column(db.Text)

    def __init__(self,title,content,category,created_time):
        self.title = title
        self.content = content
        self.created_time = created_time
        self.category = category
    
    
class Category(db.Model):
    __tablename__ = 'CATEGORY'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80))
    files = db.relationship('File')
    
    
    def __init__(self,name):
        self.name = name
        

def datas():
    db.create_all()
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java',datetime.utcnow(),java,'File Content - Java is cool!')    
    file2 = File('Hello Python',datetime.utcnow(),python,'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
#datas() 
@app.route('/')  
def index():
    return render_template('index.html',files=File.query.all())

@app.route('/files/<int:file_id>')
def file(file_id):
    file_item = File.query.get_or_404(file_id)
    return render_template('file.html',file_item=file_item)
    
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404

if __name__ == "__main__":
    app.run(port=3000)
 
# sudo service mysql start
# mysql -u root
# create database maomao
# use maomao
# run app.py

# 注销#datas()函数，创建两表
# 重新给datas()加上#
# run app.py


 
