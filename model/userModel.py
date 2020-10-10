from model.db import DB
import json


def login(account, password):
    sqlstr = "select * from user where id=\"%s\" and password = \"%s\"" % (
        account, password)
    return (DB.execution(DB.select, sqlstr))


def findPasswordByAccount(account):
    sqlstr = "select password from user where id=\"%s\"" % account
    return DB.execution(DB.select, sqlstr)


def changePassword(account, password):
    sqlstr = "update user password=\"%s\" where id=\"%s\"" % (
        password, account)
    return DB.execution(DB.update, sqlstr)


def sign(account, password, age, sex, area):
    sqlstr = "insert into user(id, password,age,sex,area) VALUES (%s, %s ,%s ,%s,%s)" % (
        account, password, age, sex, area)
    return DB.execution(DB.create, sqlstr)


def changeProfile(data, account):
    strCond = ""
    if(isinstance(data, dict)):
        for i in data.keys():
            strCond += " %s = \"%s\" and" % (i, data[i])
    
    sqlstr = "update user set %s where id=\"%s\"" % (
        strCond[0:len(strCond)-3], account)
    print(sqlstr)
    return DB.execution(DB.update, sqlstr)


def findArea(area):
    sqlstr = "select * from area "
    return DB.execution(DB.select, sqlstr)


def findUserarea(area):
    sqlstr = "select area from user where id = \"%s\"" % (
        area)
    return DB.execution(DB.select, sqlstr)