from setuptools import find_packages, setup

setup(name="led_panel_client",
      version="0.0.1",
      descrption="MicroPython LED panel client for NodeMCU microcomputer",
      url="https://github.com/Glutexo/led_panel_client",
      author="Glutexo",
      author_email="glutexo@icloud.com",
      license="MIT",
      packages=find_packages(),
      install_requires=["adafruit-ampy==1.0.5", "micropython-adafruit-max7219==1.0"],
      dependency_links=["git+https://github.com/adafruit/micropython-adafruit-max7219.git@1.0#egg=micropython-adafruit-max7219-1.0"],
      entry_points={"console_scripts": ["led_panel_client_put=led_panel_client.cli.commands:put"]})
