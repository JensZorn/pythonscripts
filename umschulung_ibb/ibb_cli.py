# -*- coding: UTF-8 -*- ###############################################################
#                             <°))))><
#
#               An example for command line interfaces and their usage
#
#                           by Jens Zorn
#
#
#       - CLIs are used by programs where an UI is not required. They were used since
#           the beginning of software development and did not change much since then.
#           UIs made computers useable for every day user, whereas CLIs require certain
#           capabilities in using and understanding the structures of data, scripts and
#           computers
#       - CLI usually start with the name of the executable (e.g. )
#       - they usually use parameters to specify the action that has to take place:
#           - arguments: are required by the command and if not given, the program may
#               run into an error (e.g. 'rm /home/user/test.py' <- '/home/user/text.py' is
#               required by the command 'rm', without it it does not know what to remove)
#           - options: optional parameters which are not required but can help the program
#               to understand what you want (e.g. 'rm -r' <- '-r' is optional, tells the 
#               command 'rm' to recursively remove files within directories (all files))
#           - flags: flags are special option parameters. They are not required and tell
#               tell the program to show certain behaviour (e.g. 'rm --help' <- '--help' 
#               tells the script to show the help for the corresponding command, in this 
#               case 'rm')
#
#
#               /o)_/_/_/__/ )          --         ( \__\_\_\_(o\
#               \ ) \ \ \  \ )          --         ( /  / / / ( /
#######################################################################################
import sys
import enquiries
import argparse
import click
from PyInquirer import prompt
from pprint import pprint

# create your own CLI with your own logic and parsing etc.
def own_cli():
    while True:
        your_command = input("Type your command (-help for help): ")
        if your_command.lower() == "-help":
            print("This is help: \n here are no other commands. Try menu.")
        elif your_command.lower() == "menu":
            print("This is the menu.\n You should try something.")
        elif your_command.lower() == "exit":
            sys.exit()
        else:
            print("Did not recognize the command. Try again")

#own_cli()

# use libraries which provide useful possibilities to make nice CLIs
def enquiries_cli():
    while True:
        options = ["menu", "help", "exit"]
        choice = enquiries.choose("This is a menu: ", options)
        if choice.lower() == "help":
            print("This is help: \n here are no other commands. Try menu.")
        elif choice.lower() == "menu":
            print("This is the menu.\n You should try something.")
        elif choice.lower() == "exit":
            sys.exit()
        else:
            print("Did not recognize the command. Try again")

#enquiries_cli()

# use the standard library for CLIs in Python: argparse
def cli_with_argparse():
    parser = argparse.ArgumentParser(description='Add some integers.')
    parser.add_argument('integers', metavar='N', type=str, nargs='+',help='interger list')
    parser.add_argument('--greeting', action='store_const',const=sum, default=max,help='sum the integers (default: find the max)')
    args = parser.parse_args()
    print(args.integers[0] + " meets " + args.integers[1])

#cli_with_argparse()


# another library for CLIs: click
@click.command()
@click.argument('name')
@click.option('--greeting', '-g')
def main(name, greeting):
    click.echo(f"{name}, meets {greeting}")

#main()

# yet another library PyInquirer
def pyinquirer():
    questions = [
        {
            'type': 'input',
            'name': 'first_name',
            'message': 'What\'s your first name',
        }
    ]
    answers = prompt(questions)
    pprint(answers)

#pyinquirer()

# other interesting librarys:
# - Docopt (for CLI)
# - Clint (for colors, usw. (all-in-one CLI library))
# - Cement
# - Cliff
# - Plac