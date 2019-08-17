import subprocess
from pathlib import Path


def reload():
    # reload settings
    print("Reloading desktop...")
    subprocess.call(["xrdb", "-load", Path(Path.home(), ".Xresources")])
    subprocess.call(["i3-msg", "restart"])
    subprocess.call(["pkill", "compton"])
    subprocess.call(["compton", "-b"])
