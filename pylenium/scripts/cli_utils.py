import subprocess
from typing import List


def run_process(tokenized_command: List[str]) -> subprocess.CompletedProcess:
    """ Run a subprocess given the tokenized command.

    Args:
        tokenized_command: Tokenized list of strings that make up the command to run.

    Returns:
        `CompletedProcess` with - args, returncode, stderr, and stdout

    Raises:
        Does not raise a `CalledProcessError`, so make sure to check the returncode for a non-zero value.
    """
    response = subprocess.run(args=tokenized_command, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    return response
