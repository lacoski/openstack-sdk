# Connect
---

## Connect From Config

Default Location
> create a connection from a file you need a YAML file
```
clouds:
  test_cloud:
    region_name: RegionOne
    auth:
      auth_url: http://xxx.xxx.xxx.xxx:5000/v2.0/
      username: demo
      password: secrete
      project_name: demo
    example:
      image_name: fedora-20.x86_64
      flavor_name: m1.small
      network_name: private
  rackspace:
    cloud: rackspace
    auth:
      username: joe
      password: joes-password
      project_name: 123123
    region_name: IAD

```

To use a configuration file called clouds.yaml in one of the default locations:
```
Current Directory
~/.config/openstack
/etc/openstack
```

# User Defined Location¶
```
export OS_CLIENT_CONFIG_FILE=/path/to/my/config/my-clouds.yaml

```

Usage

To use openstack.cloud in a project:
```
import openstack.cloud
```

