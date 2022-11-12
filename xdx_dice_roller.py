import tkinter as tk
import random as rd

#THINGS LEFT TO DO:
# 1) Implement Scrollbars in the Listboxes
# 2) Fix the way that I handle the Listbox items being added (note at bottom of script near root.mainloop())
# 3) Convert into a .exe after implementing a "HOW TO USE" button that initializes a new window as the new TOP LEVEL widget, and has a frame and Label that explains how the app works for a user.
# 4) Post to Github.


#VARIABLES:
    #referenced later in a function as global variables so that they don't get wiped from memory after the function call ends.
sr_list = []
dr_list = []
pr_list = []

#MAIN WINDOW:
root = tk.Tk()
root.title("XdX Random Die Roller")


#JOKE (currently unimplemented):
    #top label topkekw
# topL = tk.Label(root, text="Roll for inspblimfadive:", bg="#d8e7f5", fg="#444444", justify="center", wraplength=350)
# topL.grid(row=1,column=1, columnspan=3, sticky="N")


#ENTRIES:
ndice_frame = tk.LabelFrame(root, width=8, text=" # of dice -- # of sides ")
ndice_frame.grid(row=0, column=0, padx=2, columnspan=3, sticky="W")
    #entry for number of dice
ndice = tk.Entry(ndice_frame, bg="white", fg="black", width=8, justify="right")
ndice.grid(row=0, column=0, padx=1, sticky="E")
    #entry for number of sides for each die
nsides = tk.Entry(ndice_frame, bg="white", fg="black", width=8)
nsides.grid(row=0, column=2, sticky="W")


#THE D:    
    # the D
dL = tk.Label(ndice_frame, text="d", justify="center", state="disabled")
dL.grid(row=0, column=1, sticky="S")


#TOTAL FRAME:
    #frame holding total sum      
sumF = tk.LabelFrame(root, borderwidth=2, relief="groove", text="Total:")
sumF.grid(row=0, column=4, pady=3, padx=3, sticky="E")
    #total sum text initialized
sumL = tk.Label(sumF, text="(sum)")
sumL.pack(side="bottom")


#FUNCTIONS:    
def list_manager():
    #This funciton is supposed to limit the number of items in the Listboxes, but it doesn't work. I suspect this is because the number of items in the listbox isn't increasing, since the items that are being added are elements to a single list that the listbox contains. //NOTE: UNFINISHED, DOES NOT WORK.
    global sumresLB
    global dresLB
    global rollsLB

    if ((sumresLB.size() > 5) or (dresLB.size() > 5) or (rollsLB.size() > 5)):
        if sumresLB.size() > 5:
            sumresLB.delete()
        else:
            pass

        if dresLB.size() > 5:
            dresLB.pop()
        else:
            pass

        if rollsLB.size() > 5:
            rollsLB.pop()
        else:
            pass
    else:
        pass


def sum_func():
    #this function rolls the dice and returns a list with an int[0] and a dictionary[1]
    nd = int(ndice.get())
    ns_list = []
    roll_sum = 0
    for x in range(1,(nd + 1)):
        ns = rd.randint(1,int(nsides.get()))
        roll_sum += ns
        ns_list.append(ns)
    ns_dict = {nd: ns_list}
    post = [roll_sum, ns_dict]
    return post

def sumL_update():
    #defines sumL as a global variable that is defined outside of the function, and then unpacks it and resets it as a new object. NOT DEFINING THE VARIABLE AS GLOBAL WAS CAUSING DUPLICATION ERROR.
    global sumL
    sumL.pack_forget()
    post = sum_func()
    total = int(post[0])
    sumL = tk.Label(sumF, text=total)
    sumL.pack(side="bottom")
    def archive_update(post):
        global sumresL
        global dresL
        global rollsL
        global sumresLB
        global dresLB
        global rollsLB

        sr = post[0]
        dr = list(post[1].values())
        pr = "{0}d{1}".format(ndice.get(), nsides.get())
        global sr_list
        global dr_list
        global pr_list
        
        global srSBv
        global drSBv
        global prSBv
        global srSBh
        global drSBh
        global prSBh
        
        sr_list.insert(0, sr)
       
        dr_list.insert(0, dr)

        
        pr_list.insert(0, pr)
        
        # sumresL.pack_forget()
        # dresL.pack_forget()
        # rollsL.pack_forget()

        sumresLB.destroy()
        dresLB.destroy()
        rollsLB.destroy()

        a = tk.Variable(value=sr_list)
        sumresLB = tk.Listbox(sumresults, height=6, justify="center", listvariable=a)
        sumresLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")

        b = tk.Variable(value=dr_list)
        dresLB = tk.Listbox(dresults, height=6, justify="center", listvariable=b)
        dresLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")

        c = tk.Variable(value=pr_list)
        rollsLB = tk.Listbox(past_rolls, height=6, justify="center", listvariable=c)
        rollsLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")

    archive_update(post)

