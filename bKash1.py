user_info = {
    "name": "Sazzad",
    "number": "01571026673",
    "pin": 45678,
    "nid": 1033252923,
    "birth_year": 2000,
    "balance": 4553.00,
    "statement": ["14/12/24 Make Payment - Tk - 35.00", "02/12/24 Make Payment - Tk - 20.00", "28/11/24 Cash Out - Tk - 300.00"]
}

saved_meter = {

}

menu = ["Send Money", "Send Money to Non-Bkash User", "Mobile Recharge", "Payment", "Cash Out", "Pay Bill", "Download Bkash App", "My Bkash", "Reset Pin"]
mobile_recharge = ["Robi", "Airtel", "Banglalink", "Grameenphone", "Teletalk"]
cash_out = ["From Agent", "From ATM"]

pay_bill = ["Electricity (Prepaid)", "Electricity (Postpaid)", "Gas", "Water", "Internet and Phone", "TV", "City Services", "Education", "Financial Services"]
electricity = ["Palli Bidyut", "DESCO", "DPDC", "BPDB", "Sylhet BPDB", "Westzone", "NESCO"]
gas = ["Jalalabad Gas", "Sundarban Gas", "Paschimanchal Gas", "Karnaphuli Gas"]
water = ["Dhaka WASA", "Chattogram WASA", "Rajshahi WASA", "Khulna WASA (Metered)"]
internet_phone = ["BTCL", "Link3", "AmberIT", "Carnival", "Sam online", "Triangle", "KS Network", "Dot Internet"]
tv = ["Akash Digital TV", "JCCL", "Jadoo Digital"]
city_services = ["Dhaka South City Corporation", "Sylhet City Corporation"]
education = ["GPCPSC", "RCPSC", "MUBC", "VNSC", "MCPSC", "Eduman", "KPBSC", "Pay2Fee", "Uttara University"]
financial_services = ["IPDC Finance", "MetLife", "Prime Islami Life", "Pragati Life", "Guardian Life", "Delta Life", "Chartered Life", "Alpha Islami Life"]
check_make = ["Check Bill", "Make Payment"]
check_bill = ["Input Meter Number", "Saved Accounts"]

my_bkash = ["Check Balance", "Request Statement", "Change PIN", "Helpline"]

reset_pin_list = ["Send Money", "Mobile Recharge", "Payment", "Paybill", "Cash Out", "bKash to Bank", "No Transaction"]


def show_option(main_list: list, name: str = "Bkash"):
    print(f"\n\n{name}")
    for i in range(len(main_list)):
        print(f"{i+1} {main_list[i]}")
    
    user_input = int(input("Send instruction: "))
    return user_input

def get_number(name = "reciever"):
    while True:
        if user_choose == 3:
            number = input(f"Enter {name} number: ")
        else:
            number = input(f"Enter {name} bkash account number: ")
        if len(number) == 11 or len(number) == 14:
            if user_choose in [1,2,4,5,6]:
                if number == user_info["number"]:
                    print(f"You can't {menu[user_choose-1]} to your own number.")
                else:
                    break
            else:
                break
        else:
            print("Invalid Number.")
    return number

def get_amount():
    while True:
        try:
            amount = int(input("Enter amount: "))
            break
        except:
            print("Amount Error!")
    return amount

def get_reference():
    reference = input("Enter reference: ")
    return reference

def pin_to_confirm():
    pin = int(input("Enter you pin to confirm: "))
    if user_info["pin"] == pin:
            if user_choose == 8:
                if mybi == 1:
                    print(f"Your balance is {user_info['balance']}TK")
                elif mybi == 2:
                    print("\n\nStatement List: ")
                    for i in range(len(user_info["statement"])):
                        print(f"{i+1} {user_info["statement"][i]}")
            else:
                print("Successful!")
    else:
        print("Incorrect pin! Try again.")

