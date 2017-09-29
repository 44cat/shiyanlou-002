-----------------------------Learn-MySQL----------------------------
MySQL(二)
# 约束类型/关键字

```
主键：PRIMARY KEY
默认值：DEFAULT
唯一：UNIQUE
外键：FOREIGN KEY
非空：NOT NULL
```
- 创建表时用约束类型结果在插入时有影响
- 约束像规定，创建时怎么规定的，插入不符合规定则有不同的结果

# 实例

```
进入桌面目录
cd Desktop
从github克隆下需要的数据
git clone htttps://github.com/shiyanlou/SQL3
打开MySQL服务
sudo service mysql start
使用root用户登录
mysql -u root
加载git克隆后数据库包中数据
service /home/shiyanlou/Desktop/SQL3/MySQL-03-01.sql
查看一下这个库里的表
show tables;
```
# 注意
```
(PRIMARY KEY)主键是用来约束表中的一行，作为这一行的标识符，在一张表中通过主键就能准确定到一行，主键不能重复且不能为空。主键名自定义，标识有多种方式，可以放在数据类型后或者
CONSTRAINT [主键名] PRIMARY KE(表内变量)

以下约束类型都只能用在INSERT语句上

(DEFAULT)默认值当有DEFAULT约束的列，插入数据为空时,将使用默认值.

(UNIQUE)唯一约束规定一张表中的一列必须不能有重复值.

(FOREIGN KEY)外键既能确保数据库完整性,也能表现之间的关系.
一个表可以有多个外键,每个外键必须(参考)另一个表的主键,被约束的列,取值必须在他参考的列中有对应值.
建表时
CONSTRAINT [外键名] FOREIGN KEY(外键)REFERENCES [表](这个表中的主键列名)

非空约束
顾名思义建表时被约束的列在插入时必须非空.
在MySQL中违反非空约束不会报错,只有警告.表中显示为0.
```
