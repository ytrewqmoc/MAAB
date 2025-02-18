def insert_underscores(txt):
    vowels = "aeiou"
    result = ""
    count = 0
    i = 0
    while i < len(txt):
        result += txt[i]
        count += 1  
        if count % 3 == 0 and i != len(txt) - 1:
            if txt[i] in vowels or (len(result) > 1 and result[-2] == "_"):
                result += txt[i + 1]
                result += "_"
                i += 1  
            else:
                result += "_"
        i += 1  
    return result
print(insert_underscores("dhjfkgrufhdkshjfrueashdlkfhfieahuelksahdlisauhfr"))
print(insert_underscores("geyfoqawhfeyowdanicfebofawnibfeudjnclshfburaijbbei"))