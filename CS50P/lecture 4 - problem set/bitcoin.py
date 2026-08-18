#copy and pasted by ai... i have to practice more question of this...


import requests
import sys

# --- PHASE 1: Argument Check ---
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    coins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")


# --- PHASE 2: API Request ---
try:
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    )
    response.raise_for_status()  # catches HTTP errors

    data = response.json()
    current_price = data["bitcoin"]["usd"]

except requests.RequestException:
    sys.exit("Internet down")


# --- PHASE 3: Calculation ---
total_cost = coins * current_price

# --- PHASE 4: Output ---
print(f"${total_cost:,.4f}")


















#import requests
#import sys

#if len(sys.argv)!=2:
#    sys.exit("missing command-line argument")
#elif sys.argv[1] != float(sys.argv[1]):
#    sys.exit("command-line argument is not a float")

#try:
 #   coins=float(sys.argv[1])
  #  response=requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
   # print(response.json())
#except requests.RequestException:
 #   print("Internet down")