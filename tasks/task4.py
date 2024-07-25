print(
    """====================================================  
 _____       _            _       _             
/  __ \     | |          | |     | |            
| /  \/ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__|
| \__/\ (_| | | (__| |_| | | (_| | || (_) | |   
 \____/\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

===================================================
   \n"""
)
while True:
    exp = input("enter expression (q to quit) : ")
    if exp != "q":
        try:
            ans = eval(exp)
            print(f" = {ans}\n" + "--" * 15)
        except Exception as e:
            print("Error Evaluating Expression \n e")
    else:
        print("=" * 15)
        break
