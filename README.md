# Mocap

A real-time application to capture and stream hand motion data.

## Prerequisites

* [Python (>=3.6.0)](https://www.python.org)
* [OpenCV (>=4.5.0)](https://opencv.org)

## Installation

Install package:

```
pip install .
```

Use the `-e, --editable` flag to install the package in development mode.

## Usage

Run application:

```
mocap --preview
```

By default, the motion data is sent to the UDP server at `0.0.0.0:8000`. The `--preview` flag displays the motion data in a window.

Run `mocap --help` for more information.

## Container image

### Prerequisites

* [Docker Engine (>=19.03.10)](https://www.docker.com)

### Installation

Build container image:

```
docker build -t mocap:1.0.0 .
```

### Usage

Run image application:

```
docker run -d --device /dev/video0:/dev/video0 -p 8000:8000 mocap:1.0.0
```

Use the `--rm` flag to automatically remove the container when application exits.

## Copyright and license

Copyright (c) 2021, Danilo Peixoto. All rights reserved.

Project developed under a [BSD-3-Clause License](LICENSE.md).
