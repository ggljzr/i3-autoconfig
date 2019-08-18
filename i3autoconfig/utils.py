import subprocess
from pathlib import Path


def reload_settings() -> None:
    # reload settings
    print("Reloading desktop...")
    subprocess.call(["xrdb", "-load", Path(Path.home(), ".Xresources")])
    subprocess.call(["i3-msg", "restart"])
    subprocess.call(["pkill", "compton"])
    subprocess.call(["compton", "-b"])


def preflight_check() -> None:
    print("Running system preflight check...")

    requirements = ["code", "i3", "i3blocks", "xrdb", "compton"]
    ok = True

    for r in requirements:
        r_text = r
        if r == "code":
            r_text = "VS Code"

        try:
            output = subprocess.check_output(["which", r]).decode("utf-8").strip()
        except subprocess.CalledProcessError:
            print("Requirement '{}' is not installed!".format(r_text))
            ok = False
        else:
            print("Requirement '{}' found: {}".format(r_text, output))

    if not ok:
        print("Some requirements are missing, exiting...")
        exit()
