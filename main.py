contact_book = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except ValueError:
            return "The phone contains a letters!"
        except IndexError:
            return "Invalid command! Enter user name."
        except KeyError:
            return "Name doesn\'t exists."
    return inner


def hello_handler():
    print("How can I help you?")


@input_error
def add_handler(input_command_lower_case):
    input_command_list = input_command_lower_case.split()
    name, phone = input_command_list[1], input_command_list[2]
    if name.title() in contact_book.keys():
        return f'Name {name.title()} already exists.' \
                'Please use "change" command.'
    elif phone in contact_book.values():
        return f'Phone {phone} already exists. Please use "change" command.'
    else:
        title_name = name.title()
        phone = phone.removeprefix('+')
        if phone.isdecimal():
            contact_book[title_name] = phone
        else:
            print(int(phone))
    return 'Contact added!'


@input_error
def change_handler(input_command_lower_case):
    input_command_list = input_command_lower_case.split()
    name, phone = input_command_list[1], input_command_list[2]
    if name.title() not in contact_book.keys():
        return f'Name {name.title()} doesn\'t exists.' \
                'Please use "add" command.'
    elif phone in contact_book.values():
        return f'Phone {phone} already exists.' \
                'Please use "show all" to see all contacts.'
    else:
        title_name = name.title()
        phone = phone.removeprefix('+')
        if phone.isdecimal():
            contact_book[title_name] = phone
        else:
            print(int(phone))
    return 'Contact changed!'


@input_error
def phone_handler(input_command_lower_case):
    input_command_list = input_command_lower_case.split()
    name = input_command_list[1].capitalize()
    return contact_book.get(name, f'Name {name} doesn\'t exists.')


@input_error
def show_all_handler(contact_book):
    if len(contact_book) == 0:
        print(contact_book.pop('test'))
    else:
        for key, value in contact_book.items():
            print(f"Name: {key:<15} Phone: {value}")
        return contact_book


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
            elif input_cmd_lower_case[:6] == "change":
                print(change_handler(input_cmd_lower_case))
            elif input_cmd_lower_case[:5] == "phone":
                print(phone_handler(input_cmd_lower_case))
            elif input_command.lower() == "show all":
                print(show_all_handler(contact_book))
            else:
                print('=> Invalid command! <=')
            # print(contact_book)
    except KeyboardInterrupt:
        print("\nAbort the mission")
    finally:
        good_bye()


if __name__ == "__main__":
    main()
