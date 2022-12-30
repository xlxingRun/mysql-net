# 向MySQL数据库中插入数据演示

## 介绍

一个简单的python脚本，可以向指定的MySQL数据库中插入数据，支持的参数包括
- host: 主机名，IP地址
- user: 登录mysql数据库用户名
- password: 登录mysql数据库密码
- database: 创建的数据库名
- table: 创建的表名
- data_nums: 想要插入数据库中的数据数量，默认值为30
- sleep_interval: 插入数据的时间间隔，默认值为1，单位为秒

默认地，该脚本会创建数据库**grafana**，在该数据库中创建表**NetStatic**

创建的数据库表头如下：

| id(primary key) | time        | throughput | rtt  | segment |
| --------------- | ----------- | ---------- | ---- | ------- |
| 自增            | Y-m-d H:M:S | float      | int  | int     |

## 快速开始
> 使用anaconda创建python环境（可选），并进入该环境

```shell
conda create -n pymysql python=3.8
```

```
conda activate pymysql
```

> 安装环境所需要的库

```
pip install -r requirement
```

> 生成10条数据，时间间隔为1s

```shell
python main.py --data_nums 10 --sleep_interval 1
```

![terminal](figs/terminal.png)

<img src="figs/mysql-client.png" alt="mysql-client" style="zoom:67%;" />

