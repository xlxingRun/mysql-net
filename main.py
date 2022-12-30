# -*- coding: utf-8 -*-
import argparse
from email.policy import default

# *************************************************
# @Time         : 2022/12/26 11:13
# @Author       : Xiaolin Xing
# @Site         : Beijing
# @File         : main.py
# @Software:    : PyCharm
# Description   : connection with MySQL-docker server using python
# *************************************************
from MysqlUtils import MysqldbHelper


def args_parser():
    parser = argparse.ArgumentParser(description='Insert data into MySQL database')

    parser.add_argument('--host', type=str, default='localhost',
                        help='the host to connect (IP address)')
    parser.add_argument('--user', type=str, default='root',
                        help='login in MySQL: user')
    parser.add_argument('--password', type=str, default='123456',
                        help='login in MySQL: password')
    parser.add_argument('--database', type=str, default='grafana',
                        help='database name')
    parser.add_argument('--table', type=str, default='NetStatic',
                        help='table name')
    parser.add_argument('--data_nums', type=int, default=30,
                        help='The number of data to insert into table of MySQL database')
    parser.add_argument('--sleep_interval', type=int, default=1,
                        help='Interval(Second) at which data is inserted')
    _args = parser.parse_args()
    return _args


def main():
    args = args_parser()
    host = args.host
    user = args.user
    password = args.password
    database = args.database
    table = args.table

    data_nums = args.data_nums
    sleep_interval = args.sleep_interval

    sql_util = MysqldbHelper(host, user, password, database)
    sql_util.createDatabase(database)
    sql_util.createTable(database, table)
    sql_util.insertData(database, table, data_nums, sleep_interval)


if __name__ == '__main__':
    main()

