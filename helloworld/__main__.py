#!/usr/bin/env python

import argparse
import helloworld


def parse_command_line():
    " parses args for the helloworld.py funtions"

    # init parser and add arguments
    parser = argparse.ArgumentParser()

    # add emotion args
    parser.add_argument(
        "--emotion",
        help="print random emotion",
        action="store_true")

    parser.add_argument(
        "--howold",
        help="print random age",
        action="store_true")

    # parse args
    args = parser.parse_args()
    return args


def main():
    " run helloworld on parsed args"
    args = parse_command_line()
    helloworld.helloworld(
        emotion=args.emotion,
        howold=args.howold)

