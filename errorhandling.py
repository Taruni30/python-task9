#error handling
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
class negativeError(Exception):
    pass
def divide_numbers(a, b):
    try:
        logging.info("Starting division operation")

        if a < 0 or b < 0:
            raise negativeError("Negative numbers are not allowed")
        result = a / b

    except ZeroDivisionError as e:
        logging.error("Division by zero error", exc_info=True)
        print("Error: Cannot divide by zero")

    except TypeError as e:
        logging.error("Invalid data type used", exc_info=True)
        print("Error: Please enter numbers only")

    except negativeError as e:
        logging.warning(str(e))
        print(f"Custom Error: {e}")

    except Exception as e:
        logging.critical("Unexpected error occurred", exc_info=True)
        print("Unexpected error occurred")

    else:
        logging.info("Division successful")
        print("Result:", result)

    finally:
        logging.info("Execution completed\n")

if __name__ == "__main__":
    divide_numbers(10, 2)    
    divide_numbers(10, 0)     
    divide_numbers(10, "a")  
    divide_numbers(-5, 2)    