# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define main_char = Character('', color="#8883f4")
define stor = Character('Me', color="#8883f4")
define ob = Character('Ob', color="#8b0000")
define airis = Character('Airis', color="#ad2d89")
define letter = Character('Letter', color="ffffff")

image street = "bg/street.jpg"
image tavern = "bg/tavern.jpg"

# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:

    jump first_act

    return



label first_act:
    scene tavern

    main_char "It was a normal Sunday morning, I had the day off, so I was going to have breakfast and have a glass of beer."
    stor "Hey Airis, what's for breakfast today?"
    main_char "A tavern owner named Airis came out from behind the bar. A very hard-working woman, in the 3 months that I have been living in this tavern, I have never seen her sleep or rest, constantly at work. Sometimes I’m even scared for her."
    show airis2 at left
    with dissolve
    airis "And you don’t seem to know, Stor, we’ve been having the same dish for breakfast for 2 weeks now."
    stor "Is this crappy stew again? Or maybe you can cook something better for your beloved guest?"
    airis "What makes you think you're my favorite guest? Let's not make things up and order what we have."
    stor "Okay, okay, a plate of stew and a glass of beer."
    main_char "I put 1 silver and 3 copper coins on the bar counter"
    airis "There's more here than needed."
    stor "I know it's for bothering you with a scoundrel like me."
    hide airis2
    with dissolve
    main_char "I had just sat down at the table to eat beef stew and drink the desired glass of beer, when a low male voice called out to me."
    main_char "Half of the table was blocked by the shadow of the plate armor of my colleague named Ob."
    main_char "He has a bad character, of course, but you can rely on him, he will never abandon his own people, more than once thanks to him we got out of such situations that it’s scary to remember."
    show ob at left
    with dissolve
    ob "Hey, Scott, you better not start drinking in the morning. A task has appeared."
    stor "Seriously? We just returned from a mission the day before yesterday, what happened again?"
    ob "Well, better read it yourself."
    main_char "O handed me a folded note with purple sealing wax."
    stor "Wait, is it that serious? \n The last time I saw the king put a seal on orders was about 7 years ago, when his daughter disappeared. \n -I said in a whisper."
    main_char "Having torn the seal, I began to read the order, simultaneously eating the stew with my other hand."
    main_char "At first it seemed strange to me that the king himself decided to write out an order for some unimportant task, but as I read further, I understood more and more why this happened."
    main_char "he last line made me spit the soup back into my plate in surprise."
    stor "Wait, what the hell is this? How could this happen?"
    ob "Do you think I know? I was shocked myself. In general, you understand, you don’t have time to finish eating, so pack your ammunition and let’s go."
    hide ob
    with dissolve
    show letter
    with dissolve
    letter "Thirty miles north of Falo, in the village of Tillanium, an extraordinary incident occurred. About a month ago, a messenger arrived from this village with information about an infection that had killed all the livestock. A group of a priest and three healers was sent there, but after 3 weeks there was no news from them."
    letter "Tonight one of the healers arrived, completely covered in mushrooms, he conveyed information that the infection in the village was more than a simple pestilence of livestock and asked that a detachment of soldiers and several priests be sent there. Having conveyed this information, the doctor soon died."
    letter "I, King Frederick XIII, delegate this task to the detachment of Commander-in-Chief Hanji. Due date: immediately."
    hide letter
    with dissolve
    scene street
    main_char "After 10 minutes of getting ready, I was already standing on the street where Ob was waiting for me."
    stor "I'm ready, we can go. Have the others been notified yet?"
    show ob at left
    with dissolve
    ob "Yes, I already visited Tia, she went to get Arisius."
    stor "Great, then, to Hanji?"
    ob "Not right away, we need to go to one shop and we can go to the commander-in-chief."
    

    return