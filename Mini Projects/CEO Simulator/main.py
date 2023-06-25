import global_vars as G
import random

# Print intro text
print(G.START_TEXT)
print(G.COMPANY)
# Main loop of the game
winning = True
for month in range(0, G.MONTHS):
    # print month
    print("Month:", str(month + 1))
    # Draw random event
    hazard = random.randint(0,9)
    # Default nothing happens
    event = G.EVT_NOTHING
    # If special event
    if hazard < G.DIFFICULTY:
        index = random.randint(0,len(G.BASIC_EVENT_LIST)-1)
        event = G.BASIC_EVENT_LIST[index]
    # Print the event
    print(event)
    # Update company status
    G.COMPANY.update_status(event.effect)
    # Get user input
    choice = int(input("What is your action: "))
    print("")
    # Update company over choices
    G.COMPANY.update_status(event.actions[choice].effect)
    # Print earning
    earning = G.COMPANY.revenue_report()
    print("Your company made additionally", earning)
    # Report company status
    print(G.COMPANY)
    # Check company status
    status = G.COMPANY.status_check()
    if status == G.OUT_OF_MONEY:
        print(G.OUT_OF_MONEY_END_TEXT)
        winning = False
        break
    if status == G.PRODUCT_OBSOLETE:
        print(G.PRODUCT_OBSOLETE_END_TEXT)
        winning = False
        break
    if status == G.CUSTOMER_UNHAPPY:
        print(G.CUSTOMER_UNHAPPY_END_TEXT)
        winning = False
        break
    if status == G.EMPLOYEE_UNHAPPY_END_TEXT:
        print(G.EMPLOYEE_UNHAPPY_END_TEXT)
        winning = False
        break

# Made it
if winning:
    print(G.WIN_END_TEXT)