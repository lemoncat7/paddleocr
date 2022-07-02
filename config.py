
import os
import configparser

from flask import g

g_config_path = './orcconfig.ini'
g_config = {}


def get_config():
    global g_config_path
    global g_config
    if not os.path.exists(g_config_path):
        with open(g_config_path, 'w+') as f:
            f.write(
                '[base]\ntmpdir=C:\Temp\n')
    config = configparser.ConfigParser()
    config.read(g_config_path)
    check_config()
    for section in config.sections():
        for key in config.options(section):
            g_config[key] = config.get(section, key)
    # print(g_config)
    set_env()
    return g_config


def check_config():
    if 'tmpdir' not in g_config.keys():
        g_config['tmpdir'] = '.'

def set_env():
    os.environ['USERPROFILE'] = os.path.join(g_config['tmpdir'], "user")
    os.environ['TMP'] = os.path.join(os.environ['USERPROFILE'], "tmp")
    os.environ['TEMP'] = os.path.join(os.environ['USERPROFILE'], "tmp")
