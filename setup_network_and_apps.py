import json
import random

# Network settings
LEAF_NODES = 25
INTERMEDIATE_NODES = 4
UPPER_LAYER_NODES = 4
CLOUD_CAPACITY = 20000  # CPU cycles/s

LEAF_CAPACITY = 250  # CPU cycles/s
INTERMEDIATE_CAPACITY = 500  # CPU cycles/s
UPPER_LAYER_CAPACITY = 1000  # CPU cycles/s

# Storage capacity percentage (3-15% of the total application storage)
STORAGE_PERCENTAGE_RANGE = (3, 15)

# Generate applications with specific CPU and storage demands
def generate_applications(num_apps):
    applications = []
    for i in range(num_apps):
        app_id = i + 1
        cpu_demand = random.randint(10, 25)  # Fixed CPU demand in cycles/s
        storage_demand = random.randint(50, 100)  # Fixed storage demand in units
        applications.append({
            'app_id': app_id,
            'cpu_demand': cpu_demand,
            'storage_demand': storage_demand
        })
    return applications

# Generate network nodes with CPU and storage capacities
def generate_network_nodes(total_storage_capacity):
    nodes = {
        'leaf': [{'cpu': LEAF_CAPACITY, 'storage': random.randint(*STORAGE_PERCENTAGE_RANGE) * total_storage_capacity // 100} for _ in range(LEAF_NODES)],
        'intermediate': [{'cpu': INTERMEDIATE_CAPACITY, 'storage': random.randint(*STORAGE_PERCENTAGE_RANGE) * total_storage_capacity // 100} for _ in range(INTERMEDIATE_NODES)],
        'upper_layer': [{'cpu': UPPER_LAYER_CAPACITY, 'storage': random.randint(*STORAGE_PERCENTAGE_RANGE) * total_storage_capacity // 100} for _ in range(UPPER_LAYER_NODES)],
        'cloud': {'cpu': CLOUD_CAPACITY, 'storage': total_storage_capacity}  # Cloud has full storage capacity
    }
    return nodes

# Main function to generate and save applications and network nodes
def main():
    num_apps = 100  # Number of applications

    applications = generate_applications(num_apps)
    total_app_storage = sum(app['storage_demand'] for app in applications)
    network_nodes = generate_network_nodes(total_app_storage)

    # Save applications and network nodes to text files (JSON format)
    with open('applications.txt', 'w') as f:
        json.dump(applications, f)

    with open('network_nodes.txt', 'w') as f:
        json.dump(network_nodes, f)

if __name__ == "__main__":
    main()
