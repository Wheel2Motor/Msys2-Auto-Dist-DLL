import os
import sys
import subprocess


with open("dll.txt", "w", encoding="utf-8") as f:
    p = subprocess.Popen(["ldd", *sys.argv[1:]], stdout=f)
    i, e = p.communicate()
    p.terminate()
    if e:
        sys.exit(-1)


with open("dll.txt", "r", encoding="utf-8") as f:
    for line in f:
        content = line.strip()
        if not content:
            continue
        basename, path_addr = content.split(" => ")
        path = " ".join(path_addr.split(" ")[:-1])
        dirname = os.path.dirname(path)
        if path.startswith("/c/"):
            continue
        p = subprocess.Popen(["cp", path, dirname])
        p.communicate()
        p.terminate()
