import random
from datetime import datetime, timedelta
from num2words import num2words as gn

def stringify(param):
    """
    Converts the input parameter to its string representation.

    Args:
        param (any): The input parameter to be converted to a string.

    Returns:
        str: The string representation of the input parameter.
    """
    return str(param)

def GenerateIdBig(InputLength):
    """
    Generates a random ID consisting of alphanumeric characters and special symbols.

    Args:
        InputLength (int): The desired length of the generated ID.

    Returns:
        str: The generated ID.
    """
    N = int(InputLength)
    alpha = '!@$%&?^⨏⨒⨝⫰⫯ɐÆʘʭ⁕⁑⁋⁊'
    numerics = '1234567890'
    alphabets = 'apenvituq'
    res = ''.join(random.choices(alphabets + alpha + numerics, k=N))
    generatedid = 'iSCC' + res
    return generatedid

def GenerateCuponId(CuponName):
    """
    Generates a coupon ID by combining the first character of the CuponName with a randomly generated alphanumeric string.

    Args:
        CuponName (str): The name of the coupon.

    Returns:
        str: The generated coupon ID.
    """
    N = 6
    alpha = '!@$%&?^⨏⨒⨝⫰⫯ɐÆʘʭ⁕⁑⁋⁊⩂⩆⩚⩙⩸⩳⩺⪀⩱⩩⪓⫍⫑'
    numerics = '1234567890'
    res = ''.join(random.choices(alpha + numerics, k=N))
    generatedid = CuponName[:1] + 'iSC' + res
    return generatedid

def GenerateBarId(length):
    """
    Generates a Bar Code ID by integers.

    Args:
        length (int): The Length of desired number.

    Returns:
        int: The generated Bar Code ID.
    """
    N = int(length)
    numerics = '1234567890'
    res = ''.join(random.choices(numerics, k=N))
    generatedid = res
    return generatedid

def GenerateDiscount():
    """
    Generates a random discount number between 5 and 99 (inclusive).

    Returns:
        int: The randomly generated discount number.
    """
    random_list = list(range(5, 100))
    discount = random.choice(random_list)
    return discount



# Date And Time
# Get the current date
current_date = datetime.now().date()
# Get the current time
current_time = datetime.now().time()
formatted_time_24 = current_time.strftime("%H:%M:%S")

def CurrentDate():
    """
    Returns the current correct Date
    """
    return current_date


def CurrentDateTime():
    """
    Returns the current date and time in the 12-hour format.
    """
    current_datetime = datetime.now()
    formatted_datetime_12 = current_datetime.strftime("%Y-%m-%d %I:%M:%S %p")
    return formatted_datetime_12


def CurrentTime12():
    """
    Returns the current time in the 12-hour format.
    """
    current_time = datetime.now().time()
    formatted_time_12 = current_time.strftime("%I:%M:%S %p")
    return formatted_time_12


def CurrentTime24():
    """
    Returns the Current Correct Time(24 hour format).
    """
    return formatted_time_24

# jump to specific date and time

def JumpToDate(days=None, months=None, years=None):
    """
    Jumps to a specific date based on the provided number of days, months, and years.

    Args:
        days (int, optional): The number of days to jump. Positive value to jump after days, negative value to jump before days. Defaults to None.
        months (int, optional): The number of months to jump. Positive value to jump after months, negative value to jump before months. Defaults to None.
        years (int, optional): The number of years to jump. Positive value to jump after years, negative value to jump before years. Defaults to None.

    Returns:
        datetime: The new date.
    """
    # Get the current date
    current_date = datetime.now().date()

    # Calculate the date difference
    date_difference = timedelta(
        days=days or 0,
        weeks=months * 4 if months is not None else 0
    )

    # Calculate the new date
    new_date = current_date + date_difference

    if years is not None:
        new_date = new_date.replace(year=new_date.year + years)

    return new_date


def JumpToTime_12(hours=None, minutes=None, seconds=None, milliseconds=None):
    """
    Jumps to a specific time based on the provided hours, minutes, seconds, and milliseconds.

    Args:
        hours (int, optional): Number of hours to jump. Defaults to None.
        minutes (int, optional): Number of minutes to jump. Defaults to None.
        seconds (int, optional): Number of seconds to jump. Defaults to None.
        milliseconds (int, optional): Number of milliseconds to jump. Defaults to None.

    Returns:
        str: The new time in 12-hour format ("%I:%M:%S %p").
    """
    # Get the current time
    current_time = datetime.now().time()
    
    # Calculate the time difference
    time_difference = timedelta(
        hours=hours or 0,
        minutes=minutes or 0,
        seconds=seconds or 0,
        milliseconds=milliseconds or 0
    )
    # Calculate the new time
    new_time = (datetime.combine(datetime.today(), current_time) + time_difference).time()
    # Format the new time in 12-hour format
    formatted_time = new_time.strftime("%I:%M:%S %p")
    # Return the result
    return formatted_time


def JumpToTime_24(hours=None, minutes=None, seconds=None, milliseconds=None):
    """
    Jumps to a specific time based on the provided hours, minutes, seconds, and milliseconds.

    Args:
        hours (int, optional): Number of hours to jump. Defaults to None.
        minutes (int, optional): Number of minutes to jump. Defaults to None.
        seconds (int, optional): Number of seconds to jump. Defaults to None.
        milliseconds (int, optional): Number of milliseconds to jump. Defaults to None.

    Returns:
        str: The new time in 24-hour format ("%H:%M:%S").
    """
    # Get the current time
    current_time = datetime.now().time()

    # Calculate the time difference
    time_difference = timedelta(
        hours=hours or 0,
        minutes=minutes or 0,
        seconds=seconds or 0,
        milliseconds=milliseconds or 0
    )
    # Calculate the new time
    new_time = (datetime.combine(datetime.today(), current_time) + time_difference).time()
    # Format the new time in 24-hour format
    formatted_time = new_time.strftime("%H:%M:%S")
    # Return the result
    return formatted_time

def numWordic(number):
    '''
    Generates the numertic form to International Word System

    Args:
        number (int): Desired number.

    Returns:
        str: Number in Words(International format).
    '''
    return gn(number=number)