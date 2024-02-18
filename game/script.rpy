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
define unknown = Character('???', color="#bf3952")
define eri = Character ('Eri', color="#bf3952")
define mushroom = Character('Mushroom man', color="#c4416f")
define game = Character('Game system', color="ffffff")




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
image road = "bg/road.jpg"
image forest = "bg/forest.jpg"
image camp = "bg/camp.jpg"
image black = "bg/black.png"
image sunrise_forest = "bg/sunrise_forest.jpg"
image village = "bg/village.jpg"
image house_inside = "bg/house_inside.jpg"
image mushroom_hut = "bg/mushroom_hut.jpg"
image canyon = "bg/canyon.jpg"
image hall = "bg/hall.jpg"




define tavern_ambience = "audio/tavern_ambience.mp3" 
define outside_tavern = "audio/outside_tavern.mp3"
define city_centre = "audio/city_centre.mp3"
define hanji_office = "audio/hanji_office.mp3"
define journey_start = "audio/journey_start.mp3"
define strange_disease = "audio/strange_disease.mp3"
define dark_woods = "audio/dark_woods.mp3"
define campfire_stories = "audio/campfire_stories.mp3"
define major_decision = "audio/major_decision.mp3"
define enemy_encounter = "audio/enemy_encounter.mp3"
define final_sendoff = "audio/final_sendoff.mp3"
define mission_success = "audio/mission_success.mp3"
define boss_fight = "audio/boss_fight.mp3"
define mission_failed = "audio/mission_failed.mp3"
define mission_disaster = "audio/mission_disaster.mp3"
define tragedy_strikes = "audio/tragedy_strikes.mp3"


define letter_sfx = "audio/letter_SFX.mp3"
define kick_sfx = "audio/kick_SFX.mp3"
define grip_sfx = "audio/grip_SFX.mp3"
define terror_sfx = "audio/terror_SFX.mp3"






# Игра начинается здесь:
label start:


    $ priest = True
    $ panic = False
    $ potion = "None"
    $ girl = False
    $ girl_alive = True
    $ score = 0
    $ ending = "n"
    jump first_act

    return



label first_act:
    scene tavern
    play music tavern_ambience volume 0.5 fadein 1 fadeout 1 loop
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
    play sound letter_sfx volume 0.8
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
    stop music fadeout 1.0
    play music outside_tavern volume 0.25 fadein 1 fadeout 1 loop
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
            stop music fadeout 1.0
            play music city_centre volume 0.5 fadein 1 fadeout 1 loop
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
                            play sound grip_sfx volume 1.0
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
    stop music fadeout 1.0
    play music hanji_office volume 0.5 fadein 1 fadeout 1 loop
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
    stop music fadeout 1.0
    play music city_centre volume 0.5 fadein 1 fadeout 1 loop
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
    stop music fadeout 1.0
    play music strange_disease volume 0.5 fadein 1 fadeout 1 loop
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
    jump second_act
    return



