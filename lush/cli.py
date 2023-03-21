from typing import Callable
from sys import argv

commands = []


def register_command(action: Callable[[str], None]) -> Callable[[str], None]:
    commands.append({"name": action.__name__[:-len('_command')], "action": action})

    def command_action(command_argument: str):
        action(command_argument)

    return command_action


def recognize_command_and_launch() -> None:
    if len(argv) - 1 > 2:
        raise ValueError(f'Lush Interpreter expected to receive 2 arguments: the command name and its argument, '
                         f'but it received {len(argv) - 1}.')

    get_command_by_name(argv[1])(argv[0])


def get_command_by_name(command_name: str) -> Callable[[str], None]:
    return next((command for command in commands if command.get("name") == command_name))["action"]


@register_command
def lex_command(filename: str):
    pass


@register_command
def help_command(_: str):
    print('help_command is called')
