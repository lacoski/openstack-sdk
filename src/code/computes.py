import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize cloud
conn = openstack.connect(cloud='devstack')

def list_servers(conn):
    print("List Servers:")
    for server in conn.compute.servers():
        print(server)

def list_images(conn):
    print("List Images:")
    for image in conn.compute.images():
        print(image)
        print(image.id)

def list_flavors(conn):
    print("List Flavors:")
    for flavor in conn.compute.flavors():
        print(flavor)
        print(flavor.id)

def list_networks(conn):
    print("List Networks:")
    for network in conn.network.networks():
        print(network.id)

def create_vm(conn):
    print("Create Server:")

    image = conn.compute.find_image('cirros')
    flavor = conn.compute.find_flavor('m1.small')
    network = conn.network.find_network('provider')

    server = conn.compute.create_server(
        name='testsdk', image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}])

    server = conn.compute.wait_for_server(server)

#list_servers(conn)
#list_images(conn)
#list_flavors(conn)
#list_networks(conn)
#create_vm(conn)