label second_act:
    scene road
    stop music fadeout 1.0
    play music journey_start volume 0.5 fadein 1 fadeout 1 loop
    main_char "The path to the village lay north through large fields of almost ripened wheat and through a small forest."
    main_char "Although this was not the longest outing for our team, the road was still quite long."
    scene forest
    stop music fadeout 1.0
    play music dark_woods volume 0.5 fadein 1 fadeout 1 loop
    main_char "When it was already deep night, we were about a mile from the village."
    show arisius at left
    with dissolve
    arisius "Hey, there's something on the edge of the road."
    hide arisius
    with dissolve
    main_char "I looked closer at where Arisius was pointing."
    main_char "At the edge of the road something glowing reddish could be seen."
    show hanji at left
    with dissolve
    hanji "Let's come closer to get a better look."
    hanji "We are trying to be quieter, perhaps this is due to the mushrooms from the village."
    hide hanji
    with dissolve
    main_char "We came to a distance of about 15 feet and our guesses were confirmed."
    main_char "On the edge of the road lay the body of a man covered with red glowing mushrooms."
    show hanji at left
    with dissolve
    hanji "Let's examine the body and hurry to the village. Apparently the fungal disease can spread beyond the village."
    hide hanji
    with dissolve
    main_char "Coming close to the body, it became clear that this was the body of a young girl."
    stor "Hey Hanji, this is a girl, about 17 years old."
    main_char "After these words, the girl let out a loud sob and coughed. She involuntarily tried to cover her mouth with her hands and something similar to blood dripped onto her palms."
    main_char "But there was one difference. The blood gave off a slight reddish glow."
    stor "Hange, she's alive, what should we do?"
    show hanji at left
    with dissolve
    hanji "We don't have time for this, let's move on. Let's leave her here, if on the way back she's alive, we'll take her to the capital."
    stor "Hanji, but how can that be? She may die before then. It is unknown how long the mission will last."
    hanji "Stor, do you want to question my command? If I hear one more objection, then you will lie down next to this girl."
    hanji "Let's say that you went missing and we couldn't find you. No one will even look for you. All clear?"
    hanji "Now we have to go, we have a mission in the village."
    stor "Yes, Commander Hanji."
    hide hanji
    with dissolve
    main_char "It hurt to leave this girl here. Most likely, we were the last chance to survive, but now she is doomed."
    main_char "Hanji and everyone else moved towards the village. I tried to get up and follow them, but then this girl grabbed my leg."
    unknown "Hey dad, is that you?"
    stor "Hanji..."
    menu:
        "Say that the girl is conscious":
            stor "Hanji, this girl is conscious."
            show hanji at left
            with dissolve
            hanji "So what? We will not take her with us, much less waste our medicine or magical powers on her."
            stor "Hanji, you can't do that. This girl is still alive and conscious, we can’t leave her here!"
            hanji "Then, you will carry it yourself. If you can’t handle it, then none of us will help you, even if mushrooms appear on you."
            hide hanji
            with dissolve
            menu:
                "Save the girl":
                    stor "I agree with that. If I can't handle this, then don't save me. I understand what I'm doing."
                    show hanji at left
                    with dissolve
                    hanji "I understand you. I hope you still have a head on your shoulders."
                    hide hanji
                    with dissolve
                    $ girl = True
                "Leave the girl here":
                    stor "Okay, Hanji, I understand you. Sorry for disturbing."
                    show hanji at left
                    with dissolve
                    hanji "You should have done this right away and not contradicted me. We are heading to the village."
                    hide hanji
                    with dissolve
                    menu:
                        "Finish off the girl":
                            main_char "I pulled the dagger out of its sheath, plunged it into the girl’s neck and ran it along her throat."
                            main_char "The girl made a soft popping sound and her hand went limp."
                            main_char "After that, I threw back the limp hand lying near my leg and followed my team."
                            $ girl_alive = False
                        "Leave her on the road":
                            main_char "I removed my hand from my leg and accelerated after the team."
        "Tell them to wait for you":
            show hanji at left
            with dissolve
            hanji "What's there again?"
            stor "Nothing, wait for me."
            hide hanji
            with dissolve
    if girl:
        main_char "Although the girl was very thin, it was difficult to carry her along with armor and weapons."
        main_char "I was walking at the back of the group and noticed that Ob was also a little behind the others."
        show ob at left
        with dissolve
        ob "You understand how this could turn out, right?"
        stor "Yes, I understand that if something happens, it will be my responsibility and I will deal with it."
        ob "That goes without saying. I’m talking about something a little different, with this action you are jeopardizing our mission and us."
        ob "You are the first person in 10 years who decided to contradict Hanji’s commands, she just won’t let it go, seriously."
        ob "Her words that you can go missing and no one will look for you, this may be true. Be careful."
        stor "Thanks for the warning. Hurry to Hanji so she doesn't suspect anything."
        hide ob
        with dissolve
    main_char "When we almost reached the village, I saw a reddish glow from behind the trees."
    show hanji at left
    with dissolve
    hanji "So, now we’ll set up camp, regain our strength and sleep, and in the morning we’ll go to the village to figure out what happened there."
    hanji "Any objections?"
    if girl:
        main_char "I noticed how at this phrase Hanji threw a sharp glance in my direction."
    show ob at right
    with dissolve
    ob "No, Hanji, there are no objections."
    hide hanji
    with dissolve
    hide ob
    with dissolve
    scene camp
    stop music fadeout 1.0
    play music campfire_stories volume 0.5 fadein 1 fadeout 1 loop
    main_char "Me, Ob and Arisius began to set up the camp, and Hanji and Tia started the fire at this time and in about half an hour the camp was ready."
    if girl:
        main_char "When we were almost setting up the tent, I noticed that Hanji approached the girl lying on the ground and poured something from a glass flask into her mouth."
    show hanji at left
    with dissolve
    hanji "So, the patrol size is 4 people. The first will be Ob, then Arisius will replace him, then I will be, and the fourth will be Stor."
    hanji "Everyone except Ob go to bed immediately to regain your strength for tomorrow."
    if girl:
        main_char "Hanji went and leaned towards me."
        hanji "I poured a poison resistance potion into the girl's mouth. He will wake up in about 8 hours, approximately on your watch."
        hanji "Try to find out as much information as possible so that it does not become a burden for us."
        play sound grip_sfx volume 1.0
        main_char "Hanji’s hand fell on my shoulder and at the same time I felt severe pain near my collarbone. Her grip was so strong that I could feel her moving her fingers even through the leather armor."
        hanji "If you disobey my order again, your family will never see you again. They will only receive a letter from the king about how bravely you fought. All clear?"
    stor "Yes, Commander Hanji, everything is clear."
    hide hanji
    with dissolve
    if girl:
        main_char "I was glad that Hanji helped this girl, but the information that she could so easily sacrifice me was scary."
        main_char "After that, everyone except both went into the tents and tried to sleep."
    else:
        main_char "I was tormented by thoughts of what would have happened if I had saved that girl, but the thought that I might not return from this mission due to non-compliance with command frightened me even more."
    scene black
    main_char "Sleep, of course, was not going well, but after about half an hour I managed to fall asleep."
    if girl:
        play sound kick_sfx volume 0.8
        main_char "I felt something hit my stomach with force."
        hanji "Hey, good-natured fool, wake up. It's your turn to go out on patrol."
        show hanji at left
        with dissolve
        scene camp
        hanji "Moreover, your new friend woke up there. Go say hello for the sake of decency."
        stor "Yes, Commander, Hanji. I'm starting patrol."
        hide hanji
        with dissolve
    else:
        scene camp
        show hanji at left
        with dissolve
        hanji "Hey Stor, wake up. Time for your watch."
        stor "Yes, 2 minutes and I will start patrolling."
        hide hanji
        with dissolve
    if girl:
        main_char "I left the tent and saw a girl sitting near the fire and warming her hands on it."
        main_char "When she saw me getting out of the tent, she waved her hand and smiled sweetly at me."
        show eri at left
        with dissolve
        stor "Hello. What is your name?"
        eri "My name is Eri, what's yours?"
        stor "Stor. What were you doing on that road?"
        eri "To be honest, I don’t remember how I ended up like this, but that scary woman who was here before you told me that you found me on some road about a mile from here."
        eri "I don’t remember how I got there or what happened. She also said that you were the one who decided to save me. Of course, it was not very nice of her to say that she was against my salvation, but I understand her."
        stor "Well, yes. That's pretty much how it was. You don't remember anything at all what happened to you?"
        eri "Actually, I remember a little about what happened, but I was scared to tell that woman about it."
        eri "And you saved me, so I trust you and can tell you."
        eri "About a month ago, a strange man came to our village. His hat looked like a mushroom's hat, but no one thought anything of it."
        eri "He asked to stay for a couple of days to recuperate after a long journey and said that after that he would leave the village. One old woman took him in."
        eri "He actually stayed for a few days and left. This grandmother didn’t have anything missing from her house, he didn’t do anything to her, but after a couple of days strange events began."
        eri "That old woman died in her bed, and those who saw her body noticed a red glow from her body."
        eri "Then the whole village was overwhelmed by this infection. We sent a messenger to the capital, after which they sent us a priest and doctors, but they were unable to cope with this infection and they also became infected."
        eri "Everyone except the priest, he spent a long time trying to cure us and the doctors, giving them holy water and using some spells. Nothing helped."
        eri "About three days ago this man came again, after which all this began. What we thought was a mushroom-shaped hat turned out to be a real mushroom. And it was all made from mushrooms."
        eri "The priest tried to negotiate with him to do something to save the villagers, but the Mushroom Man did not listen to him and took the priest to his hut."
        eri "After this, the priest was not visible. Almost all the villagers died when I decided to run away for help. I think there is no one alive there now."
        eri "The priest and all the residents believed that the problem was with this man. Most likely, if you defeat him or persuade him to remove this infection, the infection will go away."
        stor "We'll definitely look into this. You can rely on us. My allies and I are a team that will not abandon such a matter without a solution."
        eri "Okay, I believe in you"
        main_char "The next 2 hours of my patrol were spent talking with Eri. She turned out to be an extremely sweet girl, but with a sad fate."
        main_char "Her parents and friends died due to the infection, and she was the only one who was able to escape, after which she crawled towards the city for 3 days, but fell exhausted."
        stor "Forgive me, of course, but I will have to tell information about the village and this man to my teammates. This is necessary so that we can deal with this."
        eri "Yes, I understand, it's okay. If you say that there is no way without this, then I believe you."
        hide eri
        with dissolve
        main_char "When the sun had already fully risen in the sky, everyone woke up and I told them about the history of Eri and what happened in the village."
        scene sunrise_forest
        stop music fadeout 1.0
        play music major_decision volume 0.5 fadein 1 fadeout 1 loop
        main_char "We packed up the camp and began to decide what to do with this situation."
        show hanji at left
        with dissolve
        hanji "So, we need to go to that hut and either kill this person, but then the fungal infection will not leave the village and we will not be able to save the priest."
        hanji "Or we will agree with this person so that he gets rid of this infection and gives us the priest. One problem remains. I don't know what we can offer him in return."
        hanji "Anyone have any ideas?"
        show eri at right
        with dissolve
        eri "I'm not sure, but maybe he can be convinced, because when he came the second time, when the village was overrun by mushrooms, he was disappointed with it."
        eri "Perhaps he himself does not like what is happening or it is not his fault. I think we need to talk first and find out what he needs."
        hanji "I didn’t ask your opinion, but so be it, I’ll listen to your opinion. Anyone else have any guesses?"
        stor "No, we don't have enough information. We need to first see what is happening in the village and examine this man's hut."
        hanji "Yes, I agree with that. Let's do so. If there are prerequisites that the girl’s assumption may be true, then we will try to talk and convince this person."
        hanji "So, we're heading to the village now."
        main_char "Hanji looked towards the girl."
        hanji "Can you go on your own?"
        eri "Yes, I feel better."
        hanji "So you'll be walking behind us. Try not to become a burden. Avoid any collisions with the enemy. It’s better to be silent so as not to blurt out anything unnecessary."
        hide hanji
        with dissolve
        hide eri
        with dissolve
    else:
        main_char "Hanji went to bed, and I left the tent and looked around."
        main_char "It was quite chilly, but thanks to the fire it was quite manageable. As I expected, the patrol went on without any problems until dawn."
        main_char "I suddenly felt hungry, so I took out a packed lunch from my bag and decided to warm it up on the almost burnt-out fire."
        tia "Decided to have breakfast alone?"
        show tia at left
        with dissolve
        stor "You know, it’s boring on patrol, so I decided to occupy my time with something."
        tia "Why are you always so serious? You and Ob are very much in agreement on this. I was joking."
        main_char "Tia also took out a packed lunch from her bag and handed it to me."
        tia "Warm it up, please. I'll go and warm up for now."
        hide tia
        with dissolve
        main_char "I started heating up the packed lunch on the fire while Tia went a little further into the forest to warm up."
        stor "Tia, your packed lunch is warm. You can go eat."
        ob "I'll see that you're our cook today. Will you warm me up a packed lunch too?"
        show ob at left
        with dissolve
        stor "Go to hell. Warm up yourself your own packed lunch."
        ob "Don't get so excited."
        hide ob
        with dissolve
        main_char "Me, Tia and Ob sat around the burnt fire to have breakfast, and a little later Arisius and Hanji woke up."
        main_char ""
        show hanji at left
        with dissolve
        stop music fadeout 1.0
        play music major_decision volume 0.5 fadein 1 fadeout 1 loop
        hanji "So now we need to find out what's going on in the village. Be as attentive and careful as possible."
        hanji "If you see a possible threat or enemy, immediately inform others and maintain the usual grouping."
        hanji "All clear?"
        stor "Yes, everything is clear, Commander Hanji."
        hanji "Time to head to the village."
        hide hanji
        with dissolve
    jump third_act
    #end of second act
    return







