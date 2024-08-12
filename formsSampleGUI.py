#Immigration system form
from tkinter import *

window = Tk()

window.title("Immigration Fill Out Forms")
window.geometry("1000x800")

main_frame = Frame(window)

TitleLable = Label(window, text="Immigration System Forms", font=('Arial', 40,'bold'), relief="raised", bd=10) 
TitleLable.pack()

#Note:if you do absolute x= and y= , then the button will stay fixed in place when you try to resize the window. 
# initialEADButton = Button(window, text="Initial \n EAD")
# initialEADButton.place(height= 150, width= 200, x=200, y=300)
# clientIntakeButton = Button(window, text="New Client \n Intake Form")
# clientIntakeButton.place(height= 150, width= 200, x=400, y=300)
# EADrenewalButton = Button(window, text="Renewal \n EAD")
# EADrenewalButton.place(height= 150, width= 200, x=600, y=300)

# MarriagePetButton = Button(window, text="Marriage Petition \n Form")
# MarriagePetButton.place(height= 150, width= 200, x=200, y=450)
# AsylumFormButton = Button(window, text="Asylum \n Form")
# AsylumFormButton.place(height= 150, width= 200, x=400, y=450)
# BillingFormButton = Button(window, text="Billing \n Form")
# BillingFormButton.place(height= 150, width= 200, x=600, y=450)

#Note: If you instead do relx= and rely= , then the buttons will start to move relative to the window size. 
cashBillingButton = Button(window, text="Billing Form \n(Cash)", font=('Times New Roman', 20))
cashBillingButton.place(height= 150, width= 200, relx=.20, rely=.30)
clientIntakeButton = Button(window, text="New Client \nIntake Form", font=('Times New Roman', 20))
clientIntakeButton.place(height= 150, width= 200, relx=.40, rely=.30)
cardBillingButton = Button(window, text="Billing Form \n(Card)", font=('Times New Roman', 20))
cardBillingButton.place(height= 150, width= 200, relx=.60, rely=.30)

MarriagePetButton = Button(window, text="EAD \nForm", font=('Times New Roman', 20))
MarriagePetButton.place(height= 150, width= 200, relx=.20, rely=.48)
AsylumFormButton = Button(window, text="Marriage Petition \nForm",font=('Times New Roman', 20))
AsylumFormButton.place(height= 150, width= 200, relx=.40, rely=.48)
BillingFormButton = Button(window, text="Asylum \nForm", font=('Times New Roman', 20))
BillingFormButton.place(height= 150, width= 200, relx=.60, rely=.48)


# back_btn = Button(window, text="Back", font=('Bold',12), bg='#1877f2')
# back_btn.pack(side=TOP, anchor="nw", padx=10) 


window.mainloop()