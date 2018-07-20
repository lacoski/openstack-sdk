import openstack.config

cloud_regions = openstack.config.OpenStackConfig().get_all()
for cloud_region in cloud_regions:
    print(cloud_region.name, cloud_region.region, cloud_region.config)

cloud_region = openstack.config.OpenStackConfig().get_one(
    'devstack', region_name='RegionOne')
print(cloud_region.name, cloud_region.region, cloud_region.config)