label third_act:
    if girl:
        scene village
        main_char "We headed to the village and Eri’s words turned out to be true. There was no one left alive in the village."
        main_char "We examined all the houses, but did not find the priest. Only the bodies of doctors were found."
        show eri at left
        with dissolve
        eri "That man's hut is there."
        show hanji at right
        with dissolve
        hanji "So we need to go there. Be careful, this person can hide and ambush you."
        hide eri
        with dissolve
        hide hanji
        with dissolve
        scene mushroom_hut
        stop music fadeout 1.0
        play music enemy_encounter volume 0.5 fadein 1 fadeout 1 loop
        main_char "We walked about 500 feet east and saw a small wooden hut covered in mushrooms."
        main_char "As we looked around the hut, a tall man came out of the hut covered in red glowing mushrooms."
        show mushroom at center
        with dissolve
        mushroom "Friends, I understand that you are wary of me because you don’t know what I am, but we can talk. Perhaps we will come to some kind of compromise."
        menu:
            "Yes, we should talk {i}neutral{/i}":
                $ score += 1
                mushroom "So we can talk calmly, what do you want to know?"
            "Let's start with who you are {i}information{/i}":
                mushroom "If you want to know who I am, then I will tell you."
                mushroom "I'd like to introduce myself, but I don't have a name in your idea of the word. If I contact my relatives, then they understand who I am."
                mushroom "But to make it easier, my name is Mash. I am Vegepygmy, the intelligent mushroom. Once upon a time there were a large number of us in this world, but due to some events, there were much fewer of us and the survivors had to hide."
                mushroom "Basically, we lived underground, but because of the dangers, we began to climb to the surface to find food."
                mushroom "But I am not one of the real Vegipygmies, I grew up on the body of some fallen magician. From that time on, I wandered in these forests, feeding on carrion, until I found this village."
        mushroom "Now I'm ready to answer your questions."
        menu:
            "Did you do this to the village of your own free will? {i}neutral{/i}":
                $ score += 1
                mushroom "I didn't really mean for this to happen, but I have no control over where I leave my particles."
                mushroom "I wouldn't want this to happen to anyone else. So I would like you to help me with this."
                menu:
                    "How can we help you? {i}information{/i}":
                        $ score += 1
                        #3
                        mushroom "I need a way to find a way into the underground, but there is one problem with this."
                        mushroom "Due to the structure of my body, many predators and other animals sense me from a long distance."
                        mushroom "Therefore, I need your help to get to the entrance to the underground."
                        hide mushroom
                        with dissolve
                        jump good_ending
                    "We won't help you. {i}insolence{/i}":
                        jump mid_ending
            "You will be held accountable for what you did to the village! {i}insolence{/i}":
                $ score -= 1
                mushroom "I understand that, but I couldn't do anything about what happened."
                mushroom "Apparently, we won’t be able to have an adequate conversation."
                jump mid_ending
    else:
        #bad ending
        jump bad_ending
    return


