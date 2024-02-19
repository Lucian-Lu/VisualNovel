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

transform reduced_size:
    zoom 0.25

image red_glow_gif:
    "images/anim/frame_00_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_01_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_02_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_03_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_04_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_05_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_06_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_07_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_08_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_09_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_10_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_11_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_12_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_13_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_14_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_15_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_16_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_17_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_18_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_19_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_20_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_21_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_22_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_23_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_24_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_25_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_26_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_27_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_28_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_29_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_30_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_31_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_32_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_33_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_34_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_35_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_36_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_37_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_38_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_39_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_40_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_41_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_42_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_43_delay-0.07s.gif"
    pause 0.07
    "images/anim/frame_44_delay-0.07s.gif"
    pause 0.07
    repeat



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
    $ ending = "n"
    $ antidote = False
    jump first_act

    return



label first_act:
    scene tavern
    play music tavern_ambience volume 0.5 fadein 1 fadeout 1 loop
    main_char "It was a typical Sunday morning. I had the day off, so I was going to have breakfast and a glass of beer."
    stor "Hey Airis, what's for breakfast today?"
    main_char "A tavern owner named Airis came out from behind the bar. A very hard-working woman; in the 3 months that I have been living in this tavern, I have never seen her sleep or rest. She's constantly at work."
    main_char "Sometimes I’m even scared of her."
    show airis2 at left
    with dissolve
    airis "And you don’t seem to know, Stor, we’ve been having the same dish for breakfast for 2 weeks now."
    stor "Is it the crappy stew again? Maybe you can cook something better for your beloved guest?"
    airis "What makes you think you're my favorite guest? Let's not make things up and order what we have."
    stor "Okay, okay, a plate of stew and a glass of beer."
    main_char "I put 1 silver and 3 copper coins on the bar counter."
    airis "There's more here than needed."
    stor "I know, it's for bothering you with a scoundrel like me."
    hide airis2
    with dissolve
    main_char "I had just sat down at the table to eat beef stew and drink the alluring glass of beer, when a low male voice called out to me."
    main_char "Half of the table was blocked by the shadow of the plate armor of my colleague named Ob."
    main_char "He has a bad character, but you can rely on him. He will never abandon his own people - more than once, thanks to him, we managed to get out of situations that are too scary to remember."
    show ob at left
    with dissolve
    ob "Hey, Stor, you better not start drinking in the morning. We have a new job."
    stor "Seriously? We just returned from a mission the day before yesterday, what the hell happened?"
    ob "Well, better read it yourself."
    main_char "Ob handed me a folded note with purple sealing wax."
    stor "Wait, is it that serious? The last time I saw the king put a seal on orders was 7 years ago, when his daughter disappeared. \n    -I said in a whisper."
    play sound letter_sfx volume 0.8
    main_char "Having torn the seal, I began reading the order, simultaneously eating the stew with my other hand."
    main_char "At first it seemed strange to me that the king himself decided to write out an order over some petty task, but as I read further, I understood more and more as to why he did this."
    main_char "The last line caught me by surprise, making me choke and spit the stew back into my plate."
    stor "Wait, what the hell is this? How could this happen?"
    ob "How do you think I'd know? I was shocked myself. Now that you understand you don’t have time to finish eating, pack your things and let’s go. We can't afford to waste time."
    hide ob
    with dissolve
    show letter
    with dissolve
    letter "Thirty miles north of Falo, in the village of Tillanium, an extraordinary incident occurred. About a month ago, a messenger arrived from this village with information about an infection that had killed all the livestock."
    letter "A group of a priest and three healers was sent there, but after 3 weeks there was no news from them. Tonight one of the healers arrived, his body entirely covered in mushrooms."
    letter "He shared alarming news that the infection in the village was far deadlier than a simple livestock pestilence. He strongly recommended that a detachment of soldiers and several priests be sent there. Shortly after delivering the message, the doctor succumbed to the mysterious illness."
    letter "I, King Frederick XIII, hereby delegate this task to Commander-in-Chief Hanji's detachment. Due date: immediately."
    hide letter
    with dissolve
    scene street
    stop music fadeout 1.0
    play music outside_tavern volume 0.25 fadein 1 fadeout 1 loop
    main_char "After 10 minutes, I was ready. Ob was sitting in the street, waiting for me."
    stor "Alright, I'm ready, let's get going. Have the others been notified yet?"
    show ob at left
    with dissolve
    ob "Yes, I already visited Tia, and she went to get Arisius."
    stor "Great, then, to Hanji?"
    ob "Not right away, we should probably stop by the shop to stock up for the mission."
    ob "Then again, we can't afford to waste time, so it's your call."
    hide ob
    with dissolve
    menu:
        "Go to the shop":
            $ antidote = True
            show ob at left
            with dissolve
            stor "Then let's hurry to the shop. We need to the Commander-in-Chief as soon as possible."
            ob "Yes, we only need to buy a couple of potions, it shouldn't take that long."
            hide ob
            with dissolve
            main_char "It only took 10 minutes to reach the shop, yet the incredible July heat had me feeling squeezed like a lemon."
            scene near_potion
            show ob at left
            with dissolve
            stop music fadeout 1.0
            play music city_centre volume 0.5 fadein 1 fadeout 1 loop
            stor "It's unbelievably hot today; it feels like my brain is melting."
            ob "Yeah, especially in this armor, I feel like I’m in a steam room."
            ob "The shop's right there. Are you coming in or are you going to wait outside?"
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
                    ob "Good morning, I need 3 poison resistance potions. Stor, do you need anything?"
                    main_char "I felt the pocket in which I usually carry gold, but it was empty."
                    stor "Oh.. apparently I left my bag of coins when I was packing. Guess I'm going without potions this time."
                    ob "If you need some potions, then take them. I’ll cover you; you can pay me back later."
                    stor "Thanks, Ob, then I'll take..."
                    menu:
                        "Potion of Healing":
                            $ potion = "Healing"
                        "Potion of Invisibility":
                            $ potion = "Invisibility"
                    stor "Thanks, Ob, then I'll take a Potion of [potion]."
                    ob "Then that's all we'll take, how much will it cost us?"
                    sariel "So, 3 Potions of poison resistance and a Potion of [potion] will cost 125 gold coins"
                    ob "Yeah, a little expensive, but what can you do? We don't really have a choice."
                    main_char "Ob reaches for his pouch, grabs the gold coins, and hands them to saleswoman."
                    ob "Thank you very much, have a nice day."
                    sariel "Thanks for purchase, come again."
                    hide ob
                    with dissolve
                    hide sariel
                    with dissolve
                    scene near_potion
                    stor "Hey, Ob, when did you become so empathic? You paid for me and even thanked the saleswoman."
                    stor "Did something happen to you? Be honest, I'll help."
                    show ob at left
                    with dissolve
                    ob "Very funny... Let's go to Hanji already. Hold your potion."
                "Stay outside.":
                    ob "Okay then, I'll be quick."
                    main_char "Ob went into the store, and I stayed outside."
                    show reivi at left
                    with dissolve
                    reivi "Hey Stor!"
                    main_char "The large figure of the half-orc Reivi appeared in front of me. Despite his appearance, he's an exceptionally talented student at the magic academy in Falo."
                    main_char "Reivi is studying to be a battle mage and is doing extremely well. I was in the same group as him on a couple of combat missions."
                    main_char "Even though it was last year, he had amazing combat and magic abilities. I believe he's only improved further since then."
                    reivi "How are you? Decided to go for a walk on your day off?"
                    stor "Unfortunately not, work related matters."
                    reivi "You're out of luck, it seems. The archmage loads you with work even on Sunday."
                    reivi "What kind of task is it, if not a secret?"
                    menu:
                        "Tell about the task":
                            $ panic = True
                            main_char "It was clear from Reivi's face that he was frightened by this information, but he was intently trying to hide it."
                            reivi "Wow, that sounds terrifying. I hope you can deal with this infection. I believe in you!"
                            show ob at right
                            with dissolve
                            ob "Oh, Reivi, hi! What are you doing here?"
                            reivi "Just taking a walk, nothing interesting. I better go quickly so I don't disturb you. Good luck with your mission!"
                            hide reivi
                            with dissolve
                            hide ob
                            with dissolve
                            show ob at left
                            with dissolve
                            play sound grip_sfx volume 1.0
                            main_char "As soon as Reivi walked about 20 meters from us, I felt a sharp pain in my arm. Ob grabbed my hand with such force that a bear's paw wouldn't come close to."
                            main_char "Even with the visor closed, I could feel the intensity of Ob's gaze; it seemed to burn through me."
                            ob "Stor, do you understand what you're doing? This is a secret mission! Now the whole city will know about it."
                            ob "We're finished when this reaches the king. You do understand that the letters were personally handed to everyone for a reason?"
                            ob "The king wanted to keep this as quiet as possible, but now it might as well be public knowledge. You are a complete idiot."
                            main_char "After muttering those words, Ob let go of my hand and we walked towards Hanji's office. He didn't say another word to me the whole way."
                        "Don't tell about the task":
                            $ panic = False
                            reivi "I understand that your group has secret missions, so I won't insist. In any case, best of luck to you."
                            reivi "When you return, we can go to a tavern to relax and chat over a glass or two of ale."
                            reivi "I'll be heading off now. Take care, and make sure to come back alive!"
                            hide reivi
                            with dissolve
                            main_char "After saying those words, Reivi continued down the street, yet I caught the subtle turn of his head. There was a hint of concern in his eyes regarding the situation."
                            show ob at left
                            with dissolve
                            ob "We're good to go - I've got everything we need."
                            stor "Great, let's go to Hanji's office right away."
                            hide ob
                            with dissolve
        "Don't go to the store":
            show ob at left
            with dissolve
            ob "I agree, we don't have much time. Let's go to Hanji's office quickly."
            hide ob
            with dissolve
    scene corridor
    stop music fadeout 1.0
    play music hanji_office volume 0.5 fadein 1 fadeout 1 loop
    main_char "After 20 minutes of brisk walking, me and Ob arrived outside Hanji's office."
    if panic:
        show ob at left
        with dissolve
        ob "I won’t tell anyone that Reivi knows about the mission, but don’t think that I’m doing this out of kindness."
        ob "I don't want to jeopardize our mission, so we'll pretend that you didn't say anything and that I didn't see or hear anything."
        stor "Thank you for your understanding, Ob."
        hide ob
        with dissolve
    arisius "Ah, good, you are already here."
    show arisius at left
    with dissolve
    stor "And you, as always, creep up silently. We are, after all, in the same detachment; would it kill you to greet us properly?"
    arisius "Well, I'm sorry, but it's not my fault that you are so inattentive."
    main_char "Of course, you can't tell by looking at him, but Arisius was once a completely ordinary person. However, after numerous experiments on his body, he ended up like this."
    main_char "Some parts of his body can extend, and implants have made his arms and legs much stronger. Overall, he has become more powerful, mobile and valuable in missions."
    main_char "Adding to his skill set, he also possesses basic magic skills, making him an indispensable member of our party."
    tia "Apparently everyone forgot about me."
    show tia at right
    with dissolve
    stor "Oh, Tia, you're also here. How are you doing? Long time no see."
    tia "Everything is as usual. I just returned from a trip yesterday."
    main_char "In our team, Tia is responsible for speed and surprise. She dedicated years to mastering the arts of stealth and lethality."
    main_char "Because she's an elf, it's unclear from her appearance as to how old she is, and we never felt the need to ask her. Somehow, it's never been a topic of conversation."
    hide tia
    with dissolve
    show ob at right
    ob "Well, if everyone's ready, let's go in and see Hanji."
    hide ob
    with dissolve
    hide arisius
    with dissolve
    scene cabinet
    show hanji at left
    with dissolve
    hanji "You got here quickly. I thought I would have to wait longer."
    main_char "Although I was in this office just a couple of days ago, every time it feels like the first time."
    main_char "No matter how beautiful it is in here, the feeling is unpleasant. Almost every visit brings information I'd rather not hear or see."
    main_char "It's the same story this time. If it weren't for my duty of service, I would never want to go and find out what happened in that village."
    main_char "Especially given the contents of the letter. I am sure that what I'm about to hear will be even worse than before."
    hanji "Sit down, I’ll tell you the plan of action."
    main_char "Hanji is the most strong-willed woman I've ever met. Every decision she makes, both on missions and outside of them, always proves to be correct."
    main_char "In general, Hanji is our commander. No one ever dares contradict her, because they're certain that she knows what's better."
    main_char "I've always admired Hanji. I could never give imagine dedicating myself entirely to faith in God."
    hanji "Basically, the mission is to find out what happened in the village of Tillanium and, if possible, solve the problem."
    hanji "Also, one of the key points is saving a group of healers and a priest. The priest who was sent to the village is a high-ranking member of the church of the goddess Ayun."
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
    tia "What could be more important? I spend my time, energy, and not to mention - arrows - which, by the way, are not that cheap."
    hanji "Tia, be quiet. They'll pay you enough to stock up on arrows for years. As I have already mentioned, this is a very important task for the king."
    hanji "In addition, if the mission is successful and we manage to save the priest, we will be appointed honored officers of the order."
    hanji "With this medal, you will be able to receive arrows for free in any quantity, so don’t worry about it."
    tia "Then I have no more questions."
    hide tia
    with dissolve
    show arisius at right
    with dissolve
    arisius "Any guesses as to what happened in the village?"
    arisius "To me, it doesn't seem like a simple disease, if a high-ranking priest could not deal with it."
    hanji "Yes, you're right. I took a sample of mushrooms from the body of one of the doctors who reached the capital."
    hanji "They look extremely strange. Also, I found remnants of magical effects on the mushrooms."
    hanji "Either the priest tried to cure the doctor of these mushrooms, but failed, or the mushrooms were created with magic."
    hide arisius
    with dissolve
    show ob at right
    with dissolve
    ob "The situation is, of course, not ideal. It seems like we'll require magical support."
    ob "Hanji, Arisius, we're counting on you."
    hanji "Yes, of course."
    main_char "Arisius nods."
    hanji "If there are no more questions, then we can proceed with our mission."
    hanji "Give me a few minutes to get ready. You can wait outside for now."
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
    ob "I have a really bad feeling about this task. Something just doesn't sit right with me."
    show arisius at right
    with dissolve
    arisius "I agree. In my head, I understand that it's another typical task for us, but everything inside me is screaming that there's something off about this."
    show tia at center
    with dissolve
    tia "Don't let it get to you. Arisius, you said it yourself that this is like our usual missions, which means everything will be fine."
    tia "Yes, I was also a little wary because the king himself sent us letters, but it turned out to be because of the priest, so everything is in order."
    main_char "Although Tia’s words were logical and she intended to calm us down, there was an unmistakable nervousness in her demeanor as well."
    hide ob
    with dissolve
    hide tia
    with dissolve
    hide arisius
    with dissolve
    menu:
        "Say it's going to be okay":
            stor "I agree with Tia, everything will go well. The key is to stay alert and not let our guard down."
            stor "We have already completed similar tasks so many times that this is going to feel like a breeze."
        "Say you're nervous too":
            stor "I also have a strange feeling. It feels like when we went out on our first mission."
            stor "It's probably because we've never encountered this before. Hanji is with us this time though, so we will follow her lead and everything will be fine."
            stor "Maybe..."
    show ob at left
    with dissolve
    ob "Hey, I didn’t talk about my experience to make everyone feel uneasy."
    ob "There is nothing scary about this task. We'll just do our job and that's it."
    ob "Let's put aside our nerves and concentrate on the mission."
    show hanji at right
    with dissolve
    hanji "I'm ready. What were you talking about?"
    hide ob
    with dissolve
    show arisius at left
    with dissolve
    arisius "Nothing important, Hanji. Can we move out now?"
    hanji "If everyone is ready, then yes."
    hide hanji
    with dissolve
    hide arisius
    with dissolve
    main_char "On the way to the city gates, no one said a word."
    main_char "Apparently, everyone understood that this mission was not as simple as it seemed to be."
    scene gates
    main_char "Having reached the gate, Hanji approached one of the guards and whispered something in his ear."
    show hanji
    with dissolve
    hanji "Guys, follow me here."
    stor "Hanji, shouldn't we go outside the city gates and head to the village?"
    hanji "It's only going to take 10 minutes, then we’ll head for the village; come in."
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
    main_char "Hanji pulled out a set of keys from her pocket and opened the door. From behind the door, a bittersweet smell made its way throughout the corridor."
    main_char "The smell was so strong that I had to hold my nose to prevent vomiting."
    main_char "Hanji walked inside and called for us to follow her."
    scene dungeon_room
    main_char "We entered a small room with a jelly table in the center, on which lay the body of a man whose stomach and chest were cut open."
    show hanji at left
    with dissolve
    hanji "This is the doctor who reached the capital. After his death, we decided to dissect him in order to better understand what exactly happened to him."
    hanji "All of his internal organs are covered with mushrooms, but these mushrooms have one peculiarity."
    hanji "They seem to be afraid of sunlight - or light, in general, so they only grow under the victim's clothing or areas devoid of light."
    hanji "One of those places is the victim's internal organs, which is why he died."
    hanji "I believe you all understand what will need to be done."
    show arisius at right
    with dissolve
    arisius "You'll have to use light spells if come into contact with mushrooms..."
    hanji "Precisely."
    hanji "That's all I wanted to show you, now we can head for the village."
    hide arisius
    with dissolve
    hide hanji
    with dissolve
    scene gates
    main_char "After that, we left the basement and headed towards the village."
    main_char "After what Hanji showed us, it only made me more nervous. I could not remember having seen any similar disease."
    main_char "Apparently, our fears about this not being an easy task turned out to be true."
    #end of act 1
    jump second_act
    return



