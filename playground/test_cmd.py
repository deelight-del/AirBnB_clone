#!/usr/bin/python3
import readline
from cmd import Cmd

class cmd_example(Cmd):
    prompt = "(hbtn) "
   # use_rawinput = True
    def execute(self):
        self.cmdloop()
    def do_printf(self, cmd):
        l_cmd = parse_arg(cmd)
        actual_cmd = []
        for chars in l_cmd:
            if chars:
                actual_cmd.append(chars)
        for c in actual_cmd:
            print(c)
    def emptyline(self):
        pass
    def do_quit(self, arg):
        return True
    def complete_foobar(self, text, line, begidx, endidx):
        pass
    def do_EOF(self, line):
        print()
        return True
    def precmd(self, line):
      return line

def parse_arg(str_cmd):
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
    #l_cmd = str_cmd.split(" ")
    return l_cmd

if __name__ == "__main__":
    shell = cmd_example()
    shell.execute()
    #lst = parse_arg('ll\n')
    #print(lst)
