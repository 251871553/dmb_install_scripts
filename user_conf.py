#!/usr/bin/env  python
#coding:utf-8


#dmb_agent,dmb_gov,dmb_reg,dmb_monitor,dmb_journal
#install_env='dmb_agent'
#install_env='dmb_gov'
#install_env='dmb_reg'
#install_env='dmb_monitor'
install_env='dmb_journal'


####dmb_agent####
agent_install_path='/data/agent'
agent_config_file='%s/ESCAgent/conf/agent.properties' % agent_install_path
agent_info={
'10.10.1.232':{
      'IDC':'E',
      'terminal_id':'10.10.10.10',
      'zook_url':'10.0.100.161:2181,10.0.100.161:2182,10.0.100.161:2183',
      'dfa':'HM',
      'monitor_ip':'10.10.1.13',
      'monitor_log_ip':'10.10.10.11',
      'monitor_flow_ip':'10.10.10.12',
      'journal_ip':'8.8.8.8'   } ,

'10.10.2.5':{ 
      'terminal_id':'HM001',
      'IDC':'E',
      'zook_url':'10.0.100.161:2181,10.0.100.161:2182,10.0.100.161:2183',
      'dfa':'HM', 
      'monitor_ip':'10.10.1.13',
      'monitor_log_ip':'10.10.10.11',
      'monitor_flow_ip':'10.10.10.12',
      'journal_ip':'8.8.8.8'   } ,

 }

####dmb_gov###

gov_install_path='/data/app'
gov_config_file='%s/ESCGovern/WEB-INF/classes/config/jdbc.properties' % gov_install_path

gov_info={
'10.10.1.232':{
    'sql_host':'192.168.10.10',
    'sql_port':'3306',
    'sql_username':'esc',
    'sql_password':'esc',
             } ,

'10.10.2.5':{ 
    'sql_host':'192.168.10.10',
    'sql_port':'3306',
    'sql_username':'esc',
    'sql_password':'esc',
               } ,

 }


#####dmb_reg###
reg_install_path='/data/app'
reg_config_file='%s/ESCConsole/WEB-INF/classes/jdbc.properties' % reg_install_path

reg_info={
'10.10.1.232':{
    'sql_host':'192.168.10.10',
    'sql_port':'3306',
    'sql_username':'esc',
    'sql_password':'esc',
             } ,

'10.10.2.5':{ 
    'sql_host':'192.168.10.10',
    'sql_port':'3306',
    'sql_username':'esc',
    'sql_password':'esc',
               } ,


 }

#####dmb_monitor####
monitor_install_path='/data/app'
monitor_config_file1='%s/ESCMonitor/webapps/EscMonitor/configs/conf/config.properties' % monitor_install_path
monitor_config_file2='%s/ESCMonitor/webapps/EscMonitor/configs/dbconfig/conf/provider.xml' % monitor_install_path
monitor_config_file3='%s/ESCMonitor/webapps/EscMonitor/configs/dbconfig/conf/hive.properties' % monitor_install_path

monitor_info={
'10.10.1.232':{
    'sql_host':'192.168.10.10',
    'sql_port':'3306',
    'sql_username':'esc',
    'sql_password':'esc' ,
    'jmx_ip':'192.168.10.10'  ,
    'primeserver_ip':'8.8.8.8',
    'backserver_ip':'8.8.8,8',
    'hive_url':'jdbc:hive2://VM-232-137-centos:10000/escdb',
    'hive_user':'esc',
    'hive_pass':'haha',
    'hive_table':'t_haha',
    'kafka_data_topic':'in',
    'kafka_data_user':'kafka',
    'kafka_data_keytab':'hehe',
    'kafka_data_zooker':'host1:1001,host2:1002',
    'kafka_msg_topic':'in',
    'kafka_msg_user':'kafka',
    'kafka_msg_keytab':'hehe',
    'kafka_msg_zooker':'host1:1001,host2:1002',
     
              },

'10.10.2.5':{ 
    'sql_host':'192.168.10.10',
    'sql_port':'3306',
    'sql_username':'esc',
    'sql_password':'esc' ,
    'jmx_ip':'192.168.10.10',
    'primeserver_ip':'8.8.8.8',
    'backserver_ip':'8.8.8,8',
    'hive_url':'jdbc:hive2://VM-232-137-centos:10000/escdb',
    'hive_user':'esc',
    'hive_pass':'haha',
    'hive_table':'t_haha',
    'kafka_data_topic':'in',
    'kafka_data_user':'kafka',
    'kafka_data_keytab':'hehe',
    'kafka_data_zooker':'host1:1001,host2:1002',
    'kafka_msg_topic':'in',
    'kafka_msg_user':'kafka',
    'kafka_msg_keytab':'hehe',
    'kafka_msg_zooker':'host1:1001,host2:1002',
               } ,

 }

#####dmb_journal#####
journal_install_path='/data/app'
journal_config_file='%s/ESCJournal/conf/config.properties' % journal_install_path

journal_info={
'10.10.1.232':{
    'kafka_topic':'192.168.10.10',
    'kafka_brokers':'VM-252-84-centos:9092,VM-232-137-centos:9092,VM-251-49-centos:9092,VM-249-233-centos:9092',
    'kafka_user':'esc',
    'kafka_keytab':'../conf/kafka.keytab',
             } ,

'10.10.2.5':{ 
    'kafka_topic':'192.168.10.10',
    'kafka_brokers':'VM-252-84-centos:9092,VM-232-137-centos:9092,VM-251-49-centos:9092,VM-249-233-centos:9092',
    'kafka_user':'esc',
    'kafka_keytab':'../conf/kafka.keytab',
               } ,


 }


#####main#####
if install_env=='dmb_agent':
   app_config_file=agent_config_file
   info=agent_info
elif install_env=='dmb_gov':
   app_config_file=gov_config_file
   info=gov_info
elif install_env=='dmb_reg':
   app_config_file=reg_config_file
   info=reg_info
elif install_env=='dmb_monitor':
   app_config_file=monitor_config_file1
   app_config_file1=monitor_config_file2
   app_config_file2=monitor_config_file3
   info=monitor_info
elif install_env=='dmb_journal':
   app_config_file=journal_config_file
   info=journal_info
else:
   pass
#print  app_install_file,app_info
