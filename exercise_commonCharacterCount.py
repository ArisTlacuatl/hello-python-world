'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
'''

def solution(s1, s2):
    common_chars = 0
    s3 = s2
    for let in s1:
        print('looking for the character:',let)
        print('is present in this string?:', s3)
        for i in range(0,len(s3)):
            print('character in s2:',s3[i])
            if let == s3[i]:
                common_chars += 1
                s3 = s3[:i]+s3[(i+1):]
                print(s3)
                break
            #else:
             #   pass
    print (common_chars)    
    return common_chars

s1 = 'abca'
s2 = 'xyzbac'
solution(s1,s2)