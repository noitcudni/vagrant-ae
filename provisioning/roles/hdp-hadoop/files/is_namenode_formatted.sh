#!/bin/sh

source /vagrant/files/hortonworks_env/directories.sh;
source /vagrant/files/hortonworks_env/usersAndGroups.sh;

if [ -e $DFS_NAME_DIR/current/VERSION ]; then
  exit 1 # formatted
else
  exit 0 # not formatted
fi
