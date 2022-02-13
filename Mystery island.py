print('''
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("Welcome to Mystery Island.")
print("Your mission is to find the treasure by escaping from this island's mystery.")


choice1 = input('You\'re at a bus stop, there are two buses, left one goes to island and the right one goes to your school. CHOOSE WISLEY .Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('Hmm good choice. You\'ve arrived to the destination. Look staright now you can able to see an island far across the sea, Once the adventure started there is no turning back. CHOOSE WISLEY. Type "proceed" to head forward. Type "stop" to head back to your boring life. \n').lower()
  if choice2 == "proceed":
    choice3 = input("Someone want to get rich huh? .But all of this risk will be worth it. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?. CHOOSE WISLEY . \n").lower()
    if choice3 == "red":
      print("As in the name full of FIRE. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure!, pay your tuition. You Won!")
    elif choice3 == "blue":
      print("BAD CHOICE, you waked up a Griffin . Game Over.")
    else:
      print("Seriously,.. that don't even exist . Game Over.")
  else:
    print("You have arrived to your school, submit your assignment without fail. Game Over.")
else:
  print("You returned to your normal life. Game Over.")