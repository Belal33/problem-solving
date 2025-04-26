# million , billion , millions , billions , hundred , thousand
# 2 million dollar


def from_words_into_num(s):
	str_nums = {
  'million':1000_000 ,
  'billion':1000_000_000 ,
  'millions':1000_000 ,
  'billions':1000_000_000  ,
  'hundred':100 ,  
  'thousand':1000
  }
	s = s.split(' ')
	n = 1
	for i in range(len(s)) :
		try:
			if int(s[i]) :
				n = n * int(s[i])
		except: 
			if s[i] in str_nums.keys():
				n = n * str_nums[s[i]]
	return n

def w_into_num(_str):
  s = _str.lower().split('and')
  value = 0
  for i in range(len(s)) :	
    value = value + from_words_into_num(s[i].strip().lower())
  return value



print(w_into_num("4 billion and 555 million and 956 dollars "))
