# Convert_ASM_to_BIN.py

class Convert_ASM_to_BIN:

  __jump_asm_to_bin_dict = {
                            "JGT" : "001", 
                            "JEQ" : "010", 
                            "JGE" : "011",
                            "JLT" : "100",
                            "JNE" : "101",
                            "JLE" : "110",
                            "JMP" : "111"
                          }

  __dest_asm_to_bin_dict = {
                            "M"   : "001", 
                            "D"   : "010", 
                            "MD"  : "011",
                            "A"   : "100",
                            "AM"  : "101",
                            "AD"  : "110",
                            "AMD" : "111"
                         }

  __comp_asm_to_bin_dict = {
                            "0"   : "0101010",
                            "1"   : "0111111",
                            "-1"  : "0111010",
                            "D"   : "0001100",
                            "A"   : "0110000",
                            "!D"  : "0001101",
                            "!A"  : "0110001",
                            "-D"  : "0001111",
                            "-A"  : "0110011",
                            "D+1" : "0011111",
                            "A+1" : "0110111",
                            "D-1" : "0001110",
                            "A-1" : "0110010",
                            "D+A" : "0000010",
                            "D-A" : "0010011",
                            "A-D" : "0000111",
                            "D&A" : "0000000",
                            "D|A" : "0010101",
                            "M"   : "1110000",
                            "!M"  : "1110001",
                            "-M"  : "1110011",
                            "M+1" : "1110111",
                            "M-1" : "1110010",
                            "D+M" : "1000010",
                            "D-M" : "1010011",
                            "M-D" : "1000111",
                            "D&M" : "1000000",
                            "D|M" : "1010101",

                            # Handling cases if string is in different order eg: "D+A" vs. "A+D"
                            "A+D" : "0000010",
                            "A&D" : "0000000",
                            "A|D" : "0010101",

                            "M+D" : "1000010",
                            "M&D" : "1000000",
                            "M|D" : "1010101"
                         }

  def comp(self, asm):
    return self.__comp_asm_to_bin_dict[asm]

  def dest(self, asm):
    if (asm in self.__dest_asm_to_bin_dict):
      return self.__dest_asm_to_bin_dict[asm]
    else:
      return "000"

  def jump(self, asm):
    if (asm in self.__jump_asm_to_bin_dict):
      return self.__jump_asm_to_bin_dict[asm]
    else:
      return "000"
