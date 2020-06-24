from pathlib import Path
import csv

Digits = '!#$%&();@^_`abcdefghijklmnopqrstuvwxyz~'
Digits_linux = "_;!()@&#%'^~$abcdefghijklmnopqrstuvwxyz~"
Base58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
#igits = "12345678901234567890123456789012345678901234567890123456789012";


def ConvertDigits(parIntegerToConvert):
    return self.Digits[parIntegerToConvert]

def ConvertToBase(parLongToConvert) :
    newBaseNumber = ''
    if parLongToConvert <= 35:
        #integerToConvert = self.ConvertToInteger(parLongToConvert)
        return self.ConvertDigits(parLongToConvert)
    else:
           # (q,r) = divmod(x,36) == (notRemainder,newBaseNumber) = divmod(parLongToConvert,36)
            #notRemainder = 0
            #notRemainder = parLongToConvert % 36
            #notRemainder = (parLongToConvert - notRemainder) / 36
            #newBaseNumber = self.ConvertToBase(parLongToConvert - (notRemainder * 36))
        (notRemainder,newBaseNumber) = divmod(parLongToConvert,36)
        return self.ConvertToBase(notRemainder) + self.ConvertToBase(newBaseNumber)
    
#    def ConvertToInteger(self, parLong: int) -> int:
#            integerConverted = 0
#            javaSpecialConversion = parLong.toString()
#            integerConverted = Integer.decode(javaSpecialConversion)
#            return integerConverted
#    output_directory = Path(r'/home/marcus/Desktop/temp')
output_directory = Path(r'c:/temp')

for ind in Digits:
    out_file = output_directory.joinpath(ind + '.txt')
    out_dir = output_directory.joinpath(ind)
    print(out_dir)
    out_dir.mkdir()
#---------------------------------------------------------
#    For testing
#    with open(out_file,'w',encoding='utf-8') as out_file:
#        out = csv.writer(out_file)
#        line = ind
#        out_file.write(line)
