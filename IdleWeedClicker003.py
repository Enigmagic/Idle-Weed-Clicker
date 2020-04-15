from tkinter import *
import time

root = Tk()
root.title("Idle Weed Clicker")



# values

weed = 0
weedpc = 1
weedps = 0
doesclocktick = 0

# store prices
weedupgcost = 500
sellupgcost = 750
valupgcost = 1500
autogrow1cost = 100
autosell1cost = 100



#cash
cash = 0
weedcashval = 10
weedsoldpc = 1



# main gui
Title = Label(root, text="Idle Weed Grower", bg="green")
Title.grid(row=0, column=0)


# Grow Button
def ClickWeed():
    global weed
    global weedpc
    weed += weedpc
    WeedDisplay['text'] = weed

Grow = Button(root, text="Click To Grow Weed!", command=ClickWeed, padx=25, pady=25, bg="green")
Grow.grid(row=7, column=3)

# Sell Button
def ClickCash():
    global cash
    global weed
    global weedsoldpc
    if weed >= weedsoldpc:
        weed -= weedsoldpc
        cash += (weedsoldpc * weedcashval)
        CashDisplay['text'] = cash
        WeedDisplay['text'] = weed
    else:
        print("You don't have any weed to sell.")

CashButton = Button(root, text="Click To Sell Weed!", command=ClickCash, padx=25, pady=25, bg="blue")
CashButton.grid(row=8, column=3)


# weed labels
WeedDisplay = Label(root, text=weed)
WeedDisplay.grid(row=1, column=2)
WeedLabel = Label(root, text="Weed:", bg="green")
WeedLabel.grid(row=1, column=1)


# weed per click label
WeedPerClickLabel = Label(root, text=weedpc)
WeedPerClickLabel.grid(row=2, column=2)
WeedPerClickLabel2 = Label(root, text="Weed Per Click:", bg="green")
WeedPerClickLabel2.grid(row=2, column=1)

# weed per second label
WeedPerSecondDisplay = Label(root, text=weedps)
WeedPerSecondDisplay.grid(row=3, column=2)
WeedPerSecondLabel = Label(root, text="Weed Grown Per Second:", bg="green")
WeedPerSecondLabel.grid(row=3, column=1)


# cash labels
CashLabel = Label(root, text="Cash:", bg="blue")
CashLabel.grid(row=4, column=1)
CashDisplay = Label(root, text=cash)
CashDisplay.grid(row=4, column=2)

# cash per click label
CashPerClickLabel = Label(root, text="Cash Per Click:", bg="blue")
CashPerClickLabel.grid(row=5, column=1)
CashPerClickDisplay = Label(text=weedsoldpc * weedcashval)
CashPerClickDisplay.grid(row=5, column=2)

# weed value per gram label
WeedValLabel = Label(root, text="Weed Value Per Gram:", bg="blue")
WeedValLabel.grid(row=6, column=1)
WeedValDisplay = Label(text=weedcashval)
WeedValDisplay.grid(row=6, column=2)




# Upgrade Store


# Weed Per Click Upgrade
def ClickUpg():
    global cash
    global weedpc
    global weedupgcost
    if cash >= weedupgcost:
        weedpc += 1
        cash -= weedupgcost
        weedupgcost *= 1.7
        CashDisplay['text'] = cash
        GrowUpgCostLabel['text'] = weedupgcost
        WeedPerClickLabel['text'] = weedpc
    else:
        print("You do not have enough cash for this upgrade!")

# weed per click upgrade label
GrowUpg = Button(root, text="Upgrade Lights (+1 Weed/click)", command=ClickUpg)
GrowUpg.grid(row=1, column=7)
GrowUpgCostLabel = Label(root, text=weedupgcost)
GrowUpgCostLabel.grid(row=1, column=6)


# weed sold per click upgrade
def CashUpg():
    global cash
    global weedcashval
    global sellupgcost
    global weedsoldpc
    if cash >= sellupgcost:
        weedsoldpc += 1
        cash -= sellupgcost
        sellupgcost *= 1.7
        CashDisplay['text'] = cash
        SellUpgCostLabel['text'] = sellupgcost
        CashPerClickDisplay['text'] = (weedsoldpc * weedcashval)
    else:
        print("You do not have enough cash for this upgrade!")

# cash per click upgrade
SellUpg = Button(root, text="Increase Sell Size (+1 Weed Sold/click)", command=CashUpg)
SellUpg.grid(row=2, column=7)
SellUpgCostLabel = Label(root, text=sellupgcost)
SellUpgCostLabel.grid(row=2, column=6)

# weed value upgrade
def ValueUpg():
    global cash
    global weedcashval
    global valupgcost
    if cash >= valupgcost:
        cash -= valupgcost
        weedcashval *= 1.10
        valupgcost *= 1.8
        CashDisplay['text'] = cash
        ValUpgCostLabel['text'] = valupgcost
        CashPerClickDisplay['text'] = (weedsoldpc * weedcashval)
        WeedValDisplay['text'] = weedcashval
    else:
        print("You Do Not Have Enough Cash To Purchase This Upgrade.")

ValUpg = Button(root, text="Increase Potency (+10% Weed Value)", command=ValueUpg)
ValUpg.grid(row=3, column=7)
ValUpgCostLabel = Label(root, text=valupgcost)
ValUpgCostLabel.grid(row=3, column=6)

# Auto Click Upgrade Store
def AutoGrow1Purchase():
    global cash
    global autogrow1cost
    global weedps
    global doesclocktick
    if cash >= autogrow1cost:
        cash -= autogrow1cost
        CashDisplay['text'] = cash
        weedps += 1
        autogrow1cost *= 1.5
        doesclocktick = 1
        AutoGrow1CostDisplay['text'] = autogrow1cost
        WeedPerSecondDisplay['text'] = weedps
    else:
        print("You Do Not Have Enough Cash To Purchase This Purchase.")

AutoGrow1Button = Button(root, text="Hire Gardener (Grows 1 Weed Every Second)", command=AutoGrow1Purchase)
AutoGrow1Button.grid(row=1, column=9)
AutoGrow1CostDisplay = Label(root, text=autogrow1cost)
AutoGrow1CostDisplay.grid(row=1, column=8)

time.sleep(1)
weed += weedps
WeedDisplay["text"] = weed
print(weed)

# loop
root.mainloop()
