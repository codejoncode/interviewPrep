import math
def repeatedString(s, n):
    """
    Lilah has a string, s, of lowercase English letters that she
    repeated infinitely many times. Given an integer, n find and
    print the number of letter a's in the first n letters of Lilahs
    infinite string. 

    for example, if the string s == 'abcac' and n = 10, the substring we considere is abcacabcac, the first 10 characters of her 
    infinite string. There are 4 occurrences of a in the substring.  

    Function Description 
    Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a
    in the prefix of length n in the infinitely repeating string. 

    repeatedString has the following parameter(s):
    s: a string to repeat
    n: the number of characters to consider  

    The first line contains a single string s 
    the second line contains an integer n 

    first get the string together but adding the characters to a new string until that string equals the 
    length. 

    then count the occurrences of a. 
    """
    # return n if s equals 'a'
    if s == "a":
      return n
    
    #get the max_amount of times the string can come together. 
    max_amount = math.floor(n / len(s))
    # check if len of s divides evenly into n 
    if n % len(s):
      #if it does not we will have some extra meaning the number of times we can 
      #bring the string together is a float  say  3.33 
      #So grabing the number of "a" within the shortened version of the string is neccessary
      extra = s[:n%len(s)].count("a")
      #return the max_amount of times multipled by the count of a in the string plus the extra 
      return int(s.count("a") * max_amount) + extra
    else: 
      #return the max_amount of times multipled by the count of a
      return int(s.count("a") * max_amount) 
#end of repeatedString function


print(repeatedString("aba", 10))

# print(repeatedString("a", 1000000000000))


print(repeatedString("kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm", 736778906400))

print(repeatedString("epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq", 549382313570))

#1,000,000,000,000
