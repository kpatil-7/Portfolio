# This file store variables that is shared throughout the program
from event import Event
from action import Action
from effect import Effect
from company import Company

# Difficulty (0-10) How random will be the disater
DIFFICULTY = 5

# Company start out
COMPANY = Company(10000, 50, 50, 50)

# How long
MONTHS = 12 # One year

# String constants
OUT_OF_MONEY = "OUT_OF_MONEY"
PRODUCT_OBSOLETE = "PRODUCT_OBSOLETE"
EMPLOYEE_UNHAPPY = "EMPLOYEE_UNHAPPY"
CUSTOMER_UNHAPPY = "CUSTOMER_UNHAPPY"
EVERYTHING_OKAY = "EVERYTHING_OKAY"

START_TEXT = "You are recently hired as the CEO of iDTech..."
OUT_OF_MONEY_END_TEXT = "Your company is bankrupted, you are fired."
PRODUCT_OBSOLETE_END_TEXT = "Your product is no longer relevant, your are fired."
EMPLOYEE_UNHAPPY_END_TEXT = "All of your employee quits, you are fired."
CUSTOMER_UNHAPPY_END_TEXT = "After too much customer complains, the board decided that you should be fired"
WIN_END_TEXT = "After years of management, the board decided that you should continue for another term"

# Pre made actions
ACT_HIRE_MORE = Action("Hire more employee", Effect(-500, 0, 15, 0))
ACT_LAY_OFF = Action("Layoff employee", Effect(500, 0, -15, 0))
ACT_R_AND_D = Action("Invest in R&D", Effect(-1000, 15, 0, 10))
ACT_OVER_WORK = Action("Push your employee to work more", Effect(1000, -5, -10, 0))
ACT_COMPANY_VACATION = Action("Have a company vacation", Effect(-1000, 0, 10, 0))
ACT_PULL_OUT = Action("Pull product off the market", Effect(-1500, 15, 0, -10))
ACT_APOLOGY = Action("Announce public apology", Effect(0,0,-10,10))

BASIC_ACTION_LIST = [ACT_HIRE_MORE, ACT_LAY_OFF, ACT_R_AND_D,
                     ACT_OVER_WORK, ACT_COMPANY_VACATION, ACT_PULL_OUT, ACT_APOLOGY]

# Pre made events
EVT_ENVIRONMENT_DISASTER = Event("Your company had a natural disaster", BASIC_ACTION_LIST, Effect(-2000,0,0,0))
EVT_BAD_FEEDBACK = Event("Your product recieved a bad review", BASIC_ACTION_LIST, Effect(0,0,0,-15))
EVT_PRODUCT_ERROR = Event("There was a error in your factory", BASIC_ACTION_LIST, Effect(0,-10,0,-10))
EVT_EMPLOYEE_BURN_OUT = Event("Your employee is having a burn out", BASIC_ACTION_LIST, Effect(0,0,-10,0))

EVT_NOTHING = Event("Nothing happen, use this time to improve your business", BASIC_ACTION_LIST, Effect(0,0,0,0))

BASIC_EVENT_LIST = [EVT_ENVIRONMENT_DISASTER, EVT_BAD_FEEDBACK, EVT_PRODUCT_ERROR, EVT_EMPLOYEE_BURN_OUT]
