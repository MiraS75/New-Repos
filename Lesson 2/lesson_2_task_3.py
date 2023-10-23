import math

# Define the square function to calculate the area of a square
def square(side):
    # Check if the side is an integer
    if isinstance(side, int):
        # If it's an integer, calculate the area
        return side * side
    else:
        # If it's not an integer, round up the result and return it
        return math.ceil(side * side)

# Example usage with an integer side
side_int = 5
result_int = square(side_int)
print(f"The area of a square with side {side_int}: {result_int}")

# Example usage with a floating-point side
side_float = 3.5
result_float = square(side_float)
print(f"The area of a square with side {side_float}: {result_float}")