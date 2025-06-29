# Challenge Day 19

# -  Download multiple files concurrently using threads

import requests 
import threading

# Function to download a file from a given URL and save it with the given filename
def download_file(url, filename):
    print(f"Started Downloading {filename}...")  # Print when download starts
    response = requests.get(url)  # Send HTTP request to get file content
    with open(filename, "wb") as f:  # Open file in write-binary mode
        f.write(response.content)  # Write the content to the file
    print(f"Finished Downloading {filename}")  # Print when download is finished

# List of (URL, filename) pairs for the files to be downloaded
urls = [
    ("https://www.hloom.com/download-pdf/sample-contract-agreement.pdf", "Sample.pdf"),
    ("https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf", "Dummy.pdf"),
    ("https://www.orimi.com/pdf-test.pdf", "Test.pdf")
]

threads = []  # Create an empty list to store threads

# Loop over each URL-filename pair
for url, name in urls:
    f = threading.Thread(target=download_file, args=(url, name))  # Create a thread for downloading
    f.start()  # Start the thread (begin downloading)
    threads.append(f)  # Add thread to the list so we can join it later

# Wait for all threads to complete (i.e., wait until all downloads are finished)
for thread in threads:
    thread.join()

print("Done")  # Print after all downloads are completed
