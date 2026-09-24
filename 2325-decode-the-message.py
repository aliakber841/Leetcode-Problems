class Solution(object):
    def decodeMessage(self, key, message):
        hash_table={}
        alphabets="abcdefghijklmnopqrstuvwxyz"
        letter_index=0
        for i in range(len(key)):
            current_char=key[i]
            if current_char==" ":
                continue
            if current_char not in hash_table:
                hash_table[current_char]=alphabets[letter_index]
                letter_index+=1
        
        result=""
        for i in range(len(message)):
            current_char=message[i]
            if current_char==" ":
                result+=" "
            else:
                result+=hash_table[current_char]
        
        return result