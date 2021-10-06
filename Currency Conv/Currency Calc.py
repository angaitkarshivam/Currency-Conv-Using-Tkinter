from tkinter import *

class CurrencyConv:
    def __init__(self):
        window = Tk()
        window.title("Currency Converter")
        window.configure(bg="green")


        self.amounttoconvertVar = StringVar()
        self.conversionrateVar = StringVar()
        self.convertedamountVar = StringVar()


        Label(window,font="Helvetica 12 bold", bg="green", text="Amount to Convert").grid(row=1, column=1, sticky=W)
        Entry(window, textvariable=self.amounttoconvertVar, justify=RIGHT).grid(row=1, column=2)
        Label(window, font="Helvetica 12 bold", bg="green", text="Conversion Rate").grid(row=2, column=1, sticky=W)
        Entry(window, textvariable=self.conversionrateVar, justify=RIGHT).grid(row=2, column=2)
        Label(window, font="Helvetica 12 bold", bg="green", text="Converted Amount").grid(row=3, column=1, sticky=W)
        Label(window, font="Helvetica 12 bold", bg="green", textvariable=self.convertedamountVar, justify=RIGHT).grid(
            row=3, column=2, sticky=E)




        btConvertedAmount = Button(window, font="Helvetica 12 bold", bg="blue", fg="white", text="Convert", command= self.ConvertedAmount).grid(row=4, column=2, sticky=E)
        btdelete_all = Button(window, font="Helvetica 12 bold", bg="red", fg="white", text="Clear",
                                   command=self.delete_all).grid(row=4, column=6,padx=25, pady=25, sticky=E)


        window.mainloop()

    def ConvertedAmount(self):
        amt = float(self.conversionrateVar.get())
        convertedamountVar = float(self.amounttoconvertVar.get()) * amt
        self.convertedamountVar.set(format(convertedamountVar,'10.2f'))

    def delete_all(self):
        self.amounttoconvertVar.set("")
        self.conversionrateVar.set("")
        self.convertedamountVar.set("")

CurrencyConv()