label loop:
    menu:
        "No, no one has an antidote or healing potion.":
            main_char "No one had an antidote or a healing potion."
            main_char "Soon after unsuccessful attempts to cure the priest, he breathed his last and died."
            hanji "Oh no. He died..."
            main_char "Hanji turned to us."
            show hanji at left
            with dissolve
            hanji "The mission has failed, we need to return as quickly as possible. We need to send help to this village so that the disease does not spread further."
            hide hanji
            with dissolve
            $ priest = False
            jump mid_ending_2
        "Take the healing potion out of your pocket.":
            if potion == "Healing":
                main_char "I took the healing potion out of my pocket and handed it to Hanji."
                main_char "Hanji gave the priest something to drink and he felt a little better. After this, Ob took out a bottle of antidote from his bag."
                main_char "Ob handed it to Hanji. Hanji also gave the priest an antidote."
                show hanji at left
                with dissolve
                hanji "This will help the priest reach the capital, where they will help him. Let's quickly move out of here."
                hide hanji
                with dissolve
                $ priest = True
                jump mid_ending_2
            else:
                game "Unfortunately, due to your choices throughout the story, this option is locked. Choose another option."
                jump loop
        "Ask Ob for an antidote.":
            if antidote:
                main_char "Ob took out a bottle of antidote from his bag."
                main_char "Hanji poured a bottle of antidote into the priest's mouth, after which the priest's breathing became more even."
                show hanji at left
                with dissolve
                hanji "He will be unconscious for a long time, but this will allow him to live until the capital. Let's hurry up."
                hide hanji
                with dissolve
                $ priest = True
                jump mid_ending_2
            else:
                game "Unfortunately, due to your choices throughout the story, this option is locked. Choose another option."
                jump loop
    return

