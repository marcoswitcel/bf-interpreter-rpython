#!/usr/bin/env python2

# Esse programada poder ser executado usando python2

import os;

def mainloop(program, map):
    tape = Tape()
    pc = 0
    while pc < len(program):
        code = program[pc]
        if code == ">":
            tape.advance()
        elif code == "<":
            tape.devance()
        elif code == "+":
            tape.inc()
        elif code == "-":
            tape.dec()
        elif code == ".":
            os.write(1, chr(tape.value()))
        elif code == ",":
            continue #tape.set(ord(os.read(0, 1)))
        elif code == "[":
            if tape.value() == 0:
                pc = map[pc]
                # continue # Skip forward to the matching ]
        elif code == "]":
            if tape.value() != 0:
                pc = map[pc]
                # continue # Skip back to the matching [
        pc += 1

class Tape(object):
    def __init__(self):
        self.thetape = [0]
        self.position = 0

    def value(self):
        return self.thetape[self.position]
    def set(self, val):
        self.thetape[self.position] = val
    def inc(self):
        if (self.thetape[self.position] == 255):
            self.thetape[self.position] = 0
        else:
            self.thetape[self.position] += 1
    def dec(self):
        if (self.thetape[self.position] == 0):
            self.thetape[self.position] = 255
        else:
            self.thetape[self.position] -= 1
    def advance(self):
        self.position += 1
        if len(self.thetape) <= self.position:
            self.thetape.append(0)
    def devance(self):
        self.position -= 1


def parse(program):
    """
    Essa função parseia o arquivo
    """
    parsed = []
    bracket_map = {}
    leftstack = []

    pc = 0
    for char in program:
        if char in ('[', ']', '<', '>', '+', '-', ',', '.'):
            parsed.append(char)

            if char == '[':
                leftstack.append(pc)
            elif char == ']':
                left = leftstack.pop()
                right = pc
                bracket_map[left] = right
                bracket_map[right] = left
            pc += 1

    return "".join(parsed), bracket_map

def run(input):
    program, map = parse(input.read())
    mainloop(program, map)

def run(fp):
    program_contents = ""
    while True:
        read = os.read(fp, 4096)
        if len(read) == 0:
            break
        program_contents += str(read)
    os.close(fp)
    program, bm = parse(program_contents)
    mainloop(program, bm)

def entry_point(argv):
    try:
        filename = argv[1]
    except IndexError:
        print("You must supply a filename")
        return 1
    
    run(os.open(filename, os.O_RDONLY, 0777))
    return 0

def target(*args):
    return entry_point, None

if __name__ == "__main__":
    import sys;
    entry_point(sys.argv)