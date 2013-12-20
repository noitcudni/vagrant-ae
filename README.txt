1) Install virtualbox 4.2.16
2) Install vagrant 1.3.5
http://downloads.vagrantup.com/tags/v1.3.5
3) Install ansible (on your host machine. More specically, OSX)
-- Install Xcode
-- sudo easy_install pip
-- sudo pip install ansible
4) Clone this repo
5) Boot it up
-- cd vagrant_ae
-- vagrant up

FAQ:
1) I ran into the following error when I try to do 'vagrant up'.
[default] Clearing any previously set network interfaces...
There was an error while executing `VBoxManage`, a CLI used by Vagrant
for controlling VirtualBox. The command and stderr is shown below.

  Command: ["hostonlyif", "create"]

Chances are that you are on a Mac. Run the the following command on your
host machine and do 'vagrant up' again.
-- sudo /Library/StartupItems/VirtualBox/VirtualBox restart
