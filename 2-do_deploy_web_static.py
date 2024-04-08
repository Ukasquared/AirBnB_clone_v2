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
        if not path.exists(archive_path):
            return False
        # upload archive to remote directory
        put(archive_path, "/tmp/")
        # remove .tgz 
        split_archive = archive_path.split('.')[0][9:]
        # create dir to compress the archive
        remote_directory_two = f'/data/web_static/releases/{split_archive}/'
        print(remote_directory_two)
        # create another dir in remote server
        run(f"sudo mkdir -p {remote_directory_two}")
        # uncompress the file into folder
        remote = f"/tmp/{split_archive}.tgz"
        print (remote)
        run(f"sudo tar -xvzf {remote} -C {remote_directory_two}")
        # remove the prev archive location
        run(f"sudo rm {remote}")
        # move the file into the remote_directory_two
        run(f"sudo mv {remote_directory_two}web_static/* {remote_directory_two}") 
        # remove prev symbolic link and direct to new sym link
        run(f"sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {remote_directory_two} /data/web_static/current")
        return True
    except Exception as e:
        print(e)
        return False
