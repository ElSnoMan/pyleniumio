import subprocess
from typing import List, Union


def run_process(tokenized_command: Union[List[str], str], shell=False) -> subprocess.CompletedProcess:
    """ Run a subprocess given the tokenized command.

    Args:
        tokenized_command: Tokenized list of strings that make up the command to run.
        shell: If the arg is a single string, change this to True

    Returns:
        `CompletedProcess` with - args, returncode, stderr, and stdout

    Raises:
        Does not raise a `CalledProcessError`, so make sure to check the returncode for a non-zero value.
    """
    response = subprocess.run(args=tokenized_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=shell)
    return response
