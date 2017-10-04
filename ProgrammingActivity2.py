# Welcoming the user to my adventure program
# Getting the input from the user in order to tell them what they should do

print ("Hello! Welcome to my adventure game! You are a tourist visiting the Philippines. You encounter a guy named mark and he asks you:")

# asking for their name for an introduction
name_str = raw_input("What is your name? ")
name = name_str

print "Hello,",name ," It is really nice to meet you!"

# figuring out if they have visited the Philippines or not

visited_str = raw_input("Have you ever visited the Philippines before? Yes or No?: ")
visited = visited_str

if visited == "Yes":
    print ("Great! I can give you ideas of what you could do while you're here!")
else:
    print ("That's okay! I will give you ideas of activities to keep you occupied and having fun while you're here!")

# figure out where they want to go

place_str = raw_input("Would you like to visit the beautiful islands or do community service while you are here?: ")
place = place_str

if place == "beautiful islands":
    print ("Great! I will sign you up for a tour of the gorgeous islands of the Philippines, along with many different activities!")
else:
    print ("Awesome choice! I will sign you up with a specific organization that gives food to the hungry")

# output what happened after the user made their choice

if place == "beautiful islands":
    print("You had a wonderful tour of the islands of the Philippines and captured amazing pictures that all your friends were jealous of!"
          "You are already looking forward to your next trip!")
else:
    print("You had a humbling experience doing community service in the Philippines. You fed many different people and you guys made an impact on each other's lives."
          "You are planning on coming back to continue this wonderful organization! Great job!")

print ("Thank you so much for using my adventure game!")





