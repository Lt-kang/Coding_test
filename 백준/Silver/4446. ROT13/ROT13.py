

vowels = 'a i y e o u'.split()
consonats = 'b k x z n h d c w g p v j q t s r l m f'.split()


while True:
    try:
        ans = ""
        sentance = input()
        for char in sentance:
            charisLower = False if char.isupper() else True
            
            char = char.lower()
            
            if (char in vowels):
                changeChar = vowels[(vowels.index(char)+3) %6]
                ans += changeChar if charisLower else changeChar.upper()

            elif (char in consonats):
                changeChar = consonats[(consonats.index(char)+10) %20]
                ans += changeChar if charisLower else changeChar.upper()
                
            else:
                ans += char
        print(ans)
    except:
        break