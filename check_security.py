import os
import sys

def check_files():
    required_files = ["LICENSE", "README.md", "requirements.txt"]
    missing = [f for f in required_files if not os.path.exists(f)]
    if missing:
        print(f"❌ Missing files: {', '.join(missing)}")
        sys.exit(1)
    print("✅ All required files are present.")

check_files()
