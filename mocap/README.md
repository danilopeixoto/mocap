# Mocap

A real-time application to capture hand motion data.

## Prerequisites

* [Python (>=3.6.0)](https://www.python.org)
* [OpenCV (>=4.5.0)](https://opencv.org)

## Installation

Install package:

```
pip install .
```

## Usage

Run application:

```
mocap stream --preview
```

By default, the motion data is sent to the UDP socket at `0.0.0.0:8000`. The `--preview` flag also displays the motion data in a window.

Run client:

```
mocap client
```

Run `mocap --help` for more information.

## Copyright and license

Copyright (c) 2021, Danilo Peixoto. All rights reserved.

Project developed under a [BSD-3-Clause License](LICENSE.md).
