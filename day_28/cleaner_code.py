class Arithmetic:
    """
    A class to perform basic arithmetic operations on two integers.
    """

    def __init__(self, x: int = 5, y: int = 10):
        """
        Initialize the Arithmetic class with two integers.
        
        Args:
            x (int): First number. Defaults to 5.
            y (int): Second number. Defaults to 10.
        """
        self.x = x
        self.y = y

    def addition(self) -> int:
        """
        Return the sum of x and y.
        """
        return self.x + self.y

    def multiplication(self) -> int:
        """
        Return the product of x and y.
        """
        return self.x * self.y


def greet(name: str) -> str:
    """
    Return a greeting message for the given name.

    Args:
        name (str): The user's name.

    Returns:
        str: Greeting message.
    """
    return f'Hello, {name}'


def check_age(age: int) -> str:
    """
    Check the age group based on the given age.

    Args:
        age (int): The age to evaluate.

    Returns:
        str: Category message - Minor, Adult, or Senior Citizen.
    """
    if age < 18:
        return 'You are a Minor'
    elif age < 60:
        return 'You are an Adult'
    else:
        return 'You are a Senior Citizen'


def main() -> None:
    """
    Main function to demonstrate the usage of Arithmetic, greet, and check_age functions.
    """
    arithmetic = Arithmetic()

    numbers_sum = arithmetic.addition()
    numbers_product = arithmetic.multiplication()

    print(f'Sum of two numbers is: {numbers_sum} and their product is: {numbers_product}')
    print(f'{greet("Jay")} {check_age(24)}')


if __name__ == "__main__":
    main()


    