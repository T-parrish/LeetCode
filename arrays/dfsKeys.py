# There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

# Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.

# Initially, all the rooms start locked (except for room 0). 

# You can walk back and forth between rooms freely.

# Return true if and only if you can enter every room.

class Solution(object):
  def canVisitAllRooms(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    stack = [0]
    has_key = [False] * len(rooms)
    has_key[0] = True

    while stack:
      # gets the value and removes it from array
      node = stack.pop()
      for key in rooms[node]:
        # track which rooms have been seen
        if not has_key[key]:
          has_key[key] = True
          # add the keys from the new room to the stack
          stack.append(key)


    return all(has_key)