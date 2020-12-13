"""
Name: Ifaz Alam
Date: March 18th, 2020
Description: BMI Calculator using TkInter.
"""

from tkinter import Tk, Label, Button, Entry

# Class for our program
class bmiCalc2:
  def __init__(self, master):
    self.master = master
    master.title("BMI Calculator")

    #TITLE 
    self.title = Label(master, text = "Calculate your BMI!")
    self.title.pack()

    #Asks for weight in lb
    self.labelWeight = Label(master, text = "Weight in pounds: ")
    self.labelWeight.pack()
    #Entry for response
    self.Weight = Entry(master)
    self.Weight.pack()

    #Asks for height in feet
    self.labelHeightFt = Label(master, text = "Height in feet")
    self.labelHeightFt.pack()
    #Entry for response
    self.HeightFt = Entry(master)
    self.HeightFt.pack()

    #Asks for height in inches
    self.labelHeightIn = Label(master, text = "inches")
    self.labelHeightIn.pack()
    #Entry for response
    self.HeightIn = Entry(master)
    self.HeightIn.pack()

    #Button to calculate BMI
    self.finishButton = Button(master, text = "Calculate BMI", command = self.BMI)
    self.finishButton.pack()

    #Result
    self.result = Label(master, text=" ")
    self.result.pack()

    #Button to exit program
    self.exit = Button(master, text = "Close Program", command = master.quit)
    self.exit.pack()

  #Function for calculating BMI
  def BMI(self):
    #Error message if user leaves one of the fields blank
    if self.Weight.get() == "" or self.HeightFt.get() == "" or self.HeightIn.get() == "":
      self.result.config(text = "All fields must be filled!")
    #Calculates BMI
    else:
      w = float(self.Weight.get()) / 2.205
      h = (float(self.HeightFt.get()) / 3.281) + (float(self.HeightIn.get()) / 39.37)
      self.result.config(text = "Your BMI is %.2f" % (w/h**2))
    
root = Tk()
my_gui = bmiCalc2(root)
root.mainloop()
