import matplotlib.pyplot as  plt

#Line Chart 
years=[2020,2021,2022,2023,2024,2025,2026]
admissions=[100,200,300,400,500,600,700]
plt.plot(years,admissions)
#plt.grid(True)
plt.xlabel(years)
plt.ylabel(admissions)
plt.title("Codegnan Admissions")
plt.show()

#Bar Chart
years=[2020,2021,2022,2023,2024,2025,2026]
admissions=[100,200,300,400,500,600,700]
plt.bar(years,admissions)
plt.xlabel(years)
plt.ylabel(admissions)
plt.title("Codegnan Admissions")
plt.show()

# Pie Chart
fruits=["Kiwi","Dragon","Banana","Grape","Berry"]
quatity=[10,20,30,40,50]
plt.pie(quatity,lables=fruits,autopct="%1.1f%%")
plt.show()

#Histogam 
ages=[10,20,30,30,45,50,10,10,50,45]
plt.hist(ages)
plt.show


