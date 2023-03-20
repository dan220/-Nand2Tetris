# create a class called parser
class Parser:
    def __init__(self):
        # open Add.asm file
        self.input_file = open('Add.asm', 'r')

    def hasMoreLines(self):
        return self.input_file.readline() != ''

    def advance(self, input_file):
        # skip over lines with blank space or comments
        while self.hasMoreLines() and (self.input_file[0] == '' or self.input_file[0] == '//'):
            self.input_file.readline()

    def instructionType(self):
        # check if the line is a command
        if self.input_file[0] == '@':
            return 'A_INSTRUCTION'
        elif self.input_file[0] == '(':
            return 'L_INSTRUCTION'
        else:
            return 'C_INSTRUCTION'

    def symbol(self):
        # return the symbol or decimal
        if self.instructionType() == 'A_INSTRUCTION':
            return self.input_file[1:]
        elif self.instructionType() == 'L_INSTRUCTION':
            return self.input_file[1:-1]

    def dest(self):
        # return the dest mnemonic
        if '=' in self.input_file:
            return self.input_file.split('=')[0]
        else:
            return 'null'

    def comp(self):
        # return the comp mnemonic
        if '=' in self.input_file:
            return self.input_file.split('=')[1]

    def jump(self):
        # return the jump mnemonic
        if ';' in self.input_file:
            return self.input_file.split(';')[1]
        else:
            return 'null'

    def close(self):
        self.input_file.close()




