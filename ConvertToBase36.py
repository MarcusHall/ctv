class ConvertToBase36:
    Digits = '!#$%&();@^_`abcdefghijklmnopqrstuvwxyz~'
#   Digits = "12345678901234567890123456789012345678901234567890123456789012";

    def __init__(self) -> None:
        pass

    def ConvertDigits(self, parIntegerToConvert: int) -> str:
        return self.Digits[parIntegerToConvert]

    def ConvertToBase(self, parLongToConvert: int) -> str:
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


#package net.marcushall.util;


#public class ConvertToBase35
#{
#    String ConvertDigits(int parIntegerToConvert)
#    {
#        //	String Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ;
#        //		String Digits = "!#$%&'+,-0123456789;=@^_`abcdefghijklmnopqrstuvwxyz~€ƒ†‡ˆ•”˜ˆ‘’" ;
#        //		String Digits = "!#$%&'0123456789-,;@^ˆ_`~˜”+=†‡•‰€abcdefƒghijklmnopqrstuvwxyz" ;
#        //     String Digits = "!#$%&†‡•‰€abcdefghijklmnopqrstuvwxyzz";
#        String Digits = "!#$%&();@^_`abcdefghijklmnopqrstuvwxyz~";
#        //     Digits = "12345678901234567890123456789012345678901234567890123456789012";
#        return Digits.substring(parIntegerToConvert, parIntegerToConvert + 1);
#    } // public String ConvertDigits(Long parIntegerToConvert)
#
#    public String ConvertToBase(Long parLongToConvert)
#    {
#        String newBaseNumber = "";
#
#        if (parLongToConvert <= 35)
#        {
#            int integerToConvert = ConvertToInteger(parLongToConvert);
#            return ConvertDigits(integerToConvert);
#        }
#
#        else
#        {
#            Long notRemainder = 0L;
#            notRemainder = parLongToConvert % 36;
#            notRemainder = (parLongToConvert - notRemainder) / 36;
#            newBaseNumber = ConvertToBase(parLongToConvert - (notRemainder * 36));
#            return ConvertToBase(notRemainder) + newBaseNumber;
#        }
#    } // public String ConvertToBase(Long parLongToConvert)
#
#    int ConvertToInteger(Long parLong)
#    {
#        Integer integerConverted = 0;
#        String javaSpecialConversion = parLong.toString();
#        integerConverted = Integer.decode(javaSpecialConversion);
#        return integerConverted;
#    }
#}
