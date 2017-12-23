str1 = "w,3,r,e,s,o,u,r,c,e"
print(str1.split(','))
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 2))
print(str1.rsplit(',', 5))

#rsplit will start the split from the right
# Both split and rsplit has a 2nd parameter that tells maximum number of splits