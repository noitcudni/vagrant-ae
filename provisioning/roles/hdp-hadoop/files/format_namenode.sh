#!/bin/sh
source /vagrant/files/hortonworks_env/directories.sh;
source /vagrant/files/hortonworks_env/usersAndGroups.sh;
sudo -u $HDFS_USER -H sh -c "/usr/lib/hadoop/bin/hadoop namenode -format"
