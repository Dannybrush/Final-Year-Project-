import subprocess

command = "xprop -root _NET_ACTIVE_WINDOW | sed 's/.* //'"
frontmost = subprocess.check_output(["/bin/bash", "-c", command]).decode("utf-8").strip()

print(frontmost)
