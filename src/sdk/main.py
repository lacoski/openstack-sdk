from lib import opsbase

def main():
    api = opsbase()
    api.network_list_networks()
    #api.create_vm('demolib')  
    #api.delete_server('demolib')

if __name__ == '__main__':
    main()  