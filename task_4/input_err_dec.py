
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Please provide a name and phone number along with command (e.g. add Jane 8099640..)"
        except IndexError:
            return "Enter the argument for the command."
    return inner