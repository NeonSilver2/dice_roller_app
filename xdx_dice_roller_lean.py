import tkinter as tk
import random as rd

sr_list = []
dr_list = []
pr_list = []


root = tk.Tk()
root.title("XdX Random Die Roller")


ndice_frame = tk.LabelFrame(root, width=8, text=" # of dice -- # of sides ")
ndice_frame.grid(row=0, column=0, padx=2, columnspan=3, sticky="W")
    
ndice = tk.Entry(ndice_frame, bg="white", fg="black", width=8, justify="right")
ndice.grid(row=0, column=0, padx=1, sticky="E")
    
nsides = tk.Entry(ndice_frame, bg="white", fg="black", width=8)
nsides.grid(row=0, column=2, sticky="W")

dL = tk.Label(ndice_frame, text="d", justify="center", state="disabled")
dL.grid(row=0, column=1, sticky="S")
   
sumF = tk.LabelFrame(root, borderwidth=2, relief="groove", text="Total:")
sumF.grid(row=0, column=4, pady=3, padx=3, sticky="E")
    
sumL = tk.Label(sumF, text="(sum)")
sumL.pack(side="bottom")


def sum_func():
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


sumB = tk.Button(root, height=1, bg="#ffff77", width=4, text="ROLL", command=lambda:(sumL_update()))
sumB.grid(row=0, column=3, pady=2, sticky="E")

archiveF = tk.Frame(root, bg="#dddddd", width=250, height= 80, relief="groove", borderwidth=1)
archiveF.grid(row=2, column=0, rowspan=2, columnspan=5, padx=3, sticky="N")
   
past_rolls = tk.LabelFrame(archiveF, text="Past Rolls:", relief="sunken", borderwidth=2, bg="#dddddd", fg="#000000")
past_rolls.pack(side="left")
dresults = tk.LabelFrame(archiveF, text="Die Results:", relief="sunken", borderwidth=2, bg="#dddddd", fg="#000000")
dresults.pack(side="left")
sumresults = tk.LabelFrame(archiveF, text="Archived Sums:", relief="sunken", borderwidth=2, bg="#dddddd", fg="#000000")
sumresults.pack(side="right")

rollsL = tk.Label(past_rolls, text="(xdx)")
rollsL.pack(side="top")
dresL = tk.Label(dresults, text="([x, x, x, x])")
dresL.pack(side="top")
sumresL = tk.Label(sumresults, text="(total)")
sumresL.pack(side="top")

a = tk.Variable(value=sr_list)
sumresLB = tk.Listbox(sumresults, height=6, xscrollcommand=True, justify="center", listvariable=a)
sumresLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")

b = tk.Variable(value=dr_list)
dresLB = tk.Listbox(dresults, height=6, xscrollcommand=True, justify="center", listvariable=b)
dresLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")

c = tk.Variable(value=pr_list)
rollsLB = tk.Listbox(past_rolls, height=6, xscrollcommand=True, justify="center", listvariable=c)
rollsLB.pack(pady=2, padx=2, fill="both", expand=True, side="top")


clrB = tk.Button(root, width=15, justify="center", text="Hide Archive", bg="#95c4cf", fg="#000000", command=clear_archive)
clrB.grid(row=5, column=0, columnspan=2, padx=3, pady=1, sticky="SW")

exitB = tk.Button(root, width=15, justify="center", text="Close", bg="#ff4444", command=root.quit)
exitB.grid(row=5, column=3, columnspan=2, padx=3, pady=1, sticky="SE")


root.mainloop()    