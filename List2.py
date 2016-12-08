# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
    newnum = []
    temp = []
    counter = 1
    for x in nums:
        if counter == 1:
            counter = counter+1
            temp.append(x)
            y = x
            continue
        else:
            if y == x:
                continue
            else:
                temp.append(x)
                y = x
    return temp

def remove_adjacent1(nums):
    x=1
    y = len(nums)
    while x < y :
        if nums[x] == nums[x-1]:
            del nums[x]
            y = y - 1
        else:
            x = x+ 1
    return(nums)

# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
  list3 = list1 + list2
  print (list3)
  return (sorted(list3))

def linear_merge2(l, r):
    result = []
    while l and r:
        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    result+=(l+r)[::]

    return result

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))



# Calls the above functions with interesting inputs.
def main():
  print('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])

  print()
  print('remove_adjacent1')
  test(remove_adjacent1([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent1([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent1([]), [])
  print()
  print('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])
  print()
  print('linear_merge2')
  test(linear_merge2(['11', '88', '88'], ['88']),
       ['11', '88', '88', '88'])
  test(linear_merge2(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge2(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
      main()