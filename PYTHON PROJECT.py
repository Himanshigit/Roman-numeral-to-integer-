print("HERE YOU CAN CONVERT ROMAN NUMERAL INTO AN INTEGER")
def main():
    Y=["YES","yes","Yes","y","yeah","Y"]
    N=["no","No","NO","n","N"]
    class project:
        def romantoint(self, s):
            key={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
            val=0
            for i in range(len(s)):
                if i>0 and key[s[i]]>key[s[i-1]]:
                    val+=key[s[i]]-2*key[s[i-1]]
                else:
                    val+=key[s[i]]
            return val
    s=input("ENTER ROMAN NUMBER I-MMMCMXCIX (in capital letter):  ")
    print(project().romantoint(s))
    restart=input("Do you want to convert again:  ")
    if restart in Y:
        main()
    else:
        exit()
    
main()
    
