import os
import sys

def run(cmd):
    print(f"Running: {cmd}")
    result = os.system(cmd)
    if result != 0:
        print(f"❌ Error running: {cmd}")
        sys.exit(1)

run("python3 scripts/generate.py")
run("python3 scripts/assemble_video.py")
run("python3 scripts/make_thumbnail.py")
run("python3 scripts/upload_youtube.py")
