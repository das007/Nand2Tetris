import enum

class InstructionType(enum.Enum):
  WHITESPACE = 0
  COMMENT = 1
  LABEL = 2
  A_INSTRUCTION = 3
  C_INSTRUCTION = 4