label good_ending:
    show hanji at left
    with dissolve
    hanji "Hmm, I know one rift. I think it would be suitable as a passage to the underground."
    show mushroom at right
    with dissolve
    mushroom "Where is it?"
    hanji "Ten miles from here, at the foot of the Dragon Ridge"
    mushroom "So we need to move there."
    hanji "Can you remove the effects of the mushroom disease from the village and save the priest?"
    mushroom "I can save the priest, but I cannot remove the events in the village. If I go far from here, then after a while all the mushrooms will disappear."
    hanji "Okay, then let's get to rescuing the priest."
    mushroom "Come with me."
    hide hanji
    with dissolve
    hide mushroom
    with dissolve
    main_char "The mushroom man and I went into the hut. The priest was lying on the only bed in the hut, covered in mushrooms."
    main_char "The mushroom man approached the bed and put his hand on the part of the priest’s hand covered with mushrooms and began to pronounce some strange words."
    main_char "The mushrooms began to glow much stronger, just like the man himself. After a few minutes, the mushrooms on the priest's body began to decrease in size, and the mushrooms on the man's body began to swell and become larger."
    show mushroom at right
    with dissolve
    mushroom "In a couple of days, all the mushrooms will be gone from his body. He is fine now, his life is not in danger."
    mushroom "I think he'll be unconscious for the rest of the day, so you should make it back before he wakes up."
    show hanji at left
    with dissolve
    hanji "If that's true, then we should hurry up. Let's move out."
    hide hanji
    with dissolve
    hide mushroom
    with dissolve
    scene canyon
    stop music fadeout 1.0
    play music final_sendoff volume 0.7 fadein 1 fadeout 1 loop
    main_char "The path to the rift lay through a dense forest, in which it was not very easy to walk; by noon we reached the place."
    main_char "Approaching the edge of the cliff, the mushroom man, without saying a word, looked back at us and jumped down."
    show hanji at left
    with dissolve
    hanji "My guess is that the priest will wake up in 4 hours, so let's hurry back. We have to get there before he wakes up."
    hide hanji
    with dissolve
    scene mushroom_hut
    main_char "A little before sunset we reached the hut and went inside."
    main_char "Less than half an hour later the priest woke up. The mushrooms on his body had almost completely disappeared; they were still visible from under his clothes."
    main_char "We explained to the priest what happened and he agreed to walk with us to the capital."
    scene main_square
    main_char "The next morning we delivered the priest to the capital."
    main_char "That same evening, the king called us to his chambers and personally, as promised, gave us our reward."
    scene hall
    main_char "In honor of the rescue of the priest, the king decided to throw a big feast, to which we were also invited."
    main_char "At the same feast, we were officially given our medals for bravery and declared honorary adventurers."
    show hanji at left
    with dissolve
    hanji "Stor, what are you going to do with so much money?"
    stor "I just wanted to talk about this. I will no longer be an adventurer. At least in the near future. I need some rest"
    stor "I'll go see my family. I haven’t been there for a long time; somehow I couldn’t see him on such frequent assignments."
    stor "We will renovate the house with dad, I think they will be happy."
    hanji "Stor, your parents will be glad just to see you in health."
    hanji "I probably won’t be a squad leader anymore either. Maybe I’ll go on some kind of trip to the mountains or to monasteries."
    hide hanji
    with dissolve
    scene black
    main_char "The whole feast was spent talking about our team and old times. The unanimous decision was to disband our team for an indefinite period..."
    $ ending = "g"
    jump end
    return


