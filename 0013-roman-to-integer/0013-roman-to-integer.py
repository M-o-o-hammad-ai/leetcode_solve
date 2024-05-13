class Solution(object):
   def romanToInt(self,s):
    value_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    first = 0
    prev_value = 0
    
    for char in s:
        value = value_dict[char]
        first += value
        
        if value > prev_value:
            first -= 2 * prev_value
        
        prev_value = value
        
    return first

