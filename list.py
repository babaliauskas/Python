

# ADD
# .appernd() - add one item at the end of the list
# .extend() - add to the end of a list all values passed to extend([])
# .insert() - insert an item at a given position. (position, value)

# REMOVE
# .clear() - remove all items from the list
# .pop() - Remove the item at the given position in the list, and return it.
#        - If no index is specified, removes & returns last item in the list
#        - pop(index(optional))
# .remove() - remove the item from the list whose value is passed in.
#           - Throws a ValueError if the item is not found

# LEFT OVER
# .index() - return the index of the specified item in the list 
#          - index(value, starting position(optional), end position(optional))
# .count() - return the number if times x appears in the list
# .reverse() - reverse the elements of the list (in-place)
# .sort() - sort the items of the list (in-place)
# .join() - join elements into a starting 
#         - name = ['coding', 'is', 'fun']
#         - bla = ' '.join(name) # 'coding is fun
#         - bla = '. '.join(name) # 'coding. is. fun

# Slicing:
#   - make new lists using slices of the old list
#   - some_list[start:end:step]
#   - num = [1, 2, 3, 4]
#   - num[1:] # [2, 3, 4]
#   - num[3:] # [4]
#   - num[-1:] # [4]
#   - num[-3:] # [2, 3, 4]
#   - Second Parameter :end - the index to copy to (exclusive counting)
#   - num[:2] # [1,2]
#   - num[1:2] # [2,3]
#   - Third Parameter :step - 'step' is the number to count at a time
#   - num[1::2] # [2,4]
#   - num[::2] # [1,3]
#   - num[1::-1] # [2,1]
#   - num[:1:-1] # [4,3]
#   - num[2::-1] # [2,1]

# Swapping:
#   - num = [1,2,3,4]
#   - num[1],num[2] = num[2],num[1] # [1,3,2,4]