convertFrom = input( "Please type the initials of the converted type as fallows:"
                     "\nmilimeters = mm\ncentimeters = cm\nmiles = mi\ninches = in\nkilometers = km\nfeet = ft\nyards = yd\nmeters = m\n" ).lower()
convertTo = input( "What is the type you wish to convert to as fallows:"
                   "\nmilimeters = mm\ncentimeters = cm\nmiles = mi\ninches = in\nkilometers = km\nfeet = ft\nyards = yd\nmeters = m\n" ).lower()
convertedValue = float( input( "Value for converting = " ) )


def convert_meters(self):
    if str( convertFrom ) == "mm":
        return convertedValue / 1000
    elif str( convertFrom ) == "cm":
        return convertedValue / 100
    elif str( convertFrom ) == "mi":
        return convertedValue / 0.000621371192
    elif str( convertFrom ) == "in":
        return convertedValue / 39.3700787
    elif str( convertFrom ) == "km":
        return convertedValue * 1000
    elif str( convertFrom ) == "ft":
        return convertedValue / 3.2808399
    elif str( convertFrom ) == "yd":
        return convertedValue / 1.0936133
    elif str( convertFrom ) == "m":
        return convertedValue


def meters_to_all(self):
    if str( convertTo ) == "mm":
        return self * 1000
    elif str( convertTo ) == "cm":
        return self * 100
    elif str( convertTo ) == "mi":
        return self * 0.000621371192
    elif str( convertTo ) == "in":
        return self * 39.3700787
    elif str( convertTo ) == "km":
        return self * 0.001
    elif str( convertTo ) == "ft":
        return self * 3.2808399
    elif str( convertTo ) == "yd":
        return self * 1.0936133
    elif str( convertTo ) == "m":
        return self * 1


resultInMeters = convert_meters( convertedValue )

resultInAll = meters_to_all( resultInMeters )

print( "{:0.3f} {:s} = {:0.3f} {:s}".format(convertedValue,convertFrom, resultInAll, convertTo) )
