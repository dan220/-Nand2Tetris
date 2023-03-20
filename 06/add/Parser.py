# create a class called parser
class Parser:
    def __init__(self, input_file):
        # open Add.asm file
        self.input_file = input_file
        self.current_line = 0

    def hasMoreLines(self):
        self.current_line = self.input_file.readline()
        return self.current_line != ''

    def advance(self):
        # skip over lines with blank space or comments
        print(self.current_line[0:2])
        while self.current_line[0:2] == '\n' or self.current_line[0:2] == '//':
            print(self.current_line)
            self.current_line = self.input_file.readline()

    def instructionType(self):
        # check if the line is a command
        if self.current_line[0] == '@':
            return 'A_INSTRUCTION'
        elif self.current_line[0] == '(':
            return 'L_INSTRUCTION'
        else:
            return 'C_INSTRUCTION'

    def symbol(self):
        # return the symbol or decimal
        if self.instructionType() == 'A_INSTRUCTION':
            return self.current_line[1:]
        elif self.instructionType() == 'L_INSTRUCTION':
            return self.current_line[1:-1]

    def dest(self):
        # return the dest mnemonic
        if '=' in self.current_line:
            return self.current_line.split('=')[0]
        else:
            return 'null'

    def comp(self):
        # return the comp mnemonic
        if '=' in self.current_line:
            return self.current_line.split('=')[1]

    def jump(self):
        # return the jump mnemonic
        if ';' in self.current_line:
            return self.current_line.split(';')[1]
        else:
            return 'null'

    def close(self):
        self.input_file.close()




