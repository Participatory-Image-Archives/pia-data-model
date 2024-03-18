#!/usr/bin/env python3

# Copyright @ 2015-2021 Data and Service Center for the Humanities (DaSCH)
#
# This file is part of DSP.
#
# DSP is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DSP is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public
# License along with DSP.  If not, see <http://www.gnu.org/licenses/>.


#################################################################################################
# Functions for generating and validating check codes for base64url-encoded IDs. The algorithm
# is based on org.apache.commons.validator.routines.checkdigit.ModulusCheckDigit.


# The base64url alphabet (without padding) from RFC 4648, Table 2.
base64url_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
base64url_alphabet_length = len(base64url_alphabet)


class CheckDigitException(Exception):
    def __init__(self, message):
        self.message = message


# Checks whether a code with a check digit is valid.
def is_valid(code):
    if code is None or 0 == len(code):
        return False

    try:
        modulus_result = calculate_modulus(code, True)
        return modulus_result == 0
    except CheckDigitException:
        return False


# Calculates the check digit for a code.
def calculate_check_digit(code):
    if code is None or 0 == len(code):
        raise CheckDigitException("No code provided")

    modulus_result = calculate_modulus(code, False)
    char_value = (base64url_alphabet_length - modulus_result) % base64url_alphabet_length
    return to_check_digit(char_value)


# Calculates the modulus for a code.
def calculate_modulus(code, includes_check_digit):
    length = len(code)

    if not includes_check_digit:
        length += 1

    total = 0
    i = 0

    while i < len(code):
        right_pos = length - i
        char_value = to_int(code[i])
        total += weighted_value(char_value, right_pos)
        i += 1

    if total == 0:
        raise CheckDigitException("Invalid code: {}".format(code))

    return total % base64url_alphabet_length


# Calculates the weighted value of a character in the code at a specified position.
def weighted_value(char_value, right_pos):
    return char_value * right_pos


# Converts a character at a specified position to an integer value.
def to_int(char):
    char_value = base64url_alphabet.find(char)

    if char_value == -1:
        raise CheckDigitException("Invalid base64url character: '{}'".format(char))

    return char_value


# Converts an integer value to a check digit.
def to_check_digit(char_value):
    if char_value < 0 or char_value >= base64url_alphabet_length:
        raise CheckDigitException("Invalid character value: {}".format(char_value))

    return base64url_alphabet[char_value]