from git import Repo
import sys

REPO_URL = 'https://github.com/fgdsAcero/SimpleXarrayMHWs.git'
LOCAL_DIR = './SimpleXarrayMHWs'

try:
  print("Downloading the latest SimpleXarrayMHWs repository...")
  Repo.clone_from(REPO_URL, LOCAL_DIR)
  print(f"✓ Successfully downloaded the repository to {LOCAL_DIR}!")
  print(f"✓ While comments are included in the scripts, it is recommended you check out the README.txt file.")
except Exception as e:
  print(f"✗ Error: {e}")
  sys.exit(1)
