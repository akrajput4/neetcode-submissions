class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 ={}
        dict2 ={}
        for item in s:
            if dict1.get(item):
                dict1[item] = dict1.get(item) + 1
            else:
                dict1[item] = 1

        for item in t:
            if dict2.get(item):
                dict2[item] = dict2.get(item) + 1
            else:
                dict2[item] = 1

        # print(dict1)
        # print(dict2)   
        if dict1 == dict2:
            return True
        return False         

        