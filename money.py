"""
Author : Cedric Le Gall
"""

def decompose_cash(cash:int) -> tuple:
    """
    Decompose number into simple numbers ex 485 : 400 + 80 + 5 
    """
    
    str_cash:str            = str(cash)
    output_buffer:list(int) = []
    
    for index, extract_number in enumerate(list(reversed(str_cash))):
        extract_number:int = int(extract_number)        
        wheigh:int         =  10 ** index
        
        if index == 0:
            output_buffer.append(extract_number)   
            continue
        
        output_buffer.append(extract_number * wheigh)

    return tuple(reversed(output_buffer))


def return_money(cash:int) -> dict:
    """
    Return None if it's impossible to return money with only 2, 5 or 10 €
    """    
    if cash < 2: return None

    cash_return_to_client = {
        "two":  0,
        "five": 0,
        "ten":  0
    }
    
    if cash == 2:
        cash_return_to_client["two"] = 1
        return cash_return_to_client
    
    if cash == 5:
        cash_return_to_client["five"] = 1
        return cash_return_to_client

    if cash == 10:
        cash_return_to_client["ten"] = 1
        return cash_return_to_client

    if cash % 10 == 0: 
        cash_return_to_client["ten"] = int(cash / 10)
        return cash_return_to_client    

    decomposed_cash:tuple = decompose_cash(cash)
    
    for money in decomposed_cash[:-1]:
        cash_return_to_client["ten"] += int(money / 10)
    
    last_cash:int = decomposed_cash[-1]

    if last_cash == 5:
        cash_return_to_client["five"] += 1
        return cash_return_to_client

    while last_cash >= 2:

        if (last_cash - 5) > 0:
            last_cash -= 5
            cash_return_to_client["five"] += 1
            
        else:
            last_cash -= 2
            cash_return_to_client["two"] += 1

    if last_cash > 0: return None

    return cash_return_to_client

print("1", return_money(1))
print("3", return_money(3))
print("4", return_money(4))
print("42", return_money(42))
print("43", return_money(43))
print("996354687", return_money(996354687))
print("100", return_money(100))
