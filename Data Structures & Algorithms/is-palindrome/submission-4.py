class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.lower()
        first_index = 0
        last_index = len(s) -1
        print(first_index)
        print(last_index)
        print(len(s)/2)

        while first_index <  last_index:
            
            if (s[first_index] <= 'z' and s[first_index] >="A") or (s[first_index] >='0' and s[first_index] <="9"):
                print("first",s[first_index])
            else:
                first_index = first_index + 1
                continue


            if (s[last_index] <= 'z' and s[last_index] >="A") or (s[last_index] >='0' and s[last_index] <="9"):
                print("lst",s[last_index])
            else:
                print("Ccc")
                last_index = last_index - 1
                continue


            print(first_index,last_index)
            if s[first_index] == s[last_index]:
                first_index = first_index + 1
                last_index = last_index - 1
            else: 
                return False

        return True                






        