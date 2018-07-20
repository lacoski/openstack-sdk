import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize cloud
conn = openstack.connect(cloud='devstack')

def list_networks(conn):
    print("List Networks:")
    for network in conn.network.networks():
        print(network)
        print(network.id)


list_networks(conn)