label second_act:
    scene road
    stop music fadeout 1.0
    play music journey_start volume 0.5 fadein 1 fadeout 1 loop
    main_char "The path to the village lay north through large fields of almost ripened wheat and through a small forest."
    main_char "Although this was not the longest outing for our team, the road was still quite long."
    main_char "We kept walking the whole day, making our way to the village step by step..."
    scene forest
    stop music fadeout 1.0
    play music dark_woods volume 0.5 fadein 1 fadeout 1 loop
    show red_glow_gif at reduced_size: 
        xalign 0.4
        yalign 0.5
    main_char "When it was late at night, we were only about a mile from the village."
    show arisius at left
    with dissolve
    arisius "Hey, there's something on the edge of the road."
    hide arisius
    with dissolve
    main_char "I looked closer to where Arisius was pointing."
    main_char "At the edge of the road, something glowing reddish could be seen."
    show hanji at left
    with dissolve
    hanji "Let's move closer to get a better look."
    hide hanji
    main_char "All of us are trying to be quieter than usual, perhaps this is due to the mushrooms from the village..."
    with dissolve
    hide red_glow_gif
    main_char "We came to a distance of about 15 feet and our guesses were unfortunately confirmed."
    main_char "On the edge of the road lay the body of a person covered with red glowing mushrooms."
    show hanji at left
    with dissolve
    hanji "Let's quickly examine the body. Apparently the fungal disease can spread beyond the village."
    hide hanji
    with dissolve
    main_char "Coming closer to the body, it became clear that this was the body of a young girl."
    stor "Hey Hanji, this is a girl, about 17 years old."
    main_char "After these words, the girl let out a loud sob and coughed. She involuntarily tried to cover her mouth with her hands and something similar to blood dripped onto her palms."
    main_char "But there was one difference. The blood gave off a slight reddish glow."
    stor "Hanji, she's alive! What should we do?"
    show hanji at left
    with dissolve
    hanji "We don't have time for this, let's move on. Leave her here, and if she's alive on the way back, we'll take her with us to the capital."
    stor "Hanji, how could you say that? She's barely breathing. She'll probably die before then... We don't even know how long the mission will last..."
    hanji "Stor, do you dare question my command? If I hear one more objection, you will lie down next to the girl."
    hanji "Let's say that you went missing and we couldn't find you. No one will even bothing looking for you. All clear?"
    hanji "Now we have to go, we have our mission in the village."
    stor "Yes, Commander Hanji."
    hide hanji
    with dissolve
    main_char "It hurt to leave this girl here. Most likely, we were her last chance to survive, but now she is doomed."
    main_char "Hanji and everyone else started moving towards the village. I tried to get up and follow them, but then the girl grabbed my leg."
    unknown "Hey dad, is that you?"
    stor "Hanji..."
    menu:
        "Say that the girl is conscious":
            stor "Hanji, this girl is conscious."
            show hanji at left
            with dissolve
            hanji "So what? We will not take her with us, much less waste our medicine or magic on her."
            stor "Hanji, we can't just leave her like that. She's still alive and conscious; we can't abandon her here!"
            hanji "In that case, you'll have to carry her yourself. If you can’t handle it, then none of us will help you; even if mushrooms start appearing on you."
            hide hanji
            with dissolve
            menu:
                "Save the girl":
                    stor "I understand. If I can't handle this, then don't save me. I know what I'm doing."
                    show hanji at left
                    with dissolve
                    hanji "I get what you're doing. But don't forget we're on an important mission. I hope you still have a good head on your shoulders."
                    hide hanji
                    with dissolve
                    $ girl = True
                "Leave the girl here":
                    stor "Okay Hanji, I understand. Sorry for interrupting."
                    show hanji at left
                    with dissolve
                    hanji "You should have done this right away without contradicting me. We're heading to the village."
                    hide hanji
                    with dissolve
                    menu:
                        "Finish off the girl":
                            main_char "I pulled the dagger out of its sheath, plunged it into the girl’s neck and ran it along her throat."
                            main_char "The girl made a soft popping sound and her hand went limp."
                            main_char "After that, I threw back the limp hand lying on my leg and followed my team."
                            $ girl_alive = False
                        "Leave her on the road":
                            main_char "I gently removed her hand from my leg and then went after the team."
        "Tell them to wait for you":
            show hanji at left
            with dissolve
            hanji "What is it?"
            stor "Nothing, wait for me."
            hide hanji
            with dissolve
    if girl:
        main_char "Although the girl was very thin, carrying the girl along with the weight of my armor and weapons proved to be more challenging than expected."
        main_char "I was walking at the back of the group when I noticed that Ob was also lagging behind the others."
        show ob at left
        with dissolve
        ob "You understand how this could turn out, right?"
        stor "Yes, I understand that if something happens, it will be my responsibility and I will handle it."
        ob "That goes without saying. I’m talking about something a little different - your action could jeopardize not just the mission, but all of us..."
        ob "You're the first person in 10 years to go against Hanji's commands. She won't take it lightly, trust me."
        ob "Her words about you going missing without anyone looking for you might hold true.  Be careful."
        stor "Thanks for the warning. Hurry to Hanji so she doesn't suspect anything."
        hide ob
        with dissolve
    main_char "When we neared the village, a reddish glow could be seen from behind the trees."
    show hanji at left
    with dissolve
    hanji "So, we'll set up camp now, rest, and sleep to regain our strength. In the morning we’ll go to the village to investigate what happened."
    hanji "Any objections?"
    if girl:
        main_char "I noticed how Hanji threw a sharp glance in my direction when she said that."
    show ob at right
    with dissolve
    ob "No Hanji, there are no objections."
    hide hanji
    with dissolve
    hide ob
    with dissolve
    scene camp
    stop music fadeout 1.0
    play music campfire_stories volume 0.5 fadein 1 fadeout 1 loop
    main_char "Me, Ob and Arisius began to set up the camp, while Hanji and Tia started the fire."
    main_char "In about half an hour the camp was ready."
    if girl:
        main_char "While we were setting up the tents, I noticed Hanji approaching the girl lying on the ground, and pouring something from a glass flask into her mouth."
    show hanji at left
    with dissolve
    hanji "The patrol will consist of four people: Ob will be the first one, followed by Arisius, then myself, and finally, Stor."
    hanji "Everyone, except Ob, go to bed immediately and rest up for tomorrow."
    if girl:
        main_char "Hanji went and leaned toward me."
        hanji "I administered a poison resistance potion to the girl. She should wake up in about 8 hours, around the time your watch starts."
        hanji "Try to find out as much information as possible about the village."
        play sound grip_sfx volume 1.0
        main_char "Hanji’s hand landed on my shoulder, and simultaneously, I felt a sharp pain near my collarbone. Her grip was so strong that I could feel her fingers moving through the leather armor."
        hanji "If you disobey my order again, your family will never see you again. The only news they'll receive is a letter from the king about how bravely you fought. All clear?"
    stor "Yes, Commander Hanji, everything is clear."
    hide hanji
    with dissolve
    if girl:
        main_char "While I was glad that Hanji assisted the girl, the realization that she could easily sacrifice me was a frightening thought."
        main_char "After that, everyone, except Ob, went into their tent and tried to get some sleep."
    else:
        main_char "I was tormented by thoughts of what might have happened if I had saved that girl. However, the thought of not returning from this mission due to not following Hanji's orders haunted me even more."
    scene black
    main_char "Sleep, of course, was elusive, but after about half an hour, I finally managed to drift off."
    if girl:
        play sound kick_sfx volume 0.8
        main_char "I felt something hit my stomach with force."
        hanji "Hey, good-natured fool, wake up. It's your turn to go out on patrol."
        show hanji at left
        with dissolve
        scene camp
        hanji "It looks like your new friend woke up over there. Go and say hello for the sake of decency."
        stor "Yes, Commander Hanji. I'm starting patrol."
        hide hanji
        with dissolve
    else:
        scene camp
        show hanji at left
        with dissolve
        hanji "Hey Stor, wake up. Time for your watch."
        stor "Okay, give me 2 minutes and I will start patrolling."
        hide hanji
        with dissolve
    if girl:
        main_char "I left the tent and saw the girl sitting near the fire, warming her hands to it."
        main_char "When she saw me getting out of the tent, she waved her hand and smiled sweetly at me."
        show eri at left
        with dissolve
        stor "Hello. What is your name?"
        eri "My name is Eri, what's yours?"
        stor "Stor. What were you doing on that road?"
        eri "To be honest, I don’t remember how I ended up like this. But that scary woman who was here before you mentioned that you found me on some road about a mile from here."
        eri "I don’t remember how I got there or what happened. She also said that you were the one who decided to save me. While it wasn't very nice of her to say she was against my rescue, I understand her."
        stor "Well, yes. That's pretty much how it was. Do you not remember anything about what happened to you?"
        eri "Actually, I remember a little about what happened, but I was scared to tell that woman about it."
        eri "But you saved me, so I feel like I can trust and tell you."
        eri "About a month ago, a strange man came to our village. His hat looked like a mushroom's cap, but no one thought anything of it."
        eri "He asked to stay for a couple of days to recuperate from a long journey and said that he would leave the village afterward. One old woman took him in."
        eri "He actually stayed for a few days and left. The old lady didn’t have anything missing from her house; nothing happened to her, but after a couple of days, strange events began..."
        eri "The old woman passed away in her bed, and those who saw her body noticed a red glow emanating from her body."
        eri "A few days later, the whole village succumbed to this infection. We sent a messenger to the capital, and in response, they sent us a priest and doctors. Unfortunately, they were unable to cope with this disease and also became infected."
        eri "Everyone except the priest was infected. He spent a long time trying to cure us and the doctors, giving us holy water and using all kinds of spells. Nothing helped."
        eri "About three days ago, this man returned, after which this all began. What we initially thought to be a mushroom-shaped hat turned out to be an actual mushroom. The same mushrooms that appeared on the villagers were also coming out of his body."
        eri "The priest attempted to negotiate with him in order to save the villagers, but the Mushroom Man did not listen to him and took the priest to his hut."
        eri "After this, the priest was not seen again. Nearly all of the villagers died when I decided to run away for help. I fear there may be no one alive anymore..."
        eri "The priest and all the residents believed that the problem came from that man. It's likely that defeating him or persuading him to remove the infection will make the disease will go away."
        stor "We'll definitely look into this. You can count on us. My allies and I are a team that will not abandon such matters without finding a solution."
        eri "Okay, I believe in you."
        main_char "The next 2 hours of my patrol were spent talking with Eri. She turned out to be an extremely sweet girl, though burdened with a sad fate."
        main_char "Her family and friends succumbed to the infection, leaving her as the sole survivor. She managed to escape and crawled toward the city for three days until she collapsed from exhaustion."
        stor "Forgive me Eri, but I will have to share the information about the village and the mushroom man to my teammates. It's necessary so that we can better deal with this situation."
        eri "It's okay, I understand. If you say that it's necessary, then I believe you."
        hide eri
        with dissolve
        main_char "As the sun had fully risen in the sky, everyone woke up, and I told them about Eri's story and the events that happened in the village."
        scene sunrise_forest
        stop music fadeout 1.0
        play music major_decision volume 0.5 fadein 1 fadeout 1 loop
        main_char "We packed up the camp and began to decide how to handle this situation."
        show hanji at left
        with dissolve
        hanji "So, we can either go to that hut and kill this 'mushroom man', but then the fungal infection will not leave the village and we will not be able to save the priest."
        hanji "Alternatively, we could negotiate with him to eliminate the infection and release the priest. One problem remains, however. I have no idea what we can offer him in return."
        hanji "Anyone have any ideas?"
        show eri at right
        with dissolve
        eri "I'm not entirely certain, but he probably can be convinced. The second time he visited, when the village was already overrun by mushrooms, he seemed.. disappointed."
        eri "Perhaps he doesn't like what's happening, or it might be out of his control. I think we should talk first and find out what he needs."
        hanji "I didn’t ask your opinion, girl, but you make a fair point. Maybe saving you was worth it after all. Anyone else have any other suggestions?"
        stor "I don't think so, we lack information. We should first see for ourselves what is happening in the village and examine the mushroom man's hut."
        hanji "Yes, I agree. Let's proceed accordingly. If the girl's assumption turns out to be true, we can engage in conversation and attempt to persuade this person."
        hanji "So, we're heading to the village now."
        main_char "Hanji looked towards the girl."
        hanji "Can you walk on your own?"
        eri "Yes, I feel better now."
        hanji "Then you'll be walking behind us. Try not to become a burden. Avoid any collisions with the enemy. It’s better to be silent so as not to draw their attention."
        hide hanji
        with dissolve
        hide eri
        with dissolve
    else:
        main_char "Hanji went to bed, and I left the tent and looked around."
        main_char "It was quite chilly outside, but thanks to the fire it was bearable. As expected, the patrol went on without any problems until dawn."
        main_char "I suddenly felt hungry, so I took out a packed lunch from my bag and decided to warm it up on the nearly burnt-out fire."
        tia "Decided to have breakfast alone?"
        show tia at left
        with dissolve
        stor "You know, it’s boring on patrol, so I had to occupy my time with something."
        tia "Why are you always so serious? You and Ob are very much alike in this regard. I was joking."
        main_char "Tia also took out a packed lunch from her bag and handed it to me."
        tia "Warm it up, please. I'll go and warm up for now."
        hide tia
        with dissolve
        main_char "I started heating up the packed lunch on the fire while Tia went a little further into the forest to warm up for the task ahead."
        stor "Tia, your packed lunch is ready. You can come eat."
        ob "I see that you're our cook today. Will you warm me up a packed lunch too?"
        show ob at left
        with dissolve
        stor "Go to hell. Warm up your packed lunch yourself."
        ob "Don't get so excited."
        hide ob
        with dissolve
        main_char "Me, Tia and Ob sat around the burnt fire to have breakfast, and shortly after, Arisius and Hanji woke up."
        show hanji at left
        with dissolve
        stop music fadeout 1.0
        play music major_decision volume 0.5 fadein 1 fadeout 1 loop
        hanji "Now, our priority is to investigate the situation in the village. Be vigilant and exercise caution."
        hanji "If you spot a possible threat or enemy, immediately inform others and maintain the usual grouping."
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
        main_char "As we arrived at the village, it became evident that Eri’s words turned out to be true. There was no sign of survivors."
        main_char "We thoroughly searched all the houses, but found no trace of the priest. Only the doctors' lifeless bodies were discovered."
        main_char "As we made our way further into the village, Eri broke the silence."
        show eri at left
        with dissolve
        eri "That man's hut is there."
        main_char "Eri pointed east, where a trail of reddish mushrooms could be seen."
        show hanji at right
        with dissolve
        hanji "So that's where we need to go... Everyone be on alert, this individual may be hiding, ready to ambush us."
        hide eri
        with dissolve
        hide hanji
        with dissolve
        scene mushroom_hut
        stop music fadeout 1.0
        play music enemy_encounter volume 0.5 fadein 1 fadeout 1 loop
        main_char "We walked about 500 feet east and came across a small wooden hut, overgrown with mushrooms."
        main_char "While inspecting the surroundings of the hut, a tall man came out, his body covered in red glowing mushrooms. His appearance matched the description provided by Eri; this was undoubtably the Mushroom Man."
        show mushroom at center
        with dissolve
        mushroom "Adventurers, I understand that you are wary of me because you don’t know what I am, but let us talk. Perhaps we can reach some kind of compromise."
        menu:
            "Yes, we should talk {i}neutral{/i}":
                mushroom "So we can talk calmly then. What is it you want to know?"
            "Let's start with who you are {i}information{/i}":
                mushroom "If you want to know who I am, then I will tell you."
                mushroom "I would like to introduce myself, but in your understanding of the word, I don't have a name. If I contact my relatives, however, they'd understand who I am."
                mushroom "But to things easier, my name is Mash. I am Vegepygmy, an intelligent mushroom. Once upon a time there were many of us in this world, but due to certain events, our numbers dwindled, and the survivors had to go into hiding."
                mushroom "Basically, we used to live underground. However, due to increasing dangers and lack of food, we started venturing to the surface."
                mushroom "But.. I am not a 'real' Vegipygmie; I grew up in the body of a fallen magician. Since then, I wandered in these forests, feeding on carrion until I stumbled upon this village."
        mushroom "Now I'm ready to answer your questions."
        menu:
            "Did you willingly spread the disease to this village? {i}neutral{/i}":
                mushroom "I didn't intend for this to happen, but I have no control over where I leave my spores."
                mushroom "I don't want this to happen to anyone else. So I would like you to help me."
                menu:
                    "How can we help you? {i}information{/i}":
                        mushroom "I need to find a way into the underground, however, there is one issue with this."
                        mushroom "Due to the structure of my body, many predators can detect me from a long distance."
                        mushroom "Therefore, I require your help to reach the entrance to the underground."
                        hide mushroom
                        with dissolve
                        jump good_ending
                    "We won't help you. {i}insolence{/i}":
                        jump mid_ending
            "You will be held accountable for what you did to the village! {i}insolence{/i}":
                mushroom "I understand, however I had no control over anything that happened here."
                mushroom "Unfortunately, it seems like we won't be able to have an adequate conversation."
                jump mid_ending
    else:
        jump bad_ending
    return


