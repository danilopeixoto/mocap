import os
from distutils.util import convert_path
from setuptools import setup, find_packages


def get_package_info(path):
  with open(
      convert_path(os.path.join(path, '__init__.py')), 'r') as file:
    package_info = {}
    exec(file.read(), package_info)

    return package_info

def parse_requirements(path):
  with open(convert_path(path), 'r') as file:
    return [
      line.rstrip()
      for line in file
      if not (line.isspace() or line.startswith('#'))
    ]


package_name = 'mocap'
package_info = get_package_info(package_name)

entrypoints = {
  'console_scripts': [
    f'{package_name} = {package_name}.cli:app'
  ]
}

package_data = {
  package_name: [
    'README.md',
    'LICENSE.md'
  ]
}

setup(
  name = package_name,
  version = package_info['__version__'],
  description = package_info['__description__'],
  author = package_info['__author__'],
  author_email = package_info['__email__'],
  license = package_info['__license__'],
  python_requires = '>=3.6.0',
  install_requires = parse_requirements('requirements.txt'),
  packages = find_packages(),
  entry_points = entrypoints,
  package_data = package_data,
  zip_safe = False)
