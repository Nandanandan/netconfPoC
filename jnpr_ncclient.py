import yaml
from jnprrpc import ncfrpc as ncf

if __name__ == "__main__":

    inventory_file = 'inventory.yaml'

    with open(inventory_file) as data:
        inv = yaml.load(data)
    # Load the inventory file
        for node in inv['device']:
            obj = ncf(node["ip"], node["username"],node["password"],node["po_ncf"])
            obj.get_interface()
            obj.get_version()
            print(f"{node['lo0']} in progress...")
