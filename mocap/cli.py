from typing import Optional, Tuple
from threading import Thread

import typer

from . import __version__
from .media import VideoSource, ComputeStream
from .vision import HandTracking, HandDrawing, FramerateDrawing
from .streaming import MotionDataEncoding, VideoPlayer, UDPServer, UDPClient


app = typer.Typer(add_completion = False)


@app.callback(
  invoke_without_command = True,
  context_settings = dict(help_option_names = ['-h', '--help']),
  help = 'A real-time application to capture and stream hand motion data.')
def main(
    context: typer.Context,
    version: Optional[bool] = typer.Option(
      None,
      '--version', '-v',
      help = 'Show version and exit.')):
  if version:
    typer.echo(f'Version: {__version__}')
    raise typer.Exit()
  elif not context.invoked_subcommand:
    typer.echo(context.get_help())
    raise typer.Exit()

@app.command(
  context_settings = dict(help_option_names = ['-h', '--help']),
  help = 'Process video and send motion data to UDP server.')
def server(
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
      help = 'Show preview window.')):
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

      output_stream.add_stage(MotionDataEncoding())

      output_stream.process()

      with UDPServer(hostname, port, output_stream) as server:
        if preview:
          thread = Thread(target = server.run, daemon = True)
          thread.start()

          player = VideoPlayer('Mocap', output_stream)
          player.play()
        else:
          server.run()
  except Exception as exception:
    typer.echo(f'Error: {exception}', err = True)
    typer.Exit(code = -1)

@app.command(
  context_settings = dict(help_option_names = ['-h', '--help']),
  help = 'Stream motion data from UDP server.')
def client(
    hostname: str =  typer.Option(
      '0.0.0.0',
      '--hostname, -host',
      help = 'UDP server hostname.'),
    port: int =  typer.Option(
      8000,
      '--port, -p',
      min = 0,
      help = 'UDP server port.')):
  try:
    with UDPClient(hostname, port) as client:
      while True:
        typer.echo(client.read())
  except Exception as exception:
    typer.echo(f'Error: {exception}', err = True)
    typer.Exit(code = -1)
