

def roman_num(n):
  M = ((n//1000)*"M")
  D = "CM" if  (n%1000) in range(900,1000) else ((n%1000)//500)*"D" 
  C = ( 
        'CD' if (n%1000) not in range(900,1000)  and (((n%1000)%500)//100) == 4  
        else ''  if (n%1000) in range(900,1000) 
        else (((n%1000)%500)//100)*"C"
      )
  L = "XC" if  (((n%1000)%500)%100) in range(90,100) else ((((n%1000)%500)%100)//50)*"L" 
  X = ( 
        'XL' if (((n%1000)%500)%100) not in range(90,100)  and (((((n%1000)%500)%100)%50)//10) == 4  
        else ''  if (((n%1000)%500)%100) in range(90,100) 
        else (((((n%1000)%500)%100)%50)//10)*"X" 
      )
  V = "IX" if ((((((n%1000)%500)%100)%50)%10)) == 9  else ((((((n%1000)%500)%100)%50)%10)//5)*"V"
  I = ( 
        'IV' if ((((((n%1000)%500)%100)%50)%10)) != 9 and (((((((n%1000)%500)%100)%50)%10)%5)) == 4  
        else ''  if ((((((n%1000)%500)%100)%50)%10)) == 9 
        else (((((((n%1000)%500)%100)%50)%10)%5))*"I" 
      )
  return(M + D + C  + L + X + V + I)
      
# for n in range(100,120):

#   print("#"*4 + str(n) + "#"*4 )
#   print(solution(n))
#   print('\n')
print(roman_num(4523)
      )


  







# # if n == 5 




# m = 'IV'  if (((((((n%1000)%500)%100)%50)%10)%5)) == 4 else (((((((n%1000)%500)%100)%50)%10)%5))*"I"

