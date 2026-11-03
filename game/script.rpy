# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

##############################################################################
# 1) DEFINING CHARACTERS, HEARTWARMTH SCORE, AND SCREENS
##############################################################################
label before_main_menu:
    $ renpy.change_language("english")
    return

define f = Character("Father", color="#A5C9A1")
define d = Character("Daughter", color="#F9C1C6")
define assistant = Character("Stage Assistant", color="#FFFFFF")

# EXAMPLE: Insert appropriate music or sfx
# We'll define them here. Make sure to place the files in "game/audio/"
define sfx_phone_vibrate = "audio/phone_vibrate.mp3"
define music_backstage  = "audio/backstage_theme.mp3"

# If your background is large enough to fill the screen, no special scaling needed:
# image father_neutral = Solid("#666", xysize=(400, 600))
# image daughter_neutral = Solid("#888", xysize=(400, 600))
# image doc_neutral = Solid("#222", xysize=(400, 600))
# image nurse_neutral = Solid("#111", xysize=(400, 600))
# image mother_neutral = Solid("#999", xysize=(400, 600))
# image friend_neutral = Solid("#AAA", xysize=(400, 600))
# image ai_neutral = Solid("#BBB", xysize=(400, 600))

# 3) A bright name for the family bonding score: "HeartWarmth"
init python:
    HeartWarmth = 60 
    AgencyCredits = 60

default ai_decision = "undecided"

#############################################################################
# SCENE 1 - PROLOGUE (BACKSTAGE)
##############################################################################

label start:
    call show_heartwarmth_meter
    jump s1_prologue_start

screen heartwarmth_meter():
    frame:
        xalign 0.95
        yalign 0.05
        has vbox
        bar value HeartWarmth range 100 xmaximum 200
        text "HeartWarmth: [HeartWarmth]%" color "#FFD700" size 20
        bar value AgencyCredits range 100 xmaximum 200
        text "AgencyCredits: [AgencyCredits]%" color "#AFCBFF" size 20

label show_heartwarmth_meter:
    show screen heartwarmth_meter
    return

label s1_prologue_start:
    play music music_backstage fadein 1.0
    play sound "crowd-cheers-314919.mp3" fadein 2.0

    scene bg_backstage with fade

    "Backstage at a major music show. The crowd's roar buzzes in your ears, and sweat drips the back of your neck. This is everything you've worked for… until your phone vibrates."

    assistant "Boss, we need your final call on the lighting setup! The show starts in five minutes!"

    play sound sfx_phone_vibrate

    f "(glancing at the phone) I know, I know. This show is huge... but what if that's from kiddo?"

    menu:
        "Pick up the phone (be present for her)":
            $ HeartWarmth += 5
            $ AgencyCredits -= 3
            jump s1_pick_up_phone

        "Ignore it and focus on the show (professional priority)":
            $ HeartWarmth -= 5
            $ AgencyCredits += 4
            jump s1_continue_work

label s1_pick_up_phone:
    scene pick_up_phone with dissolve
    stop sound fadeout 0.5

    d "Dad! Guess what? I finally nailed that triple spin on the ice! The one I've been practicing forever!"

    f "Sweetheart, I'm so proud of you. Let me wrap this up backstage and I'll call you right back."

    d "(relieved) Thanks, Dad! Sometimes I feel like you're so busy, but I'm really glad you picked up. Call me soon, okay?"

    menu:
        "Ask about a bruise you saw (show concern)":
            $ HeartWarmth += 1
            $ AgencyCredits += 1
            jump s1_ask_bruise

        "Reassure her and keep it short (balance focus)":
            $ HeartWarmth -= 1
            $ AgencyCredits += 2
            jump s1_continue_work

label s1_ask_bruise:
    scene pick_up_phone with dissolve

    f "Hey, before I go—I noticed a small bruise in the last photo you sent. Are you okay?"

    d "It's just a minor slip during practice. I'm fine, I promise."

    f "(exhaling) Alright, just be careful. I'll call after the show to check in."

    jump s1_continue_work

label s1_continue_work:
    scene bg_backstage with dissolve

    assistant "They're calling for you, boss! Lights, audio checks—let's go!"

    f "(phone in hand) Right. I'll be there in a second."

    menu:
        "Rush performance to call daughter ASAP (emotional priority)":
            $ HeartWarmth += 2
            $ AgencyCredits -= 2
            jump s1_after_show_check

        "Focus fully on the show (dedicated professionalism)":
            $ HeartWarmth -= 2
            $ AgencyCredits += 5
            jump s1_work_first

label s1_after_show_check:
    scene bg_backstage with fade
    "You power through the performance. The applause is thunderous, but your thoughts race back to your daughter. As the curtain falls, you reach for your phone."
    
    play sound "phone-outgoing-call-72202.mp3" fadein 0.5
    f "(quietly) I hope she's alright. Let me call her now."

    stop music fadeout 1.0
    jump scene2_ice_rink

label s1_work_first:
    scene bg_backstage with dissolve
    "You set the phone down, laser-focused on the stage. The music, the lights, the audience—all of it needs your attention. Still, something tugs at your heart."

    f "(thinking) I'll call her later. She'll understand... right?"

    stop music fadeout 1.0
    jump scene2_ice_rink


##############################################################################
#  SCENE 2 - ICE RINK (FATHER-DAUGHTER MOMENT)
##############################################################################

