#!/usr/bin/env  python
#coding:utf-8
import  os
import commands
import sys
import  re
import fileinput
import  zipfile
import user_conf
import socket, fcntl, struct


net='eth0'
#net='eno16777736'

class public:
      def __init__(self):
          pass

      def shell(self,cmd):
          status,result=commands.getstatusoutput(cmd)
          return [status,result]

      def get_local_ip(self,ifname=net):
          s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          inet = fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s', ifname[:15]))
          ret = socket.inet_ntoa(inet[20:24])
          hostname = socket.gethostname()
          return [ret,hostname]

      def config_file(self,path,oldtext,newtext):
          for line in fileinput.input(path,inplace=1):
              print   re.sub(oldtext,newtext,line),
          fileinput.close()

      def unzip(self,path,target_path):
          r = zipfile.is_zipfile(path)
          if r:
             fz = zipfile.ZipFile(path,'r')
             for file in fz.namelist():
             #print(file)  #打印zip归档中目录
                 fz.extract(file,target_path)
          else:
             print 'This file is not zip file'
      def str_code(self):          
          if re.findall('zh_CN',env_info) and re.findall('UTF-8',env_info):
             print  'check   env_utf8            \033[32m[OK]\033[0m.'
          else:
             with open('/etc/profile') as f_env:
                  open('/etc/profile', 'a').write('export LANG=zh_CN.UTF-8\n')
                  print  'install   env_utf8          \033[32m[OK]\033[0m.'
      def __del__(self):
           pass

class dmb_terminal(public):
      def __init__(self):
          public.__init__(self)
      def config(self):
          if os.path.exists('/data/agent/'):
             print  'check   /data/agent         \033[32m[OK]\033[0m.'
          else:
             os.makedirs('/data/agent/')
             agent_zip='/tmp/ESCAgent.zip'
             self.unzip(agent_zip ,'/data/agent')
             print  'install   escagent          \033[32m[OK]\033[0m.'
          IP=self.get_local_ip()[0]
          HOSTNAME=self.get_local_ip()[1]
          hosts='%s        %s\n' % (IP,HOSTNAME)
          host_file=file('/etc/hosts')
          host_info=host_file.read()
          host_file.close()

          if re.findall(IP,host_info) and re.findall(HOSTNAME,host_info):
             print  'check   hosts               \033[32m[OK]\033[0m.'
          else:
             self.shell('chmod a+w /etc/hosts')
             with open('/etc/hosts') as f_host:
                  lines = f_host.readlines()
                  lines[0:0] = [hosts]
                  open('/etc/hosts', 'w').writelines(lines)
                  print  'install   hosts             \033[32m[OK]\033[0m.'

          env_file=file('/etc/profile','r')
          env_info=env_file.read()
          env_file.close()

          if re.findall('zh_CN',env_info) and re.findall('UTF-8',env_info):
             print  'check   env_utf8            \033[32m[OK]\033[0m.'
          else:
             with open('/etc/profile') as f_env:
                  open('/etc/profile', 'a').write('export LANG=zh_CN.UTF-8\n')
                  print  'install   env_utf8          \033[32m[OK]\033[0m.'


          cron_file=file('/etc/crontab')
          cron_info=cron_file.read()
          cron_file.close()

          if re.findall('agentDaemon',cron_info):
             print  'check   cron_agent          \033[32m[OK]\033[0m.'
          else:
             with open('/etc/crontab') as f_cron:
                  open('/etc/crontab', 'a').write('* * * * * app sh /data/agent/ESCAgent/tools/agentDaemon.sh\n')
                  print  'install   cron_agent        \033[32m[OK]\033[0m.'
          #install_mom
          if os.path.exists('/data/agent/SmartMOM'):
             print  'check   /data/agent/SmartMOM             \033[32m[OK]\033[0m.'
          else:
             mom_zip='/tmp/SmartMOM.zip'
             self.unzip(mom_zip ,'/data/agent/')
             print  'install   MOM               \033[32m[OK]\033[0m.'


          #install_terminal
          if os.path.exists('/data/agent/ESCTerminal'):
             print  'check   /data/agent/ESCTerminal          \033[32m[OK]\033[0m.'
          else:
             terminal_zip='/tmp/ESCTerminal.zip'
             self.unzip(terminal_zip ,'/data/agent/')
             print  'install   ESCTerminal       \033[32m[OK]\033[0m.'

          self.shell('chown app.app  /data/agent/  -R')
          self.shell('chmod  755  /data/agent/  -R')
      def modify(self):
          IP=self.get_local_ip()[0]
          conf_dict=user_conf.info.get(IP)
          a=conf_dict.get('terminal_id')
          b=conf_dict.get('IDC')
          c=conf_dict.get('zook_url')
          d=conf_dict.get('dfa')
          e=conf_dict.get('monitor_ip')
          f=conf_dict.get('monitor_log_ip')
          g=conf_dict.get('monitor_flow_ip')
          h=conf_dict.get('journal_ip')

          self.config_file(user_conf.app_config_file,r'esc.terminal.id=.*','esc.terminal.id=%s' % a )
          self.config_file(user_conf.app_config_file,r'esc.terminal.idc=.*','esc.terminal.idc=%s' % b )
          self.config_file(user_conf.app_config_file,r'esc.zookeeper.urls=.*','esc.zookeeper.urls=%s' % c)
          self.config_file(user_conf.app_config_file,r'esc.terminal.dfa=.*','esc.terminal.dfa=%s' % d )
          self.config_file(user_conf.app_config_file,r'esc.agent.monitor.resource.address=.*','esc.agent.monitor.resource.address=%s:6672' % e )
          #self.config_file(user_conf.app_config_file,r'esc.agent.monitor.log.address=.*','esc.agent.monitor.log.address=%s:6673' %  f)
          #self.config_file(user_conf.app_config_file,r'esc.agent.monitor.flow.address=.*','esc.agent.monitor.flow.address=%s:6674' % g )
          self.config_file(user_conf.app_config_file,r'esc.agent.monitor.log.address=.*','esc.agent.monitor.log.address=%s' %  f)
          self.config_file(user_conf.app_config_file,r'esc.agent.monitor.flow.address=.*','esc.agent.monitor.flow.address=%s' % g )
          self.config_file(user_conf.app_config_file,r'journallog.process.socketip=.*','journallog.process.socketip=%s' % h )
          self.config_file(user_conf.app_config_file,r'esc.terminal.ip=.*','esc.terminal.ip=%s' % IP )
          self.shell('chown app.app  /data/agent/  -R')
      def __del__(self): 
          print  'install   EscAgent          \033[32m[OK]\033[0m.'



