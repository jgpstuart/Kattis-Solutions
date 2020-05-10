answer = ""
beg = 1

try: 
    while True:
        pattern = str(input())
        test = str(input())
        for i in range(0,len(test)):
            found_at = test.find(pattern, beg)
            beg = found_at + 1
            if found_at != -1:
                answer += str(found_at) + " "
            else:
                break
        print(answer)
        answer = ""
except EOFError:
    pass
