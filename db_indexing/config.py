import os

ROOT_DIR = "/Users/goncalocorreia/Desktop/test_folder"
BATCH_SIZE = 10000
CHROMA_PATH = "./vector_index_db"

EXCLUDE_DIRS = {
    # System & hidden
    ".DS_Store", ".Trash", ".Spotlight-V100", ".fseventsd", ".TemporaryItems", ".DocumentRevisions-V100",

    # Python
    "__pycache__", "venv", ".venv", "env", ".env", ".tox", ".mypy_cache", ".pytest_cache",

    # Node/JS/Web
    "node_modules", ".next", "dist", "build", ".parcel-cache", ".svelte-kit", ".turbo",

    # IDE & editor configs
    ".idea", ".vscode", ".history", ".atom", ".gradle", ".project", ".classpath", ".settings",

    # macOS/Apple ecosystem
    "Library", "iCloud~com~apple~CloudDocs", "Mobile Documents",

    # Logs, caches, tmp
    ".cache", "logs", "log", ".log", ".tmp", "tmp", "temp", "backup", "backups",

    # Git & VCS
    ".git", ".svn", ".hg",

    # Package manager stuff
    "brew", "homebrew", ".cargo", ".nvm", ".rvm", ".pyenv", ".bundle", ".rubygems",

    # App-specific
    ".android", ".expo", ".firebase", ".yarn", ".npm", ".dart_tool", ".flutter-plugins",

    # Others
    "build", ".lock", ".plist", "__MACOSX"
}
