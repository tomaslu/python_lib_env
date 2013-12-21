python_lib_env
==============

Command line tool for generating script for installing all currently installed libraries through pip

Usage
-----

usage: python_lib_env.py [-h] [-v] [-s] [-o OUTPUT]

Generates list of commands for installing all libraries currently installed on
the system. All arguments are optional.

<pre>
optional arguments:
  -h, --help            show this help message and exit
  -v, --version         use library version
  -s, --sudo            execute all commands as "sudo"
  -o OUTPUT, --output OUTPUT
                        output file for commands
</pre>
