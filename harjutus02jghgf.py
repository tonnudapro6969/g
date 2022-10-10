#Tõnis Kändmaa
#10.10.2022
#KILpKONNN
import turtle

#tekitan akna ja lisan muutujasse
aken = turtle.Screen()
aken.setup(300,300)
aken.title("Kilpkonna Harjutus02")



#konna loomine
konn1 = turtle.Turtle()
for x in range(5):
    
    konn1.forward(100)
    konn1.right(144)
    
    
for x in range(3):
    konn1.color("red")
    konn1.left(120)
    konn1.forward(120)
    




turtle.exitonclick()