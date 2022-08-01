async def check_cycle_in_list(input_list):
    '''
    logic to check the complete cycle in a list.
    * fetching the next index from current index array elelemt for each iteration
        * checking negative indices
        * checking index out of bound
    * marking current index as visited in a look up map
    * setting current index list value as current index itself till all the indices are visited 
    '''
    if not input_list:
        return False
    
    length_of_list = len(input_list)
    current_index = 0
    visited_index_lookup = {i: False for i in range(length_of_list)}
    
    while not visited_index_lookup.get(current_index):

        # if there is a negative index, then converting it to the equivalent positive index
        if current_index < 0:
            if (-1 * length_of_list <= next_index < 0):
                current_index = current_index % length_of_list
            else:
                # out of bound negative index
                return False
        
        if await index_out_of_bound(length_of_list, current_index):
            return False

        next_index = input_list[current_index]

        visited_index_lookup[current_index] = True
        current_index = next_index

    return False if False in set(visited_index_lookup.values()) else True

async def index_out_of_bound(length, index):
    return index > length - 1


# if __name__ == '__main__':
#     print(check_cycle_in_list([1,2,3]))
#     print(check_cycle_in_list([0,2,5]))
#     print(check_cycle_in_list([3,0,1,2]))
#     print(check_cycle_in_list([3,0,1,-3]))
#     print(check_cycle_in_list([0]))
#     print(check_cycle_in_list([1]))
#     print(check_cycle_in_list([-3]))
#     print(check_cycle_in_list([]))