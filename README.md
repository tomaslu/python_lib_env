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

For example, command:

<code>python python_lib_env.py -v -s</code>

would produce output in which every command would be executed as sudo and currently installed version would be installed. So, output would look something like this:

<pre>
sudo pip install argparse==1.2.1
sudo pip install distribute==0.6.24
sudo pip install wsgiref==0.1.2
</pre>
