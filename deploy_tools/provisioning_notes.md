配置新网站
=========

## 需要安装的包

* nginx
* python 3
* Git
* pip

以 CentOS 为例，可以执行以下命令安装

yum install nginx git python3 python3-pip

## 配置 nginx 虚拟主机

* 参考 nginx.templte.conf
* 把 SITENAME 替换成需要的域名，例如 staging.my-domain.com

## Upstart 任务

* 参考 amy.com.template.conf
* 把 SITENAME 替换成需要的域名，例如 staging.my-domain.com

## 文件夹结构

假设有用户账户，家目录为 /home/username

/home/username
└── sites
    ├── SITENAME
        ├── database
        ├── source
        └── static
