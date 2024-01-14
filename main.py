contact_book = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError:
            return "The phone contains a letters!"
        except IndexError:
            return "Invalid command!"
        except KeyboardInterrupt:
            return "AAAAAAAAAAAAAAAA"
    return inner


def hello_handler():
    print("How can I help you?")

@input_error
def add_handler(input_command_lower_case):
    input_command_list = input_command_lower_case.split()
    name, phone = input_command_list[1], input_command_list[2]
    # print(input_command_list[2])
    # print('Contact added!')
    if name.title() in contact_book.keys():
        # print(f'Name {name.title()} already exists. Please use "change" command')
        return f'Name {name.title()} already exists. Please use "change" command.'
    elif phone in contact_book.values():
        # print(f'Phone {phone} already exists. Please use "change" command')
        return f'Phone {phone} already exists. Please use "change" command.'
    else:
        title_name = name.title()
        phone = phone.removeprefix('+')
        if phone.isdecimal():
            contact_book[title_name] = phone
        else:
            # print("Not Digit")
            phone_int = int(phone)
            print(phone_int)
    # print(arg_dict)
    return 'Contact added!' # arg_dict


def change_handler(arg_name, arg_phone, arg_dict):
    lower_name = arg_name.lower()
    arg_dict[lower_name] = arg_phone
    return arg_dict


def phone_handler():
    pass


def show_all_handler(contact_book):
    for key, value in contact_book.items():
        print(f"Name: {key:<15} Phone: {value}")


def good_bye():
    print("Good bye!")


def main():
    try:
        while True:
            input_command = input('Enter your command: ')
            input_cmd_lower_case = input_command.lower()
            if input_cmd_lower_case in ("good bye", "close", "exit"):
                break
            elif input_cmd_lower_case == "hello":
                hello_handler()
            elif input_cmd_lower_case[:3] == "add":
                print(add_handler(input_cmd_lower_case))
            # elif input_command_list[0].lower() == "change":
            #     contact_book = change_handler(input_command_list[1], input_command_list[2], contact_book)
            #     print("Contact changed!")
            # elif input_command_list[0].lower() == "phone":
            #     print(f"{input_command_list[1]}\'s phone number is {contact_book.get(input_command_list[1])}")
            elif input_command.lower() == "show all":
                show_all_handler(contact_book)
            else:
                print('===>>>Invalid command!<<<===')
            print(contact_book)
    except KeyboardInterrupt:
        print("\nAbort the mission")
    finally:
        good_bye()


if __name__ == "__main__":
    main()
