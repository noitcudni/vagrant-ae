#!/usr/bin/python

import argparse
import sys
import re

todo_regex = re.compile(r"TODO-(.*?)<")

def read_in_env_file(file_path):
    r = {}
    f = open(file_path, 'r')
    for line in f:
        if line.find("=") != -1 and line.strip()[0] != '#':
            line = line[:line.find(";")]
            line = line.strip()
            key, val = line.split("=")
            r[key] = val
    return r

def fill_in_param_info(conf_dir, conf_file, kv_dict, hostname_dict):
    full_path = "%s/%s" % (conf_dir, conf_file)
    #print full_path
    f = open(full_path, "r")
    buf = []
    for line in f:
        transformed_line = line
        regex_r = todo_regex.search(line)
        if regex_r:
            to_be_replaced = regex_r.group(1)
            if to_be_replaced.find('HOSTNAME') == -1:
                # use kv_dict for substitution
                key = to_be_replaced.replace("-", "_")
                value = kv_dict[key][1:-1]
                transformed_line = todo_regex.sub(value + "<", line)
                print transformed_line
            else:
                # dealing with hostname
                host_comp = to_be_replaced.split(":")
                hostname = hostname_dict[host_comp[0]]

                if len(host_comp) == 2:
                    port = host_comp[1]
                else:
                    if to_be_replaced == "NAMENODE-HOSTNAME":
                        # the template core-site.xml file from hortonworks is missing the port num.
                        port = '8020'

                transformed_line = todo_regex.sub('hdfs://%s:%s<' % (hostname, port) ,line)
                print transformed_line

        buf.append(transformed_line)
    f.close()

    xml_str = "".join(buf)
    write_f = open(full_path, "w")
    write_f.write(xml_str)
    write_f.close()


def construct_hostname_dict(args):
    r = {
            'NAMENODE-HOSTNAME' : args.namenode,
            'SECONDARYNAMENODE-HOSTNAME' : args.snamenode,
            'RMNODE-HOSTNAME' : args.rmnode,
            'JOBHISTORYNODE-HOSTNAME' : args.jobhistory,
            }
    return r


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="fill in your hadoop parameter for you")
    parser.add_argument('--namenode', required=True, dest='namenode')
    parser.add_argument('--secondarynamenode', required=True, dest='snamenode')
    parser.add_argument('--rmnode', required=True, dest='rmnode')
    parser.add_argument('--jobhistorynode', required=True, dest='jobhistory')
    parser.add_argument('--conf_template_dir', required=True, dest='conf_dir')
    parser.add_argument('--users_and_groups_env', required=True, dest='users_and_groups_env')
    parser.add_argument('--directories_env', required=True, dest='directories_env')
    args = parser.parse_args()

    hdfs_conf_file_lst = ['core_hadoop/core-site.xml', 'core_hadoop/hdfs-site.xml', 'core_hadoop/yarn-site.xml', 'core_hadoop/mapred-site.xml']
    #hdfs_conf_file_lst = ['core_hadoop/core-site.xml', 'core_hadoop/hdfs-site.xml']

    hortonworks_param_dict = {}
    hortonworks_param_dict.update(read_in_env_file(args.users_and_groups_env))
    hortonworks_param_dict.update(read_in_env_file(args.directories_env))

    hostname_dict = construct_hostname_dict(args)

    for conf_f in hdfs_conf_file_lst:
        fill_in_param_info(args.conf_dir, conf_f, hortonworks_param_dict, hostname_dict)

