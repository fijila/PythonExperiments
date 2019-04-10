#!/bin/python3

import sys
import os
import subprocess
import inspect


# Complete the function below.

def run_process(cmd_args):
    with subprocess.Popen(cmd_args, stdout=subprocess.PIPE) as proc:
        result= proc.communicate(cmd_args)
        return result[0]


if __name__ == "__main__":

    cmd_args_cnt = 0
    cmd_args_cnt = int(input())
    cmd_args_i = 0
    cmd_args = []
    while cmd_args_i < cmd_args_cnt:
        try:
            cmd_args_item = str(input())
        except:
            cmd_args_item = None
        cmd_args.append(cmd_args_item)
        cmd_args_i += 1

    res = run_process(cmd_args);
   # print(res)
    # f.write(res.decode("utf-8") + "\n")




