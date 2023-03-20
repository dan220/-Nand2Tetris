import sys
import Parser

# initialisation main loop and variables
if __name__ == "__main__":
    # Assign input file
    input_file_text = "Add.asm"
    # open input file
    input_file = open(input_file_text, 'r')
    # Assign output file
    output_file = input_file_text.split('.')[0] + '.hack'
    # Create output file
    open(output_file, 'w')
    # Initialise parser
    parser = Parser.Parser(input_file)
    # Enter loop
    while parser.hasMoreLines():
        parser.advance()
        instruction_type = parser.instructionType()
        if instruction_type != 'C_INSTRUCTION':
            symbol = parser.symbol()
            print(symbol)


