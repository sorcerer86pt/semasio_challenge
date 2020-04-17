import argparse
import sys
import logging


# some helper constants
program_description = 'This program will given an number array return , \
find the maximum product between two numbers from the array, that is a multiple of 3.'
version = "0.0.1"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

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

    if (len(valueArray) == 0 or len(valueArray) == 1):
        raise ValueError("Insufficient number of values")

    # sort the array in reverse order (greater values first)
    sorted_array = sorted(valueArray, reverse=True)
    greatestMultipleThree = 0

    # since the array is already sorted from greatest to least the first multiple of 3 we find is the greater one
    for number in sorted_array:
        if number % 3 == 0:
            greatestMultipleThree = number
            break

    # After getting the greatest number that is already a multiple of 3, remove it from the array
    # so that in the next step, we don't by mistake or happenstance return it at the second value in
    # the tuple
    if greatestMultipleThree > 0:
        sorted_array.remove(greatestMultipleThree)

    return (greatestMultipleThree, sorted_array[0])


if __name__ == "__main__":
    main()
