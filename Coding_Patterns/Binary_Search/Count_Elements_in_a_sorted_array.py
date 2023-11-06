import First_and_last_occurence_of_element
def count( arr  , ele):
    low = First_and_last_occurence_of_element.first_occur(arr, ele)
    high = First_and_last_occurence_of_element.last_occur(arr, ele)
    if low == -1 :
        return 0
    return high - low + 1
    
