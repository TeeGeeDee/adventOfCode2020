
from typing import List, Callable

def validate_passwords(params_and_passwords: List[str],rule_func: Callable):
    """
    Given list of strings representing password with rule parameterisation, 
    return list of bools of validity of passwords

    Parameters
    ----------
    params_and_passwords : list of str
        strings are of the form "l-u l: p" where
            l is lower number
            u is upper number
            l is letter
            p is the  password (sequence of letters)
    rule_func : function
        function that takes in letter,lower,upper,password and outputs bool

    Returns
    -------
    is_valid : list of bools

    """
    params_pwds = [x.split(': ') for x in params_and_passwords]
    is_valid = [rule_func(params[-1],*params[:-2].split('-'),pwd) for params,pwd in params_pwds]
    return is_valid

def rule1(letter: str,lower: str,upper: str,password: str):
    return int(lower) <= password.count(letter) <= int(upper)

def rule2(letter: str,lower: str,upper: str,password: str):
    return (password[int(lower)-1]==letter) + (password[int(upper)-1]==letter) == 1

if __name__ == "__main__":

    with open("data.txt", "r") as f:
        passwords_with_params = [x.rstrip('\n') for x in f.readlines()]

    print('The number of valid passwords by rule 1 is {0}'.format(sum(validate_passwords(passwords_with_params,rule1))))
    print('The number of valid passwords by rule 2 is {0}'.format(sum(validate_passwords(passwords_with_params,rule2))))
