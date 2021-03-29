from typing import Optional, Tuple
from multiprocessing import Process

import typer

from . import __version__
from .media import VideoSource, ComputeStream
from .vision import HandTracking, HandDrawing, FramerateDrawing
from .streaming import VideoPlayer, UDPServer


app = typer.Typer(add_completion = False)


def show_version(value: bool):
  if value:
    typer.echo(f'Version: {__version__}')
    raise typer.Exit()

@app.command(
  context_settings = dict(help_option_names = ['-h', '--help']),
  help = 'Process video and send motion data to the UDP server.')
def main(
    source: str = typer.Option(
      '0',
      '--source', '-src',
      help = 'Video filename or device index.'),
    size: Tuple[int, int] = typer.Option(
      (640, 480),
      '--size', '-s',
      min = 0,
      help = 'Video resolution.'),
    padding: bool = typer.Option(
      False,
      '--padding', '-pad',
      help = 'Pad video and keep the original aspect ratio.'),
    hostname: str =  typer.Option(
      '0.0.0.0',
      '--hostname, -host',
      help = 'UDP server hostname.'),
    port: int =  typer.Option(
      8000,
      '--port, -p',
      min = 0,
      help = 'UDP server port.'),
    preview: bool = typer.Option(
      False,
      '--preview', '-prev',
      help = 'Show preview window.'),
    version: Optional[bool] = typer.Option(
      None,
      '--version', '-v',
      callback = show_version,
      help = 'Show version and exit.')):
  try:
    try:
      source = int(source)
    except ValueError:
      pass

    with HandTracking() as hand_tracking:
      stream = VideoSource(source, size, padding)
      stream.open()

      output_stream = ComputeStream(stream)
      output_stream.add_stage(hand_tracking)

      if preview:
        output_stream.add_stage(HandDrawing())
        output_stream.add_stage(FramerateDrawing())

      output_stream.process()

      server = UDPServer(
        hostname,
        port,
        output_stream)

      if preview:
        server_process = Process(target = server.run, daemon = True)
        server_process.start()

        player = VideoPlayer('Mocap', output_stream)
        player.play()
      else:
        server.run()
  except Exception as exception:
    typer.echo(f'Error: {exception}', err = True)
    typer.Exit(code = -1)
