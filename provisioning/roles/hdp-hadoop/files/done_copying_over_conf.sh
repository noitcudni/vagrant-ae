#!/bin/sh
source /vagrant/files/hortonworks_env/directories.sh;
source /vagrant/files/hortonworks_env/usersAndGroups.sh;

if grep -q 'Put site-specific property overrides in this file.' $HADOOP_CONF_DIR/core-site.xml; then
  #echo "no":
  exit 0;
else
  # done
  exit 1;
  #echo "yes";
fi
