from tkinter import *
import time

root = Tk()
root.title("Idle Weed Clicker Version 0.0.5")

# values

weed = 0
weedpc = 1
weedps = 0
cashps = 0
xp = 0
doesclocktick = 0

# store prices
weedupgcost = 50
sellupgcost = 50
valupgcost = 100
autogrow1cost = 25
autogrow1amount = 0
autosell1cost = 25
autosell1amount = 0

#cash
cash = 0
weedcashval = 1
weedsoldpc = 1
tokepc = 1

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
Grow.grid(row=1, column=3)

# Sell Button
def ClickCash():
    global cash
    global weed
    global weedsoldpc
    if weed >= weedsoldpc:
        weed -= weedsoldpc
        cash += (weedsoldpc * weedcashval)
        CashDisplay['text'] = round(cash, 0)
        WeedDisplay['text'] = round(weed, 0)
    else:
        print("You don't have any weed to sell.")

CashButton = Button(root, text="Click To Sell Weed!", command=ClickCash, padx=25, pady=25, bg="orange")
CashButton.grid(row=4, column=3)

# Toke Button
def ClickToke():
    global weed
    global xp
    global tokepc
    if weed >= tokepc:
        xp += tokepc
        weed -= tokepc
        WeedDisplay['text'] = round(weed, 0)
        xpDisplay['text'] = xp
    else:
        print("You don't have any weed to smoke.")

TokeButton = Button(root, text="Click To Take A Toke!", command=ClickToke, padx=25, pady=25, bg="hot pink")
TokeButton.grid(row=8, column=3)



# weed labels
WeedDisplay = Label(root, text=weed, bg="green", padx=15)
WeedDisplay.grid(row=1, column=2)
WeedLabel = Label(root, text="Weed:", bg="green")
WeedLabel.grid(row=1, column=1)


# weed per click label
WeedPerClickLabel = Label(root, text=weedpc, bg="green", padx=15)
WeedPerClickLabel.grid(row=2, column=2)
WeedPerClickLabel2 = Label(root, text="Weed Per Click:", bg="green")
WeedPerClickLabel2.grid(row=2, column=1)

# weed per second label
WeedPerSecondDisplay = Label(root, text=round(weedps, 0), bg="green", padx=15)
WeedPerSecondDisplay.grid(row=3, column=2)
WeedPerSecondLabel = Label(root, text="Weed Grown Per Second:", bg="green")
WeedPerSecondLabel.grid(row=3, column=1)


# cash labels
CashLabel = Label(root, text="Cash:", bg="orange")
CashLabel.grid(row=4, column=1)
CashDisplay = Label(root, text=round(cash,0), bg="orange", padx=15)
CashDisplay.grid(row=4, column=2)

# cash per click label
CashPerClickLabel = Label(root, text="Cash Per Click:", bg="orange")
CashPerClickLabel.grid(row=5, column=1)
CashPerClickDisplay = Label(text=weedsoldpc * weedcashval, bg="orange", padx=15)
CashPerClickDisplay.grid(row=5, column=2)

# cash per second label
CashPerSecondLabel = Label(root, text="Weed Sold Per Second:", bg="orange")
CashPerSecondLabel.grid(row=6, column=1)
CashPerSecondDisplay = Label(text=cashps * weedcashval, bg="orange")
CashPerSecondDisplay.grid(row=6, column=2)

# weed value per gram label
WeedValLabel = Label(root, text="Weed Value Per Gram:", bg="orange")
WeedValLabel.grid(row=7, column=1)
WeedValDisplay = Label(text=weedcashval, bg="orange", padx=15)
WeedValDisplay.grid(row=7, column=2)

# xp value labels
xpLabel = Label(root, text="Experience:", bg="hot pink")
xpLabel.grid(row=8, column=1)
xpDisplay = Label(root, text=xp, bg="hot pink", padx=15)
xpDisplay.grid(row=8, column=2)




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
        CashDisplay['text'] = round(cash, 0)
        GrowUpgCostLabel['text'] = round(weedupgcost, 0)
        WeedPerClickLabel['text'] = round(weedpc, 0)
    else:
        print("You do not have enough cash for this upgrade!")

