# DATA STRUCTURE: a systematic way of organixing and accessing data

# FUNCTIONS

#1 CONSTANT FUNCTION = F(n) = C for some int c
#2 LOGARITHM FUNCTION = F(n) = logbN = x iff b^x = n
#3 LINEAR FUNCTION = F(n) = n
#4 NlogN FUNCTION = F(n) = n * log2n
#5 QUADRATIC FUN = f(n) = n^2
#6 CUBIC FUNCTION = f(n) = n^3
#7 EXPONENTIAL FUNCTION = f(n) = b^n where b = base and n in exponent


#ASYMPTOTIC ANALYSIS

# A QUADRATIC ALGO O(N^2)

# def pref(s):
#     n = len(s)
#     a = [0] * n
#     for j in range(n):
#         total = 0
#         for i in range(j + 1):
#             total += s[i]
#         a[j] = total / (j + 1)
#     return a

def pref(s):
    l = len(s)
    a = [0] * l
    for i in range(l):
        a[i] = sum(s[0 : i + 1]) / (i + 1)
    return a

print(pref([1,2,3,4,5]))


# A LINEAR TIME ALGO

def linear_pref(s):
    n = len(s)
    a = [0] * n
    total = 0
    for i in range(n):
        total += s[i]
        a[i] = total/ (i + 1)
    return a

print(linear_pref([1,2,3,4]))


#  THREE WAY SET DISJOINTNESS

""" check for intersection between 3 sets"""

def disjoint(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


#   CHECK FOR UNIQUENESS

def unique(s):
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True  #O(N^2)

def unique2(s):
    temp = sorted(s)
    for i in range(1, len(temp)):
        if temp[i - 1] == temp[i]:
            return False
    return True #O(nlogn)


print(unique2([22,3,4,5,2,1]))


''' SIMPLE JUSTIFICATION TECHNIQUES

      CONTRA ATTACK 
      INDUCTION
      LOOP INVARIANTS
      '''


def find(s, val):
    for i in range(len(s)):
        if s[i] == val:
            return i
    return -1


print(find("abcde", "e"))