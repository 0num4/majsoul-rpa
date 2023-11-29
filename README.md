# majsoul-rpa

A Robotic Process Automation (RPA) framework for Mahjong Soul (雀魂)

## Prerequisites

### Protocol Buffers Compiler

Put a [protocol buffers](https://developers.google.com/protocol-buffers) compiler, `protoc`, in a PATH location.

### PyTorch

Install [PyTorch](https://pytorch.org/).

### kanachan

Install [kanachan](https://github.com/Cryolite/kanachan).

```bash
$ pip install git+https://github.com/Cryolite/kanachan
```

### Install Python Dependencies

```bash
majsoul-rpa$ pip install -U .
```

### AWS Credentials

Write AWS credential information in `$HOME/.aws/credentials`'s `majsoul-rpa` profile.

### kanachan's Model

Prepare kanachan's model and write kanachan's model configuration file `model.yaml`.

### Configuration File

Write the configuration file `config.yaml`.

### poetry への移行

setup.py の内容を実行するために install_scripts.py に移植してそれを install_scripts として呼び出している

### post-install でエラー

```
 => => transferring context: 41B                                                                           0.0s
 => ERROR [2/3] RUN apt-get update && apt-get install -y       ca-certificates       fonts-ipafont        29.5s
------
 > [2/3] RUN apt-get update && apt-get install -y       ca-certificates       fonts-ipafont       libnss3-tools       unzip       wget &&     wget -q -O - 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | apt-key add - &&     echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google.list &&     apt-get update &&     DEBIAN_FRONTEND=noninteractive apt-get install -y google-chrome-stable &&     apt-get clean && rm -rf /var/lib/apt/lists/* &&     pip3 install -U pip && pip3 install -U       mitmproxy       Pillow       redis       selenium &&     wget "https://chromedriver.storage.googleapis.com/`wget -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip" &&     unzip chromedriver_linux64.zip -d /usr/local/bin &&     rm chromedriver_linux64.zip:
#0 2.979 Get:1 http://ports.ubuntu.com/ubuntu-ports jammy InRelease [270 kB]

略

#0 28.64 W: http://dl.google.com/linux/chrome/deb/dists/stable/InRelease: Key is stored in legacy trusted.gpg keyring (/etc/apt/trusted.gpg), see the DEPRECATION section in apt-key(8) for details.
#0 28.67 Reading package lists...
#0 29.22 Building dependency tree...
#0 29.34 Reading state information...
#0 29.36 E: Unable to locate package google-chrome-stable
------
Dockerfile:5
--------------------
   4 |
   5 | >>> RUN apt-get update && apt-get install -y \
   6 | >>>       ca-certificates \
   7 | >>>       fonts-ipafont \
   8 | >>>       libnss3-tools \
   9 | >>>       unzip \
  10 | >>>       wget && \
  11 | >>>     wget -q -O - 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | apt-key add - && \
  12 | >>>     echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google.list && \
  13 | >>>     apt-get update && \
  14 | >>>     DEBIAN_FRONTEND=noninteractive apt-get install -y google-chrome-stable && \
  15 | >>>     apt-get clean && rm -rf /var/lib/apt/lists/* && \
  16 | >>>     pip3 install -U pip && pip3 install -U \
  17 | >>>       mitmproxy \
  18 | >>>       Pillow \
  19 | >>>       redis \
  20 | >>>       selenium && \
  21 | >>>     wget "https://chromedriver.storage.googleapis.com/`wget -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip" && \
  22 | >>>     unzip chromedriver_linux64.zip -d /usr/local/bin && \
  23 | >>>     rm chromedriver_linux64.zip
  24 |
--------------------
ERROR: failed to solve: process "/bin/sh -c apt-get update && apt-get install -y       ca-certificates       fonts-ipafont       libnss3-tools       unzip       wget &&     wget -q -O - 'https://dl-ssl.google.com/linux/linux_signing_key.pub' | apt-key add - &&     echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google.list &&     apt-get update &&     DEBIAN_FRONTEND=noninteractive apt-get install -y google-chrome-stable &&     apt-get clean && rm -rf /var/lib/apt/lists/* &&     pip3 install -U pip && pip3 install -U       mitmproxy       Pillow       redis       selenium &&     wget \"https://chromedriver.storage.googleapis.com/`wget -O - https://chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip\" &&     unzip chromedriver_linux64.zip -d /usr/local/bin &&     rm chromedriver_linux64.zip" did not complete successfully: exit code: 100

```
