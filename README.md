Network Configuration (setup_network_and_apps.py)
This script is designed to set up the initial state of our network by generating the specifications for both applications and network nodes. This includes:

    - Applications: Each application is assigned a fixed CPU and storage demand.

    - Network Nodes: The script creates leaf, intermediate, and upper-layer nodes with predefined CPU capacities. The storage capacities for these nodes are calculated as a percentage of the total application storage demand.

The script outputs the generated data into two JSON files: applications.txt for the applications' specifications and network_nodes.txt for the network nodes' configurations.


Request Generation (generate_requests.py)
The generate_requests.py script utilizes the data from applications.txt and network_nodes.txt to generate requests. Key functionalities include:

    - User Assignment: Users are randomly assigned to leaf nodes.

    - Request Generation: The script generates requests based on a specified probability of user activity. The popularity of applications follows Zipf's law, ensuring that a few applications are highly requested, while others are less so.

The generated requests are saved in requests.txt.


To analyze the generated data, we have two visualization scripts:

    - Application Requests Plot (plot_app_requested.py): This script visualizes the distribution of application requests. 
    
    - Leaf Nodes State (plot_leaf_nodes_state.py): This script focuses on the congestion at leaf nodes by plotting the CPU and storage demands against their capacities. 