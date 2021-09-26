# Parser.py

import re
import sys
from instruction_type import InstructionType

class Parser:

  __label = ""
  __a_instruction = ""
  __dest = ""
  __comp = ""
  __jump = ""

  def parse(self, line):
    self.__label = ""
    self.__a_instruction = ""
    self.__dest = ""
    self.__comp = ""
    self.__jump = ""
  
    line = self.__trimWhiteSpace(line)
    # check for 
    # 1. whitespace
    if (line == ""):
      return InstructionType.WHITESPACE
    
    # 2. comment
    if (self.__isComment(line)):
      return InstructionType.COMMENT
    
    # 3. Remove Trailing comments
    line = self.__removeTrailingComment(line)

    # 3. Label
    if (self.__isLabel(line)):
      return InstructionType.LABEL

    # 4. A instruction
    elif (self.__isAInstruction(line)):
      return InstructionType.A_INSTRUCTION

    # 5. C instruction
    else:
      self.__parseCInstruction(line);
      return InstructionType.C_INSTRUCTION

  def __trimWhiteSpace(self, line):
    return line.strip().replace(" ", "")

  def __isComment(self, line):
    if (line.startswith("//")):
      return True
    else:
      return False

  def __removeTrailingComment(self, line):
    return line.split("//")[0]

  def __isLabel(self, line):
    if (line[0] == '('):
      # RegEx pattern for " '(' + Alphanumeric chars including '_' i.e. [a-zA-Z0-9_\.\$] + ')' "
      labelPattern = r"^\([\w\.\$]*\)$"
      if (re.match(labelPattern, line)):
        # Removing '(' and ')' chars from the trimmedLine
        self.__label = re.sub("[\(\)]", "" , line)
        return True
      else:
        print("Syntax Error : Invalid Label")
        sys.exit(1)
    else:
      return False

  def __isAInstruction(self, line):
    if (line[0] == '@'):
      self.__a_instruction = line[1:]
      return True
    else:
      return False

  def __parseCInstruction(self, line):
    if ('=' in line):
      arr_d_c_j = line.split('=')
      self.__dest = arr_d_c_j[0]
      c_j = arr_d_c_j[1]

      if (';' in c_j):
        arr_c_j = c_j.split(';')
        self.__comp = arr_c_j[0]
        self.__jump = arr_c_j[1]
      else:
        self.__comp = c_j

    elif (';' in line):
      arr_c_j = line.split(';')
      self.__comp = arr_c_j[0]
      self.__jump = arr_c_j[1]

    else:
      self.__comp = line

  def getLabel(self):
    return self.__label

  def get_AInstruction(self):
    return self.__a_instruction

  def get_dest(self):
    return self.__dest

  def get_comp(self):
    return self.__comp

  def get_jump(self):
    return self.__jump