# NOTE: \a is the delimiter for chat pages
# Quest ids can be found in Quests.py
SCRIPT = '''
ID reward_100
SHOW laffMeter
LERP_POS laffMeter 0 0 0 1
LERP_SCALE laffMeter 0.2 0.2 0.2 1
WAIT 1.5
ADD_LAFFMETER 1
WAIT 1
LERP_POS laffMeter -1.18 0 -0.87 1
LERP_SCALE laffMeter 0.075 0.075 0.075 1
WAIT 1
FINISH_QUEST_MOVIE

# TUTORIAL

ID tutorial_mickey
LOAD_SFX soundRun "phase_3.5/audio/sfx/AV_footstep_runloop.ogg"
LOAD_CC_DIALOGUE mickeyTutorialDialogue_1 "phase_3/audio/dial/CC_%s_tutorial02.ogg"
LOAD_CC_DIALOGUE mickeyTutorialDialogue_2 "phase_3.5/audio/dial/CC_tom_tutorial_%s01.ogg"
LOAD_CC_DIALOGUE mickeyTutorialDialogue_3a "phase_3/audio/dial/CC_%s_tutorial03.ogg"
LOAD_CC_DIALOGUE mickeyTutorialDialogue_3b "phase_3/audio/dial/CC_%s_tutorial05.ogg"
LOAD_DIALOGUE mickeyTutorialDialogue_4 "phase_3.5/audio/dial/CC_tom_tutorial_mickey02.ogg"
LOCK_LOCALTOON
REPARENTTO camera render
POSHPRSCALE camera 11 7 3 52 0 0 1 1 1
LOAD_CLASSIC_CHAR classicChar
REPARENTTO classicChar render
POS classicChar 0 0 0
HPR classicChar 0 0 0
POS localToon 0 0 0
HPR localToon 0 0 0
WAIT 2
PLAY_SFX soundRun 1
LOOP_ANIM classicChar "run"
LOOP_ANIM localToon "run"
LERP_POS localToon -1.8 14.4 0 2
LERP_POS classicChar 0 17 0 2
WAIT 2
#LERP_HPR localToon -110 0 0 0.5
LERP_HPR localToon -70 0 0 0.5
LERP_HPR classicChar -120 0 0 0.5
WAIT 0.5
STOP_SFX soundRun
LOOP_ANIM localToon "neutral"
PLAY_ANIM classicChar "left-point-start" 1
WAIT 1.63
LOOP_ANIM classicChar "left-point"
CC_CHAT_CONFIRM classicChar "QuestScriptTutorial%s_1" mickeyTutorialDialogue_1
PLAY_ANIM classicChar "left-point-start" -1.5
WAIT 1.0867
LOOP_ANIM classicChar "neutral"
CC_CHAT_TO_CONFIRM npc classicChar "QuestScriptTutorial%s_2" "CFSpeech" mickeyTutorialDialogue_2
PLAY_ANIM classicChar "right-point-start" 1
WAIT 1.0867
LOOP_ANIM classicChar "right-point"
CC_CHAT_CONFIRM classicChar "QuestScriptTutorial%s_3" mickeyTutorialDialogue_3a mickeyTutorialDialogue_3b
PLAY_SFX soundRun 1
LOOP_ANIM classicChar "run"
LERP_HPR classicChar -180 0 0 0.5
WAIT 0.5
LERP_POS classicChar 0 0 0 2
WAIT 2
STOP_SFX soundRun
REPARENTTO classicChar hidden
UNLOAD_CHAR classicChar
#CHAT npc QuestScriptTutorialMickey_4 mickeyTutorialDialogue_4
REPARENTTO camera localToon
POS localToon 1.6 9.8 0
HPR localToon 14 0 0
FREE_LOCALTOON
LOCAL_CHAT_PERSIST npc QuestScriptTutorialMickey_4 mickeyTutorialDialogue_4

# TUTORIAL HQ HARRY

ID quest_incomplete_110
DEBUG "quest assign 110"
LOAD_DIALOGUE harryDialogue_01 "phase_3.5/audio/dial/CC_harry_tutorial_questscript01.ogg"
LOAD_DIALOGUE harryDialogue_02 "phase_3.5/audio/dial/CC_harry_tutorial_questscript02.ogg"
LOAD_DIALOGUE harryDialogue_03 "phase_3.5/audio/dial/CC_harry_tutorial_questscript03.ogg"
LOAD_DIALOGUE harryDialogue_04 "phase_3.5/audio/dial/CC_harry_tutorial_questscript04.ogg"
LOAD_DIALOGUE harryDialogue_05 "phase_3.5/audio/dial/CC_harry_tutorial_questscript05.ogg"
LOAD_DIALOGUE harryDialogue_06 "phase_3.5/audio/dial/CC_harry_tutorial_questscript06.ogg"
LOAD_DIALOGUE harryDialogue_07 "phase_3.5/audio/dial/CC_harry_tutorial_questscript07.ogg"
LOAD_DIALOGUE harryDialogue_08 "phase_3.5/audio/dial/CC_harry_tutorial_questscript08.ogg"
LOAD_DIALOGUE harryDialogue_09 "phase_3.5/audio/dial/CC_harry_tutorial_questscript09.ogg"
LOAD_DIALOGUE harryDialogue_10 "phase_3.5/audio/dial/CC_harry_tutorial_questscript10.ogg"
LOAD_DIALOGUE harryDialogue_11 "phase_3.5/audio/dial/CC_harry_tutorial_questscript11.ogg"
SET_MUSIC_VOLUME 0.4 activityMusic 0.5 0.7
LOCAL_CHAT_CONFIRM npc QuestScript110_1 harryDialogue_01
OBSCURE_BOOK 0
SHOW bookOpenButton
LOCAL_CHAT_CONFIRM npc QuestScript110_2 harryDialogue_02
# ARROWS_ON 0.92 -0.89 0 1.22 -0.64 90
ARROWS_ON 1.364477 -0.89 0 1.664477 -0.64 90
LOCAL_CHAT_PERSIST npc QuestScript110_3 harryDialogue_03
WAIT_EVENT "enterStickerBook"
ARROWS_OFF
SHOW_BOOK
HIDE bookPrevArrow
HIDE bookNextArrow
CLEAR_CHAT npc
WAIT 0.5
TOON_HEAD npc -0.2 -0.45 1
LOCAL_CHAT_CONFIRM npc QuestScript110_4 harryDialogue_04
ARROWS_ON 0.85 -0.75 -90 0.85 -0.75 -90
SHOW bookNextArrow
LOCAL_CHAT_PERSIST npc QuestScript110_5 harryDialogue_05
WAIT_EVENT "stickerBookPageChange-4"
HIDE bookPrevArrow
HIDE bookNextArrow
ARROWS_OFF
CLEAR_CHAT npc
WAIT 0.5
LOCAL_CHAT_CONFIRM npc QuestScript110_6 harryDialogue_06
ARROWS_ON 0.85 -0.75 -90 0.85 -0.75 -90
SHOW bookNextArrow
LOCAL_CHAT_PERSIST npc QuestScript110_7 harryDialogue_07
WAIT_EVENT "stickerBookPageChange-5"
HIDE bookNextArrow
HIDE bookPrevArrow
ARROWS_OFF
CLEAR_CHAT npc
LOCAL_CHAT_CONFIRM npc QuestScript110_8 harryDialogue_08
LOCAL_CHAT_CONFIRM npc QuestScript110_9 harryDialogue_09
LOCAL_CHAT_PERSIST npc QuestScript110_10 harryDialogue_10
ENABLE_CLOSE_BOOK
ARROWS_ON 1.364477 -0.89 0 1.664477 -0.64 90
WAIT_EVENT "exitStickerBook"
ARROWS_OFF
TOON_HEAD npc 0 0 0
HIDE_BOOK
HIDE bookOpenButton
LOCAL_CHAT_CONFIRM npc QuestScript110_11 1 harryDialogue_11
SET_MUSIC_VOLUME 0.7 activityMusic 1.0 0.4
# Lots of cleanup
UPON_TIMEOUT DEBUG "testing upon death"
UPON_TIMEOUT OBSCURE_BOOK 0
UPON_TIMEOUT ARROWS_OFF
UPON_TIMEOUT HIDE_BOOK
UPON_TIMEOUT COLOR_SCALE bookOpenButton 1 1 1 1
UPON_TIMEOUT TOON_HEAD npc 0 0 0
UPON_TIMEOUT SHOW bookOpenButton
FINISH_QUEST_MOVIE

# TUTORIAL FLIPPY

ID tutorial_blocker
LOAD_DIALOGUE blockerDialogue_01 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker01.ogg"
LOAD_DIALOGUE blockerDialogue_02 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker02.ogg"
LOAD_DIALOGUE blockerDialogue_03 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker03.ogg"
LOAD_DIALOGUE blockerDialogue_04 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker04.ogg"
LOAD_DIALOGUE blockerDialogue_05a "phase_3.5/audio/dial/CC_flippy_tutorial_blocker05.ogg"
LOAD_DIALOGUE blockerDialogue_05b "phase_3.5/audio/dial/CC_flippy_tutorial_blocker06.ogg"
LOAD_DIALOGUE blockerDialogue_06 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker07.ogg"
LOAD_DIALOGUE blockerDialogue_07 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker08.ogg"
LOAD_DIALOGUE blockerDialogue_08 "phase_3.5/audio/dial/CC_flippy_tutorial_blocker09.ogg"
HIDE localToon
REPARENTTO camera npc
FUNCTION npc "stopLookAround"
#POS camera 0.0 6.0 4.0
#HPR camera 180.0 0.0 0.0
LERP_POSHPR camera 0.0 6.0 4.0 180.0 0.0 0.0 0.5
SET_MUSIC_VOLUME 0.4 music 0.5 0.8
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_1 blockerDialogue_01
WAIT 0.8
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_2 blockerDialogue_02
WAIT 0.8
#POS camera -5.0 -9.0 6.0
#HPR camera -25.0 -10.0 0.0
LERP_POSHPR camera -5.0 -9.0 6.0 -25.0 -10.0 0.0 0.5
POS localToon 203.8 18.64 -0.475
HPR localToon -90.0 0.0 0.0
SHOW localToon
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_3 blockerDialogue_03
OBSCURE_CHAT 1 0 0
SHOW chatScButton
WAIT 0.6
ARROWS_ON -1.3644 0.91 180 -1.5644 0.74 -90
LOCAL_CHAT_PERSIST npc QuestScriptTutorialBlocker_4 blockerDialogue_04
WAIT_EVENT "enterSpeedChat"
ARROWS_OFF
BLACK_CAT_LISTEN 1
WAIT_EVENT "SCChatEvent"
BLACK_CAT_LISTEN 0
WAIT 0.5
CLEAR_CHAT localToon
REPARENTTO camera localToon
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_5 "CFSpeech" blockerDialogue_05a blockerDialogue_05b
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_6 "CFSpeech" blockerDialogue_06
OBSCURE_CHAT 0 0 0
SHOW chatNormalButton
WAIT 0.6
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_7 "CFSpeech" blockerDialogue_07
LOCAL_CHAT_CONFIRM npc QuestScriptTutorialBlocker_8 1 "CFSpeech" blockerDialogue_08
SET_MUSIC_VOLUME 0.8 music 1.0 0.4
LOOP_ANIM npc "walk"
LERP_HPR npc 270 0 0 0.5
WAIT 0.5
LOOP_ANIM npc "run"
LERP_POS npc 217.4 18.81 -0.475 0.75
LERP_HPR npc 240 0 0 0.75
WAIT 0.75
LERP_POS npc 222.4 15.0 -0.475 0.35
LERP_HPR npc 180 0 0 0.35
WAIT 0.35
LERP_POS npc 222.4 5.0 -0.475 0.75
WAIT 0.75
REPARENTTO npc hidden
FREE_LOCALTOON
UPON_TIMEOUT ARROWS_OFF
UPON_TIMEOUT OBSCURE_CHAT 0 0 0
UPON_TIMEOUT REPARENTTO camera localToon
FINISH_QUEST_MOVIE

ID quest_incomplete_120
CHAT_CONFIRM npc QuestScript120_1
# ANIM
CHAT_CONFIRM npc QuestScript120_2 1
FINISH_QUEST_MOVIE

ID quest_assign_121
CHAT_CONFIRM npc QuestScript121_1 1
FINISH_QUEST_MOVIE

ID quest_assign_130
CHAT_CONFIRM npc QuestScript130_1 1
FINISH_QUEST_MOVIE

ID quest_assign_131
CHAT_CONFIRM npc QuestScript131_1 1
FINISH_QUEST_MOVIE

ID quest_assign_140
CHAT_CONFIRM npc QuestScript140_1 1
FINISH_QUEST_MOVIE

ID quest_assign_141
CHAT_CONFIRM npc QuestScript141_1 1
FINISH_QUEST_MOVIE

# TUTORIAL COG

ID quest_incomplete_145
CHAT_CONFIRM npc QuestScript145_1 1
LOAD frame "phase_4/models/gui/tfa_images" "FrameBlankA"
LOAD tunnel "phase_4/models/gui/tfa_images" "tunnelSignA"
POSHPRSCALE tunnel 0 0 0 0 0 0 0.8 0.8 0.8
REPARENTTO tunnel frame
POSHPRSCALE frame 0 0 0 0 0 0 0.1 0.1 0.1
REPARENTTO frame aspect2d
LERP_SCALE frame 1.0 1.0 1.0 1.0
WAIT 3.0
LERP_SCALE frame 0.1 0.1 0.1 0.5
WAIT 0.5
REPARENTTO frame hidden
CHAT_CONFIRM npc QuestScript145_2 1
UPON_TIMEOUT FUNCTION frame "removeNode"
FINISH_QUEST_MOVIE

# TUTORIAL FRIENDS

ID quest_incomplete_150
CHAT_CONFIRM npc QuestScript150_1
ARROWS_ON  1.65 0.51 -120 1.65 0.51 -120
SHOW_FRIENDS_LIST
CHAT_CONFIRM npc QuestScript150_2
ARROWS_OFF
HIDE_FRIENDS_LIST
CHAT_CONFIRM npc QuestScript150_3
HIDE bFriendsList
CHAT_CONFIRM npc QuestScript150_4 1
UPON_TIMEOUT HIDE_FRIENDS_LIST
UPON_TIMEOUT ARROWS_OFF
FINISH_QUEST_MOVIE

# First Task: Assign Visit to Jester Chester
ID quest_assign_600
PLAY_ANIM npc "wave" 1
CHAT npc QuestScript600_1
LOAD_IMAGE logo "phase_3/maps/toontown-logo.png"
REPARENTTO logo aspect2d
POSHPRSCALE logo -0.4 7 0 0 0 0 0 0 0
LERP_SCALE logo 0.4 0.2 0.2 0.5
WAIT 2.5
LOOP_ANIM npc "neutral"
LERP_SCALE logo 0 0 0 0.5
WAIT 0.5
FUNCTION logo "destroy"
CLEAR_CHAT npc
CHAT_CONFIRM npc QuestScript600_2
CHAT_CONFIRM npc QuestScript600_3
CHAT_CONFIRM npc QuestScript600_4
CHAT_CONFIRM npc QuestScript600_5
PLAY_ANIM npc "wave" 1
CHAT_CONFIRM npc QuestScript600_6
LOOP_ANIM npc "neutral"
FINISH_QUEST_MOVIE

# Loopys Balls
ID quest_assign_10301
POSE_ANIM npc "wave" 20
CHAT_CONFIRM npc QuestScript10301_1
POSE_ANIM npc "neutral" 1
CHAT_CONFIRM npc QuestScript10301_2
POSE_ANIM npc "shrug" 25
CHAT_CONFIRM npc QuestScript10301_3
POSE_ANIM npc "think" 40
CHAT_CONFIRM npc QuestScript10301_4
POSE_ANIM npc "conked" 20
CHAT_CONFIRM npc QuestScript10301_5
POSE_ANIM npc "shrug" 25
CHAT_CONFIRM npc QuestScript10301_6
POSE_ANIM npc "think" 40
CHAT_CONFIRM npc QuestScript10301_7
POSE_ANIM npc "shrug" 25
CHAT_CONFIRM npc QuestScript10301_8
LOOP_ANIM npc "neutral"
FINISH_QUEST_MOVIE

# Loopys Balls
ID quest_incomplete_10301
POSE_ANIM npc "wave" 20
CHAT_CONFIRM npc QuestScript10301_1
POSE_ANIM npc "neutral" 1
CHAT_CONFIRM npc QuestScript10301_2
POSE_ANIM npc "shrug" 25
CHAT_CONFIRM npc QuestScript10301_3
POSE_ANIM npc "think" 40
CHAT_CONFIRM npc QuestScript10301_4
POSE_ANIM npc "conked" 20
CHAT_CONFIRM npc QuestScript10301_5
POSE_ANIM npc "shrug" 25
CHAT_CONFIRM npc QuestScript10301_6
POSE_ANIM npc "think" 40
CHAT_CONFIRM npc QuestScript10301_7
POSE_ANIM npc "shrug" 25
CHAT_CONFIRM npc QuestScript10301_8
LOOP_ANIM npc "neutral"
FINISH_QUEST_MOVIE
'''
