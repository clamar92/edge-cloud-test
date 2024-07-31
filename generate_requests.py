import json
import random
import numpy as np
from scipy.stats import zipf

# Assign users to leaf nodes
def assign_users_to_leaf_nodes(num_users, leaf_nodes):
    users = []
    for user_id in range(1, num_users + 1):
        leaf_node = random.randint(1, leaf_nodes)  # Assign user to a leaf node
        users.append({'user_id': user_id, 'leaf_node': leaf_node})
    return users

# Generate requests based on user activity and application popularity
def generate_requests(users, applications, user_request_probability):
    # Calculate application popularity according to Zipf's law
    num_apps = len(applications)
    ranks = np.arange(1, num_apps + 1)
    app_popularity = zipf.pmf(ranks, 1.2)
    app_popularity = app_popularity / app_popularity.sum()  # normalize to sum to 1

    requests = []
    for user in users:
        if random.random() < user_request_probability:
            app_choice = np.random.choice(num_apps, p=app_popularity)
            selected_app = applications[app_choice]
            requests.append({
                'user_id': user['user_id'],
                'leaf_node': user['leaf_node'],
                'app_id': selected_app['app_id'],
                'cpu_demand': selected_app['cpu_demand'],
                'storage_demand': selected_app['storage_demand']
            })
    return requests

# Main function to load data and generate requests
def main():
    # Load applications and network nodes from text files
    with open('applications.txt', 'r') as f:
        applications = json.load(f)

    with open('network_nodes.txt', 'r') as f:
        network_nodes = json.load(f)

    # Parameters
    num_users = 1000  # Number of users
    user_request_probability = 0.6  # Probability of a user making a request
    leaf_nodes = len(network_nodes['leaf'])

    # Generate users and requests
    users = assign_users_to_leaf_nodes(num_users, leaf_nodes)
    requests = generate_requests(users, applications, user_request_probability)

    # Save generated requests to a text file (JSON format)
    with open('requests.txt', 'w') as f:
        json.dump(requests, f)

if __name__ == "__main__":
    main()
