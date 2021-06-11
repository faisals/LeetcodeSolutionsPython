''' 
2021-06-10 17:02:38
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

''' 

strs = ["flower","flow","flight", "fles", "flor"]
strs = ["dog","racecar","car","star"]
strs = ["a"]
strs=["ab", "a"]
strs = ["dog","racecar","car","star"]
strs = ["flower","flow","flight", "fles", "flor"]

def longestCommonPrefix(strs):

    common=""
    if "" in strs:
        common=""
    elif len(strs)==1:
        common=strs[0]
    else: 
        shortest_length=len(min((word for word in strs if word), key=len))

        print(shortest_length)

        # get all words of a certain length 
        shortest_length_strs=[word for word in strs if len(word) == shortest_length]

        print(shortest_length_strs)

        # get shortest word 
        shortest_length_word=shortest_length_strs[0]
        print(shortest_length_word)
        
        # loop over the shortest word 
        while shortest_length>0:
            for i, n in enumerate(strs):
                print('checking...', n)
                if shortest_length_word[:shortest_length] in n:
                    common=shortest_length_word[:shortest_length]
                    print('common:',common)
                else:
                    print('didnt find breaking now', n)
                    common=""
                    break 
            shortest_length=shortest_length-1
    print('in the end:', common)

longestCommonPrefix(strs)


