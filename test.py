class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        num_list = []
        result = []
        char_result = []
        
        for i in s:
            num_list.append("{0:03d}".format(ord(i)))
            
            
        while len(num_list) > 0 :
            
            print(num_list, result)
            checked_number = num_list.pop(0)
            
            if checked_number in result:

                result_copy = result[:]
                
                result_copy.remove(checked_number)
                result_copy.append(checked_number)
                
                reverted_num = int("".join(result_copy))
                origin_num = int("".join(result))

                print(checked_number, origin_num, reverted_num, origin_num > reverted_num)

                if origin_num >=reverted_num:
                    result.remove(checked_number)
                    result.append(checked_number)
            
            else:
                result.append(checked_number)
    
        for j in result:
            char_result.append(chr(int(j)))
        
        print(char_result)
        return "".join(char_result)

        print(num_list)
        # print(chr(int("{0:03d}".format(ord("a")))))
        
        
        
answer = Solution()

answer.removeDuplicateLetters("bcabc")