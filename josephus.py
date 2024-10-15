"""
Assignment 6
Trinity Thompson tyt242
Marissa Shuchart ms87339

This program solves the Josephus problem using a circular linked list, determining the order in which soldiers
are eliminated from a circle until only one soldier remains.
"""
import sys

class Link:
  """
  This class represents a single link (node) in a circular linked list.
  """
  def __init__(self, data):
    """
    Initialize a new link with given data.
    """
    self.data = data # Soldier number
    self.next = None # Pointer to the next link (soldier)

class CircularList:
  """
  This class represents a circular linked list of soldiers.
  """
  # Constructor
  def __init__ ( self ):
    """
    Initialize the CircularList with no soldiers.
    """
    self.last = None # Points to the last node in the circular linked list

  def insert(self, data):
    """
    Insert a soldier at the end of the circular linked list.
    """
    new_link = Link(data)
    if self.last is None:
      # If the list is empty, point the new link to itself (circular)
      self.last = new_link
      self.last.next = self.last
    else:
      # Insert a new link and adjust the pointers to maintain the circular structure
      new_link.next = self.last.next
      self.last.next = new_link
      self.last = new_link

  def find(self, data):
    """
    Find the link with the given data, or return None if not found.
    """
    if self.last is None:
      return None # List is empty

    curr = self.last.next # Start from the first soldier
    while True:
      if curr.data == data:
        return curr # Soldier found
      curr = curr.next
      if curr == self.last.next:
        break # Circled back to the start
    return None # Soldier not found

  def delete(self, data):
    """
    Delete a link with a given data and return the link or return None if not found.
    """
    if self.last is None:
      return None # List is empty

    curr = self.last.next
    prev = self.last

    # Loop to find the link to delete
    while curr.data != data:
      if curr == self.last: # If we've checked the entire list
        return None
      prev = curr
      curr = curr.next

    # If there is only one link
    if curr == self.last and curr.next == self.last:
      self.last = None
    else:
      # Bypass the current link
      prev.next = curr.next
      if curr == self.last:
        self.last = prev # Updating last pointer if deleting last node

    return curr

  def delete_after(self, start, n):
    """
    Delete the nth Link starting from the Link start and return the data of the deleted link and the next link.
    """
    curr = start

    # Move n-1 steps to find the nth soldier
    for _ in range(n - 1):
      curr = curr.next

    # Delete the current soldier
    deleted_data = curr.data
    self.delete(curr.data)

    # Return the deleted soldier's data and the next soldier
    return deleted_data, curr.next

  def __str__(self):
    """
    Return a string representation of a Circular List.
    """
    if self.last is None:
      return "[]"

    curr = self.last.next
    result = []
    while True:
      result.append(str(curr.data))
      curr = curr.next
      if curr == self.last.next:
        break

    return "[" + ", ".join(result) + "]"

def main():
  # read number of soldiers
  line = sys.stdin.readline()
  line = line.strip()
  num_soldiers = int(line)

  # read the starting number
  line = sys.stdin.readline()
  line = line.strip()
  start_count = int(line)

  # read the elimination number
  line = sys.stdin.readline()
  line = line.strip()
  elim_num = int(line)

  # Create the circular linked list and populate with soldiers
  circular_list = CircularList()
  for soldier in range(1, num_soldiers + 1):
    circular_list.insert(soldier)

  # Find the starting soldier
  start_link = circular_list.find(start_count)

  # Print the elimination order
  curr_link = start_link
  for _ in range(num_soldiers - 1): # We need to elimate all but one soldier
    eliminated, curr_link = circular_list.delete_after(curr_link, elim_num)
    print(eliminated)

  # Print the last soldier remaining
  print(curr_link.data)

if __name__ == "__main__":
  main()
