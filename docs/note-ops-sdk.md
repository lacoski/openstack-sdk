# Config Files
openstacksdk will look for a file called clouds.yaml in the following locations:

Current Directory
~/.config/openstack
/etc/openstack

The first file found wins.

# Site Specific File Locations
In addition to ~/.config/openstack and /etc/openstack - some platforms have other locations they like to put things. openstacksdk will also look in an OS specific config dir
- USER_CONFIG_DIR
- SITE_CONFIG_DIR

Set the environment variable OS_CLIENT_CONFIG_FILE to an absolute path of a file to look for and that location will be inserted at the front of the file search list.

## USER_CONFIG_DIR is different on Linux, OSX and Windows.
- Linux: ~/.config/openstack
- OSX: ~/Library/Application Support/openstack
- Windows: C:\Users\USERNAME\AppData\Local\OpenStack\openstack

## SITE_CONFIG_DIR is different on Linux, OSX and Windows.
- Linux: /etc/openstack
- OSX: /Library/Application Support/openstack
- Windows: C:\ProgramData\OpenStack\openstack

# Usage
> Lấy config
```
python3 -m openstack.config.loader
```
