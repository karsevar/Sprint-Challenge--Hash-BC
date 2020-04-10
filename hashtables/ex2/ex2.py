#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """

    # loop through the tickets array:
        # insert each element into hashtable with 
        # source as the key and destination as the value 

    # initialize current key variable with NONE

    # loop through the tickets array again with a for loop 
    # with a duration of length 
        # insert key value within route array through route[index] = current_key 
        # find the next key in the hashtable 
    
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    current_key = 'NONE'

    for index in range(length):
        current_key = hash_table_retrieve(hashtable, current_key)
        route[index] = current_key

    return route[:-1]

ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]
result = reconstruct_trip(tickets, 3)
print(result)