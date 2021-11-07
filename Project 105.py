import pandas
import statistics
import colorama
from colorama import Fore

#The csv file was really small so i just copied all of the data into a list directly
myList = [60,61,65,63,98,99,90,95,91,96]

#Finding the mean and standard deviation
meanOfList = statistics.mean(myList)

standardDeviationOfList = statistics.stdev(myList)

#Printing the information
print(Fore.MAGENTA + "The mean of the dataset is " + Fore.CYAN + str(meanOfList) + Fore.MAGENTA +
" and the standard deviaton is " + Fore.CYAN + str(standardDeviationOfList))

