class BitClass:
    def __init__(self, num1, num2=None) -> None:
        self.num1 = num1
        self.num2 = num2

    def binaryForm(self):
        print("Binary Representation of {num1} ".format(num1=self.num1),
              bin(self.num1).replace("0b", ""))
        if self.num2:
            print("Binary Representation of {num2} ".format(num2=self.num2),
                  bin(self.num2).replace("0b", ""))

    def binaryAnd(self, num=None):
        if num:
            print("Binary And `&` of {num1} and {num} ".format(num1=self.num1, num=num),
                  self.num1 & num)
        elif self.num2:
            print("Binary And `&` of {num1} and {num} ".format(num1=self.num1, num=self.num2),
                  self.num1 & self.num2)
        else:
            print("Please Provide a number for Bitwise And `&` with {num1}".format(
                num1=self.num1))

    def binaryOr(self, num=None):
        if num:
            print("Binary Or `|` of {num1} and {num} ".format(num1=self.num1, num=num),
                  self.num1 | num)
        elif self.num2:
            print("Binary Or `|` of {num1} and {num} ".format(num1=self.num1, num=self.num2),
                  self.num1 | self.num2)
        else:
            print("Please Provide a number for Bitwise Or `|` with {num1}".format(
                num1=self.num1))

    def binaryXor(self, num=None):
        if num:
            print("Binary Xor `^` of {num1} and {num} ".format(num1=self.num1, num=num),
                  self.num1 ^ num)
        elif self.num2:
            print("Binary Xor `^` of {num1} and {num} ".format(num1=self.num1, num=self.num2),
                  self.num1 ^ self.num2)
        else:
            print("Please Provide a number for Bitwise Or `^` with {num1}".format(
                num1=self.num1))

    def binaryNot(self, num=None):
        if num:
            print("Binary Not `~` of {num1} and {num} ".format(num1=self.num1, num=num), ~self.num1, ~num)
        elif self.num2:
            print("Binary Not `~` of {num1} and {num} ".format(num1=self.num1, num=self.num2), ~self.num1, ~self.num2)
        else:
            print("Binary Not `~` of {num1}.".format(num1=~self.num1)) 

    def shiftBitLeft(self,bit):
        if bit:
            print("Shifting {bit} bit to left `<<` of {num} ".format(bit=bit, num=self.num1), self.num1<<bit)
        else:    
            print("Please provide a left shift unit.")

    def shiftBitRight(self,bit):
        if bit:
            print("Shifting {bit} bit to right `>>` of {num} ".format(bit=bit, num=self.num1), self.num1>>bit)
        else:    
            print("Please provide a right shift unit.")        



if __name__ == "__main__":
    bitClass = BitClass(121, 113)
    bitClass.binaryForm()
    bitClass.binaryAnd()
    bitClass.binaryOr()
    bitClass.binaryXor()
    bitClass.binaryNot()
    bitClass.shiftBitLeft(2)
    bitClass.shiftBitRight(3)