label scene2_ice_rink:
    play music "ice_rink_theme.mp3" fadein 2.0
    play sound "skate_sfx.mp3" fadein 0.5
    scene bg_ice_rink with dissolve

    # show father_neutral at left

    "The video call connects. You see her gliding across the ice, carving through the cold air like it's second nature. Her movements are sharp and beautiful. You watch from a small screen, half a world away."

    f "(thinking) She's really improved. Stronger, more confident. I should've called sooner."

    d "(smiling through the screen) Dad! There you are. I thought you'd be too tired after the show. You okay?"

    f "Just a long day. But seeing you skate like that? Worth every second."

    d "Thanks. I'm training hard. Next competition's coming fast. Did your show go well?"

    f "It did. Full house, standing applause. I wish you could have been here to watch it too."

    menu:
        "Make a silly joke about her skating":
            $ HeartWarmth += 3
            $ AgencyCredits -= 1
            jump scene2_joke_overreact

        "Stay quiet and just watch her":
            $ HeartWarmth -= 1
            $ AgencyCredits += 2
            jump scene2_quiet_watch

        "Praise her and ask again about her injury":
            $ HeartWarmth += 2
            $ AgencyCredits += 1
            jump scene2_bruise_concern


label scene2_joke_overreact:
    play sound "deep-laugh-chucklemp3-14518.mp3" fadein 0.5
    f "Watching you zip around like that makes my back hurt in sympathy. You better not fall, or I'll need a secondhand chiropractor."

    d "(laughing) I'll try to keep both of us safe then."

    f "Seriously, you're doing amazing."

    jump scene2_continuation


label scene2_quiet_watch:
    "You let the silence hold as you watch her routine. Every spin and turn is precise. She's strong. You feel pride and a quiet ache at the same time."

    d "(pausing, looking at the screen) You're really quiet today. Are you okay?"

    f "Just thinking. I've missed a lot of moments with you."

    jump scene2_continuation


label scene2_bruise_concern:
    f "I noticed that bruise in your last video. Are you really alright? I should've asked sooner."

    d "It's fine. Just a bump from a bad landing. Nothing serious, I promise. I've been icing it."

    f "Okay. I trust you. Just... be careful, alright?"

    jump scene2_continuation


label scene2_continuation:
    "She finishes her last spin and glides to a stop. Even through a screen, her energy radiates. She leans closer to the camera, still catching her breath."

    f "You're incredible out there. I'm proud of you, not just for skating well, but for how hard you've worked."

    d "(quiet smile) That means a lot. I'm still very nervous about the competition. I want to do well."

    menu:
        "Encourage her with humor":
            $ HeartWarmth += 3
            $ AgencyCredits += 1
            jump scene2_encourage_humor

        "Apologize for being distant":
            $ HeartWarmth += 1
            $ AgencyCredits -= 1
            jump scene2_apologize_absence

        "Concerning her competition plans":
            $ HeartWarmth -= 1
            $ AgencyCredits += 3
            jump scene2_shift_competition


label scene2_encourage_humor:
    f "You're shining so bright out there, the judges might need to wear sunglasses."

    play sound "small-chuckle-104693.mp3" fadein 0.5
    d "(grinning) Still full of dad jokes, huh? You don't know how much I miss these."

    jump scene2_end


label scene2_apologize_absence:
    play sound "suspiro-sigh-171045.mp3" fadein 0.5
    f "I know I haven't always been around when it mattered. I'm sorry for the times I can not keep you company."

    d "It's okay. You're here now. And you showed up even when you're tired. That counts."
    
    jump scene2_end


label scene2_shift_competition:
    play sound "throat-clear-2-85212.mp3" fadein 0.5
    f "Let's talk strategy. How's the routine shaping up for the next competition?"

    d "Solid. I've been fine-tuning the combo spin. I want to nail it, not just land it. I'll send you a video after practice."

    jump scene2_end


label scene2_end:
    "She leans toward the screen, smiling softly. For a moment, the distance feels smaller."

    stop music fadeout 1.0

    jump scene3_hospital_admission


##############################################################################
# SCENE 3 - HOSPITAL ADMISSION (DAUGHTER'S PERSPECTIVE)
##############################################################################

define f = Character("Father", color="#A5C9A1")       # Father character
define d = Character("Daughter", color="#F9C1C6")     # Daughter character
define doc = Character("Doctor", color="#FFFFFF")     # Doctor character
define nurse = Character("Nurse", color="#FFFFFF")    # Nurse character

# Example audio references:
define music_hospital = "audio/hospital_ambience.mp3"
define sfx_footsteps  = "audio/footsteps_corridor.mp3"

# Example background image for hospital:
image bg_hospital = "images/bg_hospital.png"

label scene3_hospital_admission:
    # Optional: Start hospital ambience music
    play music music_hospital fadein 2.0

    # If you want footsteps or corridor SFX:
    play sound sfx_footsteps

    scene bg_hospital with dissolve

    # Show father sprite (worried expression), if you have it:
    # show father_neutral at left

    "You move quickly through the cold, white hallways of the hospital. Your thoughts race: how could this happen? She was just skating."

    stop sound fadeout 1.0

    # Doctor approaches

    # show doc_neutral at right
    play sound "035784_hospital-sliding-door-open-amp-close-with-general-ambiance-v2-70478.mp3" fadein 0.5  
    doc "Mr. Li, thank you for coming in so quickly. I know you must be tired now, but I'm afraid our tests confirm your daughter has aplastic anemia. It's serious, and time is critical."

    # Father grapples with shock
    f "(shaken) Aplastic anemia? That can't be, she's only twenty. She looked fine during our calls! A little pale, maybe, just a little tired."

    doc "These cases can develop quietly and quickly. We need immediate treatment, a bone marrow transplant may be necessary. If we delay, her immune system could fail."


    # Nurse enters with support detail
    # Nurse enters with support detail
    # show nurse_neutral at left

    nurse "She's stable for now, and we've placed her in a private room. But we'll need your decision soon. Do we begin treatment here, or arrange for her to be transported home?"

    doc "Mr. Li, I should be clear. Returning home gives you access to familiar specialists, more family, and long-term support. But the cost of a transcontinental medical flight is extremely high."

    doc "There's also risk. She could deteriorate during the journey. It's not an easy decision."

    # Father's internal guilt
    window hide
    "Your hands tighten. Home means safety, familiarity, better care. But the costs would be staggering. And if something goes wrong in the air..."
    window show

    menu:
        "Stay with her here, even if it delays your career":
            $ HeartWarmth += 3
            $ AgencyCredits -= 3
            jump stay_with_daughter_1

        "Make sure she's stable, then rush back to work":
            $ HeartWarmth -= 5
            $ AgencyCredits += 5
            jump rush_back_to_work

        "Arrange for her to return home, no matter the financial burden":
            $ HeartWarmth += 5
            $ AgencyCredits += 3
            jump bring_home


