'''
Created on Dec 1, 2013

Command line tool for generating script for installing all currently installed
libraries through pip.

usage: python_lib_env.py [-h] [-v] [-s] [-o OUTPUT]

Generates list of commands for installing all libraries currently installed on
the system. All arguments are optional.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         use library version
  -s, --sudo            execute all commands as "sudo"
  -o OUTPUT, --output OUTPUT
                        output file for commands
'''
import subprocess
import argparse
import StringIO
import textwrap

def get_output(sudo, version):
    '''
    Gets output of the command.
    
    @param sudo: True if 'sudo' should be added in front of every command
    @param version: True if version should be specified with library
    
    @return: string with all the commands
    '''
    output = StringIO.StringIO()
    
    command_output = subprocess.check_output(['pip', 'freeze'])
    
    lib_lines = command_output.split('\n')
    libraries = [lib_line.split('==') for lib_line in lib_lines]
    
    for library in libraries:
        if len(library)==2:
            cmd_str = 'sudo pip install {0}' if sudo else 'pip install {0}'
            if version:
                cmd_str = cmd_str + '=={1}'
                cmd_str = cmd_str.format(library[0], library[1])
            else:
                cmd_str = cmd_str.format(library[0])
            output.write(cmd_str + '\n')
            
    return output.getvalue()

def print_cmd_output(cmd_output, output_file):
    '''
    Prints command output to either standard output or specified file.
    
    @param cmd_output: string
    @param output_file: filename path
    '''
    if output_file:
        with open(output_file, 'w') as f:
            f.write(cmd_output)
    else:
        print(cmd_output)


def main(args):
    '''
    Main function.
    
    @param args: command line arguments
    '''
    cmd_output = get_output(args.sudo, args.version)
    print_cmd_output(cmd_output, args.output)

if __name__=="__main__":
    description = textwrap.dedent('''Generates list of commands for installing all libraries currently installed
    on the system. All arguments are optional.''')
    command_line = argparse.ArgumentParser(description=description)
    command_line.add_argument('-v', '--version', action='store_true', 
                              help='use library version')
    command_line.add_argument('-s', '--sudo', action='store_true',
                              help='execute all commands as "sudo"')
    command_line.add_argument('-o', '--output',
                              help='output file for commands')
    args = command_line.parse_args()
    main(args)
