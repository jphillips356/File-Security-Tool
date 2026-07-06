import os
import json
import hashlib


def create_baseline(directory):
    data = scan_directory(directory)
    save_baseline(data)


def check_integrity(directory):
    old = load_baseline()
    new = scan_directory(directory)

    modified = []
    deleted = []
    added = []

    # Check for modified or deleted files
    for file in old:
        if file not in new:
            deleted.append(file)
        elif old[file] != new[file]:
            modified.append(file)

    # Check for new files
    for file in new:
        if file not in old:
            added.append(file)

    # Print results
    print("\nIntegrity Check Results:\n")

    if modified:
        print("MODIFIED:")
        for f in modified:
            print(" ", f)

    if deleted:
        print("\nDELETED:")
        for f in deleted:
            print(" ", f)

    if added:
        print("\nNEW:")
        for f in added:
            print(" ", f)

    if not modified and not deleted and not added:
        print("No changes detected.")


def scan_directory(directory):
    file_hashes = {}

    for root, dirs, files in os.walk(directory):
        for name in files:
            full_path = os.path.join(root, name)
            file_hashes[full_path] = hash_file(full_path)
    
    return file_hashes


def hash_file(filepath):
    sha1 = hashlib.sha1()

    with open(filepath, 'rb') as file:
        while chunk := file.read(8192):
            sha1.update(chunk)
    return sha1.hexdigest()


def save_baseline(data, filename="baseline.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)


def load_baseline():
    filename = "baseline.json"
    with open(filename, 'r') as file:
        data_dictionary = json.load(file)
    return data_dictionary