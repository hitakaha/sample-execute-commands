#!/usr/bin/env python3
"""
A sample code to execute show commands in verify_cmds directory.
"""

import verify_cmds


def main():
    print("Executed commands", " "*21, "Results")
    print("-"*39, "-"*40)

    for command in dir(verify_cmds):
        if '__' not in command:
            cmd_result = eval(f'verify_cmds.{command}.cmd_to_execute()')

            print(f'{command: <40}{cmd_result: <40}')

 
if __name__ == "__main__":
    main()