def clear_archive():
    global rollsLB
    global dresLB
    global sumresLB
    
    rollsLB.destroy()
    dresLB.destroy()
    sumresLB.destroy()



#ROLL BUTTON:
sumB = tk.Button(root, height=1, bg="#ffff77", width=4, text="ROLL", command=lambda:(sumL_update()))
sumB.grid(row=0, column=3, pady=2, sticky="E")


#ARCHIVE:
    #Archive Frame
archiveF = tk.Frame(root, bg="#dddddd", width=250, height= 80, relief="groove", borderwidth=1)
archiveF.grid(row=2, column=0, rowspan=2, columnspan=5, padx=3, sticky="N")
    #Archive Section LabelFrames
past_rolls = tk.LabelFrame(archiveF, text="Past Rolls:", relief="sunken", borderwidth=2, bg="#dddddd", fg="#000000")
past_rolls.pack(side="left")
dresults = tk.LabelFrame(archiveF, text="Die Results:", relief="sunken", borderwidth=2, bg="#dddddd", fg="#000000")
dresults.pack(side="left")
sumresults = tk.LabelFrame(archiveF, text="Archived Sums:", relief="sunken", borderwidth=2, bg="#dddddd", fg="#000000")
sumresults.pack(side="right")

    #Archive Labels
rollsL = tk.Label(past_rolls, text="(xdx)")
rollsL.pack(side="top")
dresL = tk.Label(dresults, text="([x, x, x, x])")
dresL.pack(side="top")
sumresL = tk.Label(sumresults, text="(total)")
sumresL.pack(side="top")

    #Archive Listbox Frames
# srF = tk.Frame(sumresults)
# drF = tk.Frame(dresults)
# prF = tk.Frame(past_rolls)

    #Archive Listboxes
a = tk.Variable(value=sr_list)
sumresLB = tk.Listbox(sumresults, height=6, xscrollcommand=True, justify="center", listvariable=a)
sumresLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")

b = tk.Variable(value=dr_list)
dresLB = tk.Listbox(dresults, height=6, xscrollcommand=True, justify="center", listvariable=b)
dresLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")

c = tk.Variable(value=pr_list)
rollsLB = tk.Listbox(past_rolls, height=6, xscrollcommand=True, justify="center", listvariable=c)
rollsLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")

#     #Scrollbar objects, Y then X per frame
# srSBv = tk.Scrollbar(sumresLB, orient="vertical")
# drSBv = tk.Scrollbar(dresLB, orient="vertical")
# prSBv = tk.Scrollbar(rollsLB, orient="vertical")
# srSBh = tk.Scrollbar(sumresLB, orient="horizontal")
# drSBh = tk.Scrollbar(dresLB, orient="horizontal")
# prSBh = tk.Scrollbar(rollsLB, orient="horizontal")

# srSBv.pack(side="right", fill="y")
# drSBv.pack(side="right", fill="y")
# prSBv.pack(side="right", fill="y")
# srSBh.pack(side="bottom", fill="x")
# drSBh.pack(side="bottom", fill="x")
# prSBh.pack(side="bottom", fill="x")

#CLEAR & EXIT BUTTONS:
    #clear archive button 
clrB = tk.Button(root, width=15, justify="center", text="Hide Archive", bg="#95c4cf", fg="#000000", command=clear_archive)
clrB.grid(row=5, column=0, columnspan=2, padx=3, pady=1, sticky="SW")
    #exit button
exitB = tk.Button(root, width=15, justify="center", text="Close", bg="#ff4444", command=root.quit)
exitB.grid(row=5, column=3, columnspan=2, padx=3, pady=1, sticky="SE")


    #this is a failed attempt to call list_manager() to actually get it working. I don't know how to get it to work without changing the way that I'm constructing the listboxes. Rather than destroying the listbox each time and reloading it with a new list that got longer, I should keep the same Listbox open and just delete individual elements at specific conditions. //NOTE: UNFINISHED, DOES NOT WORK.
while ((sumresLB.size() > 5) or (dresLB.size() > 5) or (rollsLB.size() > 5)):
    list_manager()

root.mainloop()    

