#!/usr/bin/env  python
#coding:utf-8
import paramiko
import user_conf
import  sys

def  sftp(hostname,localpath,remotepath):
       t = paramiko.Transport((hostname,22))
       t.connect(username = username, password = password)
       sftp = paramiko.SFTPClient.from_transport(t)
       sftp.put(localpath,remotepath)
       t.close()

def  ssh(hostname,remote_cmd):
       ssh = paramiko.SSHClient()
       ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
       ssh.connect(hostname,22,username, password)
      # stdin, stdout, stderr = ssh.exec_command(remote_cmd,get_pty=True)
       stdin, stdout, stderr = ssh.exec_command(remote_cmd)
     #  stdin.write('app\n')
    #   stdin.flush()
       result = stdout.read(),stderr.read()
       ssh.close()
       return result

username='app'
password='app'


try:
   parameter=sys.argv[1]
except Exception,e:
   print 'please input: start | stop | status,for example : python service.py start'
   sys.exit()

def service(cmd):
    for  i in  user_conf.info.keys():
          for k in ssh(i,cmd):
                      print k
         # print  '%s  is  ok'  % i
          print  '\033[32m[%s]\033[0m  is  ok'  % i
    

if user_conf.install_env == 'dmb_agent':
    if parameter == 'start':
       cmd='cd  /data/agent/ESCAgent/tools;source /etc/profile;nohup sh startAgent.sh  >  /dev/null 2>&1 &'
       service(cmd)
    elif parameter == 'stop':
       cmd='cd  /data/agent/ESCAgent/tools;source /etc/profile;nohup sh stopAgent.sh  >  /dev/null 2>&1 &'
       service(cmd)
    elif parameter == 'status':
       cmd='ps  aux  |  grep java |  grep  -v "grep" '
       service(cmd)
    else:
       print  'bad input'
    
elif user_conf.install_env == 'dmb_gov':
    if parameter == 'start':
       cmd='cd  /data/app/GOVManager/bin;source /etc/profile;sh /data/app/GOVManager/bin/startGovern.sh'
       service(cmd)
    elif parameter == 'stop':
       cmd='cd  /data/app/GOVManager/bin;source /etc/profile;sh /data/app/GOVManager/bin/stopGovern.sh'
       service(cmd)
    elif parameter == 'status':
       cmd='ps  aux  |  grep java |  grep  -v "grep" | grep "GOVManager"'
       service(cmd)
    else:
       print  'bad input'
elif user_conf.install_env == 'dmb_reg':
    if parameter == 'start':
       cmd='cd /data/app/ESCManager/bin/;source /etc/profile;sh /data/app/ESCManager/bin/startConsole.sh'
       service(cmd)
    elif parameter == 'stop':
       cmd='cd /data/app/ESCManager/bin/;source /etc/profile;sh /data/app/ESCManager/bin/stopConsole.sh'
       service(cmd)
    elif parameter == 'status':
       cmd='ps  aux  |  grep java |  grep  -v "grep" | grep "ESCManager"'
       service(cmd)
    else:
       print  'bad input'
elif user_conf.install_env == 'dmb_monitor':
    if parameter == 'start':
       cmd='cd  /data/app/ESCMonitor/bin/;source /etc/profile;sh /data/app/ESCMonitor/bin/startMonitor.sh'
       service(cmd)
    elif parameter == 'stop':
       cmd='cd  /data/app/ESCMonitor/bin/;source /etc/profile;sh /data/app/ESCMonitor/bin/stopMonitor.sh'
       service(cmd)
    elif parameter == 'status':
       cmd='ps  aux  |  grep java |  grep  -v "grep" | grep "ESCMonitor"'
       service(cmd)
    else:
       print  'bad input'
elif user_conf.install_env == 'dmb_journal':
    if parameter == 'start':
      # cmd='cd  /data/app/ESCJournal/tools;source /etc/profile;nohup sh /data/app/ESCJournal/tools/startJournal.sh > /dev/null 2>&1 &'
       cmd='cd  /data/app/ESCJournal/tools;source /etc/profile;nohup sh startJournal.sh > /dev/null 2>&1 &'
       service(cmd)
    elif parameter == 'stop':
       cmd='cd  /data/app/ESCJournal/tools;source /etc/profile;nohup sh /data/app/ESCJournal/tools/stopJournal.sh > /dev/null 2>&1 &'
       service(cmd)
    elif parameter == 'status':
       cmd='ps  aux  |  grep java |  grep  -v "grep" | grep "ESCJournal"'
       service(cmd)
    else:
       print  'bad input'
elif user_conf.install_env == 'dmb_zk':
    if parameter == 'start':
       cmd='cd /data/app/ZooKeeper/RegisterCenter/bin;source /etc/profile;sh /data/app/ZooKeeper/RegisterCenter/bin/zkServer.sh start'
      # cmd='cd /data/app/ZooKeeper/RegisterCenter/bin;source /etc/profile;sh /data/app/ZooKeeper/RegisterCenter/bin/zkServer.sh start  >  /dev/null 2>&1 &'
       service(cmd)
    elif parameter == 'stop':
       cmd='cd /data/app/ZooKeeper/RegisterCenter/bin;source /etc/profile;sh /data/app/ZooKeeper/RegisterCenter/bin/zkServer.sh stop '
    #   cmd='cd /data/app/ZooKeeper/RegisterCenter/bin;source /etc/profile;sh /data/app/ZooKeeper/RegisterCenter/bin/zkServer.sh stop  >  /dev/null 2>&1 &'
       service(cmd)
    elif parameter == 'status':
       cmd='ps  aux  |  grep java |  grep  -v "grep" | grep "ZooKeeper"'
       service(cmd)
    else:
       print  'bad input'
else:
   print  'nothing to do'

