# SymbolTable.py

class Symbol_Table:
  
  __table = {}
  __variable_base_addr = 16

  def __init__(self):
    self.__add_predefined_symbols()

  def __add_predefined_symbols(self):
    self.__table['SCREEN'] = 16384
    self.__table['KBD'] = 24576
    self.__table['SP']   = 0
    self.__table['LCL']  = 1
    self.__table['ARG']  = 2
    self.__table['THIS'] = 3
    self.__table['THAT'] = 4
    
    for i in range(0, 16):
      self.__table['R' + str(i)] = i

  def addLabelSymbol(self, symbol, instruction_addr):
    self.__table[symbol] = instruction_addr

  def addVariableSymbol(self, symbol):
    self.__table[symbol] = self.__variable_base_addr
    self.__variable_base_addr += 1

  def symbolExists(self, symbol):
    if (symbol in self.__table):
      return True
    else:
      return False

  def getSymbolValue(self, symbol):
    if (symbol in self.__table):
      return self.__table[symbol]
    else:
      return -l
	  
  # def getTable(self):
    # return self.__table