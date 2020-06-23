package net.marcushall.ctv;

public class ConversionTable
{
    String ConvertDigits(int parIntegerToConvert)
    {
        //	String Digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" ;
        //		String Digits = "!#$%&'+,-0123456789;=@^_`abcdefghijklmnopqrstuvwxyz~€ƒ†‡ˆ•”˜ˆ‘’" ;
        //		String Digits = "!#$%&'0123456789-,;@^ˆ_`~˜”+=†‡•‰€abcdefƒghijklmnopqrstuvwxyz" ;
        String Digits = "0123456789abcdefghijklmnopqrstuvwxyz";
        //     Digits = "12345678901234567890123456789012345678901234567890123456789012";

        return Digits.substring(parIntegerToConvert, parIntegerToConvert + 1);
    } // public String ConvertDigits(Long parIntegerToConvert)

    public String ConvertToBase(Long parLongToConvert)
    {
        String newBaseNumber = "";

        if (parLongToConvert <= 35)
        {
            int integerToConvert = ConvertToInteger(parLongToConvert);
            return ConvertDigits(integerToConvert);
        }

        else
        {
            Long notRemainder = 0L;
            notRemainder = parLongToConvert % 36;
            notRemainder = (parLongToConvert - notRemainder) / 36;
            newBaseNumber = ConvertToBase(parLongToConvert - (notRemainder * 36));
            return ConvertToBase(notRemainder) + newBaseNumber;
        }
    } // public String ConvertToBase(Long parLongToConvert)

    int ConvertToInteger(Long parLong)
    {
        Integer integerConverted = 0;
        String javaSpecialConversion = parLong.toString();
        integerConverted = Integer.decode(javaSpecialConversion);
        return integerConverted;
    }
}