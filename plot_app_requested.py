import json
import matplotlib.pyplot as plt
from collections import Counter

# Load requests data from file
with open('requests.txt', 'r') as f:
    requests = json.load(f)

# Count the number of requests per application
app_request_counts = Counter(request['app_id'] for request in requests)

# Get sorted application IDs and their corresponding request counts
app_ids = sorted(app_request_counts.keys())
request_counts = [app_request_counts[app_id] for app_id in app_ids]

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(app_ids, request_counts, color='tab:orange')
plt.xlabel('Application ID')
plt.ylabel('Number of Requests')
plt.title('Application Requests Distribution')
plt.tight_layout()
plt.show()
