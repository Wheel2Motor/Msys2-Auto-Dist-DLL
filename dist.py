import os
import sys
import subprocess


for exe in sys.argv[1:]:
    table = exe + "dll.txt"
    with open(table, "w", encoding="utf-8") as f:
        p = subprocess.Popen(["ldd", exe], stdout=f)
        i, e = p.communicate()
        p.terminate()
        if e:
            sys.exit(-1)
    with open(table, "r", encoding="utf-8") as f:
        for line in f:
            content = line.strip()
            if not content:
                continue
            basename, path_addr = content.split(" => ")
            path = " ".join(path_addr.split(" ")[:-1])
            dirname = os.path.dirname(exe)
            if path.startswith("/c/"):
                continue
            print("--COPY [%s]\n--TO [%s]\n" % (path, dirname))
            p = subprocess.Popen(["cp", path, dirname])
            p.communicate()
            p.terminate()
            print("--Complete")
