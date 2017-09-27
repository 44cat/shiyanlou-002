------------------Learn-MYSQL--------------------
# MySQL(一)
```
启动MySQL服务
sudo service mysql start

使用root用户登录，实验楼环境密码为空，直接回车登录
mysql -u root

查看数据库
show databases;

连接数据库
use [database_name]  （注意这里没有分号）

查看表
show tables;

退出
quit/exit
```
# MySQL(二)

## 新建数据库
CREATE DATABASE [数据库名];

## 连接数据库
```
CREATE TABLE 表名
(
列名A 数据类型(数据长度),           (用,分隔)
列名B 数据类型(数据长度),
列名C 数据类型(数据长度)             (最后的没有,)
);
````
## 新建完表后只有像元组的表
## 通过INSERT语句向表内插入数据
```
INSERT INTO 表名(列名A,列名B,列名C) VALUES(值1,值2,值3);    (有列无值插入,返回NULL)
```
