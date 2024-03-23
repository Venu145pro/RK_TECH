#A python program to convert numbers into words upto a million

def spell_number(number):
    # Define words for numbers 0 to 19
    words_0_to_19 = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
    ]
    
    # Define words for tens
    tens_words = [
        '', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'
    ]
    
    # Handle the non-positive integers
    if number == 0:
        return 'zero'
    elif number < 0:
        return 'minus ' + spell_number(-number)
    
    # handle the numbers less than 100
    elif number < 100:
        if number < 20:
            return words_0_to_19[number]
        else:
            tens = number // 10
            ones = number % 10
            return tens_words[tens] + ('' if ones == 0 else '-' + words_0_to_19[ones])
    
    # handle the numbers less than 1000
    elif number < 1000:
        hundreds = number // 100
        remainder = number % 100
        return words_0_to_19[hundreds] + ' hundred' + ('' if remainder == 0 else ' and ' + spell_number(remainder))
    
    # handle the numbers up to a million
    elif number < 1000000:
        thousands = number // 1000
        remainder = number % 1000
        return spell_number(thousands) + ' thousand' + ('' if remainder == 0 else ' ' + spell_number(remainder))
    
    # handle up to a billion
    elif number < 1000000000:
        millions = number // 1000000
        remainder = number % 1000000
        return spell_number(millions) + ' million' + ('' if remainder == 0 else ' ' + spell_number(remainder))
       
number=int(input("enter a number:"))#taking input from user
words=spell_number(number)
print(words)
