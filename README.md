# EFS Volume Demonstration with Multiple Services on Convox V2 ECS Racks

This repository demonstrates a Python application configured to run as multiple services on Convox V2 (ECS) racks, showcasing the use of a shared Amazon EFS volume. Each service writes unique data to the same files within the EFS volume, illustrating how multiple containerized services can interact with shared persistent storage.

> **Note for V2 Racks:** This example highlights the capability of V2 ECS racks on Convox to support shared EFS volumes across multiple services for persistent data storage needs.

## Structure

- **convox.yml**: Defines multiple services that share a single EFS volume mounted at `/data`. Each service is configured with a unique `SERVICE_NAME` environment variable to demonstrate shared volume access.
- **Dockerfile**: Sets up the Python environment and copies the application script into the Docker image.
- **app.py**: Modified to write and append files with unique service identifiers, proving that multiple services are accessing and modifying the same files on the shared EFS volume.

## Functionality

- **Unique Timestamped Files**: Each service creates timestamped files at one-minute intervals, appending their unique `SERVICE_NAME` to the filename and contents.
- **Shared Persistent File Updates**: Both services append entries to a common persistent file every 1.5 minutes, showcasing their concurrent access to shared volume storage.