# def pig_it(text):
#     return " ".join(x[1:] + x[0] + "ay" if x.isalnum() else x for x in text.split())

def pig_it(text):
    """
    Move the first letter of each word to the end of it,
    then add "ay" to the end of the word.
    Leave punctuation marks untouched.
    """
    ls=  text.split()
    for i,word in enumerate(ls):
        if word.isalpha():
            ls[i] = word[1:]+word[0]+"ay"
        else:continue
    return " ".join(ls)

print(pig_it("sfoisdi ioioi ii ! "))