class dmb_gov(public):
      def __init__(self):
          public.__init__(self)
      def config(self):
          env_file=file('/etc/profile','r')
          env_info=env_file.read()
          env_file.close()

          if re.findall('zh_CN',env_info) and re.findall('UTF-8',env_info):
             print  'check   env_utf8            \033[32m[OK]\033[0m.'
          else:
             with open('/etc/profile') as f_env:
                  open('/etc/profile', 'a').write('export LANG=zh_CN.UTF-8\n')
                  print  'install   env_utf8          \033[32m[OK]\033[0m.'

          if os.path.exists('/data/app'):
             print  'check   /data/app                   \033[32m[OK]\033[0m.'
          else:
             os.mkdir('/data/app')
          if os.path.exists('/data/app/ESCGovern'):
             print  'check   /data/app/ESCGovern        \033[32m[OK]\033[0m.'
          else:
             ESCGovern_zip='/tmp/ESCGovern.zip' 
             self.unzip(ESCGovern_zip ,'/data/app') 
             print  'install   ESCGovern       \033[32m[OK]\033[0m.'

          if os.path.exists('/data/app/GOVManager'):
             print  'check   /data/app/GOVManager       \033[32m[OK]\033[0m.'
          else:
             GOVManager_zip='/tmp/GOVManager.zip' 
             self.unzip(GOVManager_zip ,'/data/app') 
             print  'install   GOVManager       \033[32m[OK]\033[0m.'

          self.shell('chown app.app  /data/app/  -R  ')
          self.shell('chmod -R 755 /data/app/')

      def modify(self):
          IP=self.get_local_ip()[0]
          conf_dict=user_conf.info.get(IP)
          a=conf_dict.get('sql_host')
          b=conf_dict.get('sql_port')
          c=conf_dict.get('sql_username')
          d=conf_dict.get('sql_password')

          self.config_file(user_conf.app_config_file,r'jdbc.url=.*','jdbc.url=jdbc:mysql://%s:%s/esgdb?useUnicode=true&characterEncoding=UTF-8' % (a,b) )
          self.config_file(user_conf.app_config_file,r'jdbc.username=.*','jdbc.username=%s' % c )
          self.config_file(user_conf.app_config_file,r'jdbc.password=.*','jdbc.password=%s' % d )

          self.shell('chown app.app  /data/app/  -R  ')
          
      def __del__(self): 
          print  'install   gov               \033[32m[OK]\033[0m.'