label loop:
    if antidote and potion == "Healing":
        menu:
            "No, no one has an antidote or healing potion.":
                main_char "No one had an antidote or a healing potion."
                main_char "Following unsuccessful attempts to cure the priest, he breathed his last and passed away."
                show hanji at left
                with dissolve
                hanji "Damn it! He died..."
                main_char "Hanji turned to us."
                main_char "There was visible frustration on Hanji's face. It was the first time in many years that she failed to complete one of her missions."
                hanji "The mission has ended in failure, we need to return to the city as quickly as possible. We need to send a dispatch to the village to prevent the disease from spreading further."
                hide hanji
                with dissolve
                $ priest = False
                jump mid_ending_2
            "Take the healing potion out of your pocket.":
                if potion == "Healing":
                    main_char "I took the healing potion out of my pocket and handed it to Hanji."
                    main_char "Hanji gave the priest the potion and his face cleared up a little. After this, Ob took out a bottle of antidote from his bag."
                    main_char "Ob handed the bottle of poison resistance to Hanji, who gave it to the priest to drink."
                    show hanji at left
                    with dissolve
                    hanji "This should stabilize his condition. The priest should be able to reach the capital now, where the mages can help him. Let's start moving."
                    hide hanji
                    with dissolve
                    $ priest = True
                    jump mid_ending_2
            "Ask Ob for an antidote.":
                if antidote:
                    main_char "Ob took out a bottle of poison resistance from his bag."
                    main_char "Hanji poured the flask into the priest's mouth, after which the priest's breathing became more even."
                    show hanji at left
                    with dissolve
                    hanji "He will be unconscious for a long time, but this will hopefully allow him to live until we reach the capital. Let's hurry up."
                    hide hanji
                    with dissolve
                    $ priest = True
                    jump mid_ending_2
    elif antidote:
        menu:
            "No, no one has an antidote or healing potion.":
                main_char "No one had an antidote or a healing potion."
                main_char "Following unsuccessful attempts to cure the priest, he breathed his last and passed away."
                show hanji at left
                with dissolve
                hanji "Damn it! He died..."
                main_char "Hanji turned to us."
                main_char "There was visible frustration on Hanji's face. It was the first time in many years that she failed to complete one of her missions."
                hanji "The mission has ended in failure, we need to return to the city as quickly as possible. We need to send a dispatch to the village to prevent the disease from spreading further."
                hide hanji
                with dissolve
                $ priest = False
                jump mid_ending_2
            "Ask Ob for an antidote.":
                if antidote:
                    main_char "Ob took out a bottle of poison resistance from his bag."
                    main_char "Hanji poured the flask into the priest's mouth, after which the priest's breathing became more even."
                    show hanji at left
                    with dissolve
                    hanji "He will be unconscious for a long time, but this will allow him to live until the capital. Let's hurry up."
                    hide hanji
                    with dissolve
                    $ priest = True
                    jump mid_ending_2
    else:
        menu:
            "No, no one has an antidote or healing potion.":
                main_char "No one had an antidote or a healing potion."
                main_char "Following unsuccessful attempts to cure the priest, he breathed his last and passed away."
                show hanji at left
                with dissolve
                hanji "Damn it! He died..."
                main_char "Hanji turned to us."
                main_char "There was visible frustration on Hanji's face. It was the first time in many years that she failed to complete one of her missions."
                hanji "The mission has ended in failure, we need to return to the city as quickly as possible. We need to send a dispatch to the village to prevent the disease from spreading further."
                hide hanji
                with dissolve
                $ priest = False
                jump mid_ending_2
            "Ask your team.":
                show ob at left
                with dissolve
                ob "Sorry, nothing here."
                hide ob
                with dissolve
                show arisius at right
                with dissolve
                arisius "My pockets are empty."
                hide arisius
                with dissolve
                show tia at center
                with dissolve
                tia "You know I don't carry potions.."
                hide tia
                with dissolve
                stor "Damn it.. There's not much we can do, then.."
                jump loop
    return

