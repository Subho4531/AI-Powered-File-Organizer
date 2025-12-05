# scanner_agent.py

import os
from datetime import datetime

class ScannerAgent:
    def __init__(self, root_folder):
        self.root_folder = root_folder

    def scan(self):
        """Scan the folder and collect basic details of each file."""
        file_data_list = []

        for item in os.listdir(self.root_folder):
            full_path = os.path.join(self.root_folder, item)

            # Skip sub-folders (we can add folder scanning later if needed)
            if os.path.isdir(full_path):
                continue

            file_info = self.get_file_info(full_path)
            file_data_list.append(file_info)

        return file_data_list

    def get_file_info(self, file_path):
        """Extract basic information about a file."""
        file_name = os.path.basename(file_path)
        extension = os.path.splitext(file_name)[1].lower()
        size = os.path.getsize(file_path)
        modified_time = datetime.fromtimestamp(os.path.getmtime(file_path))

        return {
            "file_name": file_name,
            "file_path": file_path,
            "extension": extension,
            "size_bytes": size,
            "last_modified": modified_time,
        }


if __name__ == "__main__":
    # Test the scanner agent
    downloads_folder = "./"  # change path as needed
    scanner = ScannerAgent(downloads_folder)

    files = scanner.scan()
    for f in files:
        print(f)