class dmb_reg(public):
      def __init__(self):
          public.__init__(self)
      def config(self):
          env_file=file('/etc/profile','r')
          env_info=env_file.read()
          env_file.close()

          if re.findall('zh_CN',env_info) and re.findall('UTF-8',env_info):
             print  'check   env_utf8            \033[32m[OK]\033[0m.'
          else:
             with open('/etc/profile') as f_env:
                  open('/etc/profile', 'a').write('export LANG=zh_CN.UTF-8\n')
                  print  'install   env_utf8          \033[32m[OK]\033[0m.'

          if os.path.exists('/data/app'):
             print  'check   /data/app                   \033[32m[OK]\033[0m.'
          else:
             os.mkdir('/data/app')

          if os.path.exists('/data/app/ESCManager'):
             print  'check   /data/app/ESCManager        \033[32m[OK]\033[0m.'
          else:
             esc_manager_zip='/tmp/ESCManager.zip' 
             self.unzip(esc_manager_zip ,'/data/app') 
             print  'install   ESCManager        \033[32m[OK]\033[0m.'

          if os.path.exists('/data/app/ESCConsole'):
             print  'check   /data/app/ESCConsole        \033[32m[OK]\033[0m.'
          else:
             ESCConsole_zip='/tmp/ESCConsole.zip' 
             self.unzip(ESCConsole_zip ,'/data/app') 
             print  'install   ESCConsole        \033[32m[OK]\033[0m.'

          self.shell('chown app.app  /data/app/  -R ')
          self.shell('chmod -R 755 /data/app/')
      def modify(self):
          IP=self.get_local_ip()[0]
          conf_dict=user_conf.info.get(IP)
          a=conf_dict.get('sql_host')
          b=conf_dict.get('sql_port')
          c=conf_dict.get('sql_username')
          d=conf_dict.get('sql_password')

          self.config_file(user_conf.app_config_file,r'jdbc.url=.*','jdbc.url=jdbc:mysql://%s:%s/escdb?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true&failOverReadOnly=false' % (a,b) )
          self.config_file(user_conf.app_config_file,r'jdbc.username=.*','jdbc.username=%s' % c )
          self.config_file(user_conf.app_config_file,r'jdbc.password=.*','jdbc.password=%s' % d )

          self.shell('chown app.app  /data/app/  -R ')
      def __del__(self): 
          print  'install   reg               \033[32m[OK]\033[0m.'


class dmb_monitor(public):
      def __init__(self):
          public.__init__(self)
      def config(self):
          env_file=file('/etc/profile','r')
          env_info=env_file.read()
          env_file.close()

          if re.findall('zh_CN',env_info) and re.findall('UTF-8',env_info):
             print  'check   env_utf8            \033[32m[OK]\033[0m.'
          else:
             with open('/etc/profile') as f_env:
                  open('/etc/profile', 'a').write('export LANG=zh_CN.UTF-8\n')
                  print  'install   env_utf8          \033[32m[OK]\033[0m.'

          if os.path.exists('/data/app'):
             print  'check   /data/app                   \033[32m[OK]\033[0m.'
          else:
             os.mkdir('/data/app')

          if os.path.exists('/data/app/ESCMonitor'):
             print  'check   /data/app/ESCMonitor        \033[32m[OK]\033[0m.'
          else:
             ESCMonitor_zip='/tmp/ESCMonitor.zip' 
             self.unzip(ESCMonitor_zip ,'/data/app') 
             print  'install   ESCMonitor                \033[32m[OK]\033[0m.'
          self.shell('chown app.app  /data/app/  -R ')
          self.shell('chmod -R 755 /data/app/')

      def modify(self):
          IP=self.get_local_ip()[0]
          conf_dict=user_conf.info.get(IP)
          a=conf_dict.get('jmx_ip')
          b=conf_dict.get('primeserver_ip')
          c=conf_dict.get('backserver_ip')
          d=conf_dict.get('sql_host')
          e=conf_dict.get('sql_port')
          f=conf_dict.get('sql_username')
          g=conf_dict.get('sql_password')
          h=conf_dict.get('hive_url')
          i=conf_dict.get('hive_user')
          j=conf_dict.get('hive_pass')
          k=conf_dict.get('hive_table')
          l=conf_dict.get('kafka_data_topic')
          m=conf_dict.get('kafka_data_user')
          n=conf_dict.get('kafka_data_keytab')
          o=conf_dict.get('kafka_data_zooker')
          p=conf_dict.get('kafka_msg_topic')
          q=conf_dict.get('kafka_msg_user')
          r=conf_dict.get('kafka_msg_keytab')
          s=conf_dict.get('kafka_msg_zooker')


          self.config_file(user_conf.app_config_file,r'^ip.*','ip=%s' % a )
          self.config_file(user_conf.app_config_file,r'^primeserver.ip.*','primeserver.ip=%s' % b )
          self.config_file(user_conf.app_config_file,r'^backserver.ip.*','backserver.ip=%s' % c )

          self.config_file(user_conf.app_config_file1,r'<prop name="db.jdbc.url">.*','<prop name="db.jdbc.url">jdbc:mysql://%s:%s/escdb</prop>' % (d,e) )
          self.config_file(user_conf.app_config_file1,r'<prop name="db.jdbc.user">.*','<prop name="db.jdbc.user">%s</prop>' % f )
          self.config_file(user_conf.app_config_file1,r'<prop name="db.jdbc.password">.*','<prop name="db.jdbc.password">%s</prop>' % g )

          self.config_file(user_conf.app_config_file2,r'hive.connectionUrl=.*','hive.connectionUrl=%s' % h )
          self.config_file(user_conf.app_config_file2,r'hive.user=.*','hive.user=%s' % i )
          self.config_file(user_conf.app_config_file2,r'hive.password=.*','hive.password=%s' % j )
          self.config_file(user_conf.app_config_file2,r'hive.table=.*','hive.table=%s' % k )
          self.config_file(user_conf.app_config_file2,r'kafka.data.topic=.*','kafka.data.topic=%s' % l )
          self.config_file(user_conf.app_config_file2,r'kafka.data.user=.*','kafka.data.user=%s' % m )
          self.config_file(user_conf.app_config_file2,r'kafka.data.keytab=.*','kafka.data.keytab=%s' % n )
          self.config_file(user_conf.app_config_file2,r'kafka.data.zookeeper.connect=.*','kafka.data.zookeeper.connect=%s' % o )
          self.config_file(user_conf.app_config_file2,r'kafka.msg.topic=.*','kafka.msg.topic=%s' % p )
          self.config_file(user_conf.app_config_file2,r'kafka.msg.user=.*','kafka.msg.user=%s' % q )
          self.config_file(user_conf.app_config_file2,r'kafka.msg.keytab=.*','kafka.msg.keytab=%s' % r )
          self.config_file(user_conf.app_config_file2,r'kafka.msg.zookeeper.connect=.*','kafka.msg.zookeeper.connect=%s' % s )

          self.shell('chown app.app  /data/app/  -R ')

      def __del__(self): 
          print  'install   monitor           \033[32m[OK]\033[0m.'