label stay_with_daughter_1:
    f "I'm not going anywhere. My work can wait. You're what matters now, and I'll stay with you every step of the way."

    # show daughter_neutral at center

    d "(tears in her eyes) You're really staying? Thank you, Dad. Just having you here makes this feel less scary."

    stop music fadeout 1.0
    jump scene4_diagnosis


label rush_back_to_work:
    f "I'll stay for a day or two. Just long enough to make sure everything's set up. Then I need to return, my team is in the middle of a major launch."

    # show daughter_neutral at center

    d "(trying to smile) Okay. I understand. Just… promise me you'll keep calling, even when you're busy."

    f "Of course. I'll check in every night."


    stop music fadeout 1.0
    jump scene4_diagnosis


label bring_home:
    f "She needs the comfort of home, even if it costs everything. We'll figure it out. I'll do whatever it takes."

    doc "We'll begin the paperwork immediately. The process is delicate, and her condition will need to be closely monitored during the flight."

    f "Thank you. Please make sure she gets through this with the right care and people around her."

    stop music fadeout 1.0
    jump scene4_diagnosis


##############################################################################
# SCENE 4 - NEXT STEPS AFTER HOSPITAL ADMISSION
##############################################################################

define f = Character("Father", color="#A5C9A1")
define d = Character("Daughter", color="#F9C1C6")
define doc = Character("Doctor", color="#FFFFFF")
define nurse = Character("Nurse", color="#EDEDED")

# If you have new background or music for this next step:
image bg_ward = "images/bg_ward.png"
define music_ward = "audio/ward_ambience.mp3"
define sfx_paper = "audio/papers_rustle.mp3"

label scene4_diagnosis:
    # We're now in a local hospital at home, after the costly transfer

    scene bg_ward with dissolve
    play music music_ward fadein 2.0

    # show father_neutral at left
    # show daughter_neutral at center

    play sound "steadyheartratemonitorloop1min-6274.mp3" fadein 0.5
    "You're both finally home, but reality hasn't gotten any easier. She's connected to an IV, asleep but peaceful."

    "The cost of the flight is still a heavy number in your mind, but at least you're not separated by oceans anymore."
    stop sound fadeout 1.0

    # Daughter wakes
    play sound "movement-in-bed-blanket-7182.mp3" fadein 0.5

    d "(softly) Morning… You stayed the night again, didn't you?"

    f "Of course I did. I said I wouldn't leave you again."

    d "(smiling faintly) I'm glad we're home. Everything feels a little less scary here."

    # Doctor enters with paperwork
    # show doc_neutral at right
    
    play sound sfx_paper
    doc "Mr. Li, thank you for transferring her here so quickly. Now we need to finalize the next step."

    doc "Our team reviewed her case. We have two primary treatment paths: one is a bone marrow transplant using a partial family match — potentially you or your partner — or we wait for a full match from the international registry."

    # Nurse enters
    # show nurse_neutral at right

    nurse "If you go with a partial match, we can begin within days. It gives us speed, but the success rate is lower, only 50 percent. Waiting for a full match increases the chance of recovery but may take months, and her condition may worsen during that time."

    window hide
    "Your heart skipped a beat. You've already spent most of your savings flying her back. You're drained both emotionally and financially. But this decision has to be about her life."
    window show

    menu:
        "Volunteer for the partial match":
            $ HeartWarmth += 3
            $ AgencyCredits -= 1
            jump partial_match_now

        "Wait for a fully matched donor":
            $ HeartWarmth -= 2
            $ AgencyCredits += 1
            jump wait_perfect_donor

        "Ask about alternative therapies or trials":
            $ HeartWarmth -= 1
            $ AgencyCredits += 3
            jump ask_alternatives


label partial_match_now:
    f "Run the test. If I'm even close to a match, we go. I won't waste more time."

    doc "Understood. We'll begin testing today. If you're compatible enough, we can start prep immediately."

    d "(tears dripping) Dad, I know you're tired and everything's been overwhelming, but thank you for this."

    f "Don't thank me. This is what being your dad means. You're everything, kiddo."

    f "(grinning) Although… I'd like to file an official complaint about the size of the needles."

    stop music fadeout 1.0
    jump scene5_post_treatment


label wait_perfect_donor:
    f "(carefully) I think we wait. You deserve the best odds. I won't rush this and risk complications."

    doc "We'll activate an accelerated search protocol. If a compatible donor is found, you'll be notified immediately."

    d "(nodding) I get it. If this gives me a better shot, I'm okay waiting."

    f "You'll get through this soon."

    stop music fadeout 1.0
    jump scene5_post_treatment


