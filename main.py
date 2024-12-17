import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt


data ={
    "flavor":["vanila","strawberry","blueberry","chocolate","mint"],
    "votes":[20,10,10,40,10]
}

mydata=pd.DataFrame(data)
#print(mydata)

#bar plot

plt.figure(figsize=(8,5))
sb.barplot(x="flavor",y="votes",data=mydata,palette="pastel")
plt.title("votes for favorite ice cream flavors")
plt.xlabel("ice cream flavor")
plt.ylabel("votes")
plt.show()

#line plot
plt.figure(figsize=(8,5))
sb.lineplot(x="flavor",y="votes",data=mydata,color="blue")
plt.title("votes for favorite ice cream flavors")
plt.xlabel("ice cream flavor")
plt.ylabel("votes")
plt.show()

#pie plot
plt.figure(figsize=(8,5))
plt.pie(mydata["votes"],labels=mydata["flavor"],startangle=140,colors=sb.color_palette("bright"))
plt.title("votes for favorite ice cream flavors")
plt.show()