def change_pin():
    old_pin = int(input("Enter old PIN: "))
    new_pin = int(input("Enter new PIN: "))
    new_pin2 = int(input("Enter new PIN again: "))
    if old_pin == user_info["pin"]:
        if new_pin == new_pin2:
            user_info["pin"] = new_pin
            print(user_info["pin"])
            print("Your PIN has been changed Successfully.")
        else:
            print("New password doesn't match.")
    else:
        print("You've entered incorrect password.")

def reset_pin():
    nid = int(input("Enter your NID/Driving License/Passport no: "))
    birth_year = int(input("Enter your 4 digit birth year (yyyy): "))
    rpi = show_option(reset_pin_list, "Select one from last 10 outgoing transactions in 30 days:")
    amount = int(input(f"Enter {reset_pin_list[rpi-1]} transaction amount: "))
    print("Thanks for submitting all informations. We'll let you know very soon.")

    return nid, birth_year, amount

if input("Enter *247# for bkash")==str("*247#"):
    user_choose = show_option(menu)
    match user_choose:
        case 1:
            get_number()
            get_amount()
            get_reference()
            pin_to_confirm()
        case 2:
            get_number()
            get_amount()
            get_reference()
            pin_to_confirm()
        case 3:
            mbi = show_option(mobile_recharge, menu[user_choose-1])
            print("\n\nBkash")
            print("1 Prepaid")
            print("2 Postpaid")
            int(input("Send instruction: "))
            get_number(mobile_recharge[mbi-1])
            get_amount()
            pin_to_confirm()
        case 4:
            get_number("Merchant")
            get_amount()
            get_reference()
            pin_to_confirm()

        case 5:
            coi = show_option(cash_out, menu[user_choose-1])
            match coi:
                case 1:
                    get_number("Agent")
                    get_amount()
                    pin_to_confirm()
                case 2:
                    pin_to_confirm()
                case _:
                    print("Wrong Input!")

        case 6:
            pbi = show_option(pay_bill, menu[user_choose-1])
            match pbi:
                case 1:
                    show_option(electricity, pay_bill[pbi-1])
                case 2:
                    show_option(electricity, pay_bill[pbi-1])
                case 3:
                    show_option(gas, pay_bill[pbi-1])
                case 4:
                    show_option(water, pay_bill[pbi-1])
                case 5:
                    show_option(internet_phone, pay_bill[pbi-1])
                case 6:
                    show_option(tv, pay_bill[pbi-1])
                case 7:
                    show_option(city_services, pay_bill[pbi-1])
                case 8:
                    show_option(education, pay_bill[pbi-1])
                case 9:
                    show_option(financial_services, pay_bill[pbi-1])
                
            cmi = show_option(check_make)
            match cmi:
                case 1:
                    cbi = show_option(check_bill, "Check Bill")
                    match cbi:
                        case 1:
                            int(input("Enter meter number: "))
                            get_amount()
                            get_reference()
                            pin_to_confirm()
                        case 2:
                            if saved_meter:
                                print(list(saved_meter.keys()))
                            else:
                                print("No saved meter.")
                case 2:
                    get_number("Merchant")
                    get_amount()
                    get_reference()
                    pin_to_confirm()
        case 7:
            print(f"\n\n{menu[user_choose-1]}")
            print("1 Get up to 125TK bonus & exclusive offers on bKash App! Download Now!")
            int(input("Send instructions: "))
            print("Your request has been processed successfully. You'll get a sms with the app download link.")
        case 8:
            mybi = show_option(my_bkash, menu[user_choose-1])
            match mybi:
                case 1:
                    pin_to_confirm()
                case 2:
                    pin_to_confirm()
                case 3:
                    change_pin()
                case 4:
                    print("1 Call 16247 or Visit www.bkash.com for more info.")
        case 9:
            reset_pin()

        
    print(user_choose)
else:
    print("Connection problem or Invalid MMI Code")
    
    