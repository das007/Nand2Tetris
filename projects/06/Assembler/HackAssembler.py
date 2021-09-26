# HackAssembler.py

import sys
import Parser
import SymbolTable
import Convert_ASM_to_BIN
from instruction_type import InstructionType

def firstPass(asmFileName, parser, symbolTable):
  '''
  FIRST PASS : Add all labels in the Symbol Table
  '''
  # open asm file in read mode
  asmFile = open(asmFileName, 'r')
  
  instruction_count = -1
  
  for line in asmFile:
    type_of_line = parser.parse(line)

    if (type_of_line == InstructionType.WHITESPACE or type_of_line == InstructionType.COMMENT):
      continue

    elif (type_of_line == InstructionType.LABEL):
      address = instruction_count + 1
      symbolTable.addLabelSymbol(parser.getLabel(), address)
  
    else:
      instruction_count += 1

  asmFile.close()
  
def secondPass(asmFileName, parser, symbolTable, convert_ASM_to_BIN):
  '''
  SECOND PASS : parse all instructions and convert to binary
  '''
  instruction_count = -1

  # open asm file in read mode
  asmFile = open(asmFileName, 'r')

  # get binary filename and open in write mode
  asmFileName_parts = asmFileName.split('.')
  binFileName = '.'.join(asmFileName_parts[:-1])
  binFile = open(binFileName + ".hack", 'w')

  for line in asmFile:
    # print(line)
    type_of_line = parser.parse(line)

    if (type_of_line == InstructionType.WHITESPACE or type_of_line == InstructionType.COMMENT or type_of_line == InstructionType.LABEL):
      continue

    elif (type_of_line == InstructionType.A_INSTRUCTION):
      symbolValue = ""
      a_instruction = parser.get_AInstruction()

      if (a_instruction.isnumeric()):
        symbolValue = a_instruction
      else:
        if (symbolTable.symbolExists(a_instruction)):
          symbolValue = symbolTable.getSymbolValue(a_instruction)
        else:
          symbolTable.addVariableSymbol(a_instruction)
          symbolValue = symbolTable.getSymbolValue(a_instruction)

      bin_a_instruction = '0' + '{0:015b}'.format(int(symbolValue))
      binFile.write(bin_a_instruction + "\n")
      instruction_count += 1

    else:
      asm_dest = parser.get_dest()
      asm_comp = parser.get_comp()
      asm_jump = parser.get_jump()
      bin_c_instruction = '111'  + convert_ASM_to_BIN.comp(asm_comp) + convert_ASM_to_BIN.dest(asm_dest) + convert_ASM_to_BIN.jump(asm_jump)
      binFile.write(bin_c_instruction + "\n")

      instruction_count += 1

  asmFile.close()
  binFile.close()

def HackAssembler(asmFileName):
  # Initialize Parser
  parser = Parser.Parser()
  
  # Initialize Symbol_Table
  symbolTable = SymbolTable.Symbol_Table()
  
  # Initialize ASM_to_BIN Converter
  convert_ASM_to_BIN = Convert_ASM_to_BIN.Convert_ASM_to_BIN()

  # FIRST PASS : Add all labels in the Symbol Table
  firstPass(asmFileName, parser, symbolTable)
  
  # SECOND PASS : parse all instructions and convert to binary
  secondPass(asmFileName, parser, symbolTable, convert_ASM_to_BIN)
  
if (__name__ == '__main__'):
  help_msg = '''
  ==================================================
  | HELP                                           |
  ==================================================
  | Run below command to execute HackAssembler:    |
  | >> HackAssembler.py <ASM file path>            |
  | eg: >> HackAssembler.py Add.asm                |
  ==================================================
  '''

  if (len(sys.argv) < 2):
    print(help_msg)
  else:
    asmFileName = sys.argv[1]
    HackAssembler(asmFileName)