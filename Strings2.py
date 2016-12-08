# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
  if len(s) < 3:
      return s
  else:
      if s[len(s)-3:] == 'ing':
          return s+'ly'
      else:
          return s+"ing"

# E. not_bad
#  Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    a=-1
    b=-1
    a = s.find("not")
    if a!= -1:
        b= s.find('bad',a)
    if a != -1:
        if b!= -1:
            return(s[:a:]+"good"+ s[b+3:])
        else:
            return(s)
    else:
        return(s)
    return
# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back

def front_back(a, b):
        a1,a2,b1,b2= '','','',''
        sp= int(len(a)/2)
        if len(a)%2 ==0:
            a1 = a[:sp]
            a2 = a[sp:]
        else:
            a1= a[:sp+1]
            a2=a[sp+1:]

        sp = int(len(b) / 2)
        if len(b) % 2 == 0:
            b1 = b[:sp]
            b2 = b[sp:]
        else:
            b1 = b[:sp + 1]
            b2 = b[sp+1:]


        return a1+b1+a2+b2


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')
  print()
  print("not_bad")
  test(not_bad('testing is not bad'),'testing is good')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")
  print()
  print('front_back')
  test(front_back('1234','abcde'),'12abc34de')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')
if __name__ == '__main__':
  main()