label bad_ending:
    scene village
    stop music fadeout 1.0
    play music mission_disaster volume 0.5 fadein 1 fadeout 1 loop
    main_char "When we entered the village, no one was visible. Only when we started looking into the windows did we understand why the residents were not visible on the street."
    main_char "We were only able to find their bodies. They were all covered with red mushrooms."
    main_char "Some of them were completely covered with them, which was not immediately clear whether it was a person lying or simply mushrooms growing from the ground."
    show hanji at left
    with dissolve
    hanji "Apparently, no one is left alive. A terrible incident. Nobody sees the priest?"
    stor "No, I only found one of the healers. Maybe..."
    main_char "I stood over the body in white clothes, similar to the clothes of doctors, but I was not sure that it was her. All clothes were covered with dirt and blood mixed with mushroom juice."
    main_char "Hanji came up to me and examined the body."
    hanji "Yes, it's a healer, most likely a girl, but I'm not sure."
    hanji "You need to find a priest, inspect the houses."
    hide hanji
    with dissolve
    main_char "We began to examine the houses near the entrance to the village, but each one had a roughly similar appearance. Either a body lying on the floor, or a body lying on the bed."
    scene house_inside
    main_char "In one of the last houses, Arisius came up to me and showed me a note on crumpled dirty paper."
    show letter at center
    with dissolve
    letter "I, a priest of the goddess Ayun, the goddess of law, consider what is happening in this village to be unfair."
    letter "People shouldn’t die in such agony, it hurts me to watch how one by one they go to the next world, and I can’t do anything about it."
    letter "If anyone finds this note, then most likely I will already be dead. I was one of three survivors in this village. Today I am going to end their suffering, and after that I am going to go to my goddess."
    letter "When someone finds this note, quickly run away from this village and look for the priests of the goddess Talona, the goddess of diseases and poisons. Although she once served the god of death Baal, only the priests of this goddess can help in this."
    hide letter
    with dissolve
    show arisius at left
    with dissolve
    arisius "Let's go to the second floor."
    hide arisius
    with dissolve
    main_char "We went to the second floor and went into one of the rooms. It has a fun body in a loop."
    stor "We need to tell Hanji about this and get out of here as soon as possible."
    show arisius at left
    with dissolve
    arisius "You have the letter, that's why you tell me, I don't want to be near Hanji when she finds out about this. Good luck."
    hide arisius
    with dissolve
    scene village
    main_char "I left this house and went to Hanji and silently handed her a note."
    show hanji at left
    with dissolve
    main_char "It took Hanji less than a minute to read the note. Her face changed suddenly and she screamed at the top of her lungs."
    hanji "Everyone here. We are leaving. No objections. I'll tell you all the information on the way to the city."
    hide hanji
    with dissolve
    scene road
    main_char "After these words, we very quickly gathered on the main street of the village and moved towards the village."
    main_char "I glanced at Hanji a couple of times and it was clear that this situation had completely thrown her off her emotional balance."
    main_char "I've never seen her so upset. I don't know if it was because the mission went wrong or because of the sacrifices the kingdom suffered."
    main_char "Almost reaching the gate, Hanji stopped and turned to us."
    show hanji at left
    with dissolve
    hanji "No one should know about what happened in this village. If people find out about this, something irresistible could happen."
    hanji "Therefore, I ask you not to tell anyone about this. Try not to raise this topic even among yourself, others may hear it and rumors will spread throughout the kingdom."
    show arisius at right
    with dissolve
    arisius "Of course, Hanji, we understand that. Everyone will keep their mouths shut."
    stor "Yes, we will remain silent about this case, but what should we do about the situation in the village? We can't just leave her like that."
    stor "If the situation with the village is not resolved, then this disease may spread to nearby villages and soon reach the capital."
    hanji "We will tell the archmage and the king about all the information we found. I'm sure they'll sort it out."
    hanji "This is a very important matter for them, especially after the death of the priest. From now on, this mission is no longer our busines"
    hanji "In fact, I don’t want to remember what I saw in the village. I haven't encountered something like this for a long time."
    hanji "In any case, we will be given awards, so after the awards, I propose to meet in my office in the evening."
    hanji "Let us remember the memory of those who died."
    hide arisius
    with dissolve
    show ob at right
    with dissolve
    ob "I agree with Hanji, but we need to hurry to the capital to tell about what happened."
    hide ob
    with dissolve
    hide hanji
    with dissolve
    scene main_square
    main_char "About two hours later we stood in the king’s reception room and talked about what had happened in the village."
    main_char "The king and the archmage were shocked by the events, but after a short time, messengers were poisoned in search of the priests of Talana."
    main_char "And the next morning about twenty priests were sent to the village with a convoy of hundreds of warriors for protection."
    main_char "Also, the next day we were given our mission award and also medals for bravery."
    main_char "Everyone, of course, was glad that they were now recognized adventurers, but at the same time it was clear to us that we did not need this medal after what happened in the village."
    main_char "This evening we gathered in Hanji's office to honor the memory of the victims."
    scene cabinet
    stop music fadeout 1.0
    play music tragedy_strikes volume 0.5 fadein 1 fadeout 1 loop
    show hanji at left
    with dissolve
    hanji "It's finally all together. Sorry for my stinginess in emotions, but that’s how it’s supposed to be. I'm glad everyone survived this mission and returned to the city unharmed."
    main_char "For the first time in the entire time we were in the group, Hanji hugged us."
    hanji "Let's drink to the dead. Let our glasses honor their memory."
    hide hanji
    with dissolve
    main_char "We drank a glass of wine, and then another and another. When it was already late at night, conversations began about our first sorties, and we began to recall the most memorable events from our missions."
    main_char "When morning was approaching, we all began to disperse, almost everyone left. Only Hanji and I were left in the room, collecting mugs and bottles from our get-together."
    show hanji at left
    with dissolve
    hanji "Stor, I'm sorry about that girl. I would have loved to have saved her, but I was scared as hell, so we left her there. Please forgive me."
    main_char "This is the first time I've seen Hanji cry. It was more like a man's stingy surveillance than a woman's tears."
    main_char "Hanji quickly calmed down, wiped away her tears and apologized to me again."
    hanji "Stor, I can handle the rest myself, you can go rest, if there is a new mission, I will notify everyone."
    stor "Hanji, if you need any help outside of missions, then tell me, I’ll try to help."
    hanji "Thanks, Stor, I'll keep that in mind."
    hide hanji
    with dissolve
    scene black
    main_char "After that, I went to the tavern where I had lived for a long time and fell asleep."
    scene tavern
    main_char "I woke up around noon and went downstairs for a drink and a snack."
    show airis2 at left
    with dissolve
    airis "Stor, Ob came by and gave you a letter."
    hide airis2
    with dissolve
    main_char "Iris handed me a letter with purple sealing wax."
    scene black
    show letter at center
    with dissolve
    play sound terror_sfx volume 1
    letter "This morning, the commander of the archmage's special squad, Hanji Zoe, was found hanged in her office. Mushrooms similar to those from the village of Tillanium were found on her body."
    letter "Her body will be burned tonight outside the city walls. The entire special response team must be notified. This information must remain confidential."
    $ ending = "b"
    jump end
    return

