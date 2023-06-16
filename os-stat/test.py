import os
import stat
from datetime import datetime

def get_file_info(file_path):
    # Getting the stats of the file
    stats = os.stat(file_path)

    # Convert timestamp to human readable format    
    modified_time = datetime.utcfromtimestamp(stats[stat.ST_MTIME]).strftime("%Y-%m-%dT%H:%M:%SZ")
    access_time = datetime.utcfromtimestamp(stats[stat.ST_ATIME]).strftime("%Y-%m-%dT%H:%M:%SZ")
    creation_time = datetime.utcfromtimestamp(stats[stat.ST_CTIME]).strftime("%Y-%m-%dT%H:%M:%SZ")

    print(f"{modified_time=}, {stats[stat.ST_MTIME]=}")
    print(f"{access_time=}, {stats[stat.ST_ATIME]=}")
    print(f"{creation_time=}, {stats[stat.ST_CTIME]=}")
    
    # Getting owner user ID, group ID, and file size
    uid = stats.st_uid
    gid = stats.st_gid
    file_size = stats.st_size

    return {
        "Modified Time": modified_time,
        "Access Time": access_time,
        "Creation Time": creation_time,
        "Owner User ID": uid,
        "Group ID": gid,
        "File Size": file_size
    }

# Testing the function
file_info = get_file_info("./helloworld.txt")
print(file_info)

# Print current time
# Get current UTC date and time
now = datetime.utcnow()

# Convert to string in UTC format (ISO 8601)
current_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")

print("Current UTC time:", current_time)
