def generate_hashtag(s: str):
    s_cap = "".join([word.capitalize() for word in s.split()])
    return False if not s_cap or len(s_cap) > 140 else "#" + s_cap


#
# generate_hashtag('aasca ascascasewf s   efecsfecsecse     sefwecec         ')
print(generate_hashtag("   asxas xasx   "))