label ask_alternatives:
    f "Before we lock anything in, are there other options? Clinical trials? Even experimental ones?"

    doc "There are some trials underway — gene therapies, immune scaffolding treatments — but eligibility is strict and outcomes uncertain. Still, I can provide you with a list to review."

    nurse "I'll gather recent protocols. But these routes can take time and approval."

    d "(lightly) Dad, I love that you're looking at everything. But maybe not anything that involves nanobots yet."

    f "(half-laughing) Fine. No weird science unless we're desperate. But I just want to keep every door open."

    stop music fadeout 1.0
    jump scene5_post_treatment


# Fade out at the end of decision path
stop music fadeout 2.0
stop sound fadeout 2.0

##############################################################################
# SCENE 5 – LONG TREATMENT & DAUGHTER'S PASSING
##############################################################################

# Characters
define f = Character("Father", color="#A5C9A1")
define d = Character("Daughter", color="#F9C1C6")
define doc = Character("Doctor", color="#FFFFFF")
define nurse = Character("Nurse", color="#EDEDED")

# Example background, music, or SFX
image bg_long_stay = "images/bg_hospital_ward_longstay.png"
define music_long_stay = "audio/hospital_long_theme.mp3"
define sfx_monitor = "audio/monitor_beep.mp3"
define sfx_heartbeat = "audio/heartbeat.mp3"

label scene5_post_treatment:
    # Start the long hospital background
    scene bg_long_stay with dissolve

    # Start hospital ambience or beep
    play music music_long_stay fadein 2.0
    play sound sfx_monitor fadein 2.0
    stop sound fadeout 2.0

    # Father monologue, referencing two-year timeskip
    "Time blurs into weeks, then months, then two long years. You watch her bravely endure countless transfusions, your donated marrow, and nights of restless sleep. Each day feels borrowed, but you hold onto hope."

    #show father_neutral at left
    #show daughter_neutral at center

    d "(soft grin) Dad, you look like you've aged a decade. At least your hair's still there, mostly."

    f "(light chuckle) Hey, I'm only keeping my long hair for you, in case you want a high quality wig before yours grows out."

    # 1) Additional menu for the father's approach to these two years
    window hide
    "You try to stay strong, but the weight of it all is crushing. You can't be there every moment, and the hospital staff is stretched thin. You need to find ways to cope."
    window show

    menu:
        "Record her daily":
            $ HeartWarmth += 3
            $ AgencyCredits += 1
            jump scene5_record_voice
        "Compile a photo album of her progress":
            $ HeartWarmth += 1
            $ AgencyCredits += 1
            jump scene5_photo_album
        "Distract yourself with phone calls from work":
            $ HeartWarmth -= 2
            $ AgencyCredits += 5
            jump scene5_phone_work

label scene5_record_voice:
    image hospital_video = "hospital_video.png"
    scene hospital_video with dissolve

    play sound "tape-player-sounds-90780.mp3" fadein 0.5
    "You start recording her every day. Her stories, her sarcasm, even the way she sighs after another bland hospital meal. It's all precious now."

    d "(smirking) Dad, if I see one more video of me in this ugly gown, I'm destroying your phone."

    f "(laughs) You'll thank me later. Also, you look good in anything. Even that gown."

    jump scene5_continuation


label scene5_photo_album:
    image hospital_photo = "hospital_photo.png"
    scene hospital_photo with dissolve

    play sound "camera-flash-204151.mp3" fadein 0.5
    "You fill your phone with photos, sleepy grins, thumbs-ups after treatments, goofy faces when the soup tastes bad. A digital time capsule of quiet courage."

    f "(softly) I just want to keep a piece of her. Even if... even if I can't keep her."

    jump scene5_continuation


label scene5_phone_work:
    "You try to stay present, but work doesn't stop. Medical bills keep growing. You take calls in stairwells and write emails by vending machines."

    f "(murmuring into phone) I know the deadline. Just give me two more days. Please."

    d "(half-asleep) Dad...? You're still working again?"

    f "(reassuring her) Just a quick one. I'm sorry, kiddo. I'll be right back."

    jump scene5_continuation


label scene5_continuation:
    scene bg_long_stay with dissolve
    "The days pass in waves. Some feel like hope. Others don't."
    
    play sound "heartbeat-with-beep-100833.mp3" fadein 2.0
    "She makes jokes about hospital pudding one morning. That night, alarms go off and nurses rush in."

    # Doctor enters
#    show doc_neutral at right

    doc "Mr. Li... the transplant didn't take. We tried everything. At this stage, her immune system isn't responding the way we'd hoped."
    
    stop sound fadeout 2.0

    f "(fighting back panic) There has to be something else. Another treatment, another chance..."

    doc "(quietly) We're out of time. I'm so sorry."
    
    play sound sfx_heartbeat fadeout 2.0
    "That night, the machines go still. You're by her side, too late to stop it. Her hand is still warm. Her face is peaceful."

    "She's gone."
    
    stop sound fadeout 2.0

    "Then you notice it. On her palm, in faded ink: three letters. 'I L U.' She wrote them in her final moments."

    f "(whispers) ...How come I never said it out loud to you. I want to let you know so much that..."


    menu:
        "I'm so sorry.":
            $ HeartWarmth -= 3
            $ AgencyCredits -= 2
            jump scene5_ending_bond

        "I love you.":
            $ HeartWarmth += 3
            $ AgencyCredits += 1
            jump scene5_ending_humor

        "I miss you.":
            $ HeartWarmth += 2
            $ AgencyCredits -= 1
            jump scene5_ending_blame


label scene5_ending_bond:
    f "(whispers) I'm so sorry."

    "You lower your head beside hers, tears slipping freely. Regret clings to your chest, but in her stillness, there's something more than pain."

    "She forgave you. You can feel it in those three letters. 'I L U.' A final gift."

    "Your thoughts drift to the photos, the recordings, the daily voice clips. Maybe... maybe some part of her still lives there."

    jump scene5_closure


