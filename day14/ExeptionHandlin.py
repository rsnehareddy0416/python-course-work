'''try:
    if a>20:
        print("good")
except NameError:
    print("a is not defined")'''



'''try:
    a=100
    if a>20:
        print("good")
except NameError:
    print("a is not defined")
else:
    print("No errors")'''

'''try:
    if a>20:
        print("good")
except NameError:
    print("a is not defined")
finally:
    print("End of the block")'''
    

#multiple error handling
'''try:
    if a>20:
        print("good")
    a=[1,7,9,0]
    print(a[4])
except NameError:
    print("a is not defined")
except ValueError:
    print("Enter the requested data type")
except TypeError:
    print("Data types are different")
except ZeroDivisionError:
    print("can,t divide with zero")
except IndexError:
    print("The index is not present")
except KeyError:
    print("In dict this key is not present")
else:
    print("no Error")
finally:
    print("End of the block")'''



'''try:
    a=a+'8'
    print(a[8])
except (NameError,ValueError,TypeError,ZeroDivisionError,IndexError,KeyError) as e:
    print(f'Error occurred:{e}')
else:
    print('No Errors')
finally:
    print("End of the block")'''



'''try:
    a=a+'8'
    print(a[8])
except Exception as e:
    print(f'Error occurred:{e}')
else:
    print('No Errors')
finally:
    print("End of the block")'''


'''try:
    a=int(input())
    if a<0:
        raise Exception("Enter the positive value:")
except Exception as e:
    print(f'Error Occurred:{e}')
else:
    print("No errors")
finally:
    print("End of the block")'''



def zero_division_error_case():
    try:
        transactions=[]
        avg_transaction=sum(transactions)/len(transactions)
        print(f"Average Transaction={avg_transaction}")
    except ZeroDivisionError:
        print("Error:Cannot calculate average transaction because there are no numbers")
def value_error_case():
    try:
        withdraw_amount=int("100/")
        print(f"Withdrawing:{withdraw_amount}")
    except ValueError:
        print("Error:Invalid value entered.please enter a numeric value")
def type_error_case():
    try:
        balance=500
        deposit_amount="100"
        new_balance=balance+deposit_amount
        print(f"New balance={new_balance}")
    except TypeError:
        print("Error:Incompatible data types cannot add string to an integer")
def index_error_case():
    try:
        transaction_history=[200,-150,300]
        print(f"Transaction history:{transaction_history}")
    except IndexError:
        print("Error:Trying to access a transaction that does not exist.")
def key_error_case():
    try:
        accounts={"123456":{"pin":"1234","balance":3000}}
        account_number="23458"
        print("Account balance:",accounts[account_number]['balance'])
    except KeyError:
        print("Error:Account number not found")
def file_not_found_error_case():
    try:
        with open("transaction_log.txt","r") as file:
            data=file.read()
    except FileNotFoundError:
        print("Error:Transaction log file not found")
while True:
    print("\n---ATM Simulation Menu-----")
    print("1.Check Average Transaction(ZeroDivisionError)")
    print("2.Withdraw with invalid input(ValueError)")
    print("3.Deposit with invalid datatype(TypeError)")
    print("4.Access invalid Transaction history(IndexError)")
    print("5.Access  non Existent account(KeyError)")
    print("6.Read Missing Transaction Log File (FileNotFound)")
    print("Exit")
    ch=int(input("Enter choice:"))
    if ch==1:
        zero_division_error_case()
    elif ch==2:
        value_error_case()
    elif ch==3:
        type_error_case()
    elif ch==4:
        index_error_case()
    elif ch==5:
        key_error_case()
    elif ch==6:
        file_not_found_error_case()
    elif ch==7:
        print("Exiting the ATM Simulation")
    else:
        print("Invalid option.please enter valid option")
        

           
