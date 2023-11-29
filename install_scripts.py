# install_scripts.py

import subprocess
import sys


def pre_install():
    subprocess.run(
        ["protoc", "--python_out", ".", "mahjongsoul.proto"],
        cwd="majsoul_rpa/_impl",
        stdout=sys.stdout,
        stderr=sys.stderr,
        text=True,
        encoding="UTF-8",
    )


def post_install():
    subprocess.run(
        ["docker", "build", "--tag", "majsoul-rpa-sniffer-desktop", "."],
        cwd="mitmproxy",
        stdout=sys.stdout,
        stderr=sys.stderr,
        text=True,
        encoding="UTF-8",
    )
    subprocess.run(
        ["docker", "build", "--tag", "majsoul-rpa-sniffer-headless", "."],
        cwd="headless_browser",
        stdout=sys.stdout,
        stderr=sys.stderr,
        text=True,
        encoding="UTF-8",
    )