class dmb_journal(public):
      def __init__(self):
          public.__init__(self)
      def config(self):
          env_file=file('/etc/profile','r')
          env_info=env_file.read()
          env_file.close()

          if re.findall('zh_CN',env_info) and re.findall('UTF-8',env_info):
             print  'check   env_utf8            \033[32m[OK]\033[0m.'
          else:
             with open('/etc/profile') as f_env:
                  open('/etc/profile', 'a').write('export LANG=zh_CN.UTF-8\n')
                  print  'install   env_utf8          \033[32m[OK]\033[0m.'

          if os.path.exists('/data/app'):
             print  'check   /data/app                   \033[32m[OK]\033[0m.'
          else:
             os.mkdir('/data/app')

          if os.path.exists('/data/app/ESCJournal'):
             print  'check   /data/app/ESCJournal        \033[32m[OK]\033[0m.'
          else:
             ESCJournal_zip='/tmp/ESCJournal.zip' 
             self.unzip(ESCJournal_zip ,'/data/app') 
             print  'install   ESCJournal        \033[32m[OK]\033[0m.'

          self.shell('chown app.app  /data/app/ -R ')
          self.shell('chmod -R 755 /data/app/')

      def modify(self):
          IP=self.get_local_ip()[0]
          conf_dict=user_conf.info.get(IP)

          a=conf_dict.get('kafka_topic')
          b=conf_dict.get('kafka_brokers')
          c=conf_dict.get('kafka_user')
          d=conf_dict.get('kafka_keytab')

          self.config_file(user_conf.app_config_file,r'kafka.topic=.*','kafka.topic=%s' % a )
          self.config_file(user_conf.app_config_file,r'kafka.brokers=.*','kafka.brokers=%s' % b )
          self.config_file(user_conf.app_config_file,r'kafka.user=.*','kafka.user=%s' % c )
          self.config_file(user_conf.app_config_file,r'kafka.keytab=.*','kafka.keytab=%s' % d )
   
          self.shell('chown app.app  /data/app/ -R ')
      def __del__(self): 
          print  'install   journal           \033[32m[OK]\033[0m.'



if user_conf.install_env == 'dmb_agent':
    agent=dmb_terminal()
    agent.config()
    agent.modify()
elif user_conf.install_env == 'dmb_gov':
    gov=dmb_gov()
    gov.config()
    gov.modify()
elif user_conf.install_env == 'dmb_reg':
    reg=dmb_reg()
    reg.config()
    reg.modify()
elif user_conf.install_env == 'dmb_monitor':
    monitor=dmb_monitor()
    monitor.config()
    monitor.modify()
elif user_conf.install_env == 'dmb_journal':
    journal=dmb_journal()
    journal.config()
    journal.modify()
else:
   print  'nothing to do'