label mid_ending:
    $ score -= 1
    mushroom "Then, we have nothing more to say. Maybe I won't cooperate with you anymore."
    mushroom "Now your only choice is to kill me. The priest who is now in my hut will most likely die."
    mushroom "Nothing holds me back in this place or in this life anymore. I'm ready, you can start."
    hide mushroom
    with dissolve
    main_char "The mushroom man knelt down, lowered his arms and stretched out his neck."
    main_char "With a quick movement, he pulled his sword out of its sheath and cut the throat of the mushroom man."
    main_char "His head fell to the ground and at the same time the mushrooms on his body stopped glowing."
    show hanji at left
    with dissolve
    hanji "We need to check the hut. There must be a priest there."
    hide hanji
    with dissolve
    main_char "When we went inside the hut, you saw the priest lying on the only bed in the hut, covered in mushrooms."
    main_char "Hanji and Arisius ran up to the priest and tried to use healing spells and light spells, but nothing helped."
    show hanji at left
    with dissolve
    hanji "Does anyone have an antidote or healing potion?"
    hide hanji
    with dissolve
    jump loop
    return

label mid_ending_2:
    if priest:
        scene road
        stop music fadeout 1.0
        play music mission_success volume 0.5 fadein 1 fadeout 1 loop
        main_char "We reached the capital as quickly as possible, carrying the priest in our arms."
        scene dungeon_room
        main_char "We went down to the basement again, where Hanji showed us the body of one of the doctors. There was nothing in the room where the body had previously lain."
        main_char "We placed the priest on an empty table, after which the archmage arrived and began to perform some kind of ritual over the priest, and we were asked to go home."
        scene main_square
        main_char "The next day we were called to the King's reception hall, where we were presented with our award and medal for bravery."
        main_char "Coming out of the king's reception room, we saw Eri standing nearby."
        show hanji at left
        with dissolve
        hanji "Everyone, come here. You come too."
        main_char "Hanji looked towards Eri."
        hanji "So, the mission can be considered more or less successful, so today everyone is gathering in my office."
        hanji "And you will come with me. See you all."
        hide hanji
        with dissolve
        main_char "Hanji took Eri's hand and they walked away towards the market square."
        scene cabinet
        main_char "In the evening, we all gathered in Hanji’s office to honor the memory of the victims."
        show hanji at left
        with dissolve
        hanji "Let's drink to the dead. Let's honor their memory."
        hide hanji
        with dissolve
        main_char "We sat for a long time talking, but I sometimes noticed how Hanji and Eri looked at each other, which was a mystery to me."
        main_char "When, at the end of the meeting, Hanji told me where she and Eri went after our meeting with the king, everything became clear."
        show hanji at left
        with dissolve
        hanji "I want to tell you one piece of information. Eri and I visited a priest I knew and now Eri will live in the capital and serve in the church."
        stor "Wow, congratulations, Eri. I'm sure you can handle it."
        hide hanji
        with dissolve
        scene black
        main_char "A few days later, the king again called us to his place, where we saw the priest Ayun standing."
        main_char "The king and priest thanked us for the completed mission."
        if panic:
            main_char "After some time, information about the village became known to the people and the king had to leave his post."
        else:
            main_char "After some time, the king made a statement and talked about what happened and how they managed to deal with it."
        $ ending = "mg"
        jump end
    else:
        scene road
        stop music fadeout 1.0
        play music mission_failed volume 0.5 fadein 1 fadeout 1 loop
        main_char "After these words, we very quickly gathered on the main street of the village and moved towards the village."
        main_char "I glanced at Hanji a couple of times and it was clear that this situation had completely thrown her off her emotional balance."
        main_char "I've never seen her so upset. I don't know if it was because the mission went wrong or because of the sacrifices the kingdom suffered."
        main_char "Almost reaching the gate, Hanji stopped and turned to us."
        show hanji at left
        with dissolve
        hanji "No one should know about what happened in this village. If people find out about this, something irresistible could happen."
        hanji "Therefore, I ask you not to tell anyone about this. Try not to raise this topic even among yourself, others may hear it and rumors will spread throughout the kingdom."
        show arisius at right
        with dissolve
        arisius "Of course, Hanji, we understand that. Everyone will keep their mouths shut."
        hide arisius
        with dissolve
        stor "Yes, we will remain silent about this case, but what should we do about the situation in the village? We can't just leave her like that."
        stor "If the situation with the village is not resolved, then this disease may spread to nearby villages and soon reach the capital."
        hanji "We will tell the archmage and the king about all the information we found. I'm sure they'll sort it out."
        hanji "This is a very important matter for them, especially after the death of the priest. From now on, this mission is no longer our busines"
        hanji "In fact, I don’t want to remember what I saw in the village. I haven't encountered something like this for a long time."
        hanji "In any case, we will be given awards, so after the awards, I propose to meet in my office in the evening."
        hanji "Let us remember the memory of those who died."
        hide hanji
        with dissolve
        scene main_square
        main_char "After returning, we were called into the king's reception room, where we were presented with an award for the mission and a medal for courage."
        main_char "Coming out of the king's reception room, we saw Eri standing nearby."
        show hanji at left
        with dissolve
        hanji "Hey you, come here."
        main_char "Hanji looked towards Eri."
        hanji "And you will come with me. See you all."
        hide hanji
        with dissolve
        main_char "Hanji took Eri's hand and they walked away towards the market square."
        scene cabinet
        main_char "In the evening, we all gathered in Hanji’s office to honor the memory of the victims."
        show hanji at left
        with dissolve
        hanji "Let's drink to the dead. Let's honor their memory."
        hide hanji
        with dissolve
        main_char "We sat for a long time talking, but I sometimes noticed how Hanji and Eri looked at each other, which was a mystery to me."
        main_char "When, at the end of the meeting, Hanji told me where she and Eri went after our meeting with the king, everything became clear."
        show hanji at left
        with dissolve
        hanji "I want to tell you one piece of information. Eri and I visited a priest I knew and now Eri will live in the capital and serve in the church."
        stor "Wow, congratulations, Eri. I'm sure you can handle it."
        hide hanji
        with dissolve
        scene black
        if panic:
            main_char "After some time, information about the village became known to the people and the king had to leave his post."
        else:
            main_char "After some time, the king made a statement and talked about what happened and how they managed to deal with it."
        $ ending = "mb"
        jump end
    return

# jump end
label end:
    scene black
    game "Thanks for playing our game. Hope you enjoyed it."
    if ending == "g":
        game "You made it to the good ending. In our game, in addition to this ending, there are 3 more. You can try to complete it all."
        game "Remember that every decision you make can affect the course of history and its ending."
    elif ending == "mg":
        game "You made it to the medium-good ending. In our game, in addition to this ending, there are 3 more. You can try to complete it all."
        game "Remember that every decision you make can affect the course of history and its ending."
    elif ending == "mb":
        game "You made it to the medium-bad ending. In our game, in addition to this ending, there are 3 more. You can try to complete it all."
        game "Remember that every decision you make can affect the course of history and its ending."
    elif ending == "b":
        game "You made it to the bad ending. In our game, in addition to this ending, there are 3 more. You can try to complete it all."
        game "Remember that every decision you make can affect the course of history and its ending."
    return