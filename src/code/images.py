import openstack

# Initialize and turn on debug logging
openstack.enable_logging(debug=True)

# Initialize cloud
conn = openstack.connect(cloud='devstack')

openstack.enable_logging()

def list_images(conn):
    print("List Images:")
    for image in conn.image.images():
        print(image)

def upload_image(conn):
    print("Upload Image:")

    # Load fake image data for the example.
    data = 'This is fake image data.'

    # Build the image attributes and upload the image.
    image_attrs = {
        'name': 'imageSDKup',
        'data': open('cirros.qcow2', 'rb'),
        'disk_format': 'qcow2',
        'container_format': 'bare',
        'visibility': 'public',
    }
    conn.image.upload_image(**image_attrs)

def download_image(conn):
    print("Download Image:")

    # Find the image you would like to download.
    image = conn.image.find_image("cirros")

    with open("cirros.qcow2", "wb") as local_image:
        response = conn.image.download_image(image)

        # Response will contain the entire contents of the Image.
        # print(response)
        local_image.write(response)

def delete_image(conn):
    print("Delete Image:")
    example_image = conn.image.find_image('imageSDKup')
    conn.image.delete_image(example_image, ignore_missing=False)

list_images(conn)
# download_image(conn)
# upload_image(conn)
# delete_image(conn)