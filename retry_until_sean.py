import turtle

while True:
    name = ""
    while name.strip().lower() != "sean spencer":
        name = input("Enter your name: ")
        if name.strip().lower() != "sean spencer":
            print("Error, try again.")
            print("Hint: Full name")
    
    print("Access granted! Welcome, Sean <3!")
    
    age = ""
    while age not in ['34', '20']:
        age = input("Enter your age: ")
        if age not in ['34', '20']:
            print("Error, wrong! Try again!")
            print("Hint: yours or mine (when we got together).")
    
    print("CORRECT!")
    
    password = ""
    while password != '10.27.2025':
        password = input("Password? ")
        if password != '10.27.2025':
            print("Error, try again.")
            print("Hint: First Date and use periods not a slash.")
    
    print("I love you!")
    
    # Setup screen
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Heart Drawing")
    
    t = turtle.Turtle()
    t.speed(3)
    t.color("red")
    
    def draw_heart():
        t.begin_fill()
        t.left(140)
        t.forward(180)
        t.circle(-90, 200)
        t.left(120)
        t.circle(-90, 200)
        t.forward(180)
        t.end_fill()
    
    draw_heart()
    t.hideturtle()
    
    print("Hope you enjoyed <3")
    break

turtle.done()