# weed per click upgrade label
GrowUpg = Button(root, text="Upgrade Lights (+1 Weed/click)", command=ClickUpg, bg="green")
GrowUpg.grid(row=2, column=7)
GrowUpgCostLabel = Label(root, text=weedupgcost, bg="pink")
GrowUpgCostLabel.grid(row=2, column=6)


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
        CashDisplay['text'] = round(cash, 0)
        SellUpgCostLabel['text'] = round(sellupgcost, 0)
        CashPerClickDisplay['text'] = round(weedsoldpc * weedcashval, 0)
    else:
        print("You do not have enough cash for this upgrade!")

# cash per click upgrade
SellUpg = Button(root, text="Increase Sell Size (+1 Weed Sold/click)", command=CashUpg, bg="orange")
SellUpg.grid(row=5, column=7)
SellUpgCostLabel = Label(root, text=sellupgcost, bg="pink")
SellUpgCostLabel.grid(row=5, column=6)

# weed value upgrade
def ValueUpg():
    global xp
    global weedcashval
    global valupgcost
    if xp >= valupgcost:
        xp -= valupgcost
        weedcashval += 1
        valupgcost *= 2.5
        xpDisplay['text'] = round(xp, 0)
        ValUpgCostLabel['text'] = round(valupgcost, 0)
        CashPerClickDisplay['text'] = round(weedsoldpc * weedcashval, 0)
        WeedValDisplay['text'] = round(weedcashval, 0)
        CashPerSecondDisplay['text'] = round(cash, 0)
    else:
        print("You Do Not Have Enough Cash To Purchase This Upgrade.")

ValUpg = Button(root, text="Increase Potency (+1 Weed Value)", command=ValueUpg, bg="hot pink")
ValUpg.grid(row=8, column=7)
ValUpgCostLabel = Label(root, text=valupgcost, bg="pink")
ValUpgCostLabel.grid(row=8, column=6)

def AutoGrower():
    global weed
    global weedps
    if weedps > 0:
        weed += weedps
        WeedDisplay["text"] = weed
        root.after(1000, AutoGrower)
    else:
        root.after(1000, AutoGrower)

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
        AutoGrow1CostDisplay['text'] = round(autogrow1cost, 0)
        WeedPerSecondDisplay['text'] = weedps
    else:
        print("You Do Not Have Enough Cash To Purchase This Purchase.")

AutoGrow1Button = Button(root, text="Hire Gardener (Grows 1 Weed Every Second)", command=AutoGrow1Purchase, bg="green")
AutoGrow1Button.grid(row=3, column=7)
AutoGrow1CostDisplay = Label(root, text=autogrow1cost, bg="pink")
AutoGrow1CostDisplay.grid(row=3, column=6)

def AutoSeller():
    global weed
    global cash
    global cashps
    if weed >= cashps:
        weed -= (cashps)
        cash += (cashps * weedcashval)
        WeedDisplay["text"] = round(weed, 0)
        CashDisplay["text"] = round(cash, 0)
        root.after(1000, AutoSeller)
    else:
        root.after(1000, AutoSeller)

# Auto Click Upgrade Store
def AutoSell1Purchase():
    global cash
    global autosell1cost
    global cashps
    if cash >= autosell1cost:
        cash -= autosell1cost
        CashDisplay['text'] = round(cash, 0)
        cashps += 1
        autosell1cost *= 1.5
        AutoSell1CostDisplay['text'] = round(autosell1cost, 0)
        CashPerSecondDisplay['text'] = cashps
    else:
        print("You Do Not Have Enough Cash To Purchase This Purchase.")

AutoSell1Button = Button(root, text="Hire Dealer (Sells 1 Weed Every Second)", command=AutoSell1Purchase, bg="orange")
AutoSell1Button.grid(row=6, column=7)
AutoSell1CostDisplay = Label(root, text=autosell1cost, bg="pink")
AutoSell1CostDisplay.grid(row=6, column=6)

root.after(1000, AutoSeller)
root.after(1000, AutoGrower)
# loop

root.mainloop()