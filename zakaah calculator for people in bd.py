import requests
from bs4 import  BeautifulSoup

def main():
    print("Retrieving Gold-Silver price data from 'Bangladesh Jeweller's Association (BAJUS)'s website")
    print("Please Wait...")

    buying_price, selling_price = get_gold_silver_price()
    threshold_price = calc_threshold_price(selling_price)

    asset_and_debt = get_asset_and_debt()
    net_asset_in_taka = get_net_asset_in_taka(asset_and_debt, selling_price)
    

    print("\n\n-----Current Buying prices of Gold and Silver-----\n")
    for item in buying_price:
        print(f"Price of {item} is {buying_price[item]:.2f} BDT/gm")

    print("\n\n-----Current Selling prices of Gold and Silver-----\n")
    for item in selling_price:
        print(f"Price of {item} is {selling_price[item]:.2f} BDT/gm")
    

    if net_asset_in_taka >= threshold_price:
        total_zakaat = calc_zakaat(net_asset_in_taka)
        print(f"\n\nYour asset amount is {net_asset_in_taka:.2f} Taka. Which is greater than the\
 threshold value of {threshold_price:.2f} Taka.\nIf completely one year ago, you had\
 assets that surpassed the threshold value of that year then you must have to pay Zakaat This year.\
 Your Zakaat amount is {total_zakaat:.2f} Taka")
    else:
        print(f"\n\nYour asset amount is {net_asset_in_taka:.2f} Taka. Which is less than the\
 threshold value of {threshold_price:.2f} Taka.\nYou don't have to pay Zakaat.")



def get_gold_silver_price():
    # Extracting Gold and Silver prices from Bangladesh Juwellers's Association (BAJUS)
    BAJUS_URL = "https://www.bajus.org/gold-price"
    r = requests.get(BAJUS_URL)
    soup = BeautifulSoup(r.content, features='html.parser')
    gold_silver_rawtype = soup.find_all('h6')
    gold_silver_type = [row.text.strip() for row in gold_silver_rawtype]

    gold_silver_rawprice = soup.find_all('span', attrs={'class':'price'})
    gold_silver_price = []
    for row in gold_silver_rawprice:
        price, _ = row.text.split(' ')
        if ',' in price:
            price = price.replace(',', '')
        gold_silver_price.append(float(price))

    buying_price = {gold_silver_type[i] : gold_silver_price[i] for i in range(len(gold_silver_type))}

    # Extrapolated Price of 24 Karat Gold and Silver
    buying_price['24 KARAT Gold'] = buying_price['22 KARAT Gold'] * (24/22)
    buying_price['24 KARAT Silver'] = buying_price['22 KARAT Silver'] * (24/22)

    # Selling Price is 20% less than the buying price
    selling_price = {price : buying_price[price] * 0.8 for price in buying_price}

    
    return buying_price, selling_price


def calc_threshold_price(gold_silver_price):
    GOLD_THRESHOLD_GM = 85
    SILVER_THERSHOLD_GM = 595

    gold_threshold_price = GOLD_THRESHOLD_GM * gold_silver_price['24 KARAT Gold']
    silver_threshold_price = SILVER_THERSHOLD_GM * gold_silver_price['24 KARAT Silver']

    return min(gold_threshold_price, silver_threshold_price)


def get_asset_and_debt():

    gold_silver_type = [
        '24 KARAT Gold', '22 KARAT Gold', '21 KARAT Gold', '18 KARAT Gold', 'TRADITIONAL Gold',
        '24 KARAT Silver', '22 KARAT Silver', '21 KARAT Silver', '18 KARAT Silver', 'TRADITIONAL Silver',
        'money', 'business_assets', 'debts',
    ]

    asset_and_debt = {}

    print("\n\n-----Enter your current amount of gold and sliver, either in bars or ornaments or any other form.-----")
    for item in gold_silver_type:
        unit = 'Gram'
        if item == 'money':
            print("\n\n-----Add bank deposits (current, savings, fixed etc), cash in hand, stocks that were purchased to be sold in stock market or any other liquid asset etc.-----")
            unit = 'Taka'
        elif item == 'business_assets':
            print('\n\n-----Add present selling value of assets that were purchased at the intention of selling again.-----')
            unit = 'Taka'
        elif item == 'debts':
            print('\n\n-----Add all debts that are payable within next one lunar year.-----')
            unit = 'Taka'

        while True:
            amount = input(f"Enter the amount {item} that you have in {unit}: ")
            try:
                amount = float(amount)
                if amount >= 0:
                    asset_and_debt[item] = amount
                    break
                else:
                    raise ValueError
            except:
                print("Enter correct value.")
                continue

    return asset_and_debt


def get_net_asset_in_taka(asset_and_debt, gold_silver_price):
    net_asset_in_taka = 0
    for item in asset_and_debt:
        if item == 'money' or item == 'business_assets':
            net_asset_in_taka += asset_and_debt[item]
        elif item == 'debts':
            net_asset_in_taka -= asset_and_debt[item]
        else:
            net_asset_in_taka += asset_and_debt[item] * gold_silver_price[item]
            
    return net_asset_in_taka

def calc_zakaat(net_asset_in_taka):
    return (net_asset_in_taka * 2.5) / 100


if __name__ == "__main__":
    main()