# -*- coding: utf-8 -*-
import datetime
import random
import time

# *************************************************
# @Time         : 2022/12/26 11:35
# @Author       : Xiaolin Xing
# @Site         : Beijing
# @File         : MysqlUtils.py
# @Software:    : PyCharm
# Description   : basic CRUD api based on pymysql
# *************************************************


# -*- coding: utf-8 -*-
import pymysql


class MysqldbHelper:
    """

    """
    def __init__(self, host='localhost', user='root', password='123456', database=None, charset='utf8'):
        """

        :param host: localhost
        :param user: root
        :param password: 123456
        :param database: grafana
        :param charset: utf8
        """
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset
        )
        self.cursor = self.db.cursor()

    def databaseExists(self, database):
        databases = self.getDatabases()
        if database in databases:
            return True
        else:
            return False

    def tableExists(self, database, table):
        if self.databaseExists(database):
            tables = self.getTables(database)
            if table in tables:
                return True

        return False

    def createDatabase(self, database):
        """
        创建数据库
        检查数据库是否存在：
        - 存在 TODO: 是否删除，供用户选择
        - 不存在，创建
        :param database:
        :return:
        """
        if self.databaseExists(database):
            print('{} already exists.'.format(database))
        else:
            _sql = f'create database {database}'
            self.cursor.execute(_sql)
            print(f'create database {database} done.')

    def getDatabases(self):
        self.cursor.execute('show databases')
        res = self.cursor.fetchall()
        databases = []
        for row in res:
            databases.append(row[0])
        return databases

    def getTables(self, database):
        self.cursor.execute('show tables')
        res = self.cursor.fetchall()
        tables = []
        for row in res:
            tables.append(row[0])
        return tables

    def createTable(self, database, table):
        if not self.databaseExists(database):
            print(f"database {database} doesn't exist.")
        else:
            # use database;
            self.cursor.execute(f'use {database}')
            if self.tableExists(database, table):
                print(f"table {table} already exists.")
            else:
                _sql = f'create table {table}(id int primary key auto_increment, time datetime, throughput FLOAT, rtt INT, segment INT)'
                self.cursor.execute(_sql)
                self.db.commit()
                print(f'create table {table} done.')

    def insertData(self, database, table, data_num=30, sleep=0):
        self.cursor.execute(f'use {database}')
        for i in range(data_num):
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            _throughput = round(10.0 + random.random(), 2)
            _rtt = 20 + random.randint(0, 30)
            _segment = 1300 + random.randint(50, 150)
            _sql = 'insert into %s' \
                   '(time, throughput, rtt, segment) values ("%s", %f, %d, %d)' % (table, now, _throughput, _rtt, _segment)

            print(_sql)
            self.cursor.execute(_sql)
            self.db.commit()
            time.sleep(sleep)
