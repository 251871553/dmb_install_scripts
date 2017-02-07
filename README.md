# dmb_install_scripts

Environment dependence：python2.6+（python2.7 best），paramiko1.7+（pip install paramiko）

user_conf.py  
用户配置文件
放开注释设置安装脚本环境变量
各个软件差异化配置，例如agent，只需要修改value值

Scp.py
批量传输文件，scp_list中定义需要传输的文件。
Username和password定义远程登陆的用户名和密码，脚本默认将文件传输到远程/tmp目录
Ssh.py
批量远程执行install.py脚本进行部署
Username和password定义远程登陆的用户名和密码
Service.py
远程批量服务起停
Username和password定义远程登陆的用户名和密码
Debug.py
批量远程执行shell命令Username和password定义远程登陆的用户名和密码
