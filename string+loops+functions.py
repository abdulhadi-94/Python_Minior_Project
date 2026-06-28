def analyze_string(s):
    
    print("\nlength of string : ",len(s))
    print("Reverse of string : ",s[-1::-1])
    
    vowels = "aeiou"
    count=0
    for ch in s.lower():
        if ch in vowels:
            count+=1
    print("Number of vowels : ",count)

    print("\nCharacter with Positive and Negative Index : ")
    for i in range(len(s)):
        print(f"Positive Index : {i}, Negative Index : {i-len(s)},Character: {s[i]}")
        

text = (input("Enter a string: "))
if text =="":
        print("Empty string entered.")
else:
        analyze_string(text)