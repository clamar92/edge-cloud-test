import json
import matplotlib.pyplot as plt

# Load requests and network node data from files
with open('requests.txt', 'r') as f:
    requests = json.load(f)

with open('network_nodes.txt', 'r') as f:
    network_nodes = json.load(f)

# Extract leaf nodes' information from network_nodes
leaf_nodes_info = network_nodes['leaf']

# Aggregate CPU and storage demands for each leaf node
leaf_node_cpu_storage = {i: {'cpu_demand': 0, 'storage_demand': 0} for i in range(1, len(leaf_nodes_info) + 1)}

for request in requests:
    leaf_node = request['leaf_node']
    leaf_node_cpu_storage[leaf_node]['cpu_demand'] += request['cpu_demand']
    leaf_node_cpu_storage[leaf_node]['storage_demand'] += request['storage_demand']

# Prepare data for plotting
leaf_nodes = list(leaf_node_cpu_storage.keys())
cpu_demands = [leaf_node_cpu_storage[node]['cpu_demand'] for node in leaf_nodes]
storage_demands = [leaf_node_cpu_storage[node]['storage_demand'] for node in leaf_nodes]
leaf_cpu_capacities = [node['cpu'] for node in leaf_nodes_info]
leaf_storage_capacities = [node['storage'] for node in leaf_nodes_info]

# CPU Demand vs Capacity Plot
plt.figure()
plt.bar(leaf_nodes, cpu_demands, color='tab:blue', alpha=0.6, label='Requested CPU Demand')
plt.plot(leaf_nodes, leaf_cpu_capacities, color='navy', linestyle='--', label='CPU Capacity')
plt.xlabel('Leaf Node')
plt.ylabel('CPU Demand/Capacity (cycles/s)')
plt.title('CPU Demand vs Capacity per Leaf Node')
plt.legend(loc='upper left')
plt.tight_layout()

# Storage Demand vs Capacity Plot
plt.figure()
plt.bar(leaf_nodes, storage_demands, color='tab:green', alpha=0.6, label='Requested Storage Demand')
plt.plot(leaf_nodes, leaf_storage_capacities, color='darkgreen', linestyle='--', label='Storage Capacity')
plt.xlabel('Leaf Node')
plt.ylabel('Storage Demand/Capacity (units)')
plt.title('Storage Demand vs Capacity per Leaf Node')
plt.legend(loc='upper left')
plt.tight_layout()

plt.show()
