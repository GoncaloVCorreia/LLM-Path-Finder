import os
from config import ROOT_DIR, EXCLUDE_DIRS

def should_skip_dir(path):
    return any(part in EXCLUDE_DIRS for part in path.split(os.sep))

def build_file_queue():
    file_jobs = []
    for root, dirs, files in os.walk(ROOT_DIR):
        dirs[:] = [d for d in dirs if not should_skip_dir(os.path.join(root, d))]
        for folder in dirs:
            file_jobs.append((os.path.join(root, folder), False))
        for file in files:
            file_jobs.append((os.path.join(root, file), True))
    print(f"🧠 Found {len(file_jobs)} items.")
    return file_jobs
