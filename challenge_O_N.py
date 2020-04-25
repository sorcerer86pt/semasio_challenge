import argparse
import sys
import logging


# some helper constants
program_description = 'This program will given an number array return , \
find the maximum product between two numbers from the array, that is a multiple of 3.'
version = "0.0.1"


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('program.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(handler)


def preparaParser():
    parser = argparse.ArgumentParser(description=program_description)
    parser.add_argument("-V", "--version",
                        help="Show Program version", action="store_true")
    args = parser.parse_args()

    if args.version:
        sys.stdout.write("Version: {}\n".format(version))


def main():
    preparaParser()
    values = readInput()
    logger.info("Values read: %s", values)

    if len(values) == 0 or len(values) == 1:
        msg = "Mininum number of values was not given!!"
        logger.error(msg)
        sys.stderr.write(msg)
    elif len(values) == 2:
        logger.info(
            "Only 2 number given, checking if either is a multiple of 3 to give response.")

        if values[0] % 3 == 0 or values[1] % 3 == 0:
            result = values[0] * values[1]
            result_str = "Result: {}".format(result)
            logger.info(result_str)
            sys.stdout.write(result_str)
        else:
            msg = "None of the 2 number were multiple of 3, no value can be give!!"
            logger.error(msg)
            sys.stderr.write(msg)
    else:
        mult_values = getMultiplicationValues(values)
        mult_value_three = int(mult_values[0])

        if mult_value_three == 0:
            logger.error(
                "None of the numbers were multiple of 3, no value can be give!!")
        else:
            result = int(mult_values[0]) * int(mult_values[1])
            result_str = "Result: {}".format(result)
            logger.info(result_str)
            sys.stdout.write(result_str)

    sys.exit(0)


def readInput():
    """ This function will read the list of numbers from the user
    and then convert it to a integer array
    """

    valueString = str(input())
    valueArray = [int(x) for x in valueString.split()]
    return valueArray


def getMultiplicationValues(valueArray):
    """ This function will return the greatest multiple of 3 in that array and then
    the greatest other values remaining in the array

    :param valueArray: An array of numbers from we need to get the values
    :returns: An tuple for which the first value is the greatest multiple of 3 in the valueArray and then the other greatest number.
    :raises: ValueError if insufficient values in array are passed.
    """

    # Greatest number that is divisible by 3
    max_divisible_3 = -1
    # Greatest number aside from max_divisible_3
    max_otherwise = -1

    if len(valueArray) <= 2:
        raise ValueError("Insufficient number of values")

    """
        Go for each number in the array
        If the number is divisible by 3 and is greater than max_divisible_3 then we update max_divisible_3
         Special consideration must be made to also update max_otherwise with the old max_divisible_3 if it is greater that the actual max_otherwise, for the case when 3 numbers that are divisoble by 3 are the greatest. 
         Otherwise if the number is just greater than max_otherwise, we update it
        At the end we get the max number that is divisible by 3 and the other maximun value
        This guarantees that the resulting number that is obtained by multiplying this number is the greatest number that can be obtained that is a multiple of 3 
        Since we only do 1 array pass, this results in a O(N) complexity algorithm
    """

    for value in valueArray:
        logger.info("Checking value %d", value)
        if value % 3 == 0 and value > max_divisible_3:
            old_multiple_3 = max_divisible_3
            max_divisible_3 = value
            logger.info("Changed max divisible multiple of 3 to %d",
                        max_divisible_3)

            # check if the previous  max_divisble_3 is greater than max_othewise and update it with old max_divisible_3
            # This avoids the problem of having 2 multiples of 3 that are also the greatest values not being used
            if (old_multiple_3 > max_otherwise):
                max_otherwise = old_multiple_3
        elif value > max_otherwise:
            max_otherwise = value
            logger.info(
                "Change max value not divisible to 3 to %d", max_otherwise)

    return(max_divisible_3, max_otherwise)


if __name__ == "__main__":
    main()
