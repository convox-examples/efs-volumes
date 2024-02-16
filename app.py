import os
import time

# Directory to store files. This will be mounted as a volume.
storage_dir = "/data"
service_name = os.getenv("SERVICE_NAME", "default_service")

def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def create_timestamped_file():
    filename = os.path.join(storage_dir, f"{time.strftime('%Y%m%d-%H%M%S')}-{service_name}.txt")
    with open(filename, 'w') as f:
        f.write(f"Timestamp: {time.time()} by {service_name}\n")
    print(f"Created timestamped file: {filename}")

def append_to_persistent_file():
    filename = os.path.join(storage_dir, "persistent.txt")
    with open(filename, 'a') as f:
        f.write(f"Appended at: {time.strftime('%Y-%m-%d %H:%M:%S')} by {service_name}\n")
    print(f"Appended to persistent file: {filename}")

if __name__ == "__main__":
    ensure_dir_exists(storage_dir)
    while True:
        create_timestamped_file()
        time.sleep(60)
        append_to_persistent_file()
        time.sleep(30)