label good_ending:
    show hanji at left
    with dissolve
    hanji "Hmm, I know about a rift. I think it could serve as a suitable passage to the underground."
    show mushroom at right
    with dissolve
    mushroom "Where is it?"
    hanji "Approximately ten miles from here, at the base of the Dragon Ridge."
    mushroom "Seems like that's our destination, then."
    hanji "Can you cure the village and the priest of the mushroom disease?"
    mushroom "I can save the priest, but I unfortunately cannot remove undo the effects the disease had on the village. However, if I go far enough from here, then after a while all the mushrooms should begin disappearing."
    hanji "Unfortunate... Alright then, let's get to healing the priest."
    mushroom "Come with me."
    hide hanji
    with dissolve
    hide mushroom
    with dissolve
    main_char "The mushroom man and we went into the hut. The priest was lying on the only bed in the hut, his body covered in red glowing mushrooms."
    main_char "The mushroom man approached the bed, placing his hand on the section of the priest's hand covered by mushrooms, and began pronouncing some strange words."
    main_char "The mushrooms began to glow much stronger, just like the mushroom man himself. After a few minutes, the mushrooms on the priest's body dimished in size, while the mushrooms on the man's body expanded and grew larger."
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
    main_char "The path to the rift lay through a dense forest, making the journey quite difficult. By noon, we arrived at our destination."
    main_char "Approaching the edge of the cliff, the mushroom man, without saying a word, looked back at us, nodded, and jumped down."
    stor "Looks like we did it. The disease should stop now. What a strange encounter that was.."
    show ob at right
    with dissolve
    ob "I get the feeling it could've gone down much worse. We did a good job."
    show arisius at left
    with dissolve
    arisius "It's unfortunate that the villagers didn't make it. Wish we knew about the situation sooner."
    stor "On the bright side, Eri survived. She can carry on the legacy of the village, and even rebuild it eventually."
    show hanji at left
    with dissolve
    hanji "Well, we managed to complete our mission."
    hanji "My guess is that the priest will wake up in about 4 hours, so we should hurry back. We must get there before he wakes up."
    hide ob
    with dissolve
    hide arisius
    with dissolve
    hide hanji
    with dissolve
    scene mushroom_hut
    main_char "A little before sunset we reached the hut and went inside."
    main_char "Less than half an hour later the priest woke up. The mushrooms on his body had almost completely disappeared; some, however, were still visible under his clothes."
    main_char "We explained to the priest what happened and he came back with us to the capital."
    scene main_square
    main_char "The next morning, we arived in the capital, where we parted ways with the priest."
    main_char "That same evening, the king summoned us to his chambers and personally, as promised, bestowed upon us our reward"
    scene hall
    main_char "In honor of the priest's rescue, as well as the elimination of the disease, the king decided to throw a grand feast, extending an invitation to us as honorary guests."
    main_char "During the same feast, we were formally presented with medals for bravery and bestowed the honorary title of adventurers."
    main_char "We also got a massive heap of gold."
    show hanji at left
    with dissolve
    hanji "Stor, what are you going to do with so much money?"
    stor "I just wanted to talk to you about this. I feel like retiring from being an adventurer. At least for the foreseeable future. I need some rest."
    stor "I plan to visit my family; it's been a while since I last saw them. The frequent assignments made it quite difficult to do so."
    stor "I want to renovate the house with my dad; and I think they will be happy to see me again."
    hanji "Stor, your parents will be glad just to see you in good health."
    hanji "I probably won’t be a squad leader anymore either. I'm considering going on a pilgrimage or embarking on a trip to the mountains and monasteries."
    hanji "You know, you contradicting me and saving Eri taught me a great deal about the person I truly aspire to be. Perhaps my own arrogance that could've led our mission toward utter disaster. Thanks for being there, Stor."
    stor "No problem, Hanji. Glad I could help. I have to admit though, contradicting you felt scary as hell!"
    main_char "We spent some time idly chatting about our mission and our futures."
    hide hanji
    with dissolve
    show ob at right
    with dissolve
    ob "Well, my good friend, it seems like this is going to be our last encounter for quite a while. I must say, I'm going to miss your sense of humor."
    stor "Like, dear friend. For the time being, let's enjoy the spoils of a job well done."
    hide ob
    with dissolve
    scene black
    main_char "The whole feast was spent talking about our team and reminiscing about old times. The unanimous decision was to disband our team for an indefinite period..."
    $ ending = "g"
    jump end
    return


