#!/usr/bin/python3
""" This module contains definitions of some functions
that will help us in the console module"""


def parse_arg(str_cmd):
    """Function that parses the string command"""
    l_cmd = []
    characters = ""
    within_quotes = False
    for char in str_cmd:
        if char == "\"" or within_quotes:
            if char == "\"" and within_quotes:
                within_quotes = False
                l_cmd.append(characters)
                characters = ""
                continue
            elif char == "\"":
                within_quotes = True
                continue
            else:
                characters += char
        elif not within_quotes and (char == " " or char == "\n"):
            l_cmd.append(characters)
            characters = ""
        else:
            characters = characters + char
    if characters != "":
        l_cmd.append(characters)
    # remove idle words or arguments
    new_list = []
    for chars in l_cmd:
        if chars:
            new_list.append(chars)
    return new_list


def parse_dot_command(str_cmd):
    """Function that parses the string command"""
    l_cmd = []
    characters = ""
    split_string = ".,( )"
    within_quotes = False
    for char in str_cmd:
        if char == "\"" or within_quotes:
            if char == "\"" and within_quotes:
                within_quotes = False
                l_cmd.append(characters)
                characters = ""
                continue
            elif char == "\"":
                within_quotes = True
                continue
            else:
                characters += char
        elif not within_quotes and (char in split_string or char == "\n"):
            l_cmd.append(characters)
            characters = ""
        else:
            characters = characters + char
    if characters != "":
        l_cmd.append(characters)
    # remove idle words or arguments
    new_list = []
    for chars in l_cmd:
        if chars:
            new_list.append(chars)
    return new_list


def split_dot_command(command_str):
    """Function to split dot commands """
    list_of_cmd_attr = re.split(r"[.,\(\s+\)]", command_str)
    return list_of_cmd_attr
