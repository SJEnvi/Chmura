import base64
import secrets
import string
import logging


lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_char = string.punctuation
# sum of string library resources, which will create our alphabet to password generator
alphabet = lowercase_letters + uppercase_letters + digits + special_char
pwd_length = 10


def encode(string):
    """Function encoding string, take in string, converts it to bytes, encodes using base64, then decodes bytes back to
    string and return result"""
    string_in_bytes = str.encode(string)
    return base64.standard_b64encode(string_in_bytes).decode()


def decode(string):
    """Function decoding string, take in string, converts it to bytes, decodes using base64, then decodes bytes back to
        string and return result"""
    string_in_bytes = str.encode(string)
    return base64.standard_b64decode(string_in_bytes).decode()


def pwd_generator():
    """Function do not take in argument, generate defined length random password based on alphabet from string library
     then checks if password is compliant with security policy. Returns string """
    password_secure = False
    while password_secure is not True:
        pwd = ""
        for i in range(pwd_length):
                pwd += "".join(secrets.choice(alphabet))
        if any(char in lowercase_letters for char in pwd) and any(char in digits for char in pwd) and any(
            char in special_char for char in pwd) and any(char in uppercase_letters for char in pwd) == True:
            password_secure = True
    return pwd


def create_logs():
    logging.info("I inform you that your rent is due to tomorrow")
    logging.warning("Don't be late again!")
    logging.debug("Let's go and find some more bugs")
    logging.error("Opps... Something broke")


def log_return(log_level):
    logger = logging.getLogger()
    logger.setLevel(log_level.upper())
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s')
    create_logs()




def main():
    is_on = True
    while is_on:
        choice = input("Please select the function (encode/decode/password generator/logs) or type quit to exit: ").lower()
        if choice == "exit":
            is_on = False
        elif choice == "encode":
            not_encoded_text = input("Please enter text you would like to encode: ")
            print(encode(not_encoded_text))
        elif choice == "decode":
            not_decoded_text = input("Please enter text you would like to decode: ")
            print(decode(not_decoded_text))
        elif choice == "password generator":
            print(pwd_generator())
        elif choice == "logs":
            log_return(input("Choose log level: "))
        else:
            print("There is no such function... Choose again")


if __name__ == '__main__':
    main()
