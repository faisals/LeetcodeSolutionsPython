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
    
    # check if there is a null 
    if "" in strs:
        common=""
    
    # check if there is only one element in the array 
    elif len(strs)==1:
        common=strs[0]
    
    else: 
        # get the length of the shortest word(s)
        shortest_length=len(min((word for word in strs if word), key=len))
        print('shortest length word is of size:', shortest_length)

        # get all words of a certain length 
        shortest_length_strs=[word for word in strs if len(word) == shortest_length]

        print('printing all words with shortest len', shortest_length_strs)

        # chosing a random shortest word 
        shortest_length_word=shortest_length_strs[0]
        print('chosing a random shortest word to play around with:', shortest_length_word)

        # loop over the shortest word 
        while shortest_length>0:

            word_to_test=shortest_length_word[:shortest_length]
            print('word is now:', word_to_test)

            # keep total matches found 
            total_matches_found=0


            # looping over all the words 
            for i, n in enumerate(strs):

                print('checking word: ', n)
                if word_to_test in n:
                    print('full match found, going to the next word')
                    common=word_to_test
                    if total_matches_found<len(strs): 
                        total_matches_found=total_matches_found+1
                        print('total matches found:', total_matches_found)
                    else:
                        print('total matches found:', total_matches_found)
                        #return common
                else:
                    print('didnt find matching, breaking here: ', n)
                    common=""
                    total_matches_found=0
                    break 
            shortest_length=shortest_length-1
    print('in the end:', common)

longestCommonPrefix(strs)


