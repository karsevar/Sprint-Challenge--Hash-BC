#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    # loop through the weights array (using the length variable to 
    # create the duration of the loop)
        # insert values within the hashtable 
        # keys will be weights[index] - limit 
        # values will be index 

    # create and additional for loop that will loop through the 
    # weights array using again length as the duration 
        # if retrieve(hashtable(weights[index])) does not return None 
            # return both index and the value within the hashtable

    for index in range(length):
        hash_table_insert(ht, (limit-weights[index]), index)

    for index_i in range(length):
        if hash_table_retrieve(ht, (weights[index_i])):
            index_j = hash_table_retrieve(ht, (weights[index_i]))
            if index_j > index_i:
                return [index_j, index_i]
            else:
                return [index_i, index_j]
    return None

weights_3 = [4, 6, 10, 15, 16]

answer_3 = get_indices_of_item_weights(weights_3, 5, 21)
print(answer_3)

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
