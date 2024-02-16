# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define main_char = Character('', color="#8883f4")
define stor = Character('Me', color="#8883f4")
define ob = Character('Ob', color="#8b0000")
define airis = Character('Airis', color="#ad2d89")
define letter = Character('Letter', color="ffffff")
define sariel = Character('Sariel', color="#704178")
define reivi = Character('Reivi', color="#556b2f")
define arisius = Character('Arisius', color="#72b7b3")
define tia = Character('Tia', color="#fbd2c1")
define hanji = Character('Hanji', color="#401641")




image street = "bg/street.jpg"
image tavern = "bg/tavern.jpg"
image near_potion = "bg/near_potion.jpg"
image potion_shop = "bg/potion_shop.jpg"
image corridor = "bg/corridor.jpg"
image cabinet = "bg/cabinet.jpg"
image main_square = "bg/main_square.jpg"
image gates = "bg/gates.jpg"
image dungeon = "bg/dungeon.jpg"
image dungeon_room = "bg/dungeon_room.jpg"








# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    $ panic = False
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
    hide ob
    with dissolve
    menu:
        "Go to the shop":
            $ antidote = True
            show ob at left
            with dissolve
            stor "Then, let's hurry up. We need to get this task done quickly."
            ob "Yes, we just need to buy a couple of potions, it will be done quickly."
            hide ob
            with dissolve
            main_char "It took literally 10 minutes to get to the shop, but due to the incredible July heat, I was already squeezed like lemon."
            scene near_potion
            show ob at left
            with dissolve
            stor "Oh, it’s so hot today, my brains are melting."
            ob "Yes, especially in armor, I feel like I’m in a steam room."
            ob "That's it, we've arrived, will you come with me or wait outside?"
            hide ob
            with dissolve
            menu:
                "Go to the shop with Ob.":
                    scene potion_shop
                    show sariel at left
                    with dissolve
                    show ob at right
                    with dissolve
                    sariel "Good morning, welcome to the alchemy shop \"Tasha's Cauldron\"."
                    ob "Good morning, we need 3 poison resistance potions, Stor, do you need any potions?"
                    main_char "I felt the pocket in which I usually carry gold, but it was empty."
                    stor "Oh, apparently I left a bag of coins when I was packing before leaving. Apparently I'm without potions this time."
                    ob "If you need some potions, then take them, I’ll pay, then you’ll return them."
                    stor "Thanks, Ob, then I'll take..."
                    menu:
                        "Potion of Healing":
                            $ potion = "Healing"
                        "Potion of Invisibility":
                            $ potion = "Invisibility"
                    stor "Thanks, Ob, then I'll take Potion of [potion]"
                    ob "Then that's all we'll take, how much will it cost us?"
                    sariel "So, 3 Potions of poison resistance and a Potion of [potion] will cost 125 gold coins"
                    ob "Yeah, a little expensive, but what can you do? We don't really have a choice, thank you very much, have a nice day."
                    sariel "Thanks for purchase, come again. Have a good day."
                    stor "Have a good day."
                    hide ob
                    with dissolve
                    hide sariel
                    with dissolve
                    scene near_potion
                    stor "Hey, Ob, when did you become so kind? He paid for me and even said thank you to the saleswoman."
                    stor "Did something happen to you? Be honest, I'll help."
                    ob "Very funny, let's go to Hanji already. Hold your potion."
                "Stay outside.":
                    ob "Okay, then I'll be quick."
                    main_char "Ob went into the store, and I stayed near the shop."
                    show reivi at left
                    with dissolve
                    reivi "Hey Stor!"
                    main_char "The large figure of the half-orc Reivi appeared in front of me. You can't tell from him, but he is an extremely gifted student at the magic academy in Falo."
                    main_char "Reivi is studying to be a battle mage and is doing extremely well. I was in the same group with him on a combat mission a couple of times."
                    main_char "Although it was last year, he had amazing combat and magic skills. I think after a year he's gotten even better at it."
                    reivi "How are you? Decided to go for a walk on your day off?"
                    stor "Not really, work related matters."
                    reivi "You're out of luck, of course, the archmage loads you with work even on Sunday."
                    reivi "What kind of task is it, if not a secret?"
                    menu:
                        "Tell about the task":
                            $ panic = True
                            main_char "It was clear from Reivi's face that he was frightened by this information, but he was intently trying to hide it."
                            reivi "Wow, what a horror. I hope you can cope with this infection. I believe in you!"
                            show ob at right
                            with dissolve
                            ob "Oh, Reivi, hi! What are you doing here?"
                            reivi "Just taking a walk, nothing like that. I'd better go quickly, I won't disturb you, good luck."
                            hide reivi
                            with dissolve
                            hide ob
                            with dissolve
                            show ob at left
                            with dissolve
                            main_char "As soon as Reivi walked about 20 meters away from us, I felt pain in my arm. Ob grabbed my hand with such force that a bear's paw wouldn't close."
                            main_char "Even through the closed visor, I felt Ob’s gaze, which literally burned through me."
                            ob "Stor, do you understand what you're doing? This is a secret mission! Now the whole city will know about it."
                            ob "We're finished when this reaches the king. You do understand that the letters were handed to everyone for a reason?"
                            ob "The king doesn't want anyone to know about this, but now everyone will know about it. You are a complete idiot."
                            main_char "After these words, Ob let go of my hand and we walked towards Hanji. He didn't say another word to me the whole way."
                        "Don't tell about the task":
                            $ panic = False
                            reivi "I understand that your group has secret missions, I do not insist. In any case, good luck to you."
                            reivi "When you return, we can go to some tavern to relax and chat over a glass or two of ale."
                            reivi "I'll go, have a nice day. Come back alive!"
                            hide reivi
                            with dissolve
                            main_char "After these words, Reivi walked further down the street, but I managed to notice how he turned around. There was concern in his eyes about this situation."
                            show ob at left
                            with dissolve
                            ob "We can go, I bought everything we need."
                            stor "Great, let's go to Hanji quickly."
                            hide ob
                            with dissolve
        "Don't go to the store":
            $ antidote = False
            show ob at left
            with dissolve
            ob "I agree, we don't have much time, let's go to Hanji quickly."
            hide ob
            with dissolve
    scene corridor
    main_char "After 20 minutes of brisk walking, You and I stood outside Hanji's office."
    if panic:
        show ob at left
        with dissolve
        ob "I won’t tell anyone that Reivi knows about the task, but don’t think that I’m doing this out of kindness."
        ob "I don't want to jeopardize our mission, so we pretend that you didn't say anything and that I didn't see or hear anything."
        stor "Thank you for your understanding, Ob."
        hide ob
        with dissolve
    arisius "And you are already here, how good."
    show arisius at left
    with dissolve
    stor "And you, as always, creep up silently. We are, after all, in the same detachment; we might not be frightened."
    arisius "Well, I'm sorry, it's not my fault that you are so inattentive."
    main_char "Of course, you can’t tell from him, but once upon a time Arisius was an absolutely full-fledged person, but after many experiments with his body he became like this."
    main_char "Some parts of his body can extend, his arms and legs have become much stronger thanks to implants. And in general, he has become much stronger, more mobile and more useful in missions."
    main_char "This does not take into account the fact that he also has basic magic skills. Thanks to this, he is an indispensable member of our party."
    tia "Apparently everyone forgot about me."
    show tia at right
    with dissolve
    stor "Oh, and you're already here. How are you doing? Long time no see."
    tia "Everything is as usual. I just returned from a trip yesterday."
    main_char "On our team, Tia is responsible for speed and surprise. She spent years learning to be stealthy and deadly."
    main_char "She is an elf, so it’s not clear from her how old she is, and we didn’t ask. Somehow there was no need for a word."
    hide tia
    with dissolve
    show ob at right
    ob "So, let's come in if everyone is ready."
    hide ob
    with dissolve
    hide arisius
    with dissolve
    scene cabinet
    show hanji at left
    with dissolve
    hanji "And you got there quickly. I thought I would have to wait longer."
    main_char "It seems like I was in this office just a couple of days ago, but every time it feels like the first time."
    main_char "No matter how beautiful it is here, the feeling is unpleasant. Almost every time I come here, I am told or shown information that I would not like to see."
    main_char "Same thing this time. If it weren’t for my duty of service, I would never want to go now to understand what happened in that village."
    main_char "Especially considering the details that were in the letter. I am sure that now there will be more details and they will be even worse than before."
    hanji "Sit down, now I’ll tell you the plan of action."
    main_char "Hanji is the most strong-willed woman I've ever met. Every decision she makes on missions and outside of them always turns out to be correct."
    main_char "In general, Hanji is our commander. No one has ever contradicted her, because they know that she knows what will be better."
    main_char "I've always admired Hanji. I could never give myself entirely to faith in God."
    hanji "Basically, the mission is to find out what happened in the village of Tillanium and solve the problem if possible."
    hanji "Also, one of the points is saving a group of healers and a priest. The priest who was sent to the village is a high-ranking member of the church of the goddess Ayun."
    hanji "Therefore, the archmage and the king ordered us to save him first."
    hanji "If it turns out that he is dead, it will be a huge scandal."
    hanji "Do you have any questions?"
    show tia at right
    with dissolve
    tia "How much will we be paid for the mission?"
    hide tia
    with dissolve
    show arisius at right
    with dissolve
    arisius "Tia, is that all you think about? I would have asked something more important."
    hide arisius
    with dissolve
    show tia at right
    with dissolve
    tia "What could be more important? I spend my time, energy, arrows, and by the way, they are not so cheap."
    hanji "Tia, be quiet. They'll pay you enough to buy you enough arrows for a few years. I have already said that this is a very important task for the king."
    hanji "In addition, if the mission is successful and we manage to save the priest, we will be appointed honored officers of the order."
    hanji "With this medal you will be able to receive free arrows in any quantity, so don’t worry about it."
    tia "Then, I have no more questions."
    hide tia
    with dissolve
    show arisius at right
    with dissolve
    arisius "Any guesses about what happened in the village?"
    arisius "It seems to me that this is not a simple infection if such a high-ranking priest could not cope with it."
    hanji "Yes, you're right. I took a sample of mushrooms from the body of one of the doctors who reached the capital."
    hanji "They look extremely strange. Also, I found remnants of magical effects on the mushrooms."
    hanji "Either the priest tried to cure this doctor of mushrooms, but he did not succeed, or this means that the mushrooms were created by magic."
    hide arisius
    with dissolve
    show ob at right
    with dissolve
    ob "The situation, of course, is not the best. Then we will need magical support."
    ob "Hanji, Arisius, we rely on you."
    hanji "Yes, of course."
    main_char "Arisius nods."
    hanji "If there are no more questions, then we can move forward."
    hanji "I need 10 minutes to get ready. Wait outside for now."
    hide hanji
    with dissolve
    hide ob
    with dissolve
    scene main_square
    main_char "Hanji's office is located in the Heroes' Guild building, so when we went outside we found ourselves in the main square of the city."
    show ob at left
    with dissolve
    ob "I really don't like this task. Some kind of bad feeling."
    show arisius at right
    with dissolve
    arisius "I agree. It seems that in my head I understand that this is our usual task, but inside everything is screaming that something is wrong."
    show tia at center
    with dissolve
    tia "Don't make it scary. Arisius, you yourself said that this is our usual task, which means everything will go as usual."
    tia "Yes, I was also a little wary that the king himself sent us letters, but it turned out to be because of the priest, so everything is in order."
    main_char "Although Tia’s words were logical and she tried to calm us down, it was clear from her that she was also nervous."
    hide ob
    with dissolve
    hide tia
    with dissolve
    hide arisius
    with dissolve
    menu:
        "Say it's okay":
            stor "I agree with Tia, everything will go well. The main thing is not to relax and be on your guard."
            stor "We have already completed similar tasks so many times that we are already capable of any task."
        "Say you're nervous too":
            stor "I also have a strange feeling. It looks like when we went out on our first mission."
            stor "This is probably due to the fact that we have never encountered this before. Hanji is with us this time, so we will listen to her and everything will be fine."
            stor "Maybe..."
    show ob at left
    with dissolve
    ob "Hey, I didn’t tell you about my experiences so that we all start to be afraid now."
    ob "There is nothing scary about this task. We'll just do our job and that's it."
    ob "We stop being nervous and focus on the task."
    show hanji at right
    with dissolve
    hanji "I'm already ready. What are you talking about?"
    hide ob
    with dissolve
    show arisius at left
    with dissolve
    arisius "Nothing, Hanji. Can we move out now?"
    hanji "If everyone is ready, then yes."
    hide hanji
    with dissolve
    hide arisius
    with dissolve
    main_char "On the way to the city gates, no one said a word."
    main_char "Apparently, everyone understood that this task was not as simple as it seemed to us."
    scene gates
    main_char "Having reached the gate, Hanji approached one of the guards and whispered something in his ear."
    show hanji
    with dissolve
    hanji "Guys, follow me here."
    stor "Hanji, shouldn't we go outside the gate and go to the village?"
    hanji "Literally 10 minutes and we’ll go to the village, come in."
    hide hanji
    with dissolve
    scene dungeon
    main_char "We followed Hanji into the dark basement along the city wall and stopped in front of the iron door."
    show hanji at left
    with dissolve
    hanji "Just don't be scared."
    hide hanji
    with dissolve
    main_char "Hanji pulled out a set of keys from her pocket and opened the door. From behind the door there was immediately a smell of something bittersweet."
    main_char "The smell was so strong that I had to hold my nose to prevent vomiting."
    main_char "Hanji walked inside and called us to follow her."
    scene dungeon_room
    main_char "We entered a small room in which there was a jelly table in the center, on which lay the body of a man with a cut stomach and chest."
    show hanji at left
    with dissolve
    hanji "This is the doctor who reached the capital. After his death, we decided to steam him in order to better understand what exactly happened to him."
    hanji "All internal organs are covered with mushrooms, but these mushrooms have one peculiarity."
    hanji "They seem to be afraid of sunlight or light in general, so they only grow under the victim's clothing or where there is no light."
    hanji "One of these places is the internal organs, which is why the victim died."
    hanji "I think you understand what will need to be done."
    show arisius at right
    with dissolve
    arisius "You'll have to use light spells if you have to come into contact with mushrooms."
    hanji "Yes, absolutely."
    hanji "That's all I wanted to show you, now you can go to the village."
    hide arisius
    with dissolve
    hide hanji
    with dissolve
    scene gates
    main_char "After that, we left the basement and headed towards the village."
    main_char "After what Hanji showed us, it only made me more nervous. I could not remember having seen any similar disease."
    main_char "Apparently, our fears that this was not an easy task turned out to be true."
    #end of act 1






























































    return