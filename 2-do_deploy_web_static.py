#!/usr/bin/python3
"""distributes an archive to your web servers,
using the function do_deploy """
from fabric.api import local, put, env, run
from os import path

""" establishing connection with th host """
env.hosts = ['web-01.judithsolutions.tech','web-02.judithsolutions.tech']
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"

def do_deploy(archive_path):
    try:
        # path existence
        if not path.exist(archive_path):
            return False
        # upload archive to remote director
        put("{archive_path}, {remote_directory}")
        # remove .tgz 
        split_archive = archive_path.split('.')[0][9:]
        # create dir to compress the archive
        remote_directory_two = f'/data/web_static/releases/{split_archive}'
        # create another dir in remote server
        run("sudo mkdir -p {remote_directory_two}")
        # uncompress the file into folder
        run(f"sudo tar -xzf {remote_directory} -C {remote_directory_two}")
        # remove the prev archive location
        run("sudo rm -r {remote_directory}")
        # remove symbolic link
        run("sudo ln -sf {remote_directory_two} /data/web_static/current")
        return True
    except:
        return False
