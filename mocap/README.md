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

## Usage

Run application:

```
mocap --preview
```

By default, the motion data is sent to the UDP server at `0.0.0.0:8000`. The `--preview` flag displays the motion data in a window.

Run `mocap --help` for more information.

## Copyright and license

Copyright (c) 2021, Danilo Peixoto. All rights reserved.

Project developed under a [BSD-3-Clause License](LICENSE.md).
