#!/usr/bin/env python3

import sys;
import argparse
from io import TextIOWrapper;

class ValidProgram(object):
    def __init__(self, program  : str, map: dict):
        self.program = program
        self.map = map

def mainloop(validProgram : ValidProgram):
    # simplificando os nomes
    program = validProgram.program
    map = validProgram.map
    # inicilizando a tape
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
            sys.stdout.write(chr(tape.value()))
        elif code == ",":
            tape.set(ord(sys.stdin.read(1)))
        elif code == "[":
            if tape.value() == 0:
                pc = map[pc]
        elif code == "]":
            if tape.value() != 0:
                pc = map[pc]
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




def parse(program: str) -> ValidProgram :
    """
    Essa função parseia o arquivo
    """
    parsed = []
    bracket_map = {}
    leftstack: list = []
    right: int = None

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

    return ValidProgram("".join(parsed), bracket_map)

def run(input: TextIOWrapper):
    validProgram = parse(input.read())
    mainloop(validProgram)

# Se executado diretamente
if __name__ == "__main__":
    # Interface de linha de comando criada usando o módulo argparse presente na biblioteca padrão python
    # documentação da biblioteca: https://docs.python.org/3/library/argparse.html#exit-on-error
    # 
    # infelizmente o parâmetro `exit_on_error` não funciona para validação e campos obrigatórios,
    # vou deixar o bloco try/catch na esperança de que na próxima vez esse erro já esteja corrigido
    # 
    # Referências adicionais:
    # link para o stackoverflow: https://stackoverflow.com/questions/67890157/python-3-9-1-argparse-exit-on-error-not-working-in-certain-situations
    # link da issue: https://bugs.python.org/issue41255
    
    parser = argparse.ArgumentParser(description="Executa programas escritos na linguagem ""brainfuck""", exit_on_error=False)
    # argumento obrigatório
    parser.add_argument('arquivo', metavar='arquivo', type=str, help="caminho do programa `bf` a ser executado")

    try:
        args = parser.parse_args()
        input = open(args.arquivo, 'r')
        run(input)
    except argparse.ArgumentError:
        # sopostamente seria aqui que a chamada ao método `parse_args` nos traria com `exit_on_error=False`
        print("É necessário prover o argumento `arquivo` para executar um programa escolhido")
    except SystemExit:
        # porém é aqui que está caindo graças a um bug ou falta de clareza na doc,
        # além é claro de estar duplicando o aviso de campo orbigatório
        print("É necessário prover o argumento `arquivo` para executar um programa escolhido")
    