class Solution(object):
    def mapWordWeights(self, words, weights):
        hash_table={}
        alphabets="abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alphabets)):
            hash_table[alphabets[i]]=i

        result=""
        for i in range(len(words)):
            current_word=words[i]
            word_weight=0
            for j in range(len(current_word)):
                current_char=current_word[j]
                char_position=hash_table[current_char]
                word_weight+=weights[char_position]
            remainder=word_weight%26
            result+=alphabets[25-remainder]
        return result