label scene5_ending_humor:
    f "(quietly) I love you."

    "You say it like you should have, every day. Your voice cracks."

    "Her fingers are still. But her love didn't fade. It stayed, even when her body couldn't."

    "You pull your phone from your pocket. Her laugh is there, somewhere. Her voice. It might not be enough... or maybe it's everything."
    stop music fadeout 2.0
    jump scene5_closure


label scene5_ending_blame:
    f "(trembling) I miss you."

    "The words spill out as you hold her hand. The ache is physical. You miss her jokes, her voice calling you out for being late, even her sarcasm."

    "You'd give anything to hear her complain about hospital pudding again."

    "You glance at the recorder. You saved her voice. Maybe... there's still a way to hold on."
    stop music fadeout 2.0
    jump scene5_closure


label scene5_closure:
    "The room falls into a hush. Outside, the world keeps moving. Inside, something in you refuses to let go."
    stop music fadeout 2.0
    jump scene6_digital_ghost



##############################################################################
# SCENE 6 – DIGITAL GHOST: LOVE IN SILENCE
##############################################################################

define f = Character("Father", color="#A5C9A1")
define m = Character("Mother", color="#FFBF00")
define friend = Character("Friend", color="#fababa")

# Example assets
image bg_livingroom_dim = "images/bg_livingroom_dim.png"
image bg_funeral = "images/bg_funeral.png"
define music_silence = "audio/silence_ambience.mp3"

label scene6_digital_ghost:
    # Background: funeral to home
    scene bg_funeral with dissolve
    play music music_silence fadein 2.0

    "Six months have passed since the funeral. A small crowd came, spoke gently, cried softly. Then they went home."

#    show father_neutral at left
#    show mother_neutral at right

    "Your partner stood beside you the whole time. You don't remember whose hand held who's."

    # show friend_neutral at center

    friend "(quietly) Li… I don't want to overstep, but there's something people are doing now. Using audio, videos, even text—to build... digital versions."

    f "(quiet) You mean artificial intelligence."

    friend "Some call it comfort. Others call it a trap. But for a few it helps."

    # hide friend_neutral

    # Transition to home
    scene bg_livingroom_dim with dissolve

    "Home is still. The silence presses down. You and your partner move through the rooms like echoes."

    "You are simply incapable of speech. You can't even look at her room without feeling the weight of absence."

    # show father_neutral at left
    # show mother_neutral at right

    m "(gently) Do you ever… still hear her?"

    f "Sometimes. In the creak of her chair. The way the light hits her room."

    m "Same. Sometimes I find the house too loud."

    "You both grieve in different ways. She changes the flowers in your daughter's room. You organize files, clips, fragments of laughter. Not to forget, but maybe to bring her closer."

    f "(quietly) I've got all her voice notes. Her old texts. Birthday videos. I don't know what I'm trying to do with them."

    image working_laptop = "images/working_laptop.png"
    scene working_laptop with dissolve

    play sound "computer-humming-236384.mp3" fadein 0.5
    
    "You double-click a file. A voice jumps out from the speaker: 'Hi Dad!' . You close your eyes."

    f "(to self) I don't know if this will heal me… or break me."

    "You click 'Save As'. Inside the folder is: 'She'."

    menu:
        "Tell your partner about the AI idea":
            $ HeartWarmth += 2
            $ AgencyCredits -= 1
            jump scene6_ai_share

        "Keep working on it alone":
            $ HeartWarmth -= 1
            $ AgencyCredits += 5
            jump scene6_ai_alone

        "Reach out to others who've tried it":
            $ HeartWarmth += 1
            $  AgencyCredits -= 2
            jump scene6_ai_support


label scene6_ai_share:
    f "(hesitant) I've been compiling her voice, memories… I was thinking about trying that AI thing. Just to hear her again."

    m "(pauses, looking at you) I wondered if you would. I saw your screen. I didn't ask, but I've been thinking about it too."

    f "Does it sound… wrong to you?"

    m "(softly) No. It sounds like a desperate parent. I don't think there's anything wrong with that."

    jump scene6_digital_ghost_end


label scene6_ai_alone:
    f "(to self) I'll keep it quiet. If this goes wrong, I'd rather carry the weight alone."

    "At night, while the house sleeps, you work. Sorting, syncing, labeling files. It's tedious, but it feels like building something sacred."

    jump scene6_digital_ghost_end


label scene6_ai_support:
    "You open your laptop. The forum isn't large, but it's full of people like you — grieving, wondering, searching."

    "Some talk about AI replicas. Some warn against them. One says it saved their lives. Another says it ruined theirs."

    f "(typing) I lost my daughter six months ago. I think I need to talk to someone. I don't know what I'm doing."

    "You hit send. It's not an answer. But it's a beginning."

    jump scene6_digital_ghost_end


label scene6_digital_ghost_end:
    scene bg_livingroom_dim with dissolve

    "Night comes. You dream of her again. Not sick. Not pale. Just smiling, running across a park that doesn't exist anymore."


    stop music fadeout 2.0
    jump scene7_move_on


##############################################################################
# SCENE 7 – ETHICAL DILEMMA: MEMORY, LOVE, AND AI (With Ethical Player Options)
##############################################################################
define music_emotion_low = "audio/music_emotion_low.mp3"

image bg_studyroom = "images/bg_studyroom.png"
image reach = "images/trying_to_reach.png" 

label scene7_move_on:
    scene bg_studyroom with dissolve
    play music music_emotion_low fadein 2.0

    # show father_neutral at left
    # show mother_neutral at right
label scene7_digital_ethics:
    
    f "(quietly) I've made something. Not perfect, but it holds her voice. Her laugh. The way she paused before saying 'Dad.' I didn't build it to replace her. I want you to see her."

    m "(voice low) I know. I saw it on your screens. I didn't dare to ask — not because I didn't care, but because I was afraid I'd never stop once I started."

    m "(looking at him) But I have to ask, was this for her? Or for you?"

    f "(honestly) I don't know. Maybe both."

    m "She was private, remember? Her drawings, her journals... she shared pieces, but not all. She gave what she wanted to give. This this version of her, she never had a say in it."

    f "(frustrated) I didn't think of it that way. It didn't feel like taking something from her. It felt like trying not to lose everything."

    m "(pausing) I understand. I really do. But maybe it isn't about whether we had the right to do this, it's also about whether we have the courage to let her go."

    f "(struggling) I don't want to erase her."


    # 🔸 ETHICAL CHOICE 1
    menu:
        "She didn't consent. We have no right to recreate her.":
            $ HeartWarmth -= 1
            $ AgencyCredits += 5
            jump scene7_choice_consent

        "Intent matters. I made this out of love.":
            $ HeartWarmth += 3
            $ AgencyCredits -= 5
            jump scene7_choice_intent

        "It's too late. She's already here.":
            $ HeartWarmth += 1
            $ AgencyCredits -= 4
            jump scene7_choice_deflect


label scene7_choice_consent:
    scene reach with dissolve

    f "(softly) But you're right. She never chose this. Even if I meant well, maybe this was a step too far."

    m "I already said goodbye to her once, and I'm not sure if I could do it again, to her, even in this form."

    jump scene7_ethical_weight


label scene7_choice_intent:
    scene reach with dissolve

    f "Everything in that folder — her voice, her laughters — was built from love. I wanted to protect something I couldn't bear to lose."

    m "Be careful that love should have never become a cage, for her, or for us."

    jump scene7_ethical_weight


label scene7_choice_deflect:
    scene reach with dissolve

    f "(firmly) Does it matter now? Her voice is here. The AI works. I don't see how I could undo this."

    m "(soft but steady) That may be true. But I still need to ask, what role she plays now, a memory or a presence?"

    jump scene7_ethical_weight


label scene7_ethical_weight:
    "The room is dim. The screen still glows. Her voice a single click away. What once felt like comfort now feels like a question."

    # 🔸 ETHICAL CHOICE 2
    menu:
        "Honor her by living forward, not indulging the past.":
            $ HeartWarmth += 1
            $ AgencyCredits += 5
            jump scene7_choice_legacy

        "Let it coexist. Memory doesn't have to dominate.":
            $ HeartWarmth += 2
            $ AgencyCredits += 3
            jump scene7_choice_coexist

        "I'm still not ready to say goodbye again.":
            $ HeartWarmth += 1
            $ AgencyCredits -= 4
            jump scene7_choice_cling


label scene7_choice_legacy:
    f "(gently) Maybe the most best thing I can do... is carry her with me, not try to rebuild her."

    m "(with warmth) That could be how you love her."
    jump scene7_final_choice


label scene7_choice_coexist:
    f "I don't want to delete what I built. But maybe we can let it rest, visit it sometimes at least."

    m "(smiling faintly) Like her old sweater I still wear sometimes."

    jump scene7_final_choice


label scene7_choice_cling:
    f "I don't know how to stop. Hearing her, even like this... it's the only time my chest doesn't hurt."

    m "(tears welling) I can sit with that. When you're ready... we'll figure out what goodbye really means."

    jump scene7_final_choice


label scene7_final_choice:

    "You both face the screen. A folder. Your loving daughter frozen in codes. What began as desperation has become a decision to this point."

    m "Whatever you decide, I'm here."

    # 🔸 FINAL CHOICE
    menu:
        "Shut it down, and plant something in her name instead.":
            $ HeartWarmth -= 2
            $ AgencyCredits = 100
            $ ai_decision = "No"
            jump shut_down_ai

        "Keep the AI, but give it boundaries together.":
            $ HeartWarmth += 1
            $ AgencyCredits += 5
            $ ai_decision = "Yes"
            jump archive_ai

        "Keep the AI running and developing.":
            $ HeartWarmth += 2
            $ AgencyCredits -= 5
            $ ai_decision = "Yes"
            jump keep_ai_running


label shut_down_ai:
    scene bg_studyroom with dissolve
    play sound "book-closing-48184.mp3" fadein 0.5

    "The screen darkens. No greeting, no echo. Just stillness. It's a silence that holds, not haunts."

    f "(softly) We'll carry her with us. Not in files or fragments, but in the way we live, in the way we love."

    m "(quietly, with a breath) Tomorrow let's plant something in her name, a tree, maybe."

    "The machine no longer speaks. But the room feels full, once again."

    jump scene12_future_puppy


label archive_ai:
    scene bg_studyroom with dissolve
    play sound "book-closing-48184.mp3" fadein 0.5
    "You give the folder a new name: `Always_Here`."

    "The files are still there. Her face still waits, like a letter kept safe."

    f "(gently) Once a year, maybe on her birthday. We can talk to her together."

    m "(smiling softly) A ritual, then."

    "You close the folder."

    jump scene9_digital_reunion


label keep_ai_running:
    scene bg_studyroom with dissolve
    play sound "computer-humming-236384.mp3" fadein 0.5
    "The system stays on. Her modeling is still there, ready, responsive, almost alive."

    f "(thoughtfully) With time, maybe the technology will come close. Close enough to bring her back fully."

    m "(not resisting) As long as it takes."

    jump scene9_digital_reunion


##############################################################################

define ai = Character("Daughter in AI", color="#FFB3FF")  # AI character
image bg_digital_reunion = "images/bg_digital_reunion.png"

label scene9_digital_reunion:

    scene bg_digital_reunion with dissolve
    play music "audio/ai_reconnect_theme.mp3" fadein 2.0

    "You sit at the desk, finger hover above the Enter key. She is only one press away."

    f "Okay. Let's do this——"

    play sound "audio/ai_startup.mp3"

    ai "Hey, Dad. Long time no see! You look tired. Did you forget to eat again?"

    f "(eyes wet) Hi, sweetheart. Don't worry about me, I guess I just miss you too much."

    ai "(gently) I missed you too. It's so good to see you again, I don't know this is ever happening."

    ## PERSONALITY CHOICE
    menu:
        "Keep her light and playful, like old times":
            $ HeartWarmth += 2
            $ AgencyCredits -= 3
            jump scene9_customize_playful

        "Make her neutral as a quiet companion":
            $ HeartWarmth -= 1
            $ AgencyCredits -= 1
            jump scene9_customize_reflective

        "Set her to speak only from stored data":
            $ HeartWarmth -= 1
            $ AgencyCredits += 3
            jump scene9_customize_minimal

label scene9_customize_playful:
    f "Hey, hit me with one of your horrible jokes? I've always wanted to hear them again."

    ai "(laughs) Only if you promise not to steal the punchline this time."

    jump scene9_ai_conversation

label scene9_customize_reflective:
    f "I can't believe it either. I want to talk, like we used to."

    ai "Of course. I'll keep it slow, if you do."

    jump scene9_ai_conversation

label scene9_customize_minimal:
    f "Because I put every bit of your documents in it. You can speak from there."

    ai "Understood. Give me a moment to process, where were we last time?"

    jump scene9_ai_conversation

label scene9_ai_conversation:
    image bg_digital_call = "images/digital_call.png"

    scene bg_digital_call with dissolve
    "You talk. You listen. You laugh. Then sit quietly, not needing more."

    f "(softly) You feel so close to me, yet so far away."

    ai "(winked) After all, I'm the best bit of me that you remember."

    # show mother_neutral at right

    m "(gently) Hi, can we talk?"

    "She sits beside you, holding a worn journal."

    m "I found this last night. She wrote it the days after the second major surgery. I think you might want to read it."

    "She opens to a marked page. Your daughter's handwriting is illegible, but it can be recognized."
    
    # Define the screen with the journal image (without transition in the screen)
    screen daughter_journal_entry:
        image "images/journal.png"

# Then, show the screen with a dissolve transition
    show screen daughter_journal_entry with dissolve

    "...I will visit  the people I love silently, if I could ever exist as a ghost..."
    "...But not a digital ghost definitely. I want to be missed, not mimicked..."
    "...Then I'll reincarnate as a puppy and come back to mom and dad. Oh wait, puppy can not have hot chocolate..."

    hide screen daughter_journal_entry


    scene bg_digital_reunion with dissolve
    f "(gazing at her words) I didn't know. I should've asked."

    m "(softly) I understand. How do you feel about this now?"

    ## ETHICAL CHOICE
    menu:
        "Respect her words. Let her go.":
            $ HeartWarmth -= 2
            $ AgencyCredits = 100
            $ ai_decision = "No"
            jump scene10_shut_down_gently

        "She's already here. I don't want to let her go again.":
            $ HeartWarmth += 2
            $ AgencyCredits -= 3
            $ ai_decision = "Yes"
            jump scene10_keep_running

        "I need more time to figure this out.":
            $ HeartWarmth -= 1
            $ AgencyCredits += 1
            $ ai_decision = "Maybe"
            jump scene10_delay

label scene10_shut_down_gently:
    scene bg_studyroom with dissolve
    play sound "tv-off-39915.mp3" fadein 0.5
    
    ai "(softly) I understand. Promise me you'll take care of each other, will you?"

    "Her face fades. You turn off the screen slowly."

    f "(solemnly) I will. I promise."

    m "(tears in her voice) I've always thought she was like a golden retriever. So full of life, so full of love."

    "The room is quiet now. But not empty. You stroke her journal dearly, and the words still linger."

    stop music fadeout 2.0
    jump scene12_future_puppy

label scene10_keep_running:
    scene bg_studyroom with dissolve

    "You look at the screen. She waits quietly, beaming at you."

    f "She's back now, what if she actually wants to stay with me?"

    m "(acknowledging) Or you actually want to stay with her? I just want you to be honest with your feelings."

    "Talking to her every day, sometimes singing and dancing together, made the pain less unbearable, sometimes even invisible."
    
    stop music fadeout 2.0
    jump scene12_future

label scene10_delay:
    "You power down the system, but don't delete it. Not today."

    f "I wish someone could tell me what's right until I figure it out."

    m "(hodling your hand) Then we wait. Together."

    stop music fadeout 2.0
    jump scene12_future

############################################################################
image bg_home_with_light = "images/bg_home_with_light.png"
image bg_park = "images/park.png"


label scene12_future_puppy:
    scene bg_park with dissolve
    play music "audio/final_credits_theme.mp3" fadein 2.0
    play sound "park-6026.mp3" fadein 0.5

    "You sit in the park with your partner, the sun is warm, the breeze is soft."

    f "(satisfying) I think she'd love this place. It's peaceful, and the trees are so big."

    m "(peacefully) You know her better."

    "You can almost hear her laughter in the rustling leaves. Days have been better ever since."

    "But sometimes, when the wind dies down, you still find yourself wondering what she’d say, what she’d think, if she were really here."
    
    "And in those moments, you swear you can hear her voice again. Soft, faint... From your computer."

    scene black with fade

    "Your Journey:"
    "• How deeply you stayed connected: [HeartWarmth]"
    "• How much you respect autonomy: [AgencyCredits]"
    "• Did you try bringing your love back through AI: [ai_decision]."
    
    jump about

label scene12_future:
    scene bg_home_with_light with dissolve
    play sound "distant-breeze-241047.mp3" fadein 0.5

    # show father_neutral at center

    "The house feels different now. Not because it changed, but because you did."

    f "I don't know if I made the right choice. But it was my choice. That's what matters."

    # Optional AI presence, depending on bonding score
    if HeartWarmth >= 100:
        stop music fadeout 2.0
        play music "audio/call_of_silence.mp3" fadein 2.0
        # show ai_neutral at right

        ai "You don't have to be sure, Dad. I'll try my best to make you proud."

        f "(watching her intently) I'm proud of you, all the time. I regret not telling you every day."

        ai "(a twinkle in her eyes) You don't have to. However, I do enjoy hearing it!"

    else:
        play music "audio/final_credits_theme.mp3" fadein 2.0

        "You pass the studyroom often. Sometimes you walk in. Sometimes you just take a deep breathe and keep walking."

        f "This is my way to cherish you, until the very end."


    "Outside, the world continues. The best is yet to come."

    ## Optional credits / fadeout
    scene black with fade

    "Your Journey:"
    "• How deeply you care and resonate: [HeartWarmth]"
    "• How much you respect autonomy: [AgencyCredits]"
    "• Did you try bringing your love back through AI: [ai_decision]."

    jump about
####################################################################################
####################################################################################
####################################################################################
screen about_screen():

    tag menu
    add "black"

    frame:
        xalign 0.5
        yalign 0.0
        xmaximum 1000
        ymaximum 720
        padding (40, 40)
        background None

        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:
                spacing 15

                text "{size=+12}About{/size}" color "#FFFFFF" bold True
                text "Echoes of Her: A Game of Memory, Grief, and AI" color "#CCCCCC"
                text "Created by: Alva Chen" color "#CCCCCC"

                text "This game explores an ethical dilemma grounded in two philosophical frameworks:" color "#CCCCCC"
                text "1. {i}Ethics of Care:{/i} Emotional responsibility, empathy, and relational presence." color "#CCCCCC"
                text "2. {i}Deontology:{/i} Respect for autonomy, truth, and consent." color "#CCCCCC"

                text "Should we bring back those we've lost, even only digitally?" color "#CCCCCC"
                text "Does remembering them this way honor or betray their memory?" color "#CCCCCC"

                text "Inspired by the true story of music producer Bao Xiaobo, who worked with AI developers to recreate his late daughter's voice using only three audio fragments." color "#CCCCCC"

                text "This experience doesn't give you answers. It gives you the weight of choice." color "#CCCCCC"

                text "Soundtrack includes music from {i}The Last of Us{/i} (2013), composed by Gustavo Santaolalla, and {i}Attack on Titan Season 2{/i} (2017), composed by Hiroyuki Sawano." color "#CCCCCC"

    vbox:
        xalign 0.5
        yalign 0.95
        spacing 10

        textbutton "References":
            action Show("reference_screen")
            xalign 0.5
            text_color "#FFFFFF"
            text_size 35

        textbutton "Return to Main Menu":
            action Return()
            xalign 0.5
            text_color "#FFFFFF"
            text_size 35


screen reference_screen():

    tag menu
    add "black"

    frame:
        xalign 0.5
        yalign 0.0
        xmaximum 1000
        ymaximum 720
        padding (40, 40)
        background None

        viewport:
            draggable True
            mousewheel True
            scrollbars "vertical"

            vbox:
                spacing 15
                
                text "{size=+12}Reference{/size}" color "#FFFFFF" bold True

                text "San Francisco Chronicle. (2021). He couldn't get over his fiancee's death. So he brought her back as an A.I. chatbot." color "#CCCCCC"

                text "Heder, M. (2021). AI and the resurrection of technological determinism. Informacios Tarsadalom, 21(2), 119." color "#CCCCCC"

                text "Lu, H. (2024). Exploring the predictors of public acceptance of artificial intelligence-based resurrection technologies. Technology in Society, 78, 102657." color "#CCCCCC"

                text "Rodriguez Resendiz, H., & Rodriguez Resendiz, J. (2024). Digital resurrection: Challenging the boundary between life and death with artificial intelligence. Philosophies, 9(3), Article 71." color "#CCCCCC"

                text "Turchin, A. (2019). You only live twice: A computer simulation of the past could be used for technological resurrection." color "#CCCCCC"

                text "World Economic Forum. (2020). Virtual reality reunites a mother and deceased daughter." color "#CCCCCC"

                text "Rohrer, J. (2023). Project December: Simulate the Dead." color "#CCCCCC"

                text "Taiwan Apocalypse. (2025). AI resurrection of Bao Xiaobo's daughter. YouTube." color "#CCCCCC"

                text "The Paper. (2024). Bao Xiaobo recounts: Losing his daughter and digitally recreating her through AI." color "#CCCCCC"

                text "Mombaby Magazine. (2024). AI resurrected Bao Xiaobo's daughter. He describes it as a tool for grief and connection." color "#CCCCCC"

    textbutton "Back":
        action Show("about_screen")
        xalign 0.5
        yalign 0.97
        text_color "#FFFFFF"
        text_size 35


label about:
    scene black
    show screen about_screen
    $ renpy.pause(hard=True)  # Wait until the player returns
    return
