#taken help from duck ai and copy pasted some code... also made some silly mistakes

from datetime import date
import inflect
p=inflect.engine()

def main():
    user_date=input("Date: ").strip()
    min= convert(user_date)
    words = p.number_to_words(min,andword="").capitalize()
    print(f"{words}")

def convert(bdate):
    bdate=date.fromisoformat(bdate)
    today=date.today()
    min = (today - bdate).total_seconds() / 60
    return round(min)    
    
if __name__ == "__main__":
    main()