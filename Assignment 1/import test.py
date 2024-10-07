import json
import csv
from urllib.parse import urlparse

# Function to extract domain from URL for comparison
def extract_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc + parsed_url.path.rstrip('/')
    return domain

file_path = 'Final.json'
file_path2 = 'Google_Result4.json'

# Open and load JSON data for both files
with open(file_path, 'r') as file:
    data = json.load(file)

with open(file_path2, 'r') as file:
    data2 = json.load(file)

# Define columns for the CSV output
columns = ['Queries', 'Number of Overlapping Results', 'Percent Overlap', 'Spearman Correlation']

# Store the results in a list
results = []

# Initialize variables for calculating averages
total_overlap_count = 0
total_overlap_percent = 0
total_spearman = 0
query_count = 0

# Process each query
query_number = 1
for query in data:
    if query not in data2:
        continue
    
    count = 0
    sum_di = 0
    final_results = [extract_domain(url) for url in data[query]]
    google_results = [extract_domain(url) for url in data2[query]]
    
    # Compare top 10 results from Final.json and Google_Result4.json
    for i in range(len(final_results)):
        if final_results[i] in google_results:
            j = google_results.index(final_results[i])
            count += 1
            sum_di += ((i + 1) - (j + 1)) ** 2

    # Calculate Spearman coefficient without rounding
    if count == 0:
        spearman = 0
    elif count == 1:
        spearman = 1 if i == j else 0
    else:
        spearman = 1 - ((6 * sum_di) / (count * (count**2 - 1)))

    # Calculate overlap percentage
    overlap_percent = (count / 10) * 100

    # Append result to the list with final rounding
    results.append([f'Query {query_number}', count, round(overlap_percent, 2), round(spearman, 3)])

    # Update totals for averages
    total_overlap_count += count
    total_overlap_percent += overlap_percent
    total_spearman += spearman
    query_count += 1
    
    query_number += 1

# Calculate averages
if query_count > 0:
    avg_overlap_count = total_overlap_count / query_count
    avg_overlap_percent = total_overlap_percent / query_count
    avg_spearman = total_spearman / query_count
    results.append(['Averages', avg_overlap_count, avg_overlap_percent, round(avg_spearman,3)])

# Write results to a CSV file
with open('hw1.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the column headers
    writer.writerow(columns)
    # Write the data rows
    writer.writerows(results)

# Print the first 20 rows of the result (if there are at least 20), with a newline
for row in results[:20]:
    print(row, "\n")