label bad_ending:
    scene village
    stop music fadeout 1.0
    play music mission_disaster volume 0.5 fadein 1 fadeout 1 loop
    main_char "When we entered the village, there wasn't a single soul in sight. Only when we started peering into the windows did we understand the reason for the residents' absence from the streets."
    main_char "We could only locate their lifeless bodies, all of them covered in red glowing mushrooms."
    main_char "Some of them were entirely engulfed, making it unclear as to whether it was a person lying down or simply mushrooms sprouting from the ground."
    show hanji at left
    with dissolve
    hanji "It seems that there are no survivors. A terrible incident. Has anyone seen the priest?"
    stor "No, I only found one of the healers. Maybe..."
    main_char "I stood over the body clad in white clothes, resembling those of doctors, but I was uncertain whether it was one of them. All clothes were stained with dirt and a mixture of blood and mushroom juice."
    main_char "Hanji came up to me and examined the body."
    hanji "Yes, it's a healer, most likely a girl, but I can't be certain."
    hanji "We need to find the priest, check all the houses."
    hide hanji
    with dissolve
    main_char "We began to examine the houses near the entrance to the village, but each one presented a similar grim scene. Either a body lying on the floor, or a body lying on the bed."
    scene house_inside
    main_char "In one of the last houses, Arisius came up to me and showed me a note written on crumpled, dirty paper."
    show letter at center
    with dissolve
    letter "I, a priest of the goddess Ayun, the goddess of law, deem the events unfolding in this village to be unfair."
    letter "It pains me to witness people succumbing to such agony, departing to the next world one by one, all while feeling powerless."
    letter "If anyone finds this note, chances are I am most likely already dead. I am of three survivors in this village. Today, I plan to end their suffering, and thereafter, I will go meet my goddess."
    letter "When someone finds this note, quickly run away from this village and seek out priests of the goddess Talona, the deity of diseases and poisons. Although she once served the god of death Baal, only the priests of Talona can help in matter."
    hide letter
    with dissolve
    show arisius at left
    with dissolve
    arisius "Let's go to the second floor."
    hide arisius
    with dissolve
    main_char "We went to the second floor and went into one of the rooms. In there, we found a lifeless body, hanging from the ceiling..."
    stor "We need to tell Hanji about this and get out of here as soon as possible."
    show arisius at left
    with dissolve
    arisius "You found the letter, so you talk to Hanji about this. I don't want to be anywhere near Hanji when she hears about this. Good luck."
    hide arisius
    with dissolve
    scene village
    main_char "I left this house and went to Hanji, silently handed her the note."
    show hanji at left
    with dissolve
    main_char "It took Hanji less than a minute to read the note. Her face changed suddenly and she screamed at the top of her lungs."
    hanji "Everyone here. We are leaving. No objections. I'll tell you all the information on the way to the city."
    hide hanji
    with dissolve
    scene road
    main_char "Following these instructions, we swiftly assembled on the village's main street and proceeded towards the capital."
    main_char "I glanced at Hanji a couple of times and it was clear that this situation had completely thrown her off her emotional balance."
    main_char "I've never seen her so upset. I don't know if it was because the mission went wrong or because of the losses the kingdom suffered."
    main_char "Approaching the gate, Hanji came to a halt and turned toward us."
    show hanji at left
    with dissolve
    hanji "No one should know about what happened in this village. If word spreads, uncontrollable consequences could unfold."
    hanji "Therefore, I ask you not to tell anyone about this. Try not to raise this topic even among yourselves, as others may hear it and spread rumors throughout the kingdom."
    show arisius at right
    with dissolve
    arisius "Of course, Hanji, we understand. Everyone will keep their mouths shut."
    stor "Yes, our lips will be sealed about this case. But what should we do about the situation in the village? We can't just leave it like that."
    stor "If the situation with the village is not resolved, then this disease may spread to neighboring villages, eventually reaching the capital."
    hanji "We'll convey all the information we've gathered to the archmage and the king. I'm sure they call sort it all out."
    hanji "This is a very important matter to them, especially given the priest's death. Henceforth, this mission is no longer our concern."
    hanji "In fact, I don’t want to remember what I saw in the village. I haven't seen something like this in a very long time."
    hanji "Regardless, we will medals. After the ceremony, I suggest meeting in my office in the evening."
    hanji "Let us honor the memory of those who died."
    hide arisius
    with dissolve
    show ob at right
    with dissolve
    ob "I agree with Hanji, but we need to hurry to the king to tell him about what happened in the village."
    hide ob
    with dissolve
    hide hanji
    with dissolve
    scene main_square
    main_char "About two hours later, we stood in the king’s reception room, discussing the events that transpired in the village."
    main_char "The king and the archmage were visibly shocked by the events. Shortly thereafter, messengers were dispatched in search of the priests of Talana."
    main_char "The following morning, approximately twenty priests, accompanied by a convoy of hundreds of warriors for protection, were dispatched to the village."
    main_char "Also, we were given our mission award and awarded medals for bravery."
    main_char "Everyone, naturally, felt a sense of pride in being acknowledged as adventurers. At the same time, however, it was clear that we did not want this medal after what had happened in the village."
    main_char "This evening we gathered in Hanji's office to honor the memory of the victims."
    scene cabinet
    stop music fadeout 1.0
    play music tragedy_strikes volume 0.5 fadein 1 fadeout 1 loop
    show hanji at left
    with dissolve
    hanji "It all comes together in the end. Sorry for my stinginess in emotions, but that’s how it’s supposed to be. I'm glad everyone survived this mission and returned to the city unharmed."
    main_char "For the first time in the entire time we were in the group, Hanji hugged us."
    hanji "Let's drink to the dead. Let our glasses honor their memory."
    hide hanji
    with dissolve
    main_char "We drank a glass of wine, and then another, and another... When it was already late at night, conversations began about our first sorties, and we began to recall the most memorable events from our missions."
    main_char "As morning approached, everyone began to disperse, with almost everyone departing. Only Hanji and I were left in the room, collecting mugs and bottles from our get-together."
    show hanji at left
    with dissolve
    hanji "Stor, I'm sorry about that girl. I wished I could have saved her, but fear overwhelmed me, and we had to leave her behind. Please forgive me."
    main_char "This is the first time I've seen Hanji cry. It was more like a man's stingy surveillance than a woman's tears."
    main_char "Hanji quickly calmed down, wiped away her tears and apologized to me again."
    hanji "Stor, I can handle the rest on my own, you can go rest. If there is a new mission, I will notify everyone."
    stor "Hanji, if you need any help outside of missions, do let me know. I'm here to help."
    hanji "Thanks Stor, I'll keep that in mind."
    hide hanji
    with dissolve
    scene black
    main_char "After that, I went back to the tavern and fell asleep."
    scene tavern
    main_char "I woke up around noon and went downstairs for a drink and a snack."
    show airis2 at left
    with dissolve
    airis "Stor, Ob came by and dropped a letter for you."
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
    mushroom "In that case, there's no further for discussion. It seems I won't be able to cooperate with you anymore."
    mushroom "Your only choice now is to eliminate me. The priest in my hut will probably succumb to the same fate."
    mushroom "Nothing holds me back in this place or in this life anymore. I'm ready, you can start."
    hide mushroom
    with dissolve
    main_char "The mushroom man knelt down, lowered his arms and stretched out his neck."
    main_char "With a quick movement, I pulled my sword out of its sheath and cut the throat of the mushroom man."
    main_char "His head tumbled to the ground, and simultaneously, the mushrooms on his body stopped glowing."
    show hanji at left
    with dissolve
    hanji "We need to check the hut. The priest must be there."
    hide hanji
    with dissolve
    main_char "Upon entering the hut, we saw the priest lying on the only bed in the hut, his body covered in mushrooms."
    main_char "Hanji and Arisius ran up to the priest, attempting to use healing and light spells, but their efforts proved futile."
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
        main_char "We reached the capital as quickly as possible, carrying the priest on our back."
        scene dungeon_room
        main_char "We went down to the basement again, where Hanji showed us the body of one of the doctors. The room, where the body had been before, was now empty."
        main_char "We laid the priest on an empty table, and soon after, the archmage arrived and commenced a ritual over the priest. We were then instructed to return home."
        scene main_square
        main_char "The next day, we were summoned to the King's reception hall, where we were bestowed with our award and medal for bravery."
        main_char "Coming out of the king's reception room, we saw Eri standing nearby."
        show hanji at left
        with dissolve
        hanji "Everyone, come here."
        hanji "You too."
        main_char "Hanji looked towards Eri."
        hanji "So, the mission can be more or less considered successful. Therefore, today everyone is gathering in my office."
        hanji "As for you, young lady, accompany me. Until later, everyone."
        hide hanji
        with dissolve
        main_char "Hanji took Eri's hand, and together they walked away towards the market square."
        scene cabinet
        main_char "In the evening, we all gathered in Hanji’s office to honor the memory of the victims."
        show hanji at left
        with dissolve
        hanji "Let's drink to the dead. Let's honor their memory."
        hide hanji
        with dissolve
        main_char "We sat for a long time, talking about our past missions. However, I occasionally noticed the exchanged glances between Hanji and Eri, which remained a mystery to me."
        main_char "When, towards the end of the meeting, Hanji divulged where she and Eri had gone after our meeting with the king, everything fell into place."
        show hanji at left
        with dissolve
        hanji "I'd like to tell you all something. Eri and I visited a priest I know, and now Eri will reside in the capital, serving in the church."
        hide hanji
        with dissolve
        show eri at right
        with dissolve
        stor "Wow, Eri, congratulations. I'm sure you'll make a fine priestess."
        eri "Thank you, Stor. I'll try my best."
        hide eri
        with dissolve
        scene black
        main_char "A few days later, the king summoned us again to his court, where we saw Ayun, the priest we rescued, alive and well."
        main_char "The king and priest thanked us for the completed mission."
        if panic:
            main_char "After a while, information about the village incident became public knowledge, and as a consequence, the king had to step down from his position."
        else:
            main_char "After some time, the king made a statement and talked about what happened and how they successfully managed to deal with the situation."
        $ ending = "mg"
        jump end
    else:
        scene road
        stop music fadeout 1.0
        play music mission_failed volume 0.5 fadein 1 fadeout 1 loop
        main_char "Following these instructions, we swiftly assembled on the village's main street and proceeded towards the capital."
        main_char "I glanced at Hanji a couple of times and it was clear that this situation had completely thrown her off her emotional balance."
        main_char "I've never seen her so upset. I don't know if it was because the mission went wrong or because of the losses the kingdom suffered."
        main_char "Approaching the gate, Hanji came to a halt and turned toward us."
        show hanji at left
        with dissolve
        hanji "No one should know about what happened in this village. If word spreads, uncontrollable consequences could unfold."
        hanji "Therefore, I ask you not to tell anyone about this. Try not to raise this topic even among yourselves, as others may hear it and spread rumors throughout the kingdom."
        show arisius at right
        with dissolve
        arisius "Of course, Hanji, we understand. Everyone will keep their mouths shut."
        stor "Yes, our lips will be sealed about this case. But what should we do about the situation in the village? We can't just leave it like that."
        stor "If the situation with the village is not resolved, then this disease may spread to neighboring villages, eventually reaching the capital."
        hanji "We'll convey all the information we've gathered to the archmage and the king. I'm sure they call sort it all out."
        hanji "This is a very important matter to them, especially given the priest's death. Henceforth, this mission is no longer our concern."
        hanji "In fact, I don’t want to remember what I saw in the village. I haven't seen something like this in a very long time."
        hanji "Regardless, we will medals. After the ceremony, I suggest meeting in my office in the evening."
        hanji "Let us honor the memory of those who died."
        hide hanji
        with dissolve
        scene main_square
        main_char "The next day, we were summoned to the King's reception hall, where we were bestowed with our award and medal for bravery."
        main_char "Coming out of the king's reception room, we saw Eri standing nearby."
        show hanji at left
        with dissolve
        hanji "Everyone, come here."
        hanji "You too."
        main_char "Hanji looked towards Eri."
        hanji "So, the mission can be more or less considered successful. Therefore, today everyone is gathering in my office."
        hanji "As for you, young lady, accompany me. Until later, everyone."
        scene cabinet
        main_char "In the evening, we all gathered in Hanji’s office to honor the memory of the victims."
        show hanji at left
        with dissolve
        hanji "Let's drink to the dead. Let's honor their memory."
        hide hanji
        with dissolve
        main_char "We sat for a long time, talking about our past missions. However, I occasionally noticed the exchanged glances between Hanji and Eri, which remained a mystery to me."
        main_char "When, towards the end of the meeting, Hanji divulged where she and Eri had gone after our meeting with the king, everything fell into place."
        show hanji at left
        with dissolve
        hanji "I'd like to tell you all something. Eri and I visited a priest I know, and now Eri will reside in the capital, serving in the church."
        hide hanji
        with dissolve
        show eri at right
        with dissolve
        stor "Wow, Eri, congratulations. I'm sure you'll make a fine priestess."
        eri "Thank you, Stor. I'll try my best."
        hide eri
        with dissolve
        scene black
        if panic:
            main_char "After a while, information about the village incident became public knowledge, and as a consequence, the king had to step down from his position."
        else:
            main_char "After some time, the king made a statement and talked about what happened and how they successfully managed to deal with the situation."
        $ ending = "mb"
        jump end
    return

# jump end
label end:
    scene black
    game "Thanks for playing our game. Hope you enjoyed it."
    if ending == "g":
        game "Congratulations! You made it to the good ending. In our game, in addition to this ending, there are 3 more. Try to complete all of them!"
        game "Remember that every decision you make has the potential to influence the course of history and its ending."
    elif ending == "mg":
        game "You made it to the medium-good ending. In our game, in addition to this ending, there are 3 more. Try to complete all of them!."
        game "Remember that every decision you make has the potential to influence the course of history and its ending."
    elif ending == "mb":
        game "You made it to the medium-bad ending. In our game, in addition to this ending, there are 3 more. Try to complete all of them!"
        game "Remember that every decision you make has the potential to influence the course of history and its ending."
    elif ending == "b":
        game "Unfortunately, you made it to the bad ending. In our game, in addition to this ending, there are 3 more. Try to complete all of them!"
        game "Remember that every decision you make has the potential to influence the course of history and its ending."
    return