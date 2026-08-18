#new to me

#Making faces(i stuck here a decent amount of time also first igroned gave data to ai then solve in 2 line now asi gave code)



def main():
    user = input("what is your mood? ")
    print(convert(user)) 

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")

main()