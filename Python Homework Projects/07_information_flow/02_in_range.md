<!-- Problem Statement
Implement the following function which takes in 3 integers as parameters:

def in_range(n, low, high) """ Returns True if n is between low and high, inclusive. high is guaranteed to be greater than low. """ -->


def in_range(n, low, high):
  """
  Returns True if n is between low and high, inclusive. 
  high is guaranteed to be greater than low.
  """
  if n >= low and n <= high:
	    return True

  return False



def main():
    print(in_range(10, 0, 10))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()