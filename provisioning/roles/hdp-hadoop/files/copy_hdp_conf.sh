#!/bin/sh
# run it as root
source /vagrant/files/hortonworks_env/directories.sh;
source /vagrant/files/hortonworks_env/usersAndGroups.sh;

rm -rf $HADOOP_CONF_DIR
mkdir -p $HADOOP_CONF_DIR

chmod a+x $HADOOP_CONF_DIR/
chown -R $HDFS_USER:$HADOOP_GROUP $HADOOP_CONF_DIR/../
chmod -R 755 $HADOOP_CONF_DIR/../

cp -r /home/vagrant/hortonworks_conf/*/* $HADOOP_CONF_DIR/.
rm -rf /home/vagrant/hortonworks_conf
