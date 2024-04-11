#!/usr/bin/python3
""" do pack module """
from datetime import datetime
from fabric.api import local


def do_pack():
    """ do pack module """
    try:
        local(f"mkdir -p versions")
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = f"web_static_{now}.tgz"
        local(f"tar -czvf versions/{file_name} web_static")
        return "versions/{file_name}"
    except Exception as e:
        return None
