from toontown.toonbase.TTLocalizerEnglishProperty import *
from toontown.catalog import CatalogAccessoryItemGlobals
from otp.otpbase import OTPLocalizer as OL
OL.SpeedChatStaticText = OL.SpeedChatStaticTextToontown.copy()
for key in OL.SpeedChatStaticTextCommon.iterkeys():
    OL.SpeedChatStaticText[key] = OL.SpeedChatStaticTextCommon[key]

commitmantst = 'kptmptest - removable'
InterfaceFont = 'phase_3/models/fonts/ImpressBT.ttf'
ToonFont = 'phase_3/models/fonts/ImpressBT.ttf'
SuitFont = 'phase_3/models/fonts/vtRemingtonPortable.ttf'
SignFont = 'phase_3/models/fonts/MickeyFont'
MinnieFont = 'phase_3/models/fonts/MinnieFont'
FancyFont = 'phase_3/models/fonts/Comedy'
BuildingNametagFont = 'phase_3/models/fonts/MickeyFont'
BuildingNametagShadow = None
NametagFonts = (
    'phase_3/models/fonts/ImpressBT.ttf',
    'phase_3/models/fonts/AnimGothic.bam',
    'phase_3/models/fonts/Aftershock.bam',
    'phase_3/models/fonts/JiggeryPokery.bam',
    'phase_3/models/fonts/Ironwork.bam',
    'phase_3/models/fonts/HastyPudding.bam',
    'phase_3/models/fonts/Comedy.bam',
    'phase_3/models/fonts/Humanist.bam',
    'phase_3/models/fonts/Portago.bam',
    'phase_3/models/fonts/Musicals.bam',
    'phase_3/models/fonts/Scurlock.bam',
    'phase_3/models/fonts/Danger.bam',
    'phase_3/models/fonts/Alie.bam',
    'phase_3/models/fonts/OysterBar.bam',
    'phase_3/models/fonts/RedDogSaloon.bam'
)
NametagFontNames = (
    'Basic',
    'Plain',
    'Shivering',
    'Wonky',
    'Fancy',
    'Silly',
    'Zany',
    'Practical',
    'Nautical',
    'Whimsical',
    'Spooky',
    'Action',
    'Poetic',
    'Boardwalk',
    'Western'
)
NametagLabel = ' Nametag'
UnpaidNameTag = 'Basic'
ScreenshotPath = 'screenshots/'
GM_NAMES = ('TOON COUNCIL',
 'TOON TROOPER',
 'RESISTANCE RANGER',
 'GC')
ProductPrefix = 'TTPA'
Mickey = 'Mickey'
VampireMickey = 'VampireMickey'
Minnie = 'Minnie'
WitchMinnie = 'WitchMinnie'
Donald = 'Donald'
DonaldDock = 'DonaldDock'
FrankenDonald = 'FrankenDonald'
Daisy = 'Daisy'
SockHopDaisy = 'SockHopDaisy'
Goofy = 'Goofy'
SuperGoofy = 'SuperGoofy'
Pluto = 'Pluto'
WesternPluto = 'WesternPluto'
Flippy = 'Flippy'
Chip = 'Chip'
Dale = 'Dale'
JailbirdDale = 'JailbirdDale'
PoliceChip = 'PoliceChip'
lTheBrrrgh = 'The Brrrgh'
lDaisyGardens = 'Daisy Gardens'
lDonaldsDock = "Donald's Dock"
lDonaldsDreamland = "Donald's Dreamland"
lMinniesMelodyland = "Minnie's Melodyland"
lToontownCentral = 'Toontown Central'
lFunnyFarm = 'Funny Farms'
lToonHQ = 'Toon HQ'
lSellbotHQ = 'Sellbot HQ'
lGoofySpeedway = 'Goofy Speedway'
lOutdoorZone = 'Acorn Acres'
lGolfZone = 'Acorn Acres Minigames'
lPartyHood = 'Party Grounds'
GlobalStreetNames = {15000: ('to', 'on', 'Tutorial Terrace'),
 1000: ('to the', 'in the', 'Playground'),
 1100: ('to', 'on', 'Barnacle Boulevard'),
 1200: ('to', 'on', 'Seaweed Street'),
 1300: ('to', 'on', 'Lighthouse Lane'),
 1400: ('to', 'on', 'Ahoy Avenue'),
 2000: ('to the', 'in the', 'Playground'),
 2100: ('to', 'on', 'Silly Street'),
 2200: ('to', 'on', 'Loopy Lane'),
 2300: ('to', 'on', 'Punchline Place'),
 2400: ('to', 'on', 'Wacky Way'),
 3000: ('to the', 'in the', 'Playground'),
 3100: ('to', 'on', 'Walrus Way'),
 3200: ('to', 'on', 'Sleet Street'),
 3300: ('to', 'on', 'Polar Place'),
 3400: ('to', 'on', 'Arctic Avenue'),
 4000: ('to the', 'in the', 'Playground'),
 4100: ('to', 'on', 'Alto Avenue'),
 4200: ('to', 'on', 'Baritone Boulevard'),
 4300: ('to', 'on', 'Tenor Terrace'),
 4400: ('to', 'on', 'Soprano Street'),
 5000: ('to the', 'in the', 'Playground'),
 5100: ('to', 'on', 'Petunia Place'),
 5200: ('to', 'on', 'Daisy Drive'),
 5300: ('to', 'on', 'Tulip Terrace'),
 5400: ('to', 'on', 'Sunflower Street'),
 6000: ('to the', 'in the', 'Playground'),
 6100: ('to', 'on', 'Acorn Avenue'),
 6200: ('to', 'on', 'Peanut Place'),
 6300: ('to', 'on', 'Walnut Way'),
 6400: ('to', 'on', 'Legume Lane'),
 9000: ('to the', 'in the', 'Playground'),
 9100: ('to', 'on', 'Lullaby Lane'),
 9200: ('to', 'on', 'Pajama Place'),
 9300: ('to', 'on', 'Twilight Terrace'),
 10000: ('to', 'in', 'Bossbot HQ Country Club'),
 10100: ('to the', 'in the', 'Bossbot HQ Lobby'),
 10200: ('to the', 'in the', 'The Clubhouse'),
 10500: ('to the', 'in the', 'The Front Three'),
 10600: ('to the', 'in the', 'The Middle Six'),
 10700: ('to the', 'in the', 'The Back Nine'),
 11000: ('to the', 'in the', 'Sellbot HQ Courtyard'),
 11100: ('to the', 'in the', 'Sellbot HQ Lobby'),
 11200: ('to the', 'in the', 'Sellbot HQ Factory Exterior'),
 11500: ('to the', 'in the', 'Sellbot Factory'),
 12000: ('to', 'in', 'Cashbot Train Yard'),
 12100: ('to the', 'in the', 'Cashbot HQ Lobby'),
 12500: ('to the', 'in the', 'Cashbot Coin Mint'),
 12600: ('to the', 'in the', 'Cashbot Dollar Mint'),
 12700: ('to the', 'in the', 'Cashbot Bullion Mint'),
 13000: ('to', 'in', 'Lawbot HQ Courtyard'),
 13100: ('to the', 'in the', 'Courthouse Lobby'),
 13200: ('to the', 'in the', "DA's Office Lobby"),
 13300: ('to the', 'in the', 'Lawbot A Office'),
 13400: ('to the', 'in the', 'Lawbot B Office'),
 13500: ('to the', 'in the', 'Lawbot C Office'),
 13600: ('to the', 'in the', 'Lawbot D Office'),
 19000: ('to the', 'in the', 'Boardbot HQ Courtyard'),
 19100: ('to the', 'in the', 'Boardroom Lobby'),
 19200: ('to the', 'in the', 'Board Office Lobby'),
 19500: ('to the', 'in the', 'Board Office A'),
 19600: ('to the', 'in the', 'Board Office B'),
 19700: ('to the', 'in the', 'Board Office C'),
 20000: ('to the', 'in the', 'Playground')}
DonaldsDock = ('to', 'in', lDonaldsDock)
ToontownCentral = ('to', 'in', lToontownCentral)
ToontownCentralOld = ('to', 'in', 'Toontown Central\n(September 19, 2013)')
TheBrrrgh = ('to', 'in', lTheBrrrgh)
MinniesMelodyland = ('to', 'in', lMinniesMelodyland)
DaisyGardens = ('to', 'in', lDaisyGardens)
OutdoorZone = ('to', 'in', lOutdoorZone)
FunnyFarm = ('to', 'in', lFunnyFarm)
GoofySpeedway = ('to', 'in', lGoofySpeedway)
DonaldsDreamland = ('to', 'in', lDonaldsDreamland)
BossbotHQ = ('to', 'in', 'Bossbot HQ')
SellbotHQ = ('to', 'in', 'Sellbot HQ')
CashbotHQ = ('to', 'in', 'Cashbot HQ')
LawbotHQ = ('to', 'in', 'Lawbot HQ')
BoardbotHQ = ('to', 'in', 'Under Construction')
Tutorial = ('to the', 'in the', 'Toon-torial')
MyEstate = ('to', 'in', 'your house')
WelcomeValley = ('to', 'in', 'Welcome Valley')
GolfZone = ('to', 'in', lGolfZone)
PartyHood = ('to the', 'in the', lPartyHood)
Factory = 'Factory'
Headquarters = 'Headquarters'
SellbotFrontEntrance = 'Front Entrance'
SellbotSideEntrance = 'Side Entrance'
Office = 'Office'
FactoryNames = {0: 'Factory Mockup',
 11500: 'Sellbot Cog Factory',
 13300: 'Lawbot Cog Office'}
FactoryTypeLeg = 'Leg'
FactoryTypeArm = 'Arm'
FactoryTypeTorso = 'Torso'
MintFloorTitle = 'Floor %s'
CGCFloorTitle = 'Hole %s'
lCancel = 'Cancel'
lClose = 'Close'
lOK = 'OK'
lNext = 'Next'
lQuit = 'Quit'
lYes = 'Yes'
lNo = 'No'
SleepAutoReply = '%s is sleeping right now.'
lHQOfficerF = 'HQ Officer'
lHQOfficerM = 'HQ Officer'
MickeyMouse = 'please tell me if this is used it shouldnt be'
AIStartDefaultDistrict = 'Sillyville'
Cog = 'Cog'
Cogs = 'Cogs'
ACog = 'a Cog'
TheCogs = 'The Cogs'
ASkeleton = 'a Skelecog'
Skeleton = 'Skelecog'
SkeletonP = 'Skelecogs'
Av2Cog = 'a Version 2.0 Cog'
v2Cog = 'Version 2.0 Cog'
v2CogP = 'Version 2.0 Cogs'
ASkeleton = 'a Skelecog'
Foreman = 'Factory Foreman'
ForemanP = 'Factory Foremen'
AForeman = 'a Factory Foreman'
CogVP = Cog + ' VP'
CogVPs = "Cog VPs"
ACogVP = ACog + ' VP'
Supervisor = 'Mint Supervisor'
SupervisorP = 'Mint Supervisors'
ASupervisor = 'a Mint Supervisor'
President = 'Club President'
PresidentP = 'Club Presidents'
APresident = 'a Club President'
Clerk = 'Clerk'
ClerkP = 'Clerks'
AClerk = 'a Clerk'
BoardExecutive = 'Executive Board Member'
BoardExecutiveP = 'Executive Board Members'
ABoardExecutive = 'a Executive Board Member'
CogCFO = Cog + ' C.F.O.'
CogCFOs = "Cog C.F.O.'s"
ACogCFO = ACog + ' C.F.O.'
CogCJ = Cog + ' CJ'
CogCJs = "Cog CJs"
ACogCJ = ACog + ' CJ'
CogCEO = Cog + ' CEO.'
CogCEOs = "Cog CEOs"
ACogCEO = ACog + ' CEO'
TheFish = 'the Fish'
AFish = 'a fish'
Level = 'Level'
ExpBarLevel = 'Level '
ExpGagReward = 'Congratulations on reaching level %s! You can now carry 10 additional gags!'
ExpTPReward = 'Congratulations on reaching level %s! You have gained a training point!'
ExpMoneyReward = 'Congratulations on reaching level %s! You can now carry 500 additional jellybeans!'
QuestsCompleteString = 'Complete'
QuestsNotChosenString = 'Not chosen'
Period = '.'
Laff = 'Laff'
QuestInLocationString = ' %(inPhrase)s %(location)s'
QuestsDefaultGreeting = ('Hello, _avName_!',
 'Hi, _avName_!',
 'Hey there, _avName_!',
 'Say there, _avName_!',
 'Welcome, _avName_!',
 'Howdy, _avName_!',
 'How are you, _avName_?',
 'Greetings _avName_!')
QuestsDefaultIncomplete = ("How's that task coming, _avName_?",
 'Looks like you still have more work to do on that task!',
 'Keep up the good work, _avName_!',
 'Keep trying to finish that task.  I know you can do it!',
 'Keep trying to complete that task, we are counting on you!',
 'Keep working on that ToonTask!')
QuestsDefaultIncompleteProgress = ('You came to the right place, but you need to finish your ToonTask first.', 'When you are finished with that ToonTask, come back here.', 'Come back when you are finished with your ToonTask.')
QuestsDefaultIncompleteWrongNPC = ('Nice work on that ToonTask. You should go visit _toNpcName_._where_', 'Looks like you are ready to finish your ToonTask. Go see _toNpcName_._where_.', 'Go see _toNpcName_ to finish your ToonTask._where_')
QuestsDefaultComplete = ('Nice work! Here is your reward...', 'Great job, _avName_! Take this reward...', 'Wonderful job, _avName_! Here is your reward...')
QuestsDefaultLeaving = ('Bye!',
 'Goodbye!',
 'So long, _avName_.',
 'See ya, _avName_!',
 'Good luck!',
 'Have fun in Toontown!',
 'See you later!')
QuestsDefaultReject = ('Heya, _avName_!',
 'Whatcha need?',
 'Hello! How are you doing?',
 'Hi there.',
 "How's it going?",
 "Sorry _avName_, I'm a bit busy right now.",
 'Yes?',
 'Howdy, _avName_!',
 'Welcome, _avName_!',
 "Hey, _avName_! How's it hanging?",
 "Need any help?",
 "Hi _avName_, what brings you here?")
QuestsDefaultTierNotDone = ('Hello, _avName_! You must finish your current ToonTasks before getting a new one.', 'Hi there! You need to finish the ToonTasks you are working on in order to get a new one.', 'Hi, _avName_! Before I can give you a new ToonTask, you need to finish the ones you have.')
QuestsDefaultQuest = None
QuestsDefaultVisitQuestDialog = ('I heard _toNpcName_ is looking for you._where_',
 'Stop by and see _toNpcName_ when you get a chance._where_',
 'Pay a visit to _toNpcName_ next time you are over that way._where_',
 'If you get a chance, stop in and say hi to _toNpcName_._where_',
 '_toNpcName_ will give you your next ToonTask._where_')
QuestsLocationArticle = ''

def getLocalNum(num):
    return str(num)


QuestsItemNameAndNum = '%(num)s %(name)s'
QuestsCogQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsExpQuestProgress = '%(progress)s of %(numExp)s collected'
QuestsCogQuestHeadline = 'WANTED'
QuestsCogQuestSCStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsCogQuestSCStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsEliteCogQuestSCStringS = 'I need to defeat %(cogName)s%(cogLoc)s.'
QuestsEliteCogQuestSCStringP = 'I need to defeat some %(cogName)s%(cogLoc)s.'
QuestsExpQuestHeadline = 'COLLECT'
QuestsExpQuestSCStringS = 'I need to collect %(experience)s %(track)s point.'
QuestsExpQuestSCStringP = 'I need to collect %(experience)s %(track)s points.'
QuestsExpQuestCollect = 'Collect %(experience)s %(track)s points'
QuestsExpQuestCollectDesc = '%(experience)s %(track)s points'
QuestsCogQuestDefeat = 'Defeat %s'
QuestsCogQuestDefeatDesc = '%(numCogs)s %(cogName)s'
QuestsEliteCogQuestDefeat = 'Defeat %s'
QuestsEliteCogQuestDefeatDesc = '%(numCogs)s Elite %(cogName)s'
QuestsCogNewNewbieQuestObjective = 'Help a new Toon defeat %s'
QuestsCogNewNewbieQuestCaption = 'Help a new Toon %d Laff or less'
QuestsCogOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less defeat %(objective)s'
QuestsCogOldNewbieQuestCaption = 'Help a Toon %d Laff or less'
QuestsCogNewbieQuestAux = 'Defeat:'
QuestsNewbieQuestHeadline = 'APPRENTICE'
QuestsCogTrackQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogTrackQuestHeadline = 'WANTED'
QuestsCogTrackQuestSCStringS = 'I need to defeat %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestSCStringP = 'I need to defeat some %(cogText)s%(cogLoc)s.'
QuestsCogTrackQuestDefeat = 'Defeat %s'
QuestsCogTrackDefeatDesc = '%(numCogs)s %(trackName)s'
QuestsCogLevelQuestProgress = '%(progress)s of %(numCogs)s defeated'
QuestsCogLevelQuestHeadline = 'WANTED'
QuestsCogLevelQuestDefeat = 'Defeat %s'
QuestsCogLevelQuestDesc = 'a Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescC = '%(count)s Level %(level)s+ %(name)s'
QuestsCogLevelQuestDescI = 'some Level %(level)s+ %(name)s'
QuestsCogLevelQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestFloorNumbers = ('',
 'two+',
 'three+',
 'four+',
 'five+',
 'six+')
QuestsBuildingQuestBuilding = 'Building'
QuestsBuildingQuestBuildings = 'Buildings'
QuestsBuildingQuestHeadline = 'DEFEAT'
QuestsBuildingQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsBuildingQuestString = 'Defeat %s'
QuestsBuildingQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsBuildingQuestDesc = 'a %(type)s Building'
QuestsBuildingQuestDescF = 'a %(floors)s story %(type)s Building'
QuestsBuildingQuestDescC = '%(count)s %(type)s Buildings'
QuestsBuildingQuestDescCF = '%(count)s %(floors)s story %(type)s Buildings'
QuestsBuildingQuestDescI = 'some %(type)s Buildings'
QuestsBuildingQuestDescIF = 'some %(floors)s story %(type)s Buildings'
QuestsCogdoQuestCogdo = 'Field Office'
QuestsCogdoQuestCogdos = 'Field Offices'
QuestsCogdoQuestHeadline = 'DEFEAT'
QuestsCogdoQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsCogdoQuestString = 'Defeat %s'
QuestsCogdoQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsCogdoQuestDesc = 'a %(type)s Field Office'
QuestsCogdoQuestDescC = '%(count)s %(type)s Field Offices'
QuestsCogdoQuestDescI = 'some %(type)s Field Offices'
QuestFactoryQuestFactory = 'Factory'
QuestsFactoryQuestFactories = 'Factories'
QuestsFactoryQuestHeadline = 'DEFEAT'
QuestsFactoryQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsFactoryQuestString = 'Defeat %s'
QuestsFactoryQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsFactoryQuestDesc = 'a %(type)s Factory'
QuestsFactoryQuestDescC = '%(count)s %(type)s Factories'
QuestsFactoryQuestDescI = 'some %(type)s Factories'
QuestMintQuestMint = 'Mint'
QuestsMintQuestMints = 'Mints'
QuestsMintQuestHeadline = 'DEFEAT'
QuestsMintQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsMintQuestString = 'Defeat %s'
QuestsMintQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsMintQuestDesc = 'a Cog Mint'
QuestsMintQuestDescC = '%(count)s Cog Mints'
QuestsMintQuestDescI = 'some Cog Mints'
QuestStageQuestStage = 'District Attorney Office'
QuestsStageQuestStages = 'District Attorney Offices'
QuestsStageQuestHeadline = 'INFILTRATE'
QuestsStageQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsStageQuestString = 'Defeat %s'
QuestsStageQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsStageQuestDesc = 'a District Attorney Office'
QuestsStageQuestDescC = '%(count)s District Attorney Offices'
QuestsStageQuestDescI = 'some District Attorney Offices'
QuestClubQuestClub = 'Club'
QuestsClubQuestClubs = 'Cog Golf Courses'
QuestsClubQuestHeadline = 'INFILTRATE'
QuestsClubQuestProgressString = '%(progress)s of %(num)s defeated'
QuestsClubQuestString = 'Defeat %s'
QuestsClubQuestSCString = 'I need to defeat %(objective)s%(location)s.'
QuestsClubQuestDesc = 'a Cog Golf Course'
QuestsClubQuestDescC = '%(count)s Cog Golf Courses'
QuestsClubQuestDescI = 'some Cog Golf Courses'
QuestsRescueQuestProgress = '%(progress)s of %(numToons)s rescued'
QuestsRescueQuestHeadline = 'RESCUE'
QuestsRescueQuestSCStringS = 'I need to rescue a Toon%(toonLoc)s.'
QuestsRescueQuestSCStringP = 'I need to rescue some Toons%(toonLoc)s.'
QuestsRescueQuestRescue = 'Rescue %s'
QuestsRescueQuestRescueDesc = '%(numToons)s Toons'
QuestsRescueQuestToonS = 'a Toon'
QuestsRescueQuestToonP = 'Toons'
QuestsRescueQuestAux = 'Rescue:'
QuestsRescueNewNewbieQuestObjective = 'Help a new Toon rescue %s'
QuestsRescueOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less rescue %(objective)s'
QuestCogPartQuestCogPart = 'Cog Suit Part'
QuestsCogPartQuestFactories = 'Factories'
QuestsCogPartQuestHeadline = 'RETRIEVE'
QuestsCogPartQuestProgressString = '%(progress)s of %(num)s retrieved'
QuestsCogPartQuestString = 'Retrieve %s'
QuestsCogPartQuestSCString = 'I need to retrieve %(objective)s%(location)s.'
QuestsCogPartQuestAux = 'Retrieve:'
QuestsCogPartQuestDesc = 'a Cog Suit Part'
QuestsCogPartQuestDescC = '%(count)s Cog Suit Parts'
QuestsCogPartQuestDescI = 'some Cog Suit Parts'
QuestsCogPartNewNewbieQuestObjective = 'Help a new Toon retrieve %s'
QuestsCogPartOldNewbieQuestObjective = 'Help a Toon with %(laffPoints)d Laff or less retrieve %(objective)s'
QuestsDeliverGagQuestProgress = '%(progress)s of %(numGags)s delivered'
QuestsDeliverGagQuestHeadline = 'DELIVER'
QuestsDeliverGagQuestToSCStringS = 'I need to deliver %(gagName)s.'
QuestsDeliverGagQuestToSCStringP = 'I need to deliver some %(gagName)s.'
QuestsDeliverGagQuestSCString = 'I need to make a delivery.'
QuestsDeliverGagQuestString = 'Deliver %s'
QuestsDeliverGagQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsDeliverGagQuestInstructions = 'You can buy this gag in the Gag Shop once you earn access to it.'
QuestsDeliverItemQuestProgress = ''
QuestsDeliverItemQuestHeadline = 'DELIVER'
QuestsDeliverItemQuestSCString = 'I need to deliver %(article)s%(itemName)s.'
QuestsDeliverItemQuestString = 'Deliver %s'
QuestsDeliverItemQuestStringLong = 'Deliver %s to _toNpcName_.'
QuestsVisitQuestProgress = ''
QuestsVisitQuestHeadline = 'VISIT'
QuestsVisitQuestStringShort = 'Visit'
QuestsVisitQuestStringLong = 'Visit _toNpcName_'
QuestsVisitQuestSeeSCString = 'I need to see %s.'
QuestsRecoverItemQuestProgress = '%(progress)s of %(numItems)s recovered'
QuestsRecoverItemQuestHeadline = 'RECOVER'
QuestsRecoverItemQuestSeeHQSCString = 'I need to see an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToHQSCString = 'I need to return %s to an ' + lHQOfficerM + '.'
QuestsRecoverItemQuestReturnToSCString = 'I need to return %(item)s to %(npcName)s.'
QuestsRecoverItemQuestGoToHQSCString = 'I need to go to a Toon HQ.'
QuestsRecoverItemQuestGoToPlaygroundSCString = 'I need to go to %s Playground.'
QuestsRecoverItemQuestGoToStreetSCString = 'I need to go %(to)s %(street)s in %(hood)s.'
QuestsRecoverItemQuestVisitBuildingSCString = 'I need to visit %s%s.'
QuestsRecoverItemQuestWhereIsBuildingSCString = 'Where is %s%s?'
QuestsRecoverItemQuestRecoverFromSCString = 'I need to recover %(item)s from %(holder)s%(loc)s.'
QuestsRecoverItemQuestString = 'Recover %(item)s from %(holder)s'
QuestsRecoverItemQuestHolderString = '%(level)s %(holder)d+ %(cogs)s'
QuestsTrackChoiceQuestHeadline = 'CHOOSE'
QuestsTrackChoiceQuestSCString = 'I need to choose a gag track.'
QuestsTrackChoiceQuestMaybeSCString = 'Maybe I should choose %s.'
QuestsTrackChoiceQuestString = 'Choose a gag track.'
QuestsFriendQuestHeadline = 'FRIEND'
QuestsFriendQuestSCString = 'I need to make a friend.'
QuestsFriendQuestString = 'Make a friend'
QuestsMailboxQuestHeadline = 'MAIL'
QuestsMailboxQuestSCString = 'I need to check my mail.'
QuestsMailboxQuestString = 'Check your mail'
QuestsPhoneQuestHeadline = 'CLARABELLE'
QuestsPhoneQuestSCString = 'I need to call Clarabelle.'
QuestsPhoneQuestString = 'Call Clarabelle'
QuestsFriendNewbieQuestString = 'Make %d friends %d laff or less'
QuestsFriendNewbieQuestProgress = '%(progress)s of %(numFriends)s made'
QuestsFriendNewbieQuestObjective = 'Make friends with %d new Toons'
QuestsTrolleyQuestHeadline = 'TROLLEY'
QuestsTrolleyQuestSCString = 'I need to ride the trolley.'
QuestsTrolleyQuestString = 'Ride on the trolley'
QuestsTrolleyQuestStringShort = 'Ride the trolley'
QuestsMinigameNewbieQuestString = '%d Minigames'
QuestsMinigameNewbieQuestProgress = '%(progress)s of %(numMinigames)s Played'
QuestsMinigameNewbieQuestObjective = 'Play %d minigames with new Toons'
QuestsMinigameNewbieQuestSCString = 'I need to play minigames with new Toons.'
QuestsMinigameNewbieQuestCaption = 'Help a new Toon %d laff or less'
QuestsMinigameNewbieQuestAux = 'Play:'
QuestsMaxHpReward = 'Your Laff limit has been increased by %s.'
QuestsMaxHpRewardPoster = 'Reward: %s point Laff boost'
QuestsMoneyRewardSingular = 'You get 1 Jellybean.'
QuestsMoneyRewardPlural = 'You get %s Jellybeans.'
QuestsMoneyRewardPosterSingular = 'Reward: 1 Jellybean'
QuestsMoneyRewardPosterPlural = 'Reward: %s Jellybeans'
QuestsMaxMoneyRewardSingular = 'You can now carry 1 more Jellybean.'
QuestsMaxMoneyRewardPlural = 'You can now carry %s more Jellybeans.'
QuestsMaxMoneyRewardPosterSingular = 'Reward: Carry 1 Jellybean'
QuestsMaxMoneyRewardPosterPlural = 'Reward: Carry %s Jellybeans'
QuestsMaxGagCarryReward = 'Your can now carry %s more gags.'
QuestsMaxGagCarryRewardPoster = 'Reward: +%s Gag Capacity'
QuestsMaxQuestCarryReward = 'You can now have %s ToonTasks.'
QuestsMaxQuestCarryRewardPoster = 'Reward: Carry %s ToonTasks'
QuestsTeleportReward = 'You now have teleport access to %s.'
QuestsTeleportRewardPoster = 'Reward: Teleport access to %s'
QuestsTrackTrainingReward = 'You can now train for "%s" gags.'
QuestsTrackTrainingRewardPoster = 'Reward: Gag training'
QuestsTrackProgressReward = 'You now have frame %(frameNum)s of the %(trackName)s track animation.'
QuestsTrackProgressRewardPoster = 'Reward: "%(trackName)s" track animation frame %(frameNum)s'
QuestsTrackCompleteReward = 'You may now carry and use "%s" gags.'
QuestsTrackCompleteRewardPoster = 'Reward: Final %s track training'
QuestsClothingTicketReward = 'You can change your clothes'
QuestsClothingTicketRewardPoster = 'Reward: Clothing Ticket'
TIPQuestsClothingTicketReward = 'You can change your shirt for a TIP shirt'
TIPQuestsClothingTicketRewardPoster = 'Reward: TIP Clothing Ticket'
QuestsCheesyEffectRewardPoster = 'Reward: %s'
QuestsCogSuitPartReward = 'You now have a %(cogTrack)s %(part)s Cog Suit Part.'
QuestsCogSuitPartRewardPoster = 'Reward: %(cogTrack)s %(part)s Part'
QuestsCogSuitMeritReward = 'You have earned %(numMerits)s %(meritType)s'
QuestsCogSuitMeritRewardPoster = 'Reward: %(numMerits)s %(meritType)s'
QuestsStreetLocationThisPlayground = 'in this playground'
QuestsStreetLocationThisStreet = 'on this street'
QuestsStreetLocationNamedPlayground = 'in the %s playground'
QuestsStreetLocationNamedStreet = 'on %(toStreetName)s in %(toHoodName)s'
QuestsLocationString = '%(string)s%(location)s'
QuestsLocationBuilding = "%s's building is called"
QuestsLocationBuildingVerb = 'which is'
QuestsLocationParagraph = '\x07%(building)s "%(buildingName)s"...\x07...%(buildingVerb)s %(street)s.'
QuestsGenericFinishSCString = 'I need to finish a ToonTask.'
QuestsMediumPouch = 'Medium Pouch'
QuestsLargePouch = 'Large Pouch'
QuestsSmallBag = 'Small Bag'
QuestsMediumBag = 'Medium Bag'
QuestsLargeBag = 'Large Bag'
QuestsExtraLargeBag = 'Extra Large Bag'
QuestsExtraLargeBackpack = 'Extra Large Backpack'
QuestsSmallBackpack = 'Small Backpack'
QuestsMediumBackpack = 'Medium Backpack'
QuestsLargeBackpack = 'Large Backpack'
QuestsItemDict = {1: ['Pair of Glasses', 'Pairs of Glasses', 'a '],
 2: ['Fish', 'Fish', 'a '],
 3: ['Blackboard', 'Blackboards', 'a '],
 4: ['Book', 'Books', 'a '],
 5: ['Candy Bar', 'Candy Bars', 'a '],
 6: ['Piece of Chalk', 'Pieces of Chalk', 'a '],
 7: ['Kite', 'Kites', 'a '],
 8: ['Tesla Coil', 'Tesla Coils', 'a '],
 9: ['Battery', 'Batteries', 'a '],
 10: ['Bottle of Vanishing Cream', 'Bottles of Vanishing Cream', 'a '],
 11: ['Container of Visible Ink', 'Containers of Visible Ink', 'a '],
 12: ['Octopus ink', 'Octopus inks', 'some '],
 13: ['Package', 'Package', 'a '],
 14: ['Goldfish receipt', 'Goldfish receipts', 'a '],
 15: ['Goldfish', 'Goldfish', 'a '],
 16: ['Oil', 'Oils', 'some '],
 17: ['Grease', 'Greases', 'some '],
 18: ['Water', 'Waters', 'some '],
 19: ['Gear report', 'Gear reports', 'a '],
 20: ['Blackboard Eraser', 'Blackboard Erasers', 'a '],
 21: ['Watercooler', 'Watercoolers', 'a '],
 22: ['Bottled Can', 'Bottled Cans', 'a '],
 23: ['Beret', 'Berets', 'a '],
 24: ['Top Hat', 'Top Hats', 'a '],
 25: ['Books', 'Books', 'some '],
 26: ['Needle', 'Needles', 'a '],
 27: ['Toxic Waste', 'Samples of Toxic Waste', 'some '],
 28: ['Can of Tuna', 'Cans of Tuna', 'a '],
 29: ['Passport', 'Passports', 'a '],
 30: ['Gift', 'Gifts', 'a '],
 31: ['Salt Shaker', 'Salt Shakers', 'a '],
 32: ['Goods', 'Goods', 'some '],
 33: ['Orange', 'Oranges', 'an '],
 34: ['Barrel of Jellybeans', 'Barrels of Jellybeans', 'a '],
 35: ['Camera', 'Cameras', 'a '],
 36: ['Paint Brush', 'Paint Brushes', 'a '],
 37: ['Music Note', 'Music Notes', 'a '],
 38: ['Memo From The Factory Foreman', 'Memos From The Factory Foreman', 'a '],
 39: ['Glasses', 'Pairs of Glasses', 'Dr. Ivanna Cee\'s '],
 40: ['Snow Globe', 'Snow Globes', 'a '],
 41: ['Favorite Snow Globe', 'Favorite Snow Globes', 'Shakey\'s '],
 42: ['Boarding Ticket', 'Boarding Tickets', 'a '],
 43: ['Suitcase', 'Suitcases', 'a '],
 44: ['Glasses', 'Pairs of Glasses', 'Dr. Friezeframe\'s '],
 45: ['Bowl of Soup', 'Bowls of Soup', 'a '],
 46: ['Ice Skates', 'Ice Skates', 'some '],
 47: ['Broken Steering Wheel', 'Broken Steering Wheels', 'a '],
 48: ['Repaired Steering Wheel', 'Repaired Steering Wheels', 'a '],
 49: ['Glasses', 'Pairs of Glasses', 'Dr. Blinky\'s '],
 50: ['Glasses', 'Pairs of Glasses', 'Dr. Bleary\'s '],
 51: ['Bottle', 'Bottles', 'a '],
 52: ['Donut', 'Donuts', 'a '],
 53: ['Teleportation Access Memo', 'Teleportation Access Memos', 'a '],
 54: ['Pair of Tap Dancing Shoes', 'Pairs of Tap Dancing Shoes', 'a '],
 55: ['Pillows', 'Pillows', 'some '],
 56: ['Watch', 'Watches', 'a '],
 57: ['Record', 'Records', 'a '],
 58: ['Power Generator', 'Power Generators', 'a '],
 59: ['Sellbot Suit Piece', 'Sellbot Suit Pieces', 'a '],
 60: ['Package Receipt', 'Package Receipts', 'a '],
 61: ['Toenail Clipper', 'Toenail Clippers', 'a '],
 62: ['Boxing Glove', 'Boxing Gloves', 'a '],
 63: ['Boxing Bag', 'Boxing Bags', 'a '],
 64: ['Jimmy', 'Jimmys', 'one '],
 65: ['Meatballs', 'Meatballs', 'some '],
 66: ['Rake', 'Rakes', 'a '],
 67: ['Sword', 'Swords', 'a '],
 68: ['Cash', 'Rolls of Cash', 'some '],
 110: ['TIP Clothing Ticket', 'Clothing Tickets', 'a '],
 1000: ['Clothing Ticket', 'Clothing Tickets', 'a '],
 1001: ['Dried Suit', 'Dried Suits', 'a '],
 1002: ['Signed Check', 'Signed Checks', 'a '],
 1003: ['Board', 'Boards', 'a '],
 1004: ['Lucky Hook', 'Lucky Hooks', 'a '],
 1005: ['Cloth', 'Pieces of Cloth', 'some '],
 1006: ['Sail', 'Sails', 'a '],
 1007: ['Fishing Rod', 'Fishing Rods', 'a '],
 1008: ['Fishing Hook', 'Fishing Hooks', 'a '],
 1009: ['Can of Worms', 'Cans of Worms', 'a '],
 1010: ['Fish', 'Fish', 'some '],
 1011: ['Chips', 'Bags of Chips', 'some '],
 1012: ['Taxi Keys', 'Taxi Keys', 'some '],
 1013: ['Striped Shirt', 'Striped Shirts', 'a '],
 1014: ['Hat', 'Hats', 'a '],
 1015: ['Glasses', 'Glasses', 'some '],
 1016: ['Lipstick', 'Lipsticks', 'some '],
 1017: ['Blowdryer', 'Blowdryers', 'a '],
 1018: ['Earrings', 'Pairs of Earrings', 'some '],
 1019: ['Make-Up Kit', 'Make-Up Kits', 'a '],
 1020: ['Deed to Seacastle Contractors', 'Deeds', 'a '],
 1021: ["Glasses", "Glasses", "Captain Carl's  "],
 1022: ["Glasses", "Glasses", "Rusty Ralph's "],
 1023: ["Glasses Framework", "Glasses Frameworks", "a "],
 1024: ['Metal', 'Bars of Metal', 'some '],
 1025: ['Light Bulbs', 'Light Bulbs', 'some '],
 1026: ['Glass', 'Plates of Glass', 'some '],
 2001: ['Textbook', 'Textbooks', 'a '],
 2002: ['Magnifying Glass', 'Magnifying Glasses', 'a '],
 2003: ['Lime', 'Limes', 'some '],
 2004: ['Lemon', 'Lemons', 'some '],
 2005: ['Cup', 'Cups', 'a '],
 2006: ['Gear Garnish', 'Gear Garnish', 'some '],
 2007: ['Ice Cube', 'Ice Cubes', 'an '],
 2008: ['Lemonade', 'Lemonade', 'some '],
 2009: ['Chocolate Mould', 'Chocolate Moulds', 'a '],
 2010: ['Chocolate Shavings', 'Chocolate Shavings', 'some '],
 2011: ['Sugar', 'Sugar', 'some '],
 2012: ['Recipe', 'Recipes', 'a '],
 2013: ['Wrapper', 'Wrappers', 'a '],
 2014: ['Chocolate Bar', 'Chocolate Bars', 'a '],
 2015: ['Jar of Jellybeans', 'Jars of Jellybeans', 'a '],
 2016: ['Package', 'Packages', 'a '],
 2017: ['Banana Peel', 'Banana Peels', 'a '],
 2018: ['Net', 'Nets', 'a '],
 2019: ['Saxophone', 'Saxophones', 'a '],
 2020: ['Label Sorter', 'Label Sorters', 'a '],
 2021: ['Glasses', 'Glasses', 'a pair of '],
 2022: ['Urgent Memo', 'Urgent Memos', 'an '],
 2023: ['Data Plan', 'Data Plans', 'a '],
 2024: ['Payment Plan', 'Payment Plan', 'a '],
 2025: ['Legal Agreement', 'Legal Agreements', 'a '],
 2026: ['Work Phone', 'Work Phones', 'a '],
 2027: ['Activated Phone', 'Activated Phones', 'an '],
 2028: ['Blueprint', 'Blueprints', 'a '],
 2029: ['Straightjacket', 'Straightjacket', 'a '],
 2030: ['Box of straightjackets', 'Boxes of straightjackets', 'a '],
 2031: ['Ambulance Keys', 'Ambulance Keys', 'a set of '],
 2032: ['Ambulance Tire', 'Ambulance Tires', 'an '],
 2033: ['Diesel Engine', 'Diesel Engines', 'a '],
 2034: ['Invisible Ink', 'Invisible Ink', 'a bottle of '],
 2035: ['Fountain Pen', 'Fountain Pens', 'a '],
 2036: ['Ink Sac', 'Ink Sacs', 'an '],
 4001: ["Tire", "Tires", 'a '],
 4002: ["Bologna Sandwich", "Bologna Sandwiches", 'a '],
 4003: ['Meatball Sub', 'Meatball Subs', 'a '],
 4004: ["Old Silverware", "Sets of Old Silverware", 'some '],
 4005: ["Old Clock", "Old Clocks", 'an '],
 4006: ["Old Tea Set", "Old Tea Sets", 'an '],
 4007: ["Electric Keyboard", "Electric Keyboards", 'an '],
 4008: ['Note', 'Notes', 'a '],
 4009: ['Golf Club', 'Golf Clubs', 'a '],
 4010: ['Soccer Ball', 'Soccer Balls', 'a '],
 4011: ["Cashbot HQ Plans", "Cashbot HQ Plans", 'some '],
 4012: ['Golden Delicious Salmon', 'Golden Delicious Salmons', 'a '],
 4013: ['Passport', 'Passports', 'a '],
 4014: ['Music Note', 'Music Notes', 'a '],
 4015: ['Memo', 'Memos', 'a '],
 5001: ['Bushel of Berries', 'Bushels of Berries', 'a '],
 5002: ['Cabbage', 'Cabbages', 'a '],
 5003: ['Lettuce', 'Leaves of Lettuce', 'some '],
 5004: ['Letter', 'Letters', 'a '],
 5005: ['Package', 'Packages', 'a '],
 5006: ['14-Carrot Ring', '14-Carrot Rings', 'a '],
 5007: ['14-Carrot Necklace', '14-Carrot Necklaces', 'a '],
 5008: ['Shower Head', 'Shower Heads', 'a '],
 5009: ['Flowerpot', 'Flowerpots', 'a '],
 5010: ['Marbles', 'Sets of Marbles', 'some '],
 5011: ['Seltzer Bottle', 'Seltzer Bottles', 'a '],
 5012: ['Safe', 'Safes', 'a '],
 5013: [lSellbotHQ + ' Blueprints', lSellbotHQ + ' HQ Blueprints', 'some '],
 5014: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5015: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5016: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 5017: [lSellbotHQ + ' Memo', lSellbotHQ + ' Memos', 'a '],
 3001: ['Tuxedo', 'Tuxedos', 'a '],
 3002: ['Lawbot HQ Plans', 'Lawbot HQ Plans', 'some '],
 3003: ['Lawbot HQ Blueprints', 'Lawbot HQ Blueprints', 'some '],
 3004: ['External Temperature Sensor', 'External Temperature Sensors', 'an '],
 3005: ['Temperature Readings', 'Temperature Readings', 'some '],
 3006: ['Ice cream cone', 'Ice cream cones', 'an '],
 3007: ['Ice Cube', 'Ice Cubes', 'an '],
 3008: ['Pliers', 'Pliers', 'some '],
 3009: ["Plumber's Snake", "Plumber's Snakes", 'a '],
 3010: ['Pirate Hat', 'Pirate Hats', 'a '],
 3011: ['Fedora', 'Fedoras', 'a '],
 3012: ['Mittens', 'Mittens', 'a pair of '],
 3013: ['Aviator Hats', 'Aviator Hats', 'some '],
 3014: ['Loaf of Bread', 'Loaves of Bread', 'a '],
 3015: ['Hambuger Rolls', 'Hamburger Rolls', 'some '],
 3016: ['Swiss Cheese Lump', 'Swiss Cheese Lumps', 'a '],
 3017: ['Cheddar Cheese', 'Lumps of Cheddar Cheese', 'some '],
 3018: ['Grill', 'Grills', "Chef Bumblesoup's "],
 3019: ['Solar Powered Blankets', 'Solar Powered Blankets', 'some '],
 3020: ['Sickle Probe', 'Sickle Probes', 'a '],
 3021: ['Sharp Tooth', 'Sharp Teeth', 'a '],
 3022: ['Eyepatch', 'Eyepatches', 'an '],
 3023: ['Make-Up Kit', 'Make-Up Kits', 'a '],
 3024: ['Scale', 'Scales', 'a '],
 3025: ['Shiny Beak', 'Shiny Beaks', 'a '],
 3026: ['Shiny Tooth', 'Shiny Teeth', 'a '],
 3027: ['Gold Tooth', 'Gold Teeth', 'a '],
 3028: ['Pie Chart', 'Pie Charts', 'a '],
 3029: ['Lumpy Cheese', 'Lumpy Cheeses', 'a '],
 3030: ['Big White Wig', 'Big White Wigs', 'a '],
 6001: ['Warm Blankets', 'Warm Blankets', 'some '],
 6002: ['Humidifier', 'Humidifiers', 'a '],
 6003: ['Ring', 'Rings', 'a '],
 6004: ['Insurance Card', 'Insurance Cards', 'an '],
 6005: ['Bolts', 'Bolts', 'some '],
 6006: ['Straw', 'Bits of Straw', 'some '],
 6007: ['Wood', 'Chunks of Wood', 'some '],
 6008: ['Bricks', 'Bricks', 'some '],
 6009: ['Straw, Wood, and Brick', 'Straws, Wood, Bricks', 'some '],
 6010: ['Allergy Pill', 'Allergy Pills', 'an '],
 6011: ['Shipping Bill', 'Shipping Bills', 'a '],
 6012: ['Zoot Suit', 'Zoot Suits', 'a '],
 7001: ['Plain Bed', 'Plain Beds', 'a '],
 7002: ['Fancy Bed', 'Fancy Beds', 'a '],
 7003: ['Blue Bedspread', 'Blue Bedspreads', 'a '],
 7004: ['Paisley Bedspread', 'Paisley Bedspreads', 'a '],
 7005: ['Pillows', 'Pillows', 'some '],
 7006: ['Hard Pillows', 'Hard Pillows', 'some '],
 7007: ['Pajamas', 'Pajamas', 'a pair of '],
 7008: ['Footie Pajamas', 'Footie Pajamas', 'a pair of '],
 7009: ['Puce Footie Pajamas', 'Puce Footie Pajamas', 'a pair of '],
 7010: ['Fuchsia Footie Pajamas', 'Fuchsia Footie Pajamas', 'a pair of '],
 7011: ['Cauliflower Coral', 'Cauliflower Coral', 'some '],
 7012: ['Slimy Kelp', 'Slimy Kelp', 'some '],
 7013: ['Pestle', 'Pestles', 'a '],
 7014: ['Jar of Wrinkle Cream', 'Jars of Wrinkle Cream', 'a '],
 7016: ['Toon Training Manual', 'Toon Training Manuals', 'some ']
 }
QuestsHQOfficerFillin = lHQOfficerM
QuestsHQWhereFillin = ''
QuestsHQBuildingNameFillin = lToonHQ
QuestsHQLocationNameFillin = 'in any neighborhood'
QuestsTailorFillin = 'Tailor'
QuestsTailorWhereFillin = ''
QuestsTailorBuildingNameFillin = 'Clothing Store'
QuestsTailorLocationNameFillin = 'in any neighborhood'
QuestsTailorQuestSCString = 'I need to see a Tailor.'
QuestMovieExpJbReward = 'You have earned %(exp)d experience points and %(money)d jellybeans.'
QuestMovieQuestChoiceCancel = 'Come back later if you need a ToonTask! Bye!'
QuestMovieTrackChoiceCancel = 'Come back when you are ready to decide! Bye!'
QuestMovieQuestChoice = 'Choose a ToonTask.'
QuestMovieTrackChoice = 'Ready to decide? Choose a track, or come back later.'
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
TheBrrrghTrackQuestDict = {GREETING: '',
 QUEST: 'Now you are ready.\x07Go out and walk the earth until you know which track you would like to choose.\x07Choose wisely, because this is your final track.\x07When you are certain, return to me.',
 INCOMPLETE_PROGRESS: 'Choose wisely.',
 INCOMPLETE_WRONG_NPC: 'Choose wisely.',
 COMPLETE: 'Very wise choice!',
 LEAVING: 'Good luck.  Return to me when you have mastered your new skill.'}
QuestDialog_3225 = {QUEST: "Oh, thanks for coming, _avName_!\x07The Cogs in the neighborhood frightened away my delivery person.\x07I don't have anyone to deliver this salad to _toNpcName_!\x07Can you do it for me? Thanks so much!_where_"}
QuestDialog_2910 = {QUEST: 'Back so soon?\x07Great job on those Cogs.\x07Now I need one more favor.\x07Could you get some flour from _toNpcName_ for me?\x07I\'m running really low in supply of that._where_'}
QuestDialogDict = {
 164: {QUEST: 'Phew, tired yet?\x07You know... You look like you could use some new gags.\x07Go see %s, maybe he can help you out._where_' % Flippy},
 165: {QUEST: 'Heya! I remember seeing you in the streets earlier.\x07I don\'t believe I formally introduced myself...\x07I\'m Flippy, Mayor of the Toon Council here in Toontown.\x07Hopefully we\'ll be seeing each other a lot more often!\x07It looks like you need to practice training your gags.\x07First, I want you to start by defeating 3 Cogs.'},
 166: {QUEST: 'Hey there _avName_!\x07I hear you\'re looking for some training?\x07Well I\'d be happy to help teaching you the ropes, but I let _toNpcName_ borrow my manuals!\x07Pop over to him and get them back so we can start!_where_'},
 167: {QUEST: 'Hey! You\'re the toon Flippy sent over,\x07Unfortunately I lost the manuals when some cogs took over my building!\x07I bet one of them out there still has them!\x07Go destroy some cogs until you find the Manuals!_where_', COMPLETE: 'You found them!'},
 168: {QUEST: 'Great work _avName_, now just run them back to _toNpcName_!_where_'},
 # Toontown Central Tasks
 # Task Zero
 2000: {QUEST:  "_toNpcName_ has some books that are overdue!\x07He's been studying about the silly bones in our bodies.\x07Could you go ask him to return those books?_where_"}, #Pete to Dr Tom to collect School Books (visit)
 2001: {QUEST:  "Oh no the books are already overdue?\x07Some pesky cogs stole those books before I got a chance to read them!\x07Go recover those for me please!_where_"}, #Dr Tom kill some cogs to recover School Books
 2002: {QUEST:  "Alright, let's take a look at these books...\x07Wow this font is super small!\x07Where did my magnifying glass go?\x07I bet those pesky cogs stole it!\x07Go get it back please!"}, #Dr Tom kill some cogs to recover magnifying glass
 2003: {QUEST:  "Ah much better!\x07Wait a minute...\x07This doesn't make any sense!\x07Could you go ask _toNpcName_ to decode these for me?"}, #Dr Tom visit Dr. Pulyurleg to decode the books
 2004: {QUEST:  "Alright let's take a look here...\x07Oh, this is so simple!\x07Give me second while I write this all down for him...\x07There! Done!\x07Go give these back to _toNpcName_."}, #Dr. Pulyurleg visit Dr Tom to return decoded books
 2005: {QUEST:  "This makes so much sense now!\x07Now that I have these decoded notes, go return these books for me please!", COMPLETE: "Thank you so much for doing this, _avName_!"}, #Dr Tom visit Pete to return the decoded books

 # Task One
 2010: {QUEST:  "Oh man, I'm parched!\x07Listen, _toNpcName_ told me earlier she was going to make a batch of lemonade.\x07Could you do me a favor and get a pitcher of it from her?_where_"}, #Flippy to Limeys limes (visit)
 2011: {GREETING: "Ahoy!",
		QUEST:  "Huh? You want some lemonade?\x07Well unfortunately, I was fishing earlier and dropped my ingredients in the pond.\x07Would you mind fishing those up for me?",
		LEAVING: ''}, #Limey fish to find some limes
 2012: {GREETING: '',
		QUEST:  "Yep, these were the limes I was looking for!\x07However, I forgot that I dropped the lemons in there too!\x07Could you do me a favor and get those for me?",
		LEAVING: ''}, #Limey fish to find some lemons 
 2013: {GREETING: '',
		QUEST:  "Thanks again!\x07So listen, I decided to go fishing AGAIN, and...\x07Well, I dropped the cups I had on me when I leaned to grab my catch.\x07Could you go grab those out for me?",
		LEAVING: ''}, #Limey fish to find some Acorn Cups
 2014: {QUEST:  "Thanks for getting these, I'll make sure to wash them before I use them.\x07I should really stop carrying my supplies on me when I fish, don't ya think?\x07Speaking of supplies, I need 3 glasses of water to make this with.\x07Mind going and buying those from the gag shop?",
		LEAVING: ''}, #Limey buy 3 glasses of water
 2015: {GREETING: '',
		QUEST:  "Awesome!\x07Okay, next I need three fruit pie slices, they pair great with the lemonade!",
		LEAVING: ''}, #Limey buy 3 fruit pie slices
 2016: {GREETING: '',
		QUEST:  "Yeah, these will be really tasty.\x07Now, I'm having trouble with my juicer.\x07Go and defeat a few cogs and see if you can get a Gear Garnish from them.",
		LEAVING: ''}, #Limey kill some cogs to recover a Gear Garnish
 2017: {GREETING: '',
		QUEST:  "Alright, last item, I promise.\x07I need ice cubes, which you can grab off of Cold Callers.\x07Go defeat them until you can find three.",
		LEAVING: ''}, #Recover 3 Ice Cubes fron Cold Callers
 2018: {QUEST:  "Alright, here you go!\x07Deliver this pitcher, these cups and these pies to _toNpcName_.", COMPLETE: "Thanks _avName_, this should quench my thirst just nicely.\x07I'll be sure to go thank Limey for the pies, as well.\x07Anyways, here's your reward."}, #Deliver Lemonade to Flippy in Toon Hall 
 
 # Task Two
 2020: {QUEST:  "Hey, _avName_!\x07Could you head on over to _toNpcName_ and do him several favors?\x07I heard he needs some help with his new chocolate bars._where_"}, # Flippy to Sal Snicker (visit)   
 2021: {QUEST:  "Hello! You must be _avName_.\x07Anyways, let me tell you what happened.\x07Just a few hours ago, those pesky cogs raided my building and took my supplies!\x07I found out that the Penny Pinchers have my moulds.\x07Could you get those back for me please?"}, # Kill Penny Pinchers to recover Chocolate Moulds
 2022: {QUEST:  "Yep, that's all of them!\x07Next, the Pencil Pushers should have my chocolate shavings.\x07They've mistaken my chocolate shavings for pencil shavings, how funny is that?"}, # Kill Pencil Pushers to recover Chocolate Shavings 
 2023: {QUEST:  "Alright, I'll get to work melting those into the moulds.\x07So, it looks like the Bloodsuckers have my sugar.\x07Would you mind grabbing it from them?"}, # Kill Bloodsuckers to recover Sugar
 2024: {QUEST:  "Time to add the sugar!\x07Now to see what I have to do next...\x07Uh oh!!!\x07I think the Con Artists took my recipe, they were in here right before it went missing.\x07Go defeat them until you find it."}, # Kill Con Artists to recover recipe
 2025: {QUEST:  "Awesome! Now we can get finished on this bad boy.\x07Rumor has it that the Telemarketers keep some wrappers in their rolodexes.\x07Would you be able to grab some for me?\x07Why do I need them, you ask?\x07How else would I deliver this chocolate?"}, # Kill Telemarketers to recover Wrappers
 2026: {QUEST:  "And voila! Freshly made chocolate bars!\x07I promised to give Banker Bob one, would you kindly this one to him?_where_"}, # Deliver Chocolate Bar to Banker Bob
 2027: {QUEST:  "Are these the new chocolate bars?\x07Mmm~ Thiff 'if so good!\x07 Eheh, excuse me. Please, deliver these beans to Sal for me."}, # Deliver Money to Sal Snicker
 2028: {QUEST:  "Thanks so much for making that delivery for me!\x07Now, I need a huge favor.\x07Rumor has it that the Cashbots have been planning a heist on my shop.\x07I can't let that happen!\x07Can you take down a handful of those pesky cogs for me please?"}, # Kill 10 Cashbots 
 2029: {QUEST:  "Great! Now they won't be pulling anything sneaky off!\x07I just got a call from Flippy, and he wanted to try one of my chocolate bars.\x07Please deliver this to him. He also said there would be a reward involved.", COMPLETE: "Oh this chocolate bar looks good.\x07WHOA, THIS IS BRILLIANT!!!\x07Thanks for delivering this gift of heaven to my office!\x07Here is your reward..."}, #Deliver Chocolate Bar To Flippy
 
 # Task Three
 2030: {QUEST:  "Let's get down to business, _avName_.\x07_toNpcName_ would like to inform you about the Cog departments and even about those horrid newly-built Cogs._where_"}, # Flippy to Librarian Larry (visit)
 2031: {QUEST:  "Welcome, new student!\x07Ah, so you're here for the lecture on the Cogs I see?\x07Let's discuss the difference between each department first.\x07Originally, Toontown was invaded by four types of Cogs: Sellbots, Cashbots, Lawbots, and Bossbots.\x07Sellbots are into marketing...\x07Cashbots love to handle the money...\x07Lawbots like to lay down the law...\x07And Bossbots love to boss everyone around and be in charge.\x07For now, I would like you to demonstarte your knowledge in being able to differentiate these types of Cogs.\x07Defeat 5 Sellbots and then return to me."}, # Kill 5 Sellbot  
 2032: {QUEST:  "Welcome, new student!\x07Ah, so you're here for the lecture on the Cogs I see?\x07Let's discuss the difference between each department first.\x07Originally, Toontown was invaded by four types of Cogs: Sellbots, Cashbots, Lawbots, and Bossbots.\x07Sellbots are into marketing...\x07Cashbots love to handle the money...\x07Lawbots like to lay down the law...\x07And Bossbots love to boss everyone around and be in charge.\x07For now, I would like you to demonstarte your knowledge in being able to differentiate these types of Cogs.\x07Defeat 5 Cashbots and then return to me."}, # Kill 5 Cashbot
 2033: {QUEST:  "Welcome, new student!\x07Ah, so you're here for the lecture on the Cogs I see?\x07Let's discuss the difference between each department first.\x07Originally, Toontown was invaded by four types of Cogs: Sellbots, Cashbots, Lawbots, and Bossbots.\x07Sellbots are into marketing...\x07Cashbots love to handle the money...\x07Lawbots like to lay down the law...\x07And Bossbots love to boss everyone around and be in charge.\x07For now, I would like you to demonstarte your knowledge in being able to differentiate these types of Cogs.\x07Defeat 5 Lawbots and then return to me."}, # Kill 5 Lawbot
 2034: {QUEST:  "Welcome, new student!\x07Ah, so you're here for the lecture on the Cogs I see?\x07Let's discuss the difference between each department first.\x07Originally, Toontown was invaded by four types of Cogs: Sellbots, Cashbots, Lawbots, and Bossbots.\x07Sellbots are into marketing...\x07Cashbots love to handle the money...\x07Lawbots like to lay down the law...\x07And Bossbots love to boss everyone around and be in charge.\x07For now, I would like you to demonstarte your knowledge in being able to differentiate these types of Cogs.\x07Defeat 5 Bossbots and then return to me."}, # Kill 5 Bossbot
 2035: {GREETING: '',
		QUEST: "Great work on those Cogs.\x07Now, I think I can tell you about the newly introduced Cog department: The Boardbots.\x07The Boardbots have more power than all the other Cogs and are in charge of everything that goes around Cogs Incorporated.\x07I would like you to go and defeat 5 Boardbots then return to me."},
 2036: {QUEST:  "Have any trouble with those Boardbots?\x07Now that you've seen the 5 major Cog types, its time to introduce you to the subclasses of Cogs.\x07Now, Cogs also come in different shapes and forms, depending on how they were built.\x07Right now, you'll only counter regular Cogs, and Elite Cogs.\x07Later, in more Cog inhibited areas such as HQs, you will find other special types of Cogs, such as Skelecogs, V2, Virtual Cogs, and Elite V2 Cogs.\x07Ugh, I get shivers just thinking of them!\x07Anyways, around the playgrounds, you'll notice difference in the levels of the Cogs.\x07I want you to avoid those weak level one Cogs and attempt to defeat those stronger Cogs out there."}, # Kill 5 Level 2+ Cogs
 2037: {QUEST:  "Hope that wasn't to hard. Now, I want you to defeat five Elite Cogs.\x07Elite Cogs pose a very significant risk to the happiness of our toons.\x07They are stronger, have more health, and can even dodge better than the average Cog. Oh, what a nightmare!\x07I'm only sending you on this mission, toon, because I belive you are strong enough to handle it.\x07Just be careful out there.\x07Defeat 5 Elite Cogs."}, # Kill 5 Elite Cogs
 2038: {QUEST: "How'd you do on those Elite Cogs?\x07Finally, I would like you to do something small but a little difficult.\x07I want you to take care of those high leveled Cogs, the level 4+ ones.\x07You can find them on Wacky Way and Silly Street.", COMPLETE: "Great job on all those Cogs!\x07You've passed my lesson. Congrats!"},
 
 # Task Four
 2040: {QUEST:  "Welcome back, _avName_!\x07_toNpcName_ is in need of some help.\x07Would you mind helping him deliver some packages?_where_"}, # Flippy to Postmaster Pete
 2041: {QUEST:  "Hey, nice to meet you _avName_!\x07I need your help.\x07The high leveled Cogs around here tend to steal all the packages that I need delivered.\x07Can you go get several of them back for me please?"}, # Recover 5 packages from level 3+ cogs in Toontown Central
 2042: {QUEST:  "Alright, thank you for that.\x07Would you mind delivering this one to Rancid Robert?_where_"}, # Deliver a Package to Rancid Robert
 2043: {QUEST:  "Hey, is this my package?\x07Oh, I'm sorry. I'm too down right now to sign for it...\x07Maybe you could help me?\x07See, those Boardbots storm in here and take away all my Banana Peels and I just feel like nothing without them.\x07Could you get those back for me? There were about 7 of them."}, # Recover 7 banana peels from Boardbots in Toontown Central
 2044: {QUEST:  "Thanks, but I'm still not feeling normal...\x07Maybe if you could get those nets of mine that those Bossbots stole from me..."}, # Recover 5 nets from Bossbots in Toontown Central
 2045: {GREETING: '',
		QUEST:  "Now, if only that Connoisseur would return my favorite saxophone...",
		LEAVING: ''}, # Recover a saxophone from a Connosieur
 2046: {QUEST:  "Oh I feel a lot better now!\x07Let me just sign for this package...\x07Wait a darn minute, this doesn't belong to me?\x07It belongs to _toNpcName_!!!_where_.", COMPLETE:"Awesome! That's the package I ordered.\x07Let me just sign for this and, BAM!\x07Here is a reward, kind toon..."}, # Return to Charlie Chortle, tell him the show is on

 # Task Five
 2050: {QUEST:  "Great work so far _avName_\x07Could you do me a quick favor and drop this off for _toNpcName_?\x07It got delivered here for some reason..._where_"}, # Flippy Deliver Package to Liar Liar
 2051: {QUEST:  "Yay! A new delivery...\x07Wait, this isn't for me. This is for _toNpcName_, my biggest competitor._where_"}, # Liar Liar Deliver Package to Pants On Fire
 2052: {QUEST:  "Yay! A new delivery...\x07Wait, this isn't for me. This is for _toNpcName_, my biggest competitor._where_"}, # Pants On Fire Deliver Package to Liar Liar
 2053: {QUEST:  "Yay! A new delivery...\x07Wait, not you again _avName_. This isn't for me!\x07Take it back to _toNpcName_. He can find out where it's meant to be._where_"}, # Liar Liar in to Postmaster Pete
 2054: {QUEST:  "What's that you've got there, _avName_?\x07Oh, well that's not right... This label is all messed up.\x07I would fix it, but my sorter got stolen when some Boardbots took over my building.\x07Could you go get it back for me?"}, # Recover Label Sorter from Boardbots
 2055: {QUEST:  "Alright, here's the proper label.\x07Return this to Pants On Fire for me please._where_"}, # Postmaster Pete Deliver Package to Pants On Fire
 2056: {QUEST:  "Yay! A new delivery...\x07Wait, not you again _avName_.\x07Oh, this looks like the right package. Thanks!\x07Could you do me a favor, and go grab my glasses?\x07They were stolen by a Flunky."}, # Recover Glasses from Connoisseur
 2057: {QUEST:  "Ah, good. I can finish writing this memo now.\x07Alright, would you mind delivering this to _toNpcName_?_where_"}, # Deliver Urgent Memo to Shirley U. Jest
 2058: {QUEST:  "Is this from Pants On Fire?\x07Alright... Mhm... I see...\x07He believes that he'd be a bit more mellow about being neighbors if there were less level 2+ Cogs on this steet.\x07Maybe this could lead to peace between us if you help us out."}, # Defeat 5 Level 2+ Cogs on Wacky Way
 2059: {GREETING: '',
		QUEST:  "Now that you took care of Pants On Fire, maybe you could mellow me out.\x07Please reduce the amount of high leveled Cogs in this playground and then I'll give you a reward.", 
		COMPLETE: "Oh, thank you so much!\x07Here is your reward..."}, # Defeat 4 Level 4+ Cogs on Wacky Way

 # Task Six
 2060: {QUEST:  "My friend, _toNpcName_, has been having problems with the cogs lately.\x07Would you mind going over to his shop and helping him out?_where_"}, # Flippy to Tony Maroni
 2061: {GREETING: '',
		QUEST:  "Ay, you must be _avName_ whom was sent to help out, eh?\x07There have been some Bossbots roughing up my clients lately.\x07Mind making 'em go away?", # Defeat 5 level 3+ Bossbots
		LEAVING: ''},
 2062: {GREETING: '',
		QUEST:  "Ey, forget about 'em, yeah?\x07While you were out there, a group of lawbots came by and made one of my customers sad.\x07Can ya go teach 'em a lesson for me?\x07I'm tryin' ta work ova here!!! C'mon!",
		LEAVING: ''}, # Defeat 10 Lawbots
 2063: {QUEST:  "Last task, boss.\x07Some cogs have been halting my supply trains, taking their pies and such.\x07I need you to make sure they don't do that again, kapeesh?", COMPLETE: "Alright, a deals a deal."}, # Defeat 6 level 2+ Cogs
 
 # Task Seven
 2070: {QUEST:  "_toNpcName_ has been having a ton of issues with Cogs in the surrounding area.\x07Could you possibly go help him with whatever he needs?_where_"}, # Flippy to Louise Connection
 2071: {QUEST:  "I just had a package of cell phones delivered here and a Sellbot just came around and stole it!\x07Could you please go get it back for me?"}, # Recover a package from Sellbots
 2072: {QUEST:  "I just had a package of cell phones delivered here and a Cashbot just came around and stole it!\x07Could you please go get it back for me?"}, # Recover a package from from Cashbots
 2073: {QUEST:  "I just had a package of cell phones delivered here and a Lawbot just came around and stole it!\x07Could you please go get it back for me?"}, # Recover a package from Lawbots
 2074: {QUEST:  "I just had a package of cell phones delivered here and a Bossbot just came around and stole it!\x07Could you please go get it back for me?"}, # Recover a package from Bossbots
 2075: {QUEST:  "Thanks for getting that package back for me.\x07I need to make sure those Bossbots don't get greedy and try to steal these phones for their work.\x07Please defeat 5 of them then come back to me."}, # Defeat 5 Boardbots
 2076: {QUEST:  "Thanks for getting that package back for me.\x07Now, I need to make sure those Sellbots don't steal these phones and sell them for higher prices, ripping off toons everywhere!\x07Please defeat 5 of them then come back to me."}, # Defeat 5 Sellbots
 2077: {QUEST:  "Now I need a couple of those greedy Middlemen out of the picture..."}, # Defeat 2 Middlemen
 2078: {QUEST:  "Now I need a couple of those greedy Glad Handers out of the picture..."}, # Defeat 2 Glad Hander
 2079: {QUEST:  "Alright, here you go.\x07What is it, you ask?\x07You're nosy, but I suppose it couldn't hurt.\x07It's a cellphone that needs to be delivered to _toNpcName_._where_", COMPLETE: "Oh, is this from Louise Connection?\x07Awesome! Can't wait to get started with this thing!\x07Anyways, here's your reward!"}, # Deliver an activated cell phone to Loony Louis

 # Task Eight
 2080: {QUEST:  "Hiya! You are getting pretty far!\x07Hmm, your gags look like they can use a little more work though.\x07How about you get a few more points in your Throw track?"}, # Flippy - Collect 20 Throw Points
 2081: {QUEST:  "Great work! Your Throw gags are looking a lot better now!\x07But now your Squirt gags are a little too far behind.\x07Go put some work into your Squirt gags and come back to me when you are done."}, # Collect 20 Squirt Points
 2082: {QUEST:  "Now your gags are looking stronger then ever!\x07Now that that's done, do you mind bringing over a Cream Pie Slice to _toNpcName_?_where_"}, # Deliver a Cream Pie Slice to Ma Putrid 
 2083: {QUEST:  "Oh wow! This Cream Pie Slice looks delicious! Thank you so much _avName_!\x07Spamonia Biggles called me recently and told me she is in desperate need of a squirt gun.\x07Could you go deliever her one for me?"}, # Deliver a squirt gun to Spamonia Biggles
 2084: {QUEST:  "This is just what I was looking for! Thank you _avName_!\x07Flippy told me he has a task for you, go see him immediately."}, # Visit Flippy
 2085: {QUEST:  "Hey there! I see Biggles sent you right over here, perfect!\x07I need you to go and defeat some cogs for some reasearch."}, # Defeat 5 cogs
 2086: {QUEST:  "Perfect! This will help my research a lot.\x07For your last task I need you to defeat some higher level cogs.", COMPLETE: "Our research will be greatly advanced because of you!\x07Thank you for all your help _avName_!"}, # Defeat 3 level 4+ cogs
 
 # Task Nine
 2090: {QUEST:  "Thank god you are here _avName_!\x07Sticky Lou is in desperate need of assistance with an unexpected wave of Cogs surrounding his shop!\x07Please go to him and help him with whatever he needs._where_"}, # Flippy to Sticky Lou
 2091: {QUEST:  "There are just too many!!! I don't know what to do!\x07Oh, _avName_! I didn't notice you there!\x07Please help me with all these Cogs, there are way too many for me to handle on my own."}, # Defeat 30 Cogs in Toontown Central
 2092: {QUEST:  "Thank you so much _avName_, that makes me feel a lot more safe roaming the streets!\x07We need to start taking out the big cogs now.\x07Go defeat some level 2+ Cogs on Wacky Way..."}, # Defeat 4 Level 2+ Cogs on Wacky Way
 2093: {QUEST:  "A sprinkle of level 3+ Cogs on Punchline Place..."}, # Defeat 3 Level 3+ Cogs on Punchline Place
 2094: {QUEST:  "A dash of level 4+ Cogs on Silly Street..."}, # Defeat 2 Level 4+ Cogs on Silly Street
 2095: {QUEST:  "And a hint of lime of level 4+ Cogs on Loopy Lane!"}, # Defeat 2 Level 5+ Cogs on Loopy Lane
 2096: {QUEST:  "While you were away, I assumed everything was fine.\x07I was heading to the Post Office to store these top secret blueprints, and then a strong Cog roaming this street took it away.\x07You just have to get those blueprints back for me! Within the Cogs' hands, who knows what could happen?", COMPLETE: "All of the toons and I appreicate all you have done for us.\x07The streets will now be a lot safer with all you have done.\x07Please take this reward!"}, # Recover a Blueprint from Level 5+ Cogs in Toontown Central

 # Task Ten
 2100: {QUEST:  "_toNpcName_ has gone completely mad about how the Cogs have been acting around here.\x07Could you go see what's up?_where_"}, # Flippy to Shorty Fuse
 2101: {GREETING: '',
		QUEST:  "These Cogs are giving me a short fuse, and I feel like I'm about to EXPLODE!!!\x07Ooooh, those high leveled Cogs around here, they need a lesson taught to them...",
		LEAVING: ''}, # Defeat 5 Level 3+ Cogs in Toontown Central
 2102: {GREETING: '',
		QUEST:  "Now, those Lawbots...\x07THEY REALLY JUST GET MY FUSE DOWN TO THE BOTTOM!!!",
		LEAVING: "KA-BOOM!!!!!!"}, # Defeat 10 Lawbots
 2103: {GREETING: '',
		QUEST:  "Now, those Bossbots...\x07THEY REALLY JUST GET MY FUSE DOWN TO THE BOTTOM!!!",
		LEAVING: "KA-BOOM!!!!!!"}, # Defeat 10 Bossbots
 2104: {GREETING: '',
		QUEST:  "Now, those Boardbots...\x07THEY REALLY JUST GET MY FUSE DOWN TO THE BOTTOM!!!",
		LEAVING: "KA-BOOM!!!!!!"}, # Defeat 10 Boardbots
 2105: {GREETING: '',
		QUEST: "IT'S NOT FAIR!!!\x07WHY ARE THERE SO MANY HIGH LEVELED SELLBOTS???",
		LEAVING: "MY HEAD IS ABOUT TO BURST, I'M SO ANGRY!!"}, # Defeat 3 Level 4+ Sellbots
 2106: {GREETING: '',
		QUEST: "IT'S NOT FAIR!!!\x07WHY ARE THERE SO MANY HIGH LEVELED CASHBOTS???",
		LEAVING: "MY HEAD IS ABOUT TO BURST, I'M SO ANGRY!!"}, # Defeat 3 Level 4+ Cashbots
 2107: {QUEST:  "Oof, oof, I'm cooling down now...\x07Several more Cogs and I should be normal...", COMPLETE: "Sunshine, lollipops and, rainbows butterflies...\x07Thank you so much for this warm, happy feeling _avName_.\x07Here is a well deserved reward..."}, # Defeat 10 Cogs in Toontown Central
 
 # Task Eleven
 2110: {QUEST:  "Hey _avName_, we've almost run out of things for you to do!\x07Next up, the Toon Clinic is in need of some supplies.\x07First, pay a visit to _toNpcName_, and see what he needs."}, # Flippy to Charlie Doggenbottom
 2111: {QUEST:  "Hello, are you our help?\x07Awesome, because things have been really hectic around here.\x07To start with, a bunch of our straightjackets were stolen."}, # Recover 10 straightjackets from the cogs in AA
 2112: {QUEST:  "Alright, thanks for getting those back from the cogs.\x07If you wouldn't mnd, could you deliver those to _toNpcName_?"}, # Deliver 10 straightjackets to Dr. Sensitive
 2113: {QUEST:  "Are these the straight jackets that were stolen?\x07Thank you so much. No time to Dawdle though, _toNpcName_ is in need of some help."}, # Visit Nurse Nancy
 2114: {QUEST:  "Hey, so glad you're here.\x07Would you mind going out and defeating some Ambulance Chasers for me?\x07They've been a real pain lately."}, # Defeat 5 Ambulance Chasers
 2115: {QUEST:  "Well, it seems they got angry, because they stole a set of our ambulance keys.\x07Could you go out and defeat a few more?\x07You should be able to recover the keys from them."}, # Collect a set of ambulance keys from Ambulance Chasers
 2116: {QUEST:  "Thank you so much for recovering those!\x07Now, could you go visit _toNpcName_? He's supposed to have some new tires for us."}, # Visit Loony Louis
 2117: {QUEST:  "Oh man, what am I gonna do?\x07Oh hey! Are you here for the tires?\x07Well, unfortunately there was an accident in delivery.\x07They ended up in the pond somehow, and I don't have my fishing pole.\x07Would you mind going and fishing those up for mee collaborative text?"}, # Collect 4 ambulance tires from fishing
 2118: {QUEST:  "Alright, I'll have those delivered to the clinic right away.\x07We had a diesel engine being delivered too, but it was stolen by some higher level cogs.\x07Would you mind going out and grabbing it?\x07Just defeat some five level cogs until you find it.", COMPLETE: "Hey, is that the engine?\x07Man, how did you carry that all the way here?\x07Anyways, thanks, here's your reward."}, # Collect a diesel engine from level 5+ cogs
 
 # Task Twelve, MEGATASK OF ZONE
 2120: {QUEST:  "Good to see you again, _avName_!\x07_toNpcName_ asked me for some help, could you go visit them and see what they need?"}, # Flippy to Nona Seeya
 2121: {QUEST:  "I'm in a bit of a stick right now -- I lost all my invisible ink!\x07I'm almost certain that I dropped them in a pond, could you be a dear and fish them back for me?"}, # Recover 4 invisible ink from the fish
 2122: {QUEST:  "Great work! There's just one problem; I have nothing to write with! A bunch of glad handers came in and ransacked my shop taking my fountain pens.\x07Go defeat some of those filthy Glad Handers and get them back!"}, # Recover 4 fountain pens from glad handers
 2123: {QUEST:  "Amazing!\x07I do owe flippy a pen of mine so how about you go take one of these to him?_where_"}, # Deliver a fountain pen to Flippy"},
 2124: {QUEST:  "Oh, it's you again?\x07A pen? Well, tell Nona Seeya I said thank you!"}, # Return to Nona Seeya
 2125: {QUEST:  "Hey, you're back! I just remembered I also owe _toNpcName_ a fountain pen too so go ahead and deliver this to him."}, # Deliver a fountain pen 
 2126: {QUEST: "Heya, son! I've never seen you before.\x07A fountain pen? Well, my apprecations! There's just one problem...\x07I can't write with all those cogs stomping around! How about you go defeat some of those higher cogs and then maybe I could?"}, # Defeat 8 level 4+ cogs in TTC
 2127: {QUEST:  "Hmmm... Still too shaky. Try defeating some of the elite cogs, then."}, # Defeat 4 level 5+ cogs in TTC
 2128: {QUEST:  "Ugh! The shakings better but I can't focus with all those noisy cog buildings!\x07Defeat one cog building for me, would you?"}, # Defeat a cog building
 2129: {QUEST:  "Just right! I can write again! Go back to Nona Seeya and tell her I said thanks."}, # Return to Nona Seeya
 2130: {QUEST:  "You're back? I almost thought that you let me forever!\x07Anyways, my friend Inky Ivon just asked me for a fountain pen. Would you please deliver one to him?"}, # Deliver a fountain pen to Inky Ivon
 2131: {QUEST:  "Aye, son! You got that fountain pen for me?\x07What do you think about doing me a favor, while you're here?\x07I need some Inc Sacs for this pen, which you should be able to fish up for me.ait "}, # Fish for 15 Inc Sacks
 2132: {QUEST:  "Thanks for that! Now I can actually use this pen.\x07Go back to Nona Seeya and tell her I'm very grateful."}, # Return to Nona Seeya
 2133: {QUEST:  "Alright, I need you to deliver another one.This one is going to...\x07Ah! Deliver this one to Postmaster Pete"}, # Deliver a fountain pen to Postmaster Pete
 2134: {QUEST:  "Hey, is this my pen from Nona Seeya?\x07Alright, now I can sign these pack....\x07Wait, where did those packages go??\x07Oh dear, those cogs that were in here earlier must have stolen them!\x07Alright, could you go get them back for me?"}, # Collect 10 packages from Level 4+ cogs
 2135: {QUEST:  "And that's it. Thank you, kindly return to Flippy when you're ready."}, # Return to Flippy
 2136: {QUEST:  "Hey there, done with your deliveries?\x07Alright, for your last task I need you to...\x07Go defeat a two story building, or higher!", COMPLETE: "Thank you so much!\x07Hope you are feeling better now that you've completed everything for me.\x07Alright, I think you're finally ready to move out. I'm going to send you off to Acorn Acres, so that you can do some more training work for them.\x07Beware, as that playground is significantly more infested with cogs \x07However, I know that you're ready for it.\x07Alright, good luck! \x07 Best be getting on your way now."}, # Defeat a 2+ story building
 
 #AA Task One
 3000: {QUEST: "You must be new around here?\x07_toNpcName_ could use help from a new guy like you._where_"},
 3001: {GREETING: '',
		QUEST: "Welcome, _avName_!\x07Every day, I spend my dedicated time to helping the citizens of Acorn Acres with their problems.\x07Today, I need a break. I've been working non-stop every day for the past few months!\x07Don't worry, there aren't that many citizens who need help today.\x07I want you to start by helping _toNpcName_.\x07It seems her humidifiers have been stolen and she is freezing cold in her shop.\x07Please take these warm blankets please._where_"},
 3002: {GREETING: '',
		QUEST: "Brrrr...\x07O-o-ohhh are th-th-those blankets for m-me?\x07Ahhh, that's refreshing...\x07Anyways, the Cogs around here have stolen my humidifiers and I need them back!\x07Could you please go get them for me?",
		LEAVING: ''},
 3003: {GREETING: '',
		QUEST: "Great!\x07Now let _toNpcName_ know that everything here is okay.",
		LEAVING: ''},
 3004: {GREETING: 'Brilliant work, _avName_!',
		QUEST: "Next, I need you to help calm down _toNpcName_.\x07Between you and me, he's a little crazy..._where_",
		LEAVING: ''},
 3005: {GREETING: '',
		QUEST: "The Cashbots around here, they make me SO uncomfortable!\x07I can't relax knowing that there are plenty of them around here roaming the streets!",
		LEAVING: ''},
 3006: {GREETING: '',
		QUEST: "No, no, the high leveled Cogs on this street...\x07Are they just waiting for me to let my guard down?",
		LEAVING: ''},
 3007: {GREETING: '',
		QUEST: "Ahh, what a lovely morning!\x07What's that, _avName_? _toNpcName_ wants to know if I'm alright?\x07Well, why wouldn't I be? Tell him that everything is okay around here!",
		COMPLETE: "Alright, here's your next assignment.\x07Wait... that's all I had for you.\x07Well, I guess this mean I owe you something.",
		LEAVING: ''},
		
 #AA Task Two
 3010: {QUEST: "_toNpcName_ is trying to earn a spot as a full time detective.\x07Only issue is that he's not the brightest when it comes to solving crimes..._where_"},
 3011: {GREETING: '',
		QUEST: "Greetings, _avName_.\x07Are you going to help me solve a case today?\x07There has been a lot of crime around town, and I suspect those Swindlers are up to it!\x07Those suspicious masks tell us the truth: they are guilty!\x07Go defeat some of them and bring them to justice!",
		LEAVING: ''},
 3012: {GREETING: '',
		QUEST: "No... Crime is still at a normal rate...\x07Maybe it's the Boardbots in general causing crimes?",
		LEAVING: ''},
 3013: {GREETING: '',
		QUEST: "The crime rate got even higher after you left!\x07I'm starting to suspect that those Bloodsuckers are up to no good...",
		LEAVING: ''},
 3014: {GREETING: '',
		QUEST: "Why isn't the crime rate dropping?\x07It may not have been those Bloodsuckers, but perhaps those high leveled Lawbots in general...",
		LEAVING: ''},
 3015: {GREETING: '',
		QUEST: "The crime rate got even higher after you left!\x07I'm starting to suspect that those Penny Pinchers are up to no good...",
		LEAVING: ''},
 3016: {GREETING: '',
		QUEST: "Why isn't the crime rate dropping?\x07It may not have been those Penny Pinchers, but perhaps those high leveled Cashbots in general...",
		LEAVING: ''},
 3017: {GREETING: '',
		QUEST: "While you were gone, three shops have been broken into!\x07Ugh, I'm a terrible detective, completely on the wrong case...\x07Just defeat those Cogs until the crime rate drops.",
		COMPLETE: "Wow!\x07A lot of shopkeepers are calling me saying how good my detective work was!\x07Thanks for all your help, _avName_.\x07Here's a reward.",
		LEAVING: ''},

 #AA Task Three
 3020: {QUEST: "Oh no! There was a break-in at _toNpcName_'s store!\x07Go see what's up and how you can help her._where_"},
 3021: {GREETING: '',
		QUEST: "Those Elite Cogs came in here and trashed my place!\x07Once they left, I saw that my most expensive ring has been stolen.\x07I'm not sure, but I think it was a Tightwad who took it.\x07Could you get it back for me please? He could be anywhere with it!",
		LEAVING: ''},
 3022: {GREETING: '',
		QUEST: "Thanks for getting that back for me, hun!\x07Now I need you to teach those Elites a lesson.",
		COMPLETE: "Amazing work!",
		LEAVING: ''},
 #AA Task Four
 3030: {QUEST: "Looks like there's an issue at the insurance agency._where_"},
 3031: {QUEST: "The Ambulance Chasers have been causing issues to the Toons around here.\x07They get in accidents often with them and when they need to exchange insurance information, those Cogs just run off with their insurance cards!\x07A Toon just called in and said his insurance card was taken, so I suspect it was an Ambulance Chaser.\x07Why not take some down and see if you can get it back?"},
 3032: {GREETING: '',
		QUEST: "No insurance card?\x07Maybe they passed it along to one of their friends...",
		LEAVING: ''},
 3033: {QUEST: "Great job! Now bring that to _toNpcName_ as soon as possible!_where_"},
 3034: {QUEST: "Thanks for getting my insurance card back!\x07I don't know if you'd be willing to do a favor for me, but a bunch of Cogs just broke in and stole my bolts.\x07I need them back for a secret project that I'm constructing.\x07If you could get those back for me, that'd be fantastic!"},
 3035: {QUEST: "You got them back! Thank you so much!\x07I guess _toNpcName_ needs to see you again now that you're done with me."},
 3036: {QUEST: "Those strong Lawbots are still causing trouble around town.\x07If you could take down some of them, I will give you a reward.",
		COMPLETE: "Well, a deal is a deal..."},

 #AA Task Five
 3040: {QUEST: "_toNpcName_ has an idea for creating a new tent and needs your help._where_"},
 3041: {QUEST: "So, I guess you heard about my new tent, huh?\x07Yep, but the only issue is that the only supplier of the material I need keeps getting robbed of his material.\x07Try to see if you can help get it back._where_"},
 3042: {GREETING: '',
		QUEST: "Hey, _avName_. How can I help you?\x07You need straw, wood, and brick?\x07Well, I'd love to give you some, but you'd have to get it back for me first.\x07To begin with, the Sellbots huffed and puffed and took my supply of straw.\x07I'll need about 10 bits of those back.",
		LEAVING: ''},
 3043: {GREETING: '',
		QUEST: "Then the Lawbots huffed and puffed and took my supply of wood...",
		LEAVING: ''},
 3044: {GREETING: '',
		QUEST: "Then the Cashbots huffed and puffed, but they failed to take my supply of brick!\x07Only later, they called some of their high leveled friends in to take the supply, which they succeeded to do...",
		LEAVING: ''},
 3045: {GREETING: '',
		QUEST: "Great! Now take these to _toNpcName_",
		COMPLETE: "Wow, you actually got the materials!\x07I'll be sure to credit you if I ever end up making this new tent.\x07Here's a reward for your help...",
		LEAVING: ''},
		
 #AA Task Six
 3050: {QUEST: "_toNpcName_ is throwing a party and needs help passing out invitations._where_"},
 3051: {GREETING: 'Hey dawg.',
		QUEST: "Yeah, I'm having a killer party tonight for the residents of my fellow street.\x07Only issue is that some of them are too scared of the Cogs on this street to try to make it here.\x07I need you to calm their nerves for me, then report back to me if they can come or not.\x07First, I need you to check on _toNpcName_._where_",
		LEAVING: "Peace, dawg!"},
 3052: {QUEST: "Yeah, I'd love to go to Reid's party, but I don't like those high leveled Cogs roaming around this street as I try to walk out of my shop.\x07I'll be glad to go to his party if you could defeat several of them."},
 3053: {QUEST: "Great! Let _toNpcName_ know that he'll see me tonight!",
		LEAVING: ''},
 3054: {GREETING: "One guest down, two to go.",
		QUEST: "Next, I need you to go get _toNpcName_ to chill and come to the party!_where_",
		LEAVING: "Peace, dawg!"},
 3055: {QUEST: "Sure, I'd go to Reid's party if there weren't so many Boardbots on this street!"},
 3056: {QUEST: "Let _toNpcName_ know that I'll be there!"},
 3057: {GREETING: "Wow, you're good at this dawg.",
		QUEST: "Finally, I want you to go get word from _toNpcName_ that she'll be there._where_",
		LEAVING: "Good luck, dawg!"},
 3058: {QUEST: "I'll go to the party if you could take down one of those big buildings around here.\x07If you could do that, it'd relieve the stress I have thinking my building will be taken over if I leave it..."},
 3059: {GREETING: '',
		QUEST: "Oh, thank you for calming me down.\x07Can't wait for the party!",
		COMPLETE: "Aye dawg, this party is going to be great!\x07Here's a reward for ya, dawg...",
		LEAVING: ''},

 #AA Task Seven
 3060: {QUEST: "_toNpcName_ is having an issue with medicine._where_"},
 3061: {GREETING: '',
		QUEST: "Oh this is just awful!\x07The Cogs just raided my shop and took all the allergy pills that I have to give to my patients.\x07I had about 15 of them before they took over.\x07Please, go get them back for me!",
		COMPLETE: "Yes! That's all of them.\x07Here's a nifty reward for you!",
		LEAVING: ''},

 #AA Task Eight
 3070: {QUEST: "The spirit of the town has gone down and _toNpcName_ needs help bringing it back up._where_"},
 3071: {GREETING: '',
		QUEST: "Those Cogs are always trying to take away the spirit of the town.\x07I feel like those Downsizer bring them down more than anyone else.\x07Why not defeat some of them and regain some spirit to the toons of this town?",
		LEAVING: "Good luck, buddy!"},
 3072: {GREETING: '',
		QUEST: "Next, I need you to defeat several Toxic Managers before they poison the spirit filled inside each toon.",
		LEAVING: ''},
 3073: {GREETING: '',
		QUEST: "Finally, take down a few of those big and ugly Cog Buildings",
		COMPLETE: "Yep! The spirit of this town seems to be shining again!\x07Thanks for your help. Here's your reward...",
		LEAVING: ''},
		
 #AA Task Nine
 3080: {QUEST: "Ahh yes, it appears that the Cogs have been giving toons some burning feeling, according to _toNpcName_.\x07Could you go see what's up?_where_"},
 3081: {GREETING: '',
		QUEST: "You're here about the burning case?\x07Yes, it appears that Cold Callers have been burning toons with their Hot Air attacks.\x07They're dangerous and must be stopped.\x07Defeat a handful then report back to me.",
		LEAVING: ''},
 3082: {GREETING: '',
		QUEST: "Next, those Tightwads love to do some firing.\x07Some toons come in here with a fully burnt body, and it's just awful.\x07Go teach those punks a lesson, why don't ya?",
		LEAVING: ''},
 3083: {GREETING: '',
		QUEST: "To finish off, I want you to take down a handful of strong Cogs that defeat toons with a painful burn.",
		COMPLETE: "Seems like someone turned down the heat, no?\x07Thanks for all your help, _avName_. Here's a reward for ya...",
		LEAVING: ''},
		
 #AA Task Ten
 3090: {QUEST: "According to _toNpcName_, the stronger Cogs are causing trouble everywhere they go._where_"},
 3091: {QUEST: "I've been hearing reports of those high leveled Bossbots causing an issue all over town.\x07Can you defeat several of them please?"},
 3092: {QUEST: "I've been hearing reports of those high leveled Lawbots causing an issue all over town.\x07Can you defeat several of them please?"},
 3093: {QUEST: "I've been hearing reports of those high leveled Cashbots causing an issue all over town.\x07Can you defeat several of them please?"},
 3094: {QUEST: "I've been hearing reports of those high leveled Sellbots causing an issue all over town.\x07Can you defeat several of them please?"},
 3095: {QUEST: "I've been hearing reports of those high leveled Boardbots causing an issue all over town.\x07Can you defeat several of them please?"},
 3096: {QUEST: "Great job!\x07Now, if you could take down a couple of those Cog Buildings in revenge of what they've done, I'll give you a reward.",
		COMPLETE: "Well, a deal's a deal."},
		
 #AA Task Eleven
 3100: {QUEST: "There have been a lot of toons going sad and _toNpcName_ knows the reason why._where_"},
 3101: {QUEST: "You want to know why toons keep going sad? Well I'll tell you why.\x07Those high level 6+ Cogs are just the biggest threat to every toon out there.\x07Toons kept coming in here telling me \"Ohhhh, how awful it was fighting those awfully strong robots.\"\x07Please defeat a handful of them and then I'll give you a reward.",
		COMPLETE: "As I promised..."},
		
 #AA Task Twelve
 3110: {QUEST: "Setting up shop on a street like Walnut Way is rough with all those high leveled Cogs.\x07_toNpcName_ would like to check your gags to see if you could defend yourself on such a street._where_"},
 3111: {QUEST: "Have you seen the Cogs that roam out there?\x07Awful how strong they are.\x07I never want you to have a struggle when fighting those kinds of Cogs.\x07First, you'll need stronger gags.\x07Go out and train your throw."},
 3112: {GREETING: '',
		QUEST: "Now how about training that squirt too?",
		LEAVING: ''},
 3113: {GREETING: '',
		QUEST: "Great work! Now let me see that new throw gag of yours.",
		LEAVING: ''},
 3114: {GREETING: '',
		QUEST: "Now how about that squirt...",
		COMPLETE: "Well, it's a start, but you'll need more gags if you want to fight the highest set of Cogs around here.\x07Here a reward to help you progress...",
		LEAVING: ''},
		
 #AA MEGA TASK
 3200: {QUEST: "_toNpcName_ has major issues with the strong Cogs around the town._where_"},
 3201: {GREETING: '',
		QUEST: "Thank you for coming, _avName_.\x07Each day, I try to build a new home for new toons to move into, but the strong Cogs keep interupting my construction to prevent new toons from moving into town.\x07I'm about to get working on another house in the backyard, and I need you to make sure that those strong Cogs don't get in the way.\x07Start by defeating some Spin Doctors.",
		LEAVING: ''},
 3202: {GREETING: '',
		QUEST: "Back already?\x07I barely even started on this house.\x07Try defeating some Money Bags while I continue building, they seem to cause issues too.",
		LEAVING: ''},
 3203: {GREETING: '',
		QUEST: "Now, those Two-Faces are just a handful to deal with!",
		LEAVING: ''},
 3204: {GREETING: '',
		QUEST: "I'm almost done with the base.\x07Just defeat some of those creepy Magnates while I put on some of the finishing touches.",
		LEAVING: ''},
 3205: {GREETING: '',
		QUEST: "The base is all set. Now I need a roof to work with.\x07Can you see if _toNpcName_ can build me a new roof?_where_",
		LEAVING: ''},
 3206: {GREETING: '',
		QUEST: "A new roof? I can get that done in minutes!\x07While I do it, I need you to keep those Elite Cogs in check and make sure they don't come in here and take my materials.",
		LEAVING: ''},
 3207: {GREETING: '',
		QUEST: "Finished that roof and shipped it off.\x07Could you go give this bill to _toNpcName_? He could mail the check to me.",
		LEAVING: ''},
 3208: {GREETING: '',
		QUEST: "A bill? I thought we were friends!\x07Oh well, it's no big deal.\x07Now, I just need you to ensure that those high leveled Bossbots don't destroy this new home.\x07A new toon is suppose to move in tomorrow, you know.",
		LEAVING: ''},
 3209: {GREETING: '',
		QUEST: "A bill? I thought we were friends!\x07Oh well, it's no big deal.\x07Now, I just need you to ensure that those high leveled Lawbots don't destroy this new home.\x07A new toon is suppose to move in tomorrow, you know.",
		LEAVING: ''},
 3210: {GREETING: '',
		QUEST: "A bill? I thought we were friends!\x07Oh well, it's no big deal.\x07Now, I just need you to ensure that those high leveled Cashbots don't destroy this new home.\x07A new toon is suppose to move in tomorrow, you know.",
		LEAVING: ''},
 3211: {GREETING: '',
		QUEST: "A bill? I thought we were friends!\x07Oh well, it's no big deal.\x07Now, I just need you to ensure that those high leveled Sellbots don't destroy this new home.\x07A new toon is suppose to move in tomorrow, you know.",
		LEAVING: ''},
 3212: {GREETING: '',
		QUEST: "A bill? I thought we were friends!\x07Oh well, it's no big deal.\x07Now, I just need you to ensure that those high leveled Boardbots don't destroy this new home.\x07A new toon is suppose to move in tomorrow, you know.",
		LEAVING: ''},
 3213: {GREETING: '',
		QUEST: "Finally, we don't want to scare the new toon away with those tall, disgusting buildings.\x07Take down a few and then I'll give you a neat reward.",
		COMPLETE: "Thank you for all your hard work in helping me.\x07I'll be sure to tell this new toon about you, you're a great citizen!\x07Here's a big reward for you...",
		LEAVING: ''},
		
 #DD Task One
 4000: {QUEST: "I'm not sure exactly why, but _toNpcName_ is looking for help.\x07Please go see what's wrong with her._where_"},
 4001: {GREETING: '',
		QUEST: "Oh, thank you for taking my request!\x07You see, the Bossbots came in here and took all my dried suits!\x07I think there were about 10 of them. Please get them before customers expect their suits back!",
		LEAVING: ''},
 4002: {GREETING: '',
		QUEST: "Thank goodness you got them back.\x07One of my customers came in while you were out recovering the dried suits and I told him you'd deliver it once you got back._where_",
		LEAVING: "Make sure you don't leave without a signed check!"},
 4003: {GREETING: 'Ahoy, me bucko!',
		QUEST: "Ah, that be me dry cleaning, thanks matey!\x07Eh? A signed check?\x07Errr, I gotta clear something up with me bank before I sign ye a check.\x07While I do that, maybe ye can defeat some of them big meaty Cogs on this street.",
		LEAVING: "Good luck matey!"},
 4004: {GREETING: '',
		QUEST: "Argh, here be me check.\x07Return it to _toNpcName_.",
		COMPLETE: "Thanks so much for your help!\x07Here's a reward...",
		LEAVING: ''},
		
 #DD Task Two
 4010: {QUEST: "_toNpcName_ seems to have crashed his pirate ship and needs help recovering from the incident._where_"},
 4011: {GREETING: 'Ahoy Matey!',
		QUEST: "Come to help me, ye say?\x07Ye see, I was sailing through the seven seas, collecting me treasure, when suddenly I was attacked!\x07Cogs everywhere came flying down! Shiver me timbers, it's a horror to remember!\x07I need ye to help repair me pirate ship so I can continue to sail across the dock.\x07First, I need ye to fish out some boards of wood that the beavers drop in the pond on this here street.",
		LEAVING: ''},
 4012: {GREETING: 'Avast, Matey!',
		QUEST: "Arrrgh! Ye have brought me the boards, how wonderful!\x07Next, I need me lucky hook. The Backstabbers took it from me, and no pirate is right without his lucky hook!",
		LEAVING: ''},
 4013: {GREETING: '',
		QUEST: "Me lucky hook! The most valuable treasure I've ever come across!\x07Matey ye have done me a good service, but how could I ever sail without my sail?\x07I know! _toNpcName_ can make me a whicked sail in a heartbeat!\x07Could ye go get a sail from him?_where_",
		LEAVING: ''},
 4014: {GREETING: '',
		QUEST: "A new sail for Jack?\x07Arrrgh, I'd love to help, but I'm afraid that the Sellbots took all my pieces of cloth.\x07If you recover those for me, I'll gladly make a new sail.",
		LEAVING: ''},
 4015: {GREETING: '',
		QUEST: "Excellent!\x07I'll get started on this sail right away.\x07While I'm making this sail, please defeat some of the Cogs around here.",
		LEAVING: ''},
 4016: {GREETING: '',
		QUEST: "Great! Take this back to _toNpcName_ immediately!",
		LEAVING: ''},
 4017: {GREETING: 'That be a brilliant sail ye got there!',
		QUEST: "Time for me to get started on me ship.\x07While I repair me ship, I need ye to defeat some of them buildings out there to take revenge on those Cogs.\x07Don't worry matey, there is a treasuring reward with this here quest!",
		COMPLETE: "The ship is all sailed!\x07Thank ye so much for all your help.\x07Would ye like to sign up as a matey of mine?\x07No? Then here be a reward instead...",
		LEAVING: ''},

 #DD Task Three
 4020: {QUEST: "_toNpcName_ is going on a big fishing expedition, but is totally unprepared._where_"},
 4021: {QUEST: "Ah yes, the fishing expedition.\x07I'm not ready to go and I could use a few favors.\x07Don't worry, there's a reward involved in this job.\x07First, I need a nice fishing rod from _toNpcName_. He makes some high quality fishing rods._where_"},
 4022: {QUEST: "So, you need some of my finest fishing rods, hmm?\x07I'd love to show you the display, but the Money Bags took all 5 of my fishing rods...",
		LEAVING: ''},
 4023: {GREETING: '',
		QUEST: "Hey! There's my display!\x07I guess I could give _toNpcName_ one for free since he sent you to help me.",
		LEAVING: ''},
 4024: {GREETING: '',
		QUEST: "Wow! What an excellent fishing rod!\x07Next, I need a bunch of hooks.\x07The Cashbots raided my supply and ran off with them.",
		LEAVING: ''},
 4025: {GREETING: '',
		QUEST: "Finally, I want you to fish out some cans of worms that I accidentally left on my last trip to the pond on this street.",
		LEAVING: '',
		COMPLETE: "Yep, that's everything!\x07I'm all set and ready to go, all thanks to you!\x07Here's a reward..."},
		
 #DD Task Four
 4030: {QUEST: "_toNpcName_'s shop has been a mess ever since the Cogs broke in._where_"},
 4031: {GREETING: '',
		QUEST: "Oh, those awful Cogs!\x07First, those Sellbots came in and stole all my fish...",
		LEAVING: ''},
 4032: {GREETING: '',
		QUEST: "Then those nasty Boardbots stole all my chips!",
		LEAVING: ''},
 4033: {GREETING: '',
		QUEST: "Now it doesn't even feel safe to go boating with all these Cogs around the docks...",
		COMPLETE: "Hmm, the area feels a lot safer.\x07Thanks for helping me out, _avName_. Sorry I was acting so uneasy.\x07Here's a reward for your troubles.",
		LEAVING: ''},

 #DD Task Five
 4040: {QUEST: "_toNpcName_'s taxi service has been going downhill because of the Cogs roaming the streets.\x07He wants to get back in business and needs help._where_"},
 4041: {GREETING: '',
		QUEST: "Hey, _avName_. I'm in a bit of a fix.\x07My taxi service went out of business a long time ago when the Cogs first invaded.\x07I didn't do anything to fix my business, and now I have these bills that I can't pay off.\x07I need help restoring this business and it involves taking down those Cogs.\x07First, start by defeating the higher leveled Cogs on this street.",
		LEAVING: ''},
 4042: {GREETING: '',
		QUEST: "Great job!\x07Now, may I ask that you defeat those Cashbots?\x07They like to call my taxi over and take all the money I've earned.",
		LEAVING: ''},
 4043: {GREETING: '',
		QUEST: "Finally, I need my taxi keys back.\x07I'm pretty sure that they were taken by a Cashbot...",
		COMPLETE: "Thanks for all your help, _avName_.\x07I think I'm ready to go back in business!\x07Here's your reward..."},
		
 #DD Task Six
 4050: {QUEST: "_toNpcName_'s lost and found has been raided by the Cogs.\x07He needs all the help he can get to get his inventory back._where_"},
 4051: {QUEST: "It's just awful! All the lost items here have been stolen!\x07Can you please help me get each item back?\x07First, the striped shirts I had were stolen by a bunch of Bossbots."},
 4052: {QUEST: "Perfect! A call came in about a lost striped shirt while you were away.\x07Let me see those shirts.\x07Mhm... Uh-huh... Oh, here it is.\x07Take this to _toNpcName_ please._where_"},
 4053: {QUEST: "My stolen striped shirt! You found it!\x07What? You thought I lost it?\x07No, those Lawbots love to steal my inventory. I was just lucky someone found my favorite striped shirt.\x07I know you're busy, but you don't think you could defeat some of those bratty Lawbots for me, do you?"},
 4054: {QUEST: "Thanks for your help.\x07Please bring this jar of jellybeans to _toNpcName_ for his troubles."},
 4055: {QUEST: "Oh, he didn't have to pay. That's so sweet.\x07Next, I want you to recover some hats taken by the Connoisseurs.\x07Believe it or not, they love to mix and match hats outside of those Top Hats."},
 4056: {QUEST: "Awesome! Now I need you to deliver this hat to _toNpcName_._where_"},
 4057: {GREETING: '',
		QUEST: "Oh yep, that's my hat.\x07Give my thanks to _toNpcName_.",
		LEAVING: ''},
 4058: {QUEST: "Finally, I need you to get back the inventory of glasses.\x07I'm not sure which specific Cogs took them, so just defeat those Cogs until you get them all back.",
		COMPLETE: "I'll just deliver these on my own.\x07Thanks for all your help."},
		
 #DD Task Seven
 4060: {QUEST: "_toNpcName_'s world famous make-up supply has been taken and she needs help getting it back._where_"},
 4061: {GREETING: '',
		QUEST: "Oh hey, _avName_.\x07I'm kind of in a mess right now. Those evil feminine Cogs raided my supply of make-up!\x07First, those Name Droppers took all my lipstick...",
		LEAVING: ''},
 4062: {GREETING: '',
		QUEST: "Now, I need my blowdryers back from those Micromanagers.",
		LEAVING: ''},
 4063: {GREETING: '',
		QUEST: "Then there were my special earrings that were taken by those Number Crunchers...",
		LEAVING: ''},
 4064: {GREETING: '',
		QUEST: "And lastly, my secret Make-Up Kit was taken by a Mingler...",
		COMPLETE: "Wow! You got it all back!\x07Let me repay you for all your hard work...",
		LEAVING: ''},
		
 #DD Task Eight
 4070: {QUEST: "_toNpcName_ has an issue with those strong Cashbots._where_"},
 4071: {GREETING: '',
		QUEST: "Oh, those strong Cashbots are always busting my pipes and taking my water supply.\x07Can you defeat a handful of them for me? It'd really relieve my stress.",
		LEAVING: ''},
 4072: {GREETING: '',
		QUEST: "Now, I want them to feel the pain I feel when they bust my pipes.\x07Defeat several Cashbot Buildings and I'll reward you.",
		COMPLETE: "Alright, I'll stick to my word.\x07Thanks for your help.",
		LEAVING: ''},
		
 #DD Task Nine
 4080: {QUEST: "It seems like the Cogs are trying to put _toNpcName_ out of business.\x07We can't let another toon lose their shop to the Cogs! Go see what's up._where_"},
 4081: {GREETING: '',
		QUEST: "Oh _avName_, it's just awful. Those Cogs keep trying to work out a deal to take ownership to my building.\x07A bunch of Middlemen come in here and always try to work out a deal with me.\x07When I refuse to accept, they damage my inventory and I'm sick of it!\x07Defeat those Middlemen and then return to me please.",
		LEAVING: ''},
 4082: {GREETING: '',
		QUEST: "Now those Sellbots are after the deed to my building so that they can sell it!\x07How do I know this? I got a note that stated they were after the deed.\x07Please go defeat those Sellbots.",
		LEAVING: ''},
 4083: {GREETING: '',
		QUEST: "I was wrong!\x07A Boardbot came in and took the deed to my building while you were away!",
		COMPLETE: "You got it back!\x07Thanks for making me feel safe again, _avName_."},
		
 #DD Task Ten
 4090: {QUEST: "_toNpcName_ just called in and said that those Flunkies are causing trouble for him._where_"},
 4091: {GREETING: '',
		QUEST: "Those Flunkies have just been obnoxious lately.\x07They think they deserve more respect and think they should be the only ones to wear glasses to feel superior.\x07As a result, they stole glasses from a client of mine.\x07Could you get them back for me?",
		LEAVING: ''},
 4092: {GREETING: '',
		QUEST: "Great! Now take these to _toNpcName_ right away!_where_",
		LEAVING: ''},
 4093: {GREETING: '',
		QUEST: "Ahoy matey!\x07Arrgh, these be me glasses indeed.\x07Give me thanks to _toNpcName_.",
		LEAVING: ''},
 4094: {GREETING: '',
		QUEST: "Now I need you to retrieve another stolen pair from those Flunkies.",
		LEAVING: ''},
 4095: {GREETING: '',
		QUEST: "Those brats left a scratch on here!\x07I'll need a new frame. Perhaps a fancy one from the Connoisseurs",
		LEAVING: ''},
 4096: {GREETING: '',
		QUEST: "Perfect! Let me just fit this in correctly...\x07And there we go.\x07Take this to _toNpcName_ immediately._where_",
		LEAVING: ''},
 4097: {GREETING: '',
		QUEST: "Oh goodie, my reading glasses!\x07Send my thanks to _toNpcName_",
		LEAVING: ''},
 4098: {GREETING: '',
		QUEST: "OK, one last thing and then I'll give you a reward.\x07Earlier, the Bossbots came in here and raided the glasses drop off.\x07I need those back, for they must be fixed and returned today.",
		COMPLETE: "Awesome! Thanks for your help.\x07As I said before, I will give you a reward.",
		LEAVING: ''},
	
 #DD Task Eleven
 4100: {QUEST: "Think you're tough? _toNpcName_ wants to test your strength._where_"},
 4101: {GREETING: '',
		QUEST: "So, ya think you're tough?\x07Prove it to me. Defeat some of those Boardbots then return to me.",
		LEAVING: ''},
 4102: {GREETING: '',
		QUEST: "Oh, not tough enough for ya?\x07See if _toNpcName_ has a tougher challenge for ya._where_",
		LEAVING: ''},
 4103: {GREETING: '',
		QUEST: "So, ya think you're tough, eh?\x07Prove it. Defeat some of those Spin Doctors and prove that they can't take ya on a spin.",
		LEAVING: ''},
 4104: {GREETING: '',
		QUEST: "Not tough enough for ya, eh?\x07See if _toNpcName_ has a tougher challenge for ya._where_",
		LEAVING: ''},
 4105: {GREETING: '',
		QUEST: "So, ya think you're tough, do ya?\x07Prove it to me. Defeat some of the toughest Cogs out there.",
		LEAVING: ''},
 4106: {GREETING: '',
		QUEST: "Not tough enough for ya, hmm?\x07See if _toNpcName_ has a tougher challenge for ya._where_",
		LEAVING: ''},
 4107: {GREETING: '',
		QUEST: "So, ya think you're tou- Oh it's just ya again.\x07Hmm, I see ya completed all our challenges, so now I'll give ya an even tougher challenge.\x07Once ya defeat several large buildings, ya will have proven that you're a tough one.",
		COMPLETE: "Ya seem to be tough enough to me.\x07Here's a reward for ya toughness...",
		LEAVING: ''},
		
 #DD Task Twelve
 4110: {QUEST: "Your gags look like they could use some work.\x07Go see _toNpcName_ and see how you should train them._where_"},
 4111: {QUEST: "Oh yes, you could use some new gags.\x07For every gag that hits a Cog, you get points for that gag.\x07You can earn more points in Cog Invasions, Cog Headquarters, and any Cog Facility.\x07I want you to train your throw a little bit and then return to me."},
 4112: {QUEST: "Now you should train your squirt."},
 4113: {GREETING: '',
		QUEST: "Great! Can I see that new throw gag of yours?",
		LEAVING: ''},
 4114: {GREETING: '',
		QUEST: "How about that new squirt?",
		COMPLETE: "Good job on that training.\x07Here's a little bonus for your troubles.",
		LEAVING: ''},
		
 #DD Mega Task
 4200: {QUEST: "Oh no! It seems a Cog cargo ship just crashed into the big lighthouse!\x07That is the pure symbol of Donald's Dock and everyone is panicking at its destruction.\x07_toNpcName_ needs your help collecting material in order to repair the lighthouse._where_"},
 4201: {GREETING: '',
		QUEST: "Hey, _avName_. This isn't a great time...\x07Oh you're here about the lighthouse? Thank goodness.\x07I need all the help I can get.\x07First, I need some metal.\x07There's no metal shop here in Donald's Dock, but I think that _toNpcName_ has metal for his clock repair shop._where_",
		LEAVING: ''},
 4202: {GREETING: '',
		QUEST: "I did have metal, but those Cogs took my entire supply.\x07If you could get them back for me, I'll give you some to take back to Doctor Drift.",
		LEAVING: ''},
 4203: {GREETING: '',
		QUEST: "Well, a promise is a promise.\x07Take this metal to _toNpcName_.",
		LEAVING: ''},
 4204: {GREETING: '',
		QUEST: "Next on the list are some light bulbs.\x07See if _toNpcName_ has a spare supply of them._where_",
		LEAVING: ''},
 4205: {GREETING: '',
		QUEST: "Light bulbs?\x07Yeah, I had a supply, but they were taken by the Lawbots.\x07If you get them back, they're yours to keep.",
		LEAVING: ''},
 4206: {GREETING: '',
		QUEST: "Light bulbs?\x07Yeah, I had a supply, but they were taken by the Bossbots.\x07If you get them back, they're yours to keep.",
		LEAVING: ''},
 4207: {GREETING: '',
		QUEST: "Great job on those light bulbs!\x07I just found out that the Cogs in charge of the destruction were those awful Corporate Raiders.\x07Go invade those Bossbot buildings or attack them at Bossbot HQ in revenge for what they have done to our beloved town.",
		LEAVING: ''},
 4208: {GREETING: '',
		QUEST: "Alright, I've got the base of the lighthouse done.\x07We're going to need someone to paint this lighthouse once we're done.\x07The citizens did love the old design and only _toNpcName_ knew how to paint it.\x07Can you see if he'll paint it again?_where_",
		LEAVING: ''},
 4209: {GREETING: '',
		QUEST: "No way I'll go over to Lighthouse Lane to paint that new lighthouse!\x07At least, not with those strong Cogs over there...",
		LEAVING: ''},
 4210: {GREETING: '',
		QUEST: "You got rid of some of those strong Cogs for me?\x07Alright fine, tell _toNpcName_ that I'll come paint the lighthouse once it's ready.",
		LEAVING: ''},
 4211: {GREETING: '',
		QUEST: "Finally, I need some glass to protect the lights and to provide a brighter shine.\x07I haven't seen a glass studio anywhere around here, but I'm pretty sure _toNpcName_ knows where to get some glass._where_",
		LEAVING: ''},
 4212: {GREETING: '',
		QUEST: "Glass? I don't have any.\x07However, I could really use some for my mart since it's in high demand.\x07I think that the Cashbots have glass on them. Maybe you could get some from them?\x07Not sure why they would carry that around. Isn't that a bit dangerous?",
		LEAVING: ''},
 4213: {GREETING: '',
		QUEST: "Glass? I don't have any.\x07However, I could really use some for my mart since it's in high demand.\x07I think that the Sellbots have glass on them. Maybe you could get some from them?\x07Not sure why they would carry that around. Isn't that a bit dangerous?",
		LEAVING: ''},
 4214: {GREETING: '',
		QUEST: "Oh perfect!\x07Take these over to _toNpcName_ right away!",
		LEAVING: ''},
 4215: {GREETING: '',
		QUEST: "I have to put the finishing touches on the lighthouse.\x07In a final revenge act on those Cogs, I'd like you to take down a few of their biggest Cog Buildings.",
		COMPLETE: "Thank you, citizen for all your hard work.\x07The citizens of Donald's Dock are all grateful and in your debt.\x07Here's a big reward for your help.",
		LEAVING: ''},
		
 #DG Task One
 5000: {QUEST: "Oh no! The Cogs have ruined all of _toNpcName_'s world famous berries!_where_"},
 5001: {GREETING: '',
		QUEST: "So you've heard the news _avName_?\x07Yeah, all my berries are gone. Squashed. Blended. Stolen.\x07However, I have a solution to get my shop started up again.\x07_toNpcName_ is a berry supplier who recently moved into this town and it'd be great if you could ask him to help me out._where_",
		LEAVING: ''},
 5002: {QUEST: "Oh? Barry needs a new supplier?\x07Alright, but first I'll need a couple of favors since I don't do this kind of thing for free.\x07First, those Bossbots make me feel nervous and uneasy when walking around town.\x07They try to act like they have total control of my supply, since they are \"The Boss.\"\x07Could you defeat a handful of them for me?"},
 5003: {GREETING: '',
		QUEST: "Now, I want you to take out some of those Bean Counters.\x07They come to my berry garden and pick them all off the bushes.\x07That's not even the worst part, they'll just pick them off before they're ready and just leave them on the ground!\x07They say it's for the war against the beans and the fruits, which makes no sense at all...\x07I guess they're going crazy.",
		LEAVING: ''},
 5004: {GREETING: '',
		QUEST: "Alright, I'll officially be Barry's supplier.\x07Take this first sample of berries to _toNpcName_.",
		LEAVING: ''},
 5005: {GREETING: '',
		QUEST: "So I have a supplier?\x07That's fantastic!\x07I just need one more favor from you, then I'll give you a reward.\x07I'm worried that the strong Cogs on this street are going to try and destroy my berry supply again.\x07Can you take down a handful so that doesn't happen again?",
		COMPLETE: "Thanks for all your help.",
		LEAVING: ''},
		
 #DG Task Two
 5010: {QUEST: "Hmm. It seems that the Sellbots are having a factory salad party.\x07Why is this important? They stole several cabbages and some lettuce from _toNpcName_._where_"},
 5011: {GREETING: '',
		QUEST: "Oh no!\x07Those Sellbots were on their way to the factory and they stopped by and stole all my important cabbages!\x07Can you get them back for me please?",
		LEAVING: ''},
 5012: {GREETING: '',
		QUEST: "Oh thank you, but a Mover & Shaker came in here and took some of my lettuce while you were gone.\x07Maybe you passed him? He was on his way to the factory as well.",
		COMPLETE: "Thank you.",
		LEAVING: ''},

 #DG Task Three
 5020: {QUEST: "Seems that slowpoke _toNpcName_ can't hold on to his mail._where_"},
 5021: {GREETING: "Helloooooooo _avName_.",
		QUEST: "My... supply... of... letters........\x07All... stolen... by... Selbots........\x07Whom... work... in... the........\x07Factory.\x07Can... you... get... them........\x07Back... for... me... please?",
		LEAVING: "Goooooooooooood luck!"},
 5022: {GREETING: '',
		QUEST: "Thank... you.\x07Now... I... need... my........\x07Packages... back... which... were........\x07Taken... by... factory... Cogs........\x07As... well.",
		COMPLETE: "Thank... you... for... all........\x07Your... help!\x07Here... is... a... reward........",
		LEAVING: "Gooooooood-bye!"},
		
 #DG Task Four
 5030: {QUEST: "_toNpcName_ is unhappy with how little class the Cogs have for this town and is giving a big reward to those who can help take them down._where_"},
 5031: {GREETING: "Mhmm, welcome _avName_.",
		QUEST: "Oh, those Cogs have no class around here!\x07Those awfully strong Lawbots ruin everything with their false laws! There's not a spec of class in them.\x07Take down the toughtest of them and then return to me.",
		LEAVING: ''},
 5032: {GREETING: "I'm quite charmed of your hard work.",
		QUEST: "Now those Head Hunters are just a vacuum of class.\x07They just take all the class away!\x07Both theoretically and literally. They stole all my 14-Carrot Rings.\x07I need you to get them back for me.",
		LEAVING: ''},
 5033: {GREETING: "I'm quite charmed of your hard work.",
		QUEST: "Now those Two-Face are just a vacuum of class.\x07They just take all the class away! Both theoretically and literally. They stole all my 14-Carrot Rings.\x07I need you to get them back for me.",
		LEAVING: ''},
 5034: {GREETING: '',
		QUEST: "Ohhh, it seems I've dropped my 14-Carrot Necklace while taking a walk around this street.\x07Maybe someone pawned it at _toNpcName_'s shop. Can you go see?_where_",
		LEAVING: "Ugh, that pawn shop lacks so much class!\x07Sometimes, I think it should be shut down."},
 5035: {GREETING: '',
		QUEST: "A 14-Carrot Necklace? You wouldn't happen to by working for Tammy Tuber?\x07Ugh, she's so snooty and annoying with her \"Everything must have class policy.\"\x07I'll give this necklace back, but first you must do something for me.\x07I want you take make this street safer and take out a handful of Cogs.",
		LEAVING: ''},
 5036: {GREETING: '',
		QUEST: "Fine, take this necklace back to that snooty _toNpcName_.",
		LEAVING: "Just saying that name makes me shudder..."},
 5037: {GREETING: "Ohhhh my necklace! My beautiful necklace!",
		QUEST: "Finally, those ugly Cog Buildings around here have the least amount of class.\x07Take down some of them and then return to me for a big reward.",
		LEAVING: '',
		COMPLETE: "Ohhhh, the class feels much better around here.\x07Thanks for helping me clean up those filthy low-class Cogs."},

 #DG Task Five
 5040: {QUEST: "_toNpcName_ needs help taking down Cogs that have broken the law._where_"},
 5041: {GREETING: "Greetings _avName_!",
		QUEST: "We've got several Cog crimes going on around town and I need your help to bring them to justice.\x07We just got a report of Penny Pinchers pulling off Pinch and Runs. Go bring them to justice!",
		LEAVING: ''},
 5042: {GREETING: '',
		QUEST: "A report just came in! The Glad Handers are blinding toons with their bright and shiny teeth.\x07They must be stopped!",
		LEAVING: ''},
 5043: {GREETING: '',
		QUEST: "Apparently, those Head Hunters are taking toons from their shops and putting them to work in Cog Headquarters.\x07We can't let this happen! Stop them at once!",
		LEAVING: ''},
 5044: {GREETING: '',
		QUEST: "We're getting alerts of those Legal Eagles arresting toons for laws that don't exist.\x07They soar the skies and sweep those innocent right into Cog prision.\x07This is highly unacceptable! They must be stopped!",
		COMPLETE: "No more reports, _avName_.\x07Take this reward for your hard work.",
		LEAVING: ''},
		
 #DG Task Six
 5050: {QUEST: "_toNpcName_ suspects a suspicious activity going on at the Sellbot Factory._where_"},
 5051: {QUEST: "I have a feeling that those Sellbots are plotting a huge invasion, but I'm not so sure.\x07I need you to shut down a few factories so they won't have enough Cogs for the invasion.",
		COMPLETE: "Turns out I was wrong. It was just another rumor from Donald Frump...\x07Here's a reward for your troubles."},
		
 #DG Task Seven
 5060: {QUEST: "_toNpcName_ is investigating in Sellbot Headquarters and can use your help._where_"},
 5061: {GREETING: '',
		QUEST: "Hey _avName_.\x07As you heard, I'm investigating into Sellbot Headquarters.\x07If you didn't know, Sellbots and most Cogs in general communicate with each other through memos.\x07I want to find out what the head of Sellbot Headquarters, the Vice President, is up to.\x07Go around each part of Sellbot Headquarters and retrieve a memo for me, starting with the Junkyard.",
		LEAVING: ''},
 5062: {GREETING: '',
		QUEST: "Let's read, shall we?\x07\"Dear Sellbots,\"\x07\"As you know, several toons have been breaking into my office and have been snooping around for information.\"\x07\"They even pushed me off the edge, and as you know, THAT HOLE IN THE JUNKYARD ISN'T GOING TO REPAIR ITSELF! GET TO WORK, SLACKERS!\"\x07\"Signed, the Vice President.\"\x07Hmm, not much to learn from here. We already knew this information.\x07Check if any Cogs outside the factory have any useful information.",
		LEAVING: ''},
 5063: {GREETING: '',
		QUEST: "\"Dear Sellbots of the Factory,\"\x07\"Stop leaving Cog Parts out in the open. I've been getting reports of toons taking them and creating disguises.\"\x07\"Anyways, those blueprints for our top secret project, you decide who holds on to them. Whoever it is must have them stick to them like glue.\"\x07\"Signed, the Vice President.\"\x07Now this is information that we need!\x07Go find those blueprints and then return them to me.",
		COMPLETE: "Just as I suspected. These blueprints are encrypted.\x07I'm going to send these to the nearest HQ and see if they can decrypt it.\x07Thanks for your help! Here is your reward...",
		LEAVING: ''},
		
 #DG Task Eight
 5070: {QUEST: "The Travel Agency in this playground has been having very slow business lately because the Cogs give the Toons fear of going on vacation.\x07_toNpcName_ could use your help in stopping those Cogs._where_"},
 5071: {GREETING: '',
		QUEST: "Ahh, yes. As you've heard, my business has been very slow.\x07Those Boardbots scare shopkeepers around here from leaving their shops and taking a nice vacation, which takes away the need for a travel agent.\x07I'm sure if you defeated a bunch of them, they'd feel safer about going on vacation.",
		LEAVING: ''},
 5072: {GREETING: '',
		QUEST: "Ahh, yes. As you've heard, my business has been very slow.\x07Those Sellbots scare shopkeepers around here from leaving their shops and taking a nice vacation, which takes away the need for a travel agent.\x07I'm sure if you defeated a bunch of them, they'd feel safer about going on vacation.",
		LEAVING: ''},
 5073: {GREETING: '',
		QUEST: "Ahh, yes. As you've heard, my business has been very slow.\x07Those Cashbots scare shopkeepers around here from leaving their shops and taking a nice vacation, which takes away the need for a travel agent.\x07I'm sure if you defeated a bunch of them, they'd feel safer about going on vacation.",
		LEAVING: ''},
 5074: {GREETING: '',
		QUEST: "Ahh, yes. As you've heard, my business has been very slow.\x07Those Lawbots scare shopkeepers around here from leaving their shops and taking a nice vacation, which takes away the need for a travel agent.\x07I'm sure if you defeated a bunch of them, they'd feel safer about going on vacation.",
		LEAVING: ''},
 5075: {GREETING: '',
		QUEST: "Ahh, yes. As you've heard, my business has been very slow.\x07Those Bossbots scare shopkeepers around here from leaving their shops and taking a nice vacation, which takes away the need for a travel agent.\x07I'm sure if you defeated a bunch of them, they'd feel safer about going on vacation.",
		LEAVING: ''},
 5076: {GREETING: '',
		QUEST: "Excellent work!\x07I just need one more favor.\x07Toons are also afraid of those Loan Sharks.\x07Whenever they encounter one, it leaves them with a bite they can't forget.\x07I can't send my clients places with those awful Cogs!\x07I want you to defeat 10 of them and then return to me for a nifty reward.",
		COMPLETE: "Well, here you go.",
		LEAVING: ''},
 
 #DG Task Nine
 5080: {QUEST: "_toNpcName_ has felt really uneasy lately and is asking for help._where_"},
 5081: {GREETING: '',
		QUEST: "I can't take those strong Cogs anymore!\x07They're always taking over my shop and destroying my inventory!\x07Oh, _avName_ thank goodness you came to help.\x07Can you please take care of some of the strongest Cogs on this street?",
		LEAVING: ''},
 5082: {GREETING: '',
		QUEST: "Those Mover & Shakers from Sellbot Headquarters love to prank me every other day.\x07They quake outside my shop and break all my shower heads.\x07Can you go teach them a lesson?",
		LEAVING: ''},
 5083: {GREETING: "Ahh!",
		QUEST: "As you were a way, a Name Dropper took one of my shower heads to the factory!",
		COMPLETE: "Thanks for your help! I feel a lot better.\x07Here is something for your troubles...",
		LEAVING: ''},
		
 #DG Task Ten
 5090: {QUEST: "_toNpcName_ has a big scoop and he needs you to interview a client._where_"},
 5091: {GREETING: "Heya, _avName_!",
		QUEST: "I've gotta big scoop on _toNpcName_'s investigation!\x07Toons everywhere have had their sweet treats stolen right under their noses, and they can't seem to figure out the thieves.\x07Ya think ya can get me a full scoop on the investigate?_where_",
		LEAVING: "Get that scoop, fella!"},
 5092: {GREETING: '',
		QUEST: "Here about the sweet treat mystery?\x07I've almost got leads, but I have no way to narrow the culprit down.\x07Before I give you an interview, I want to catch the culprit red handed.\x07I suspect that the Sellbots are the cause of this.\x07Can you defeat some of them and see if the rate of thievery decreases?",
		LEAVING: ''},
 5093: {GREETING: '',
		QUEST: "The rate of sweets being stolen haven't changed...\x07Maybe the Lawbots are the cause of this?",
		LEAVING: ''},
 5094: {GREETING: '',
		QUEST: "Yes! The rate is slowly decreasing!\x07Now we just gotta figure out which Lawbot would have a motive for stealing sweets.\x07I'm thinking it'd be the Bottom Feeders. Defeat some and see if the rate has changed.",
		LEAVING: ''},
 5095: {GREETING: '',
		QUEST: "Nothing...\x07Wait, it has to be those Bloodsuckers!\x07Of course, they're always after sugar because of their super sweet tooth.\x07Defeat some of them and then I'll make a conclusion.",
		LEAVING: ''},
 5096: {GREETING: '',
		QUEST: "Yep. The sweet culprit were the Bloodsuckers, no doubt.\x07The rate has been dropping ever since you've left to defeat them.\x07Go report this back to _toNpcName_.",
		LEAVING: '',
		COMPLETE: "Wowza! What a grand scoop!\x07Thanks for gettin' this for me.\x07I've just gotta give ya a reward for this grand scoop!"},
		
 #DG Task Eleven
 5100: {QUEST: "A major break-in just happened at _toNpcName_'s shop._where_"},
 5101: {GREETING: '',
		QUEST: "A lot of Cogs just broke into my store and after they all leave, I notice that all my flowerpots are gone!\x07Can you get them back for me please?",
		COMPLETE: "Oh, thank you so much.\x07Now if only there was a way for me to repay you...\x07Oh, I know!",
		LEAVING: ''},
		
 #DG Task Twelve
 5110: {QUEST: "It seems that there is a shortage of Gags at _toNpcName_'s shop._where_"},
 5111: {GREETING: '',
		QUEST: "Oh _avName_, I've lost my marbles and I'm going crazy!\x07So go get them back from those level 5+ Cogs!",
		LEAVING: ''},
 5112: {GREETING: '',
		QUEST: "Oh, my marbles! I feel sane again.\x07Now, I need a drink, and I only drink Seltzer from those Cashbots.",
		LEAVING: ''},
 5113: {GREETING: '',
		QUEST: "How refreshing.\x07Now I don't feel safe without my safes...\x07They were taken by the Sellbots for some top secret project.",
		LEAVING: '',
		COMPLETE: "Safe at last."},
		
 #DG Mega Task
 5200: {QUEST: "Oh, it seems that _toNpcName_ has a huge challenge for you.\x07He has seen you helping toons all over town and would like to see if you could complete his really challenging task._where_"},
 5201: {GREETING: "Heya, buddy.",
		QUEST: "So I see you took my challenge. That means there's no backing down now.\x07I will take you through a series of challenges that involves defeating some of the strongest Cogs you've seen.\x07Start by defeating a large amount of level 6+ Cogs.",
		LEAVING: "See ya, buddy."},
 5202: {GREETING: "Welcome back, buddy.",
		QUEST: "I want to see how quickly you can train your gags.\x07Start by earning 400 Throw points.",
		LEAVING: "Good luck, buddy."},
 5203: {GREETING: '',
		QUEST: "Now earn 400 Squirt points.",
		LEAVING: ''},
 5204: {GREETING: "Good job, buddy.",
		QUEST: "Now, I want to see if you can handle those tough Elites.\x07Return to me when you have defeated 20.",
		LEAVING: "Best of luck to ya, buddy."},
 5205: {GREETING: '',
		QUEST: "Now try to defeat 10 Corporate Raiders.\x07You can find them in buildings or in Bossbot HQ.",
		LEAVING: ''},
 5206: {GREETING: '',
		QUEST: "Now try to defeat 10 Legal Eagles.\x07You can find them in buildings or in Lawbot HQ.",
		LEAVING: ''},
 5207: {GREETING: '',
		QUEST: "Now try to defeat 10 Loan Sharks.\x07You can find them in buildings or in Cashbot HQ.",
		LEAVING: ''},
 5208: {GREETING: '',
		QUEST: "Now try to defeat 10 Minglers.\x07You can find them in buildings or in Sellbot HQ.",
		LEAVING: ''},
 5209: {GREETING: '',
		QUEST: "Now try to defeat 5 Big Fish.\x07You can find them in Boardbot buildings.",
		LEAVING: ''},
 5210: {GREETING: "Fantastic work, buddy!",
		QUEST: "Now for an even tougher challenge.\x07I want you to defeat 5 4+ story Cog Buildings.",
		LEAVING: ''},
 5211: {GREETING: "Excellent job, buddy!",
		QUEST: "Time to steer our focus away from the playgrounds in Toontown and onto Sellbot HQ.\x07In any Cog HQ, you can find early developed and incomplete Cogs called Skelecogs.\x07They roam around Cog HQ Courtyards and inside the facilities.\x07I want you to defeat 15 Skelecogs in Sellbot HQ, whether it's outside or inside the factory.",
		LEAVING: "See ya, buddy."},
 5212: {GREETING: "Good job, buddy.",
		QUEST: "Now I want you to defeat 48 Cogs in the factory.\x07Actually, if you take out all the Cogs in the factory, you should be done with this task.",
		LEAVING: ''},
 5213: {GREETING: '',
		QUEST: "Finally, I want you to gather a group of toons, infiltrate the Sellbot Lobby, and then defeat the Senior Vice President.\x07This is a dangerous job, and you must be prepared for the worst.\x07It's best if you train your gags before attempting this challenge.",
		LEAVING: '',
		COMPLETE: "Wow, you really did a great job with this challenge.\x07Take this huge reward for your success."},
		
 #MML Task One
 6000: {QUEST: "_toNpcName_ wants you to infiltrate the mints in the Cashbot Headquarters._where_"},
 6001: {GREETING: "",
		QUEST: "Ah, you're here about the mint situation, huh?\x07Let me explain: The Coin Mints are a threat to the citizens of Minnie's Melodyland.\x07According to my theory, if the Cogs in the Coin Mint activate all the stompers at once, it could cause a wicked earthquake that could destroy Minnie's Melodyland.\x07Luckily, the Cashbots don't know this yet.\x07I want you to defeat some of those workers in the Coin Mint before they find out about this.",
		LEAVING: ''},
 6002: {GREETING: '',
		QUEST: "Oh no!\x07I think some Robber Barons were eavesdropping on our conversation!\x07They went back to the Coin Mint. Go stop them before the news spreads!",
		LEAVING: '',
		COMPLETE: "While you were away, I did some recalculations.\x07Well, it seems that my theory was... rather wrong.\x07Yeah, sorry for wasting your time. Let me make it up to you."},

 #MML Task Two		
 6010: {QUEST: "_toNpcName_ isn't able to repair customer tires with those Cogs bugging him._where_"},
 6011: {GREETING: '',
		QUEST: "Oh, _avName_, you've gotta help me!\x07I keep trying to repair these tires and a bunch of Boardbots come in when I'm finished and pop them all.\x07They have no right to do that!\x07Please go defeat several of them while I repair more tires.",
		LEAVING: ''},
 6012: {GREETING: '',
		QUEST: "Perfect. Got these tires repaired with no issues from those Boardbots.\x07In fact, could you make a couple deliveries for me?\x07Start by returning this tire to _toNpcName_._where_",
		LEAVING: ''},
 6013: {GREETING: '',
		QUEST: "Oh hey, my tire!\x07Thank you, but may I ask for a favor?\x07See, the reason I got into an accident was because I was driving behind a Mr. Hollywood.\x07He thought it was funny to shine those bright teeth on my windshield and I couldn't see where I was going.\x07Those Mr. Hollywoods are a threat to toons everywhere and they must be punished.\x07Go out and defeat several of them.",
		LEAVING: ''},
 6014: {GREETING: '',
		QUEST: "Good job on those Hollywoods.\x07_toNpcName_ just called to ask you to return to him.",
		LEAVING: ''},
 6015: {GREETING: '',
		QUEST: "Alright, next delivery goes to _toNpcName_._where_",
		LEAVING: ''},
 6016: {GREETING: '',
		QUEST: "Ah, my tire.\x07Thanks, but I need some help real quick if you don't mind.\x07Cogs everywhere have been stealing and destroying Toons karts, claiming them to be theirs and committing insurance fraud.\x07Now, there's no way I can prove it so I have to give them payment regardless.\x07If you could defeat a lot of Cogs, that'd show them not to mess with my insurance.",
		LEAVING: ''},
 6017: {GREETING: '',
		QUEST: "_toNpcName_ just called. He wants to see you again.",
		LEAVING: '',
		COMPLETE: "Thank you for delivering those tires for me.\x07I've got a reward for your help..."},
		
 #MML Task Three
 6020: {QUEST: "_toNpcName_ has a certain issue with the Mint Supervisors.\x07I'm not sure why, but can you check it out anyways?_where_"},
 6021: {GREETING: '',
		QUEST: "Hey _avName_.\x07Those Supervisors that run the Cashbot Mints are just so uncool.\x07I asked them to fund my shop and they refused, so I think you should go teach a few a lesson.\x07What? You think I'm being unreasonable?\x07Stop being uncool and just do it.",
		LEAVING: "Stay cool.",
		COMPLETE: "Groovy, thanks for the help.\x07Here's a cool reward..."},
		
 #MML Task Four
 6030: {QUEST: "_toNpcName_ can't enjoy a meal without those Cashbots interrupting him._where_"},
 6031: {GREETING: '',
		QUEST: "Heya _avName_.\x07Those-a darn Cashbots are always-a takin' my lunch.\x07I was just enjoying a bologna sandwich and then a Cashbot comes-a in here and takes it to the mint.\x07He said that he needed HIS lunch break.\x07Why couldn't he just get-a his own lunch?\x07Could you-a get my delicious sandwich back for me please?",
		LEAVING: ''},
 6032: {GREETING: '',
		QUEST: "Oh-a no!\x07I went to get a meatball sub while you were away and another Cashbot came in and-a took it!\x07He also needed a lunch break and refuses to-a pay for his own meals.\x07Can you-a get that back for me please?",
		LEAVING: '',
		COMPLETE: "Oh-a thank you!"},
		
 #MML Task Five
 6040: {QUEST: "_toNpcName_'s antique shop has just been robbed._where_"},
 6041: {GREETING: '',
		QUEST: "Oh thank goodness you're here, _avName_. Maybe you could help me?\x07All of my antiques were taken by the Cogs.\x07First, I'll need all my old silverware back.\x07I think those were taken by the Cashbots...",
		LEAVING: ''},
 6042: {GREETING: '',
		QUEST: "Oh thank goodness you're here, _avName_. Maybe you could help me?\x07All of my antiques were taken by the Cogs.\x07First, I'll need all my old silverware back.\x07I think those were taken by the Lawbots...",
		LEAVING: ''},
 6043: {GREETING: '',
		QUEST: "Ooo you got them back.\x07Next, I need my old clocks back from the Sellbots.",
		LEAVING: ''},
 6044: {GREETING: '',
		QUEST: "Ooo you got them back.\x07Next, I need my old clocks back from the Bossbots.",
		LEAVING: ''},
 6045: {GREETING: '',
		QUEST: "Finally, I'll need my old tea sets back from those Boardbots.",
		COMPLETE: "Thank you so much for all your help.\x07Here's your reward...",
		LEAVING: ''},

 #MML Task Six
 6050: {QUEST: "_toNpcName_ is a great electric keyboard player and people really want to hire her for special gatherings.\x07However, due to the amount of issues she has had with the Cogs, she retired and refuses to play anymore.\x07The toons around here would really like to see her come out of retirement, so see what you could do to help out._where_"},
 6051: {GREETING: '',
		QUEST: "Come out of retirement?\x07No way! Not with those strong Cogs around.\x07I'll need a few favors before I decide on this.\x07Start by destroying some of those high leveled Cogs.",
		LEAVING: ''},
 6052: {GREETING: '',
		QUEST: "Long ago, the Cashbots decided to have their own gathering in the coin mint.\x07They stole instruments from all over the town, including my prize electric keyboard.\x07I need you to get that back if you want me to play at all.",
		LEAVING: ''},
 6053: {GREETING: '',
		QUEST: "There's no way I'm leaving this shop with those Cog Buildings around here!",
		LEAVING: '',
		COMPLETE: "Alright, you've convinced me to come out of retirement.\x07Thanks for all those favors I asked you to do. Let me make it up to you."},
		
 #MML Task Seven
 6060: {QUEST: "_toNpcName_'s job is to settle in new toons and have them feel comfy around the new environment.\x07This time, he's planning a surprise birthday party for one of the new toons and needs help setting up._where_"},
 6061: {GREETING: '',
		QUEST: "Hey, _avName_!\x07I need your help. See, I'm setting up a surprise party for _toNpcName_ and I'm not nearly ready!\x07First, I need him to have a reason to come here, so deliver this note to him saying we're having a secret gathering of important toons in Minnie's Melodyland._where_",
		LEAVING: ''},
 6062: {GREETING: '',
		QUEST: "What's this note?\x07\"An important gathering for important people.\"\x07Gee, I'd love to go but I don't want to leave this shop until the amount of high leveled Cashbots are decreased dramatically.",
		LEAVING: ''},
 6063: {GREETING: '',
		QUEST: "Alright, I'll go to this super important meeting.\x07Hmm, that's strange. It's planned on the same day as my birthday...",
		LEAVING: ''},
 6064: {GREETING: '',
		QUEST: "So he'll come? Great!\x07Now we'll just need a birthday cake for him.",
		LEAVING: ''},
 6065: {GREETING: '',
		QUEST: "Oh, this looks delicious!\x07Next, I'll need a few storm clouds.\x07Whenever toons throw a party, they surround their shops with storm clouds to prevent Cogs from crashing the party.",
		COMPLETE: "Thank you so much for all your help.\x07I'm sure he'll have a blast!\x07Here's a reward for you...",
		LEAVING: ''},
		
 #MML Task Eight
 6070: {QUEST: "_toNpcName_ is having a conflict with those rank eight Cogs._where_"},
 6071: {GREETING: "What's with all this swagger?",
		QUEST: "Here I am just minding my own business when suddenly, a bunch of strong Cogs come in here raiding my sporting goods!\x07Can't thou lend me a hand and get my equipment back?\x07First, those Big Cheeses broke in here and took all my golf clubs.",
		LEAVING: ''},
 6072: {GREETING: "What's with all this swagger?",
		QUEST: "Here I am just minding my own business when suddenly, a bunch of strong Cogs come in here raiding my sporting goods!\x07Can't thou lend me a hand and get my equipment back?\x07First, those Robber Barons broke in here and took all my golf clubs.",
		LEAVING: ''},
 6073: {GREETING: '',
		QUEST: "Then, those Head Honchos came in here and took all my Soccer Balls.",
		LEAVING: ''},
 6074: {GREETING: '',
		QUEST: "Then, those Mr. Hollywoods came in here and took all my Soccer Balls.",
		LEAVING: ''},
 6075: {GREETING: '',
		QUEST: "Then, those Big Wigs came in here and took all my Soccer Balls.",
		LEAVING: ''},
 6076: {GREETING: '',
		QUEST: "I thank thee for getting my equipment back, but the thought of those higher up Cogs just infuriates me!\x07Can thou do me a favor and defeat those higher up Cogs.",
		COMPLETE: "I thank thee.\x07Thy shall have a grand reward...",
		LEAVING: ''},
		
 #MML Task Nine
 6080: {QUEST: "_toNpcName_ needs help investigating Cashbot Headquarters._where_"},
 6081: {GREETING: '',
		QUEST: "Let me tell you a little story.\x07The other day, a couple of friends and I decided to infiltrate the Cashbot Coin Mint.\x07Less than halfway through the mint, we went sad. It seemed that those Skelecogs were a lot tougher than they should be.\x07As I was forced out of the mint, something caught my eye. I saw a file labeled \"TOP SECRET PLANS\"\x07I need you to infiltrate that Coin Mint and get those plans.\x07I'm pretty sure they let the higher up Cogs hold on to those types of important files...",
		LEAVING: ''},
 6082: {GREETING: '',
		QUEST: "Ugh, I can't read these plans.\x07Maybe _toNpcName_ can read these plans better than I could._where_",
		LEAVING: ''},
 6083: {GREETING: '',
		QUEST: "Ah, Susan Soprano just called to inform me about these plans.\x07Let's see, it seems like the Coin Mint Skelecogs have been upgraded and are about to invade Toontown!\x07We can't let those strong Skelecogs invade us! Stop them quickly!",
		COMPLETE: "Great job citizen!",
		LEAVING: ''},
		
 #MML Task Ten
 6090: {QUEST: "Not sure why, but _toNpcName_ needs help on her broadcast._where_"},
 6091: {GREETING: '',
		QUEST: "Breaker, breaker. This is Telly Prompter LIVE with some action news.\x07Today, I have _avName_ who has agreed by taking this task to help deal with the massive flood of Elite Cogs introduced to Toontown.\x07If they complete this task, then they shall be rewarded strongly.",
		LEAVING: "That's all for the news! We'll be back later!",
		COMPLETE: "This just in, _avName_ has swept the streets clean of a handful of Elite Cogs.\x07Here's that reward that was promised..."},
		
 #MML Task Eleven
 6100: {QUEST: "Need some experience?\x07_toNpcName_ is offering a lot to anyone who can provide him with some assistance._where_"},
 6101: {GREETING: '',
		QUEST: "Yeah, I can hit you up with some big experience points if you do me a few favors.\x07First, those Bossbots are always getting on my nerves.\x07Defeat a bunch of them and then come back to me.",
		LEAVING: ''},
 6102: {GREETING: '',
		QUEST: "Yeah, I can hit you up with some big experience points if you do me a few favors.\x07First, those Lawbots are always getting on my nerves.\x07Defeat a bunch of them and then come back to me.",
		LEAVING: ''},
 6103: {GREETING: '',
		QUEST: "Now, I'm getting quite sick of those Toxic Managers making the streets unsafe around here.\x07They let their Acid Rain hit the streets and it burns the feet of the toons who walk on it.\x07Defeat several of them for the greater good.",
		LEAVING: ''},
 6104: {GREETING: '',
		QUEST: "Now, I'm getting quite sick of those Downsizers bringing toons down.\x07Whenever I hang out with a friend who was attacked by a Downsizer, they act all depressed and aren't any fun.\x07Defeat several of them for the greater good.",
		LEAVING: ''},
 6105: {GREETING: '',
		QUEST: "Those tall Sellbot Buildings are just so ugly!\x07Take down some of them and then return to me for one last thing.",
		LEAVING: ''},
 6106: {GREETING: '',
		QUEST: "Those tall Cashbot Buildings are just so ugly!\x07Take down some of them and then return to me for one last thing.",
		LEAVING: ''},
 6107: {GREETING: '',
		QUEST: "Those tall Boardbot Buildings are just so ugly!\x07Take down some of them and then return to me for one last thing.",
		LEAVING: ''},
 6108: {GREETING: '',
		QUEST: "Finally, rumor has it that there is a golden delicious salmon swimming around the ponds of Minnie's Melodyland.\x07If you could catch that for me to have for dinner, then I will give you your big reward.",
		LEAVING: '',
		COMPLETE: "Well, I guess a deal is a deal."},
		
 #MML Task Twelve
 6110: {QUEST: "_toNpcName_ was about to go traveling but his passport was stolen._where_"},
 6111: {GREETING: '',
		QUEST: "Please help me! A Legal Eagle stole my passport.\x07He said it wasn't legal without any evidence and just took it! I need it back so I can go travel.",
		COMPLETE: "Thank you.",
		LEAVING: ''},
		
 #MML Mega Task
 6200: {QUEST: "It seems like the Cogs have launched a massive invasion against Minnie's Melodyland.\x07The streets were flooded with them all of a sudden and it seems they have ruined the tune of the playground.\x07_toNpcName_ needs your help getting it back, as well as the other citizens of Minnie's Melodyland._where_"},
 6201: {GREETING: '',
		QUEST: "Oh, you must be here about the issue with the tune of this playground.\x07Let me explain, not long ago, the Cogs were ordered to invade Minnie's Melodyland and make the peaceful and beautiful sound of the playground come to a stop.\x07Nobody is certain who the leader of this operation is, and I am trying to figure out who it could be.\x07While I investigate, could you go see _toNpcName_ to see how you could help fix the tune around here?_where_",
		LEAVING: ''},
 6202: {GREETING: '',
		QUEST: "Oh, it's just terrible what happened here.\x07The Cogs took all the beautiful music notes that power the instruments and sound around here.\x07You must get them back for us.\x07Once you collect them all, bring them to me and I'll redistribute them properly.",
		LEAVING: ''},
 6203: {GREETING: '',
		QUEST: "Excellent!\x07I'll get these notes back in the right places they need to be in.\x07Go see if _toNpcName_ still needs any help.",
		LEAVING: ''},
 6204: {GREETING: '',
		QUEST: "I'm still investigating on who the leader may be, but _toNpcName_ is in charge of taking down the Cog Buildings.\x07Go see if you can help her._where_",
		LEAVING: ''},
 6205: {GREETING: '',
		QUEST: "Ah, you're here about the buildings, huh?\x07Well, if the Cogs are going to take over our buildings, we're going to need to take them back.\x07Bring down some of the tallest buildings around here.",
		LEAVING: ''},
 6206: {GREETING: '',
		QUEST: "While you were out defeating buildings, _toNpcName_ called to say that she had some news for you.",
		LEAVING: ''},
 6207: {GREETING: '',
		QUEST: "While you were away, I talked with _toNpcName_ and he claims to have some sort of clue on how we can find out who the leader is.\x07Go see what you can do for him._where_",
		LEAVING: ''},
 6208: {GREETING: '',
		QUEST: "Ah, you must've came from Barbara, hmm?\x07I found out that a few Cogs were given memos to launch the attack.\x07If we can figure out who signed it, that's who the leader is.",
		LEAVING: ''},
 6209: {GREETING: '',
		QUEST: "No, the signature is scratched off here. Must've been a worn out memo.\x07I know. Maybe a Big Cheese has a better memo.\x07After all, the Cogs at the top of the corporate ladder get the most classified information.",
		LEAVING: ''},
 6210: {GREETING: '',
		QUEST: "No, the signature is scratched off here. Must've been a worn out memo.\x07I know. Maybe a Big Wig has a better memo.\x07After all, the Cogs at the top of the corporate ladder get the most classified information.",
		LEAVING: ''},
 6211: {GREETING: '',
		QUEST: "No, the signature is scratched off here. Must've been a worn out memo.\x07I know. Maybe a Robber Baron has a better memo.\x07After all, the Cogs at the top of the corporate ladder get the most classified information.",
		LEAVING: ''},
 6212: {GREETING: '',
		QUEST: "No, the signature is scratched off here. Must've been a worn out memo.\x07I know. Maybe a Mr. Hollywood has a better memo.\x07After all, the Cogs at the top of the corporate ladder get the most classified information.",
		LEAVING: ''},
 6213: {GREETING: '',
		QUEST: "No, the signature is scratched off here. Must've been a worn out memo.\x07I know. Maybe a Head Honcho has a better memo.\x07After all, the Cogs at the top of the corporate ladder get the most classified information.",
		LEAVING: ''},
 6214: {GREETING: '',
		QUEST: "Okay, let's check out the signature...\x07\"Signed, the CFO.\"\x07Bingo! It was all planned by our neighboring Cashbot fiends! I should've known.\x07Well, if they're going to invade our town, let's just invade their workplace.\x07Go and stop those workers in the Cashbot Coin Mint. That'll slow down their production progress.",
		LEAVING: ''},
 6215: {GREETING: '',
		QUEST: "Next, shut down a Dollar Mint, the higher up Mint in Cashbot Headquarters.",
		LEAVING: ''},
 6216: {GREETING: '',
		QUEST: "Now I want you to show that CFO a lesson and teach him not to mess with us.\x07Gather a group of toons and get out there and defeat him!",
		COMPLETE: "The number of Cogs around here have decreased a ton.\x07I'm pretty sure that CFO learned his lesson, or at least I hope he did.\x07Here, take this as a thanks on behalf of the citizens of Minnie's Melodyland...",
		LEAVING: ''},
		
 #TB Task One
 7000: {QUEST: "_toNpcName_ is offering experience points to those who can help her with a small job._where_"},
 7001: {GREETING: '',
		QUEST: "Hey _avName_. I need you to do me a couple favors.\x07Firstly, I lent a tuxedo to _toNpcName_ awhile back and he's overdue for returning it.\x07Can you go see if he can return it to me?_where_",
		LEAVING: ''},
 7002: {GREETING: '',
		QUEST: "Oh, you came in just in time, _avName_.\x07I need your help.\x07The Bossbots raided my building and once they left, I noticed that my tuxedo was missing!\x07Can you get that back for me please?",
		LEAVING: ''},
 7003: {GREETING: '',
		QUEST: "Awesome! Thanks for getting that back for me.\x07Now, why did you come here in the first place?\x07Oh, you needed to return that tuxedo to _toNpcName_, hmm?\x07Alright, tell her I say thanks.",
		LEAVING: ''},
 7004: {GREETING: '',
		QUEST: "Alright, that's one job done.\x07Now I want you to defeat some of those high leveled Cogs for me. They make me feel uneasy whenever I work here.",
		LEAVING: '',
		COMPLETE: "Thanks for taking care of those Cogs.\x07Here, this is for you..."},
		
 #TB Task Two
 7010: {QUEST: "Oh no. _toNpcName_ is running his mouth again about those Lawbots..._where_"},
 7011: {GREETING: '',
		QUEST: "Those no good Lawbots.\x07They come into our town, make fake laws, destroy our buildings, they need to be stopped.\x07I think we should build a wall blocking all ties between Lawbot Headquarters and The Brrrgh. It'll be huge.\x07However, before we cut off all ties, I must know their secrets.\x07I need you to snoop around, gather any important information you can find.",
		LEAVING: "Did I forget to mention that we'd make those Lawbots pay for the wall too?"},
 7012: {GREETING: '',
		QUEST: "Excellent. Now I need some blueprints.\x07Go find them while I analyze these plans.",
		LEAVING: '',
		COMPLETE: "Hmm. These plans state that they plan to extend the Lawbot Headquarters.\x07However, with these new blueprints, we can get started on that wall where they plan to extend.\x07All thanks to you, citizen.\x07Let me give you a HUGE reward."},

 #TB Task Three
 7020: {QUEST: "_toNpcName_ is investigating in the unusual changes in temperature around The Brrrgh and needs helps conducting research._where_"},
 7021: {GREETING: '',
		QUEST: "This is no good, _avName_.\x07The temperatures around this playground are going higher than zero degrees celsius which is not normal for this type of environment.\x07I need you to get me some temperature readings from my good friend _toNpcName_._where_",
		LEAVING: ''},
 7022: {GREETING: '',
		QUEST: "Need some temperature readings?\x07I'd love to help you out, but all my external temperature sensors for The Brrrgh have been stolen from the Cogs.\x07I need you to get new ones for me. Start by getting one from Walrus Way.",
		LEAVING: ''},
 7023: {GREETING: '',
		QUEST: "Let me get the temperature readings from this while you get a new sensor from Sleet Street.",
		LEAVING: ''},
 7024: {GREETING: '',
		QUEST: "Next I'll need one on that newly built street, Arctic Avenue.",
		LEAVING: ''},
 7025: {GREETING: '',
		QUEST: "And finally, one right here on beautiful Polar Place.",
		LEAVING: ''},
 7026: {GREETING: '',
		QUEST: "Good grief! These reading are on the roof!\x07Take these to _toNpcName_ right away.",
		LEAVING: ''},
 7027: {GREETING: '',
		QUEST: "Just as I've thought, Polar Place temperatures are increasing dramatically over time.\x07This street is also increasing a little in temperature, and Walrus Way and Sleet Street are unaffected.\x07From the looks of this, all streets near Lawbot Headquarters are increasing in temperature. They must be the cause of this.\x07Go shut down a few A-Offices and see if that takes down some steam.",
		LEAVING: '',
		COMPLETE: "Hmm, I can't really tell if this has changed anything around here.\x07I'll need time to do some analyzing, but I'll be sure to get back to you.\x07In the meantime, here's a reward for your help..."},
		
 #TB Task Four
 7030: {QUEST: "_toNpcName_ needs help opening his store._where_"},
 7031: {GREETING: '',
		QUEST: "Hey, _avName_. I could really use your help.\x07I was getting ready to open for business, when suddenly, my buildings was invaded by Big Wigs.\x07They stole all my Ice Cream Cones and I need them back as soon as possible!\x07Can you please go get them for me?",
		LEAVING: ''},
 7032: {GREETING: '',
		QUEST: "Hey, _avName_. I could really use your help.\x07I was getting ready to open for business, when suddenly, my buildings was invaded by Mr. Hollywoods.\x07They stole all my Ice Cream Cones and I need them back as soon as possible!\x07Can you please go get them for me?",
		LEAVING: ''},
 7033: {GREETING: '',
		QUEST: "Hey, _avName_. I could really use your help.\x07I was getting ready to open for business, when suddenly, my buildings was invaded by Big Cheeses.\x07They stole all my Ice Cream Cones and I need them back as soon as possible!\x07Can you please go get them for me?",
		LEAVING: ''},
 7034: {GREETING: '',
		QUEST: "Hey, _avName_. I could really use your help.\x07I was getting ready to open for business, when suddenly, my buildings was invaded by Robber Barons.\x07They stole all my Ice Cream Cones and I need them back as soon as possible!\x07Can you please go get them for me?",
		LEAVING: ''},
 7035: {GREETING: '',
		QUEST: "Thank you so much for getting those cones back for me!\x07Now, while I continue to set up for when I open, can you take down some buildings around here?\x07The customer should never feel intimidated when going to their favorite ice cream store.",
		LEAVING: '',
		COMPLETE: "Thanks for the help."},
	
 #TB Task Five
 7040: {QUEST: "Walt has been experiencing issues with his plumbing supplies._where_"},
 7041: {GREETING: "Hey, _avName_.",
		QUEST: "I was wondering when you'd get here.\x07I need you to go see my buddy Blue Lou.\x07I need some pliers and he's the only toon I know that would supply them._where_",
		LEAVING: ''},
 7042: {GREETING: '',
		QUEST: "Pliers? I don't have any in stock, but I know where to find them.\x07In order to make them, I need some Ice Cubes from this here playground.",
		LEAVING: ''},
 7043: {GREETING: '',
		QUEST: "Now I need you to take these to _toNpcName_, he'll know what to do with these._where_",
		LEAVING: ''},
 7044: {GREETING: '',
		QUEST: "You need me to make some pliers?\x07Well, my business works in awhile where all material for my items come from sturdy dried ice.\x07These ice cubes are just not ready.\x07Let me take these and make a fresh batch of dried ice.\x07While I do so, I need you to defeat some of those high leveled Cogs out there.",
		LEAVING: ''},
 7045: {GREETING: '',
		QUEST: "While you were gone, I took the courtesy of making these sturdy pliers.\x07Take 'em to Walt for me, will ya?",
		LEAVING: ''},
 7046: {GREETING: '',
		QUEST: "Perfect!\x07Now, I need a...\x07Uh, what did I need again?\x07Sorry, I suffer a bit from short-term memory.\x07I'm afraid it'll take me awhile to remember...\x07Can you do me a favor and take down a couple of those tallest buildings for me while I try to think?",
		LEAVING: ''},
 7047: {GREETING: '',
		QUEST: "I remembered now.\x07I need a Plumber's Snake. Can't be a good plumber without it.\x07I think _toNpcName_ has an extra one in stock that he can give to me._where_",
		LEAVING: ''},
 7048: {GREETING: '',
		QUEST: "A Plumber's Snake?\x07Yeah, I can give you one if you could defeat some of those annoying Sellbots for me.",
		LEAVING: ''},
 7049: {GREETING: '',
		QUEST: "Alright, a deal's a deal.\x07Take these back to Walt right away.",
		COMPLETE: "Awesome!\x07Now I'll need a...\x07Oh, there's my short-term memory again.\x07You know, I don't want this to hold you back, so once I remember, I'll go out and get the supplies myself.\x07Anyways, here's a reward for all your help...",
		LEAVING: ''},
		
 #TB Task Six
 7050: {QUEST: "Oh no! It seems the Cogs have taken all of _toNpcName_'s hats!_where_"},
 7051: {GREETING: '',
		QUEST: "Oh man, _avName_. This is just awful!\x07The Cogs busted in here and took all of my hats!\x07I need you to get them all back to me!\x07I'd like you to start by getting back all the Top Hats from the Connoisseurs.\x07Let's see, I think there were about 12 of them...",
		LEAVING: ''},
 7052: {GREETING: '',
		QUEST: "Ooo shiny.\x07I mean, uh, now I'll need some pirate hats back in my stock.\x07I didn't see which Cogs took them, but I'm positive it was those ugly Corporate Raiders.",
		LEAVING: ''},
 7053: {GREETING: '',
		QUEST: "Yarrrgh did it!\x07No? Didn't like that one?\x07Well, now I'll need my fedoras back.\x07There were about 15 of them, and I think they were taken by the Sellbots.",
		LEAVING: ''},
 7054: {GREETING: '',
		QUEST: "Yarrrgh did it!\x07No? Didn't like that one?\x07Well, now I'll need my fedoras back.\x07There were about 15 of them, and I think they were taken by the Bossbots.",
		LEAVING: ''},
 7055: {GREETING: '',
		QUEST: "Yarrrgh did it!\x07No? Didn't like that one?\x07Well, now I'll need my fedoras back.\x07There were about 15 of them, and I think they were taken by the Cashbots.",
		LEAVING: ''},
 7056: {GREETING: '',
		QUEST: "Hmm, I can't seem to track down where my Aviator Hats could be.\x07My good friend _toNpcName_ may have borrowed them, but I can't seem to remember.\x07Can you go ask her if she has them?_where_",
		LEAVING: ''},
 7057: {GREETING: 'H-h-hey, _avName_.',
		QUEST: "A-a-a-aviator Hats?\x07Y-y-yes I h-have them.\x07B-b-but I can't move without my m-m-mittens.\x07A c-c-cog took them not l-l-long ago, so they sh-should be around h-h-here.",
		LEAVING: 'G-g-good luck!'},
 7058: {GREETING: "Oh y-y-you got them b-b-back for me.",
		QUEST: "Ahhh, that's much better.\x07Let me just reach below the desk and...\x07Here you go! Take these to _toNpcName_ right away!",
		LEAVING: ''},
 7059: {GREETING: '',
		QUEST: "Yep, that's all of my hats alright!\x07Now, I'm worried that those Lawbots have been planning to take over my building and take all my hats again.\x07To intimidate them, I want you to defeat some of their highest buildings. That'll teach 'em to back off.",
		LEAVING: '',
		COMPLETE: "You have done a wonderful job in helping me.\x07Thank you so much for all your help.\x07Let me give you a big reward..."},
		
 #TB Task Seven
 7060: {QUEST: "_toNpcName_ has a bad feeling about the Lawbot Offices._where_"},
 7061: {GREETING: '',
		QUEST: "Hey, _avName_. I've got a bad feeling about something...\x07You know how magnets work? They've got a North and a South pole, right?\x07Well, I feel like there's a stronger north pole in Toontown and that's because of the overpopulation of Lawbots in Lawbot Headquarters.\x07I need you to defeat a handful of those Lawbots working in those offices.",
		COMPLETE: "Things are looking normal again.",
		LEAVING: ''},
		
 #TB Task Eight
 7070: {QUEST: "_toNpcName_ needs help gathering ingredients for his world famous hambrrrghers._where_"},
 7071: {GREETING: '',
		QUEST: "Oh, you're just in time _avName_.\x07I don't have all that I need to create my signature burger, \"The Hambrrrghers.\"\x07See, I've already gathered the meat, but it didn't occur to me that I was missing some hamburger rolls.\x07I need some rolls, specifically from _toNpcName_. She makes the best kinds of bread._where_",
		LEAVING: ''},
 7072: {GREETING: '',
		QUEST: "Hamburger rolls?\x07Yeah, I can get you some, but I'll need you to do me a favor first.\x07The Bossbots around here decided to break into this here store and take all my loaves of bread.\x07If you get them all back for me, I'll gladly give you these here hamburger rolls.",
		LEAVING: ''},
 7073: {GREETING: '',
		QUEST: "I reckon a deal's a deal.\x07Take these here rolls to _toNpcName_.",
		LEAVING: ''},
 7074: {GREETING: '',
		QUEST: "Perfect! These rolls smell great too.\x07Next, I'll need some of the best kind of cheddar cheese in town.\x07I hate to do this, but I'll need you to get it from _toNpcName_ down in Acorn Acres.\x07It's the only cheese shop in this town._where_",
		LEAVING: ''},
 7075: {GREETING: '',
		QUEST: "Cheddar cheese?\x07I'm not sure if I have any. I could always check the storage room, but I've lost the key.\x07While I look for it, could you do me a huge favor?\x07Earlier, when I was sampling off some slices of swiss cheese, The Big Cheeses decided to come in here and take all 10 of my lumps!\x07Could you get those back for me?",
		INCOMPLETE_PROGRESS: "Nope, still haven't found that key...",
		LEAVING: ''},
 7076: {GREETING: '',
		QUEST: "Ah, yes. You got those lumps back.\x07Lucky for you, I found the storage key AND had some cheddar cheese in stock.\x07I'll be glad to give these to you for your hard work.",
		LEAVING: ''},
 7077: {GREETING: '',
		QUEST: "Sweet! You got the cheddar!\x07However, while you were away, a Lawbot came in here and took my best grill to use at a cookoff in the Lawbot District Attorney Office.\x07I don't understand why they'd have a cookoff in such a workspace, but you have to get it back for me!",
		LEAVING: '',
		COMPLETE: "Woo! You got them back for me!\x07I owe you a free hambrrrgher, but for now, take this as my thanks."},
		
 #TB Task Nine
 7080: {QUEST: "A toon's home is very special in one's heart.\x07_toNpcName_ values The Brrrgh like his home and wants nothing more than to protect it from those filthy Cogs._where_"},
 7081: {GREETING: '',
		QUEST: "The Brrrgh used to be a great and fun place.\x07We'd build snowmen, have snowball fights, make snow angels, all of that fun stuff.\x07Now, with those strict Elite Cogs roaming the place, we can't even leave our own shops!\x07I want this place to feel like a home again, not just for me, but for everyone in The Brrrgh.\x07Oh, _avName_, you just have to defeat those Elite Cogs for our sake!",
		LEAVING: '',
		COMPLETE: "Home, sweet, home."},
	
 #TB Task Ten	
 7090: {QUEST: "_toNpcName_ needs help retrieving a shipment of Solar Powered Blankets safely._where_"},
 7091: {GREETING: '',
		QUEST: "Welcome, _avName_!\x07As you may know, The Brrrgh gets very little sunlight and Solar Powered Blankets require it in order to work.\x07Every time I create a new batch, I send 'em over to _toNpcName_ down in Daisy Gardens for the most amount of sunlight.\x07This method provides the most amount of energy for the blankets, which means they last for a very long amount of time.\x07However, the post offices around Toontown have had packing issues with them, such as some of the blankets short-circuiting during delivery, and have stopped supporting shipment of the blankets.\x07I'll need you to collect those blankets for me._where_",
		LEAVING: ''},
 7092: {GREETING: '',
		QUEST: "Ah, you're here to pick up Ray's blankets?\x07I'm afraid they're not fully charged yet.\x07While they're still charging, I want to send you on a small mission.\x07Rumor has it that the Lawbots are trying to find away to take away the sunshine from Daisy Gardens so that we can't have our flowers.\x07Without our flowers, we'd have no spirit.\x07If you could defeat some of their strongest workers, I'll bet that'd distract them from their plans.",
		INCOMPLETE_PROGRESS: "The blankets aren't fully charged yet.\x07Have you finished taking down those workers?",
		LEAVING: ''},
 7093: {GREETING: '',
		QUEST: "Ah, the blankets just finished charging.\x07Take these back to _toNpcName_.",
		LEAVING: ''},
 7094: {GREETING: '',
		QUEST: "Awesome!\x07Now, I'll need one last favor and then I'll give you a big reward.\x07Although it's usually cloudy, we still have little rays of sunlight shine down here every now and then.\x07Customers will need that sunshine, no matter how weak it is, to charge up once they've used all the energy from the blankets.\x07However, those tall Cog Buildings take away those little rays of sunshine from us.\x07Please defeat some of the tallest buildings around here.",
		COMPLETE: "I appreciate all your help.\x07Here's a reward out of gratitude...",
		LEAVING: ''},
		
 #TB Task Eleven
 7100: {QUEST: "The Cogs are causing some dential issues for _toNpcName_._where_"},
 7101: {GREETING: "Tsk, tsk.",
		QUEST: "Toons keep coming in here with cavities.\x07I've noticed quite a trend with these cavities though.\x07Each toon comes in here saying that the last thing they did was fighting a Cashbot.\x07I'm sure those Cashbots are damaging our toons' teeth.\x07I don't know how they are doing so, but they must be stopped.",
		LEAVING: "Keep those teeth shiny."},
 7102: {GREETING: "Tsk, tsk.",
		QUEST: "Toons keep coming in here with cavities.\x07I've noticed quite a trend with these cavities though.\x07Each toon comes in here saying that the last thing they did was fighting a Sellbot.\x07I'm sure those Sellbots are damaging our toons' teeth.\x07I don't know how they are doing so, but they must be stopped.",
		LEAVING: "Keep those teeth shiny."},
 7103: {GREETING: '',
		QUEST: "Tsk, tsk.\x07While you were away, those Boardbots went and took my Sickle Probe.",
		LEAVING: '',
		COMPLETE: "Thanks for getting that back for me. Couldn't work without it.\x07Let me give you a reward for your help..."},
		
 #TB Task Twelve
 7110: {QUEST: "_toNpcName_ is working on an electrical problem and can't work with the Cogs distracting him._where_"},
 7111: {GREETING: '',
		QUEST: "I'm working on an issue with the electric circuit, but the Cogs outside are just too loud and distracting.\x07Can you defeat a whole bunch of them so I can work in peace?\x07If I don't get this done, the entire electric grid in Toontown could fail.",
		LEAVING: '',
		COMPLETE: "Ah, peace and quiet."},
		
 #TB Mega Task
 7200: {QUEST: "Uh oh... _toNpcName_ is looking for you.\x07He's the meanest, eldest, and toughest toon in town._where_",
		LEAVING: "Don't ask me why he wants you! I just hand out these tasks!"},
 7201: {GREETING: "Welcome, young apprentice.",
		QUEST: "I see you've been helping out the toons around The Brrrgh and have been doing a pretty good job at it, as well.\x07Before you head out for your next adventures, I went to test your stealth, skills, loyalty, and intelligence.\x07Your first test will be to defeat those vicious Loan Sharks.",
		LEAVING: "Don't come back without proof of defeat.\x07About 20 Shark Teeth will be enough proof."},
 7202: {GREETING: "Welcome, young apprentice.",
		QUEST: "I see you've been helping out the toons around The Brrrgh and have been doing a pretty good job at it, as well.\x07Before you head out for your next adventures, I went to test your stealth, skills, loyalty, and intelligence.\x07Your first test will be to defeat those filthy Corporate Raiders.",
		LEAVING: "Don't come back without proof of defeat.\x07About 20 Eyepatches will be enough proof."},
 7203: {GREETING: "Welcome, young apprentice.",
		QUEST: "I see you've been helping out the toons around The Brrrgh and have been doing a pretty good job at it, as well.\x07Before you head out for your next adventures, I went to test your stealth, skills, loyalty, and intelligence.\x07Your first test will be to defeat those beautiful and gorgeous- I mean, hideous Minglers.",
		LEAVING: "Don't come back without proof of defeat.\x07About 20 Make-Up Kits will be enough proof."},
 7204: {GREETING: "Welcome, young apprentice.",
		QUEST: "I see you've been helping out the toons around The Brrrgh and have been doing a pretty good job at it, as well.\x07Before you head out for your next adventures, I went to test your stealth, skills, loyalty, and intelligence.\x07Your first test will be to defeat those brainless Big Fish.",
		LEAVING: "Don't come back without proof of defeat.\x07About 15 Scales will be enough proof."},
 7205: {GREETING: "Welcome, young apprentice.",
		QUEST: "I see you've been helping out the toons around The Brrrgh and have been doing a pretty good job at it, as well.\x07Before you head out for your next adventures, I went to test your stealth, skills, loyalty, and intelligence.\x07Your first test will be to defeat those soaring Legal Eagles.",
		LEAVING: "Don't come back without proof of defeat.\x07About 20 Shiny Beaks will be enough proof."},
 7206: {GREETING: "Ah, nice work young apprentice.",
		QUEST: "For your next test, I would like you to defeat some of those self-centered Mr. Hollywoods.",
		LEAVING: "Again, you will need proof of their defeat.\x0715 Shiny Teeth will be enough."},
 7207: {GREETING: "Ah, nice work young apprentice.",
		QUEST: "For your next test, I would like you to defeat some of those sneaky Robber Barons.",
		LEAVING: "Again, you will need proof of their defeat.\x0715 Gold Teeth will be enough."},
 7208: {GREETING: "Ah, nice work young apprentice.",
		QUEST: "For your next test, I would like you to defeat some of those greedy Head Honchos.",
		LEAVING: "Again, you will need proof of their defeat.\x0710 Pie Charts will be enough."},
 7209: {GREETING: "Ah, nice work young apprentice.",
		QUEST: "For your next test, I would like you to defeat some of those good-smelling Big Cheeses.",
		LEAVING: "Again, you will need proof of their defeat.\x0715 Lumpy Cheeses will be enough."},
 7210: {GREETING: "Ah, nice work young apprentice.",
		QUEST: "For your next test, I would like you to defeat some of those poorly-styled Big Wigs.",
		LEAVING: "Again, you will need proof of their defeat.\x0715 Big White Wigs will be enough."},
 7211: {GREETING: "Tsk, tsk. You were a bit slow with that test.",
		QUEST: "Hopefully, you could be a bit faster defeating those strong Elite Cogs.",
		LEAVING: "C'mon. Time's ticking. I ain't getting any younger over here."},
 7212: {GREETING: "OK.",
		QUEST: "You may not like this next test.\x07However, you're not doing this just for me.\x07Not just for you.\x07But for this whole town.\x07Protecting everyone in our town should be your duty.\x07And I'd like you to continue that duty by taking down some of the tallest buildings around here.",
		LEAVING: "Remember this.\x07You don't throw a pie with your hand.\x07You throw it with your heart."},
 7213: {GREETING: "Brilliant work, young apprentice.",
		QUEST: "But you're not done yet.\x07Oh? Hmm?\x07Yeah sure, I can ask.\x07Oh, you must be wondering who I'm talking to.\x07No, I'm not crazy and talking to ghosts. This here is my Talking Toad.\x07This toad and his girlfriend have been going out for quite some time, and he thinks he's ready to take the relationship to the next level.\x07We'll need a wedding cake just incase he does decide to take it there.",
		LEAVING: "You want me to be your best man, toad?\x07I don't know, I'll need some time to think about that..."},
 7214: {GREETING: "Brilliantwork, young apprentice.",
		QUEST: "But you're not done yet.\x07Oh? Hmm?\x07Oh, you must be wondering who I'm talking to.\x07No, I'm not crazy and talking to ghosts. This here is my Talking Toad.\x07He requests a drink, and his favorite comes from a fresh spring geyser.\x07Don't ask me why he like it specifically from there, he's a weird fella.\x07I need you to bring one of them here so I can set that up for him.",
		LEAVING: "Oh, quit denying it toad. You are a bit of a weirdo."},
 7215: {GREETING: '',
		QUEST: "Alright, enough child's work. Let's get down to business.\x07Our evil neighboring Lawbots are planning a trial against one of our toons, Bumpy Bumblebehr.\x07Bumpy is one of our top resistance toons who was taken while infiltrating a Lawbot D-Office alone.\x07If he gets taken away, the toon resistance will weaken.\x07We can't let that happen, we must win the trial.\x07In order to do that, we must make sure they don't overload themselves with lawyers.\x07Defeat some of those strong lawyers in the Lawbot A-Office.",
		LEAVING: "C'mon! There's no time to waste."},
 7216: {GREETING: '',
		QUEST: "Apparently, the Lawbots weren't sending A-Office lawyers to the trial...\x07They're sending the B-Office laywers...\x07You've got to stop them, quickly!",
		LEAVING: ''},
 7217: {GREETING: "Great! Now they're down to around eight or ten lawyers.",
		QUEST: "I'd ask you to defeat them, but the trial is about to start.\x07I need you to gather a group of toons, sneak into the trial disguised as lawyers, and win that trial.",
		LEAVING: "It is a dangerous and risky task, but I trust that you'll do well."},
 7218: {GREETING: '',
		QUEST: "The news just came out. Bumpy was found not guilty.\x07Oh, and a call from HQ Randy came in. The Bossbots around Acorn Acres are stirring up trouble.\x07Go see what you can do to help.\x07What? You are expecting a reward?\x07Well you're not getting one.\x07Back in my day, we worked out of generosity to protect this town. You toons are so greedy nowadays.",
		COMPLETE: "Hey, _avName_.\x07It seems the Bossbots are coming out of their headquarters and attacking Acorn Acres.\x07We need you to stop them.\x07Once you're ready, the other HQ Officers here and I will offer you tasks requiring help to the toons of Acorn Acres once again.\x07Oh? You need to go back to The Brrrgh and Lil Oldman refused to grant you it?\x07No worries. I'll just give you teleport access and a reward that you probably deserve.",
		LEAVING: ''}}
		
		
ChatGarblerDog = ['woof', 'arf', 'rruff']
ChatGarblerCat = ['meow', 'mew']
ChatGarblerMouse = ['squeak', 'squeaky', 'squeakity']
ChatGarblerHorse = ['neigh', 'brrr']
ChatGarblerRabbit = ['eek',
 'eepr',
 'eepy',
 'eeky']
ChatGarblerDuck = ['quack', 'quackity', 'quacky']
ChatGarblerMonkey = ['ooh', 'ooo', 'ahh']
ChatGarblerBear = ['growl', 'grrr']
ChatGarblerPig = ['oink', 'oik', 'snort']
ChatGarblerDeer = ['meh', 'mee']
ChatGarblerBat = ['eee', 'yee', 'eew']
ChatGarblerBeaver = ['ear', 'air', 'ree']
ChatGarblerGator = ['snort', 'crunch', 'chomp']
ChatGarblerFox = ['awo', 'ring ding', 'ow']
ChatGarblerDefault = ['blah']
Bossbot = 'Bossbot'
Lawbot = 'Lawbot'
Cashbot = 'Cashbot'
Sellbot = 'Sellbot'
Boardbot = 'Boardbot'
BossbotS = 'a Bossbot'
LawbotS = 'a Lawbot'
CashbotS = 'a Cashbot'
SellbotS = 'a Sellbot'
BoardbotS = 'a Boardbot'
BossbotP = 'Bossbots'
LawbotP = 'Lawbots'
CashbotP = 'Cashbots'
SellbotP = 'Sellbots'
BoardbotP = 'Boardbots'
BossbotSkelS = 'a Bossbot Skelecog'
LawbotSkelS = 'a Lawbot Skelecog'
CashbotSkelS = 'a Cashbot Skelecog'
SellbotSkelS = 'a Sellbot Skelecog'
BoardbotSkelS = 'a Boardbot Skelecog'
BossbotSkelP = 'Bossbot Skelecogs'
LawbotSkelP = 'Lawbot Skelecogs'
CashbotSkelP = 'Cashbot Skelecogs'
SellbotSkelP = 'Sellbot Skelecogs'
BoardbotSkelP = 'Boardbot Skelecogs'
SkeleRevivePostFix = ' v2.0'
AvatarDetailPanelOK = lOK
AvatarDetailPanelCancel = lCancel
AvatarDetailPanelClose = lClose
AvatarDetailPanelLookup = 'Looking up details for %s.'
AvatarDetailPanelFailedLookup = 'Unable to get details for %s.'
AvatarDetailPanelPlayer = 'Player: %(player)s\nWorld: %(world)s'
AvatarDetailPanelPlayerShort = '%(player)s\nWorld: %(world)s\nLocation: %(location)s'
AvatarDetailPanelRealLife = 'Offline'
AvatarDetailPanelOnline = 'District: %(district)s\nLocation: %(location)s\nLevel: %(level)s\nToon ID: %(toonId)s'
AvatarDetailPanelOnlinePlayer = 'District: %(district)s\nLocation: %(location)s\nPlayer: %(player)s\nLevel %(level)s'
AvatarDetailPanelOffline = 'District: offline\nLocation: offline\nLevel %s\nToon ID: %s'
AvatarShowPlayer = 'Show Player'
OfflineLocation = 'Offline'
PlayerToonName = 'Toon: %(toonname)s'
PlayerShowToon = 'Show Toon'
PlayerPanelDetail = 'Player Details'
AvatarPanelFriends = 'Friends'
AvatarPanelWhisper = 'Whisper'
AvatarPanelSecrets = 'True Friends'
AvatarPanelGoTo = 'Go To'
AvatarPanelPet = 'Show Doodle'
AvatarPanelIgnore = 'Ignore'
AvatarPanelIgnoreCant = 'Okay'
AvatarPanelStopIgnoring = 'Stop Ignoring'
AvatarPanelReport = 'Report'
AvatarPanelCogLevel = 'Level: %s'
AvatarPanelCogDetailClose = lClose
AvatarPanelDetail = 'Toon Details'
AvatarPanelGroupInvite = 'Invite'
AvatarPanelGroupMerge = 'Resulting in'
AvatarPanelGroupRetract = 'Retract Invitation'
AvatarPanelGroupMember = 'Already In Group'
AvatarPanelGroupMemberKick = 'Remove'
ReportPanelTitle = 'Report A Player'
ReportPanelBody = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Use "Ignore" on the toon\'s panel\n\nDo you really want to report %s to a Moderator?'
ReportPanelBodyFriends = 'This feature will send a complete report to a Moderator. Instead of sending a report, you might choose to do one of the following:\n\n  - Teleport to another district\n  - Break your friendship\n\nDo you really want to report %s to a Moderator?\n\n(This will also break your friendship)'
ReportPanelCategoryBody = 'You are about to report %s. A Moderator will be alerted to your complaint and will take appropriate action for anyone breaking our rules. Please choose the reason you are reporting %s:'
ReportPanelBodyPlayer = 'This feature is stilling being worked on and will be coming soon. In the meantime you can do the following:\n\n  - Go to DXD and break the friendship there.\n - Tell a parent about what happened.'
ReportPanelCategoryLanguage = 'Foul Language'
ReportPanelCategoryPii = 'Sharing/Requesting Personal Info'
ReportPanelCategoryRude = 'Rude or Mean Behavior'
ReportPanelCategoryName = 'Bad Name'
ReportPanelCategoryHacking = 'Hacking'
ReportPanelConfirmations = ('You are about to report that %s has used obscene, bigoted or sexually explicit language.',
 'You are about to report that %s is being unsafe by giving out or requesting a phone number, address, last name, email address, password or account name.',
 'You are about to report that %s is bullying, harassing, or using extreme behavior to disrupt the game.',
 "You are about to report that %s has created a name that does not follow the Project Altis rules.",
 'You are about to report that %s has hacked/tampered with the game or used third party software.')
ReportPanelWarning = "We take reporting very seriously. Your report will be viewed by a Moderator who will take appropriate action for anyone breaking our rules. If your account is found to have participated in breaking the rules, or if you make false reports or abuse the 'Report a Player' system, a Moderator may take action against your account. Are you absolutely sure you want to report this player?"
ReportPanelThanks = 'Thank you! Your report has been sent to a Moderator for review. There is no need to contact us again about the issue. The moderation team will take appropriate action for a player found breaking our rules.'
ReportPanelRemovedFriend = 'We have automatically removed %s from your Toon Friends List.'
ReportPanelRemovedPlayerFriend = 'We have automatically removed %s as a Player friend so as such you will not see them as your friend in any Project Altis product.'
ReportPanelAlreadyReported = 'You have already reported %s during this session. A Moderator will review your previous report.'
IgnorePanelTitle = 'Ignore A Player'
IgnorePanelAddIgnore = 'Would you like to ignore %s for the rest of this session?'
IgnorePanelIgnore = 'You are now ignoring %s.'
IgnorePanelRemoveIgnore = 'Would you like to stop ignoring %s?'
IgnorePanelEndIgnore = 'You are no longer ignoring %s.'
IgnorePanelAddFriendAvatar = '%s is your friend, you cannot ignore them while you are friends.'
IgnorePanelAddFriendPlayer = '%s (%s)is your friend, you cannot ignore them while you are friends.'
PetRequestBadLocation = 'Your doodle is too far away to teleport here!'
PetRequestAlreadyPresent = 'Your doodle is already with you!'
PetPanelFeed = 'Feed'
PetPanelCall = 'Call'
PetPanelGoTo = 'Go To'
PetPanelOwner = 'Show Owner'
PetPanelDetail = 'Pet Details'
PetPanelScratch = 'Scratch'
PetDetailPanelTitle = 'Trick Training'
PetTrickStrings = {0: 'Jump',
 1: 'Beg',
 2: 'Play dead',
 3: 'Rollover',
 4: 'Backflip',
 5: 'Dance',
 6: 'Speak'}
PetMoodAdjectives = {'neutral': 'neutral',
 'hunger': 'hungry',
 'boredom': 'bored',
 'excitement': 'excited',
 'sadness': 'sad',
 'restlessness': 'restless',
 'playfulness': 'playful',
 'loneliness': 'lonely',
 'fatigue': 'tired',
 'confusion': 'confused',
 'anger': 'angry',
 'surprise': 'surprised',
 'affection': 'affectionate'}
SpokenMoods = {'neutral': 'neutral',
 'hunger': ["I'm tired of Jellybeans! How'bout giving me a slice of pie?", "How'bout a Red Jellybean? I'm tired of the Green ones!", "Oh, those Jellybeans were for planting?!! But I'm hungry!"],
 'boredom': ["I'm dying of boredom over here!", "You didn't think I understood you, huh?", 'Could we, like, DO something already?'],
 'excitement': ["Wow, it's you, it's you, it's you!",
                'mmm, Jellybeans, mmm!',
                'Does it GET any better than this?',
                "Happy April Toons' Week!"],
 'sadness': ["Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go, Don't go...", "I'll be good, I promise!", "I don't know WHY I'm sad, I just am!!!"],
 'restlessness': ["I'm sooo restless!!!"],
 'playfulness': ["Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play, Let's play...", 'Play with me or I dig up some flowers!', 'Lets run around and  around and around and around and around and around...'],
 'loneliness': ['Where have you been?', 'Wanna cuddle?', 'I want to go with you when you fight Cogs!'],
 'fatigue': ['That swim in the pond really tired me out!', 'Being a Doodle is exhausting!', 'I gotta get to Dreamland!'],
 'confusion': ['Where am I? Who are you again?', "What's a Toon-up again?", "Whoa, I'm standing between you and the Cogs! Run away!"],
 'anger': ['... and you wonder why I never give you a Toon-up?!!!', 'You always leave me behind!', 'You love your gags more than you love me!'],
 'surprise': ['Of course Doodles can talk!', 'Toons can talk?!!', 'Whoa, where did you come from?'],
 'affection': ["You're the best Toon EVER!!!!!!!!!!", 'Do you even KNOW how great you are?!?', 'I am SO lucky to be with you!!!']}
DialogQuestion = '?'
FriendsListLabel = 'Friends'
TeleportPanelOK = lOK
TeleportPanelCancel = lCancel
TeleportPanelYes = lYes
TeleportPanelNo = lNo
TeleportPanelCheckAvailability = 'Trying to go to %s.'
TeleportPanelNotAvailable = '%s is busy right now; try again later.'
TeleportPanelIgnored = '%s is ignoring you.'
TeleportPanelNotOnline = "%s isn't online right now."
TeleportPanelWentAway = '%s went away.'
TeleportPanelUnknownHood = "You don't know how to get to %s!"
TeleportPanelUnavailableHood = '%s is not available right now; try again later.'
TeleportPanelDenySelf = "You can't go to yourself!"
TeleportPanelOtherShard = "%(avName)s is in district %(shardName)s, and you're in district %(myShardName)s.  Do you want to switch to %(shardName)s?"
TeleportPanelBusyShard = '%(avName)s is in a full District.'
BattleBldgBossTaunt = "I'm the boss."
CogdoBattleBldgBossTaunt = "I don't take meetings with Toons."
FactoryBossTaunt = "I'm the Foreman."
FactoryBossBattleTaunt = 'Let me introduce you to the Foreman.'
MintBossTaunt = "I'm the Supervisor."
MintBossBattleTaunt = 'You need to talk to the Supervisor.'
StageBossTaunt = "My Justice isn't Blind."
StageBossBattleTaunt = 'I am above the Law.'
CountryClubBossTaunt = "I'm the Club President."
CountryClubBossBattleTaunt = 'You need to talk to the Club President.'
BoardOfficeBossTaunt = "I'm the Executive Board Member."
BoardOfficeBossBattleTaunt = 'You need to talk to the Executive Board Member.'
ForcedLeaveCountryClubAckMsg = 'The Club President was defeated before you could reach him. You did not recover any Stock Options.'
ToonHealJokes = [['What goes TICK-TICK-TICK-WOOF?', 'A watchdog! '],
 ['Why do male deer need braces?', "Because they have 'buck teeth'!"],
 ['Why is it hard for a ghost to tell a lie?', 'Because you can see right through him.'],
 ['What did the ballerina do when she hurt her foot?', 'She called the toe truck!'],
 ['What has one horn and gives milk?', 'A milk truck!'],
 ["Why don't witches ride their brooms when they're angry?", "They don't want to fly off the handle!"],
 ['Why did the dolphin cross the ocean?', 'To get to the other tide.'],
 ['What kind of mistakes do spooks make?', 'Boo boos.'],
 ['Why did the chicken cross the playground?', 'To get to the other slide!'],
 ['Where does a peacock go when he loses his tail?', 'A retail store.'],
 ["Why didn't the skeleton cross the road?", "He didn't have the guts."],
 ["Why wouldn't they let the butterfly into the dance?", 'Because it was a moth ball.'],
 ["What's gray and squirts jam at you?", 'A mouse eating a doughnut.'],
 ['What happened when 500 hares got loose on the main street?', 'The police had to comb the area.'],
 ["What's the difference between a fish and a piano?", "You can tune a piano, but you can't tuna fish!"],
 ['What do people do in clock factories?', 'They make faces all day.'],
 ['What do you call a blind dinosaur?', "An I-don't-think-he-saurus."],
 ['If you drop a white hat into the Red Sea, what does it become?', 'Wet.'],
 ['Why was Cinderella thrown off the basketball team?', 'She ran away from the ball.'],
 ['Why was Cinderella such a bad player?', 'She had a pumpkin for a coach.'],
 ["What two things can't you have for breakfast?", 'Lunch and dinner.'],
 ['What do you give an elephant with big feet?', 'Big shoes.'],
 ['Where do baby ghosts go during the day?', 'Day-scare centers.'],
 ['What did Snow White say to the photographer?', 'Some day my prints will come.'],
 ["What's Tarzan's favorite song?", 'Jungle bells.'],
 ["What's green and loud?", 'A froghorn.'],
 ["What's worse than raining cats and dogs?", 'Hailing taxis.'],
 ['When is the vet busiest?', "When it's raining cats and dogs."],
 ['What do you call a gorilla wearing ear-muffs?', "Anything you want, he can't hear you."],
 ['Where would you weigh a whale?', 'At a whale-weigh station.'],
 ['What travels around the world but stays in the corner?', 'A stamp.'],
 ['What do you give a pig with a sore throat?', 'Oinkment.'],
 ['What did the hat say to the scarf?', 'You hang around while I go on a head.'],
 ["What's the best parting gift?", 'A comb.'],
 ['What kind of cats like to go bowling?', 'Alley cats.'],
 ["What's wrong if you keep seeing talking animals?", "You're having Disney spells."],
 ['What did one eye say to the other?', 'Between you and me, something smells.'],
 ["What's round, white and giggles?", 'A tickled onion.'],
 ['What do you get when you cross Bambi with a ghost?', 'Bamboo.'],
 ['Why do golfers take an extra pair of socks?', 'In case they get a hole in one.'],
 ['What do you call a fly with no wings?', 'A walk.'],
 ['Who did Frankenstein take to the prom?', 'His ghoul friend.'],
 ['What lies on its back, one hundred feet in the air?', 'A sleeping centipede.'],
 ['How do you keep a bull from charging?', 'Take away his credit card.'],
 ['What do you call a chicken at the North Pole?', 'Lost.'],
 ['What do you get if you cross a cat with a dog?', 'An animal that chases itself.'],
 ['What did the digital watch say to the grandfather clock?', 'Look dad, no hands.'],
 ['Where does Ariel the mermaid go to see movies?', 'The dive-in.'],
 ['What do you call a mosquito with a tin suit?', 'A bite in shining armor.'],
 ['What do giraffes have that no other animal has?', 'Baby giraffes.'],
 ['Why did the man hit the clock?', 'Because the clock struck first.'],
 ['Why did the apple go out with a fig?', "Because it couldn't find a date."],
 ['What do you get when you cross a parrot with a monster?', 'A creature that gets a cracker whenever it asks for one.'],
 ["Why didn't the monster make the football team?", 'Because he threw like a ghoul!'],
 ['What do you get if you cross a Cocker Spaniel with a Poodle and a rooster?', 'A cockapoodledoo!'],
 ['What goes dot-dot-dash-dash-squeak?', 'Mouse code.'],
 ["Why aren't elephants allowed on beaches?", "They can't keep their trunks up."],
 ['What is at the end of everything?', 'The letter G.'],
 ['How do trains hear?', 'Through the engineers.'],
 ['What does the winner of a marathon lose?', 'His breath.'],
 ['Why did the pelican refuse to pay for his meal?', 'His bill was too big.'],
 ['What has six eyes but cannot see?', 'Three blind mice.'],
 ["What works only when it's fired?", 'A rocket.'],
 ["Why wasn't there any food left after the monster party?", 'Because everyone was a goblin!'],
 ['What bird can be heard at mealtimes?', 'A swallow.'],
 ['What goes Oh, Oh, Oh?', 'Santa walking backwards.'],
 ['What has green hair and runs through the forest?', 'Moldy locks.'],
 ['Where do ghosts pick up their mail?', 'At the ghost office.'],
 ['Why do dinosaurs have long necks?', 'Because their feet smell.'],
 ['What do mermaids have on toast?', 'Mermarlade.'],
 ['Why do elephants never forget?', 'Because nobody ever tells them anything.'],
 ["What's in the middle of a jellyfish?", 'A jellybutton.'],
 ['What do you call a very popular perfume?', 'A best-smeller.'],
 ["Why can't you play jokes on snakes?", 'Because you can never pull their legs.'],
 ['Why did the baker stop making donuts?', 'He got sick of the hole business.'],
 ['Why do mummies make excellent spies?', "They're good at keeping things under wraps."],
 ['How do you stop an elephant from going through the eye of a needle?', 'Tie a knot in its tail.'],
 ["What goes 'Ha Ha Ha Thud'?", 'Someone laughing his head off.'],
 ["My friend thinks he's a rubber band.", 'I told him to snap out of it.'],
 ["My sister thinks she's a pair of curtains.", 'I told her to pull herself together!'],
 ['Did you hear about the dentist that married the manicurist?', 'Within a month they were fighting tooth and nail.'],
 ['Why do hummingbirds hum?', "Because they don't know the words."],
 ['Why did the baby turkey bolt down his food?', 'Because he was a little gobbler.'],
 ['Where did the whale go when it was bankrupt?', 'To the loan shark.'],
 ['How does a sick sheep feel?', 'Baah-aahd.'],
 ["What's gray, weighs 10 pounds and squeaks?", 'A mouse that needs to go on a diet.'],
 ['Why did the dog chase his tail?', 'To make ends meet.'],
 ['Why do elephants wear running shoes?', 'For jogging of course.'],
 ['Why are elephants big and gray?', "Because if they were small and yellow they'd be canaries."],
 ['If athletes get tennis elbow what do astronauts get?', 'Missile toe.'],
 ['Did you hear about the man who hated Santa?', 'He suffered from Claustrophobia.'],
 ['Why did ' + Donald + ' sprinkle sugar on his pillow?', 'Because he wanted to have sweet dreams.'],
 ['Why did ' + Goofy + ' take his comb to the dentist?', 'Because it had lost all its teeth.'],
 ['Why did ' + Goofy + ' wear his shirt in the bath?', 'Because the label said wash and wear.'],
 ['Why did the dirty chicken cross the road?', 'For some fowl purpose.'],
 ["Why didn't the skeleton go to the party?", 'He had no body to go with.'],
 ['Why did the burglar take a shower?', 'To make a clean getaway.'],
 ['Why does a sheep have a woolly coat?', "Because he'd look silly in a plastic one."],
 ['Why do potatoes argue all the time?', "They can't see eye to eye."],
 ['Why did ' + Pluto + ' sleep with a banana peel?', 'So he could slip out of bed in the morning.'],
 ['Why did the mouse wear brown sneakers?', 'His white ones were in the wash.'],
 ['Why are false teeth like stars?', 'They come out at night.'],
 ['Why are Saturday and Sunday so strong?', 'Because the others are weekdays.'],
 ['Why did the archaeologist go bankrupt?', 'Because his career was in ruins.'],
 ['What do you get if you cross the Atlantic on the Titanic?', 'Very wet.'],
 ['What do you get if you cross a chicken with cement?', 'A brick-layer.'],
 ['What do you get if you cross a dog with a phone?', 'A golden receiver.'],
 ['What do you get if you cross an elephant with a shark?', 'Swimming trunks with sharp teeth.'],
 ['What did the tablecloth say to the table?', "Don't move, I've got you covered."],
 ['Did you hear about the time ' + Goofy + ' ate a candle?', 'He wanted a light snack.'],
 ['What did the balloon say to the pin?', 'Hi Buster.'],
 ['What did the big chimney say to the little chimney?', "You're too young to smoke."],
 ['What did the carpet say to the floor?', 'I got you covered.'],
 ['What did the necklace say to the hat?', "You go ahead, I'll hang around."],
 ['What goes zzub-zzub?', 'A bee flying backwards.'],
 ['How do you communicate with a fish?', 'Drop him a line.'],
 ["What do you call a dinosaur that's never late?", 'A prontosaurus.'],
 ['What do you get if you cross a bear and a skunk?', 'Winnie-the-phew.'],
 ['How do you clean a tuba?', 'With a tuba toothpaste.'],
 ['What do frogs like to sit on?', 'Toadstools.'],
 ['Why was the math book unhappy?', 'It had too many problems.'],
 ['Why was the school clock punished?', 'It tocked too much.'],
 ["What's a polygon?", 'A dead parrot.'],
 ['What needs a bath and keeps crossing the street?', 'A dirty double crosser.'],
 ['What do you get if you cross a camera with a crocodile?', 'A snap shot.'],
 ['What do you get if you cross an elephant with a canary?', 'A very messy cage.'],
 ['What do you get if you cross a jeweler with a plumber?', 'A ring around the bathtub.'],
 ['What do you get if you cross an elephant with a crow?', 'Lots of broken telephone poles.'],
 ['What do you get if you cross a plum with a tiger?', 'A purple people eater.'],
 ["What's the best way to save water?", 'Dilute it.'],
 ["What's a lazy shoe called?", 'A loafer.'],
 ["What's green, noisy and dangerous?", 'A thundering herd of cucumbers.'],
 ['What color is a shout?', 'Yellow!'],
 ['What do you call a sick duck?', 'A mallardy.'],
 ["What's worse then a giraffe with a sore throat?", "A centipede with athlete's foot."],
 ['What goes ABC...slurp...DEF...slurp?', 'Someone eating alphabet soup.'],
 ["What's green and jumps up and down?", 'Lettuce at a dance.'],
 ["What's a cow after she gives birth?", 'De-calf-inated.'],
 ['What do you get if you cross a cow and a camel?', 'Lumpy milk shakes.'],
 ["What's white with black and red spots?", 'A Dalmatian with measles.'],
 ["What's brown has four legs and a trunk?", 'A mouse coming back from vacation.'],
 ["What does a skunk do when it's angry?", 'It raises a stink.'],
 ["What's gray, weighs 200 pounds and says, Here Kitty, kitty?", 'A 200 pound mouse.'],
 ["What's the best way to catch a squirrel?", 'Climb a tree and act like a nut.'],
 ["What's the best way to catch a rabbit?", 'Hide in a bush and make a noise like lettuce.'],
 ['What do you call a spider that just got married?', 'A newly web.'],
 ['What do you call a duck that robs banks?', 'A safe quacker.'],
 ["What's furry, meows and chases mice underwater?", 'A catfish.'],
 ["What's a funny egg called?", 'A practical yolker.'],
 ["What's green on the outside and yellow inside?", 'A banana disguised as a cucumber.'],
 ['What did the elephant say to the lemon?', "Let's play squash."],
 ['What weighs 4 tons, has a trunk and is bright red?', 'An embarrassed elephant.'],
 ["What's gray, weighs 4 tons, and wears glass slippers?", 'Cinderelephant.'],
 ["What's an elephant in a fridge called?", 'A very tight squeeze.'],
 ['What did the elephant say to her naughty child?', 'Tusk!  Tusk!'],
 ['What did the peanut say to the elephant?', "Nothing -- Peanuts can't talk."],
 ['What do elephants say when they bump into each other?', "Small world, isn't it?"],
 ['What did the cashier say to the register?', "I'm counting on you."],
 ['What did the flea say to the other flea?', 'Shall we walk or take the cat?'],
 ['What did the big hand say to the little hand?', 'Got a minute.'],
 ['What does the sea say to the sand?', 'Not much.  It usually waves.'],
 ['What did the stocking say to the shoe?', 'See you later, I gotta run.'],
 ['What did one tonsil say to the other tonsil?', 'It must be spring, here comes a swallow.'],
 ['What did the soil say to the rain?', 'Stop, or my name is mud.'],
 ['What did the puddle say to the rain?', 'Drop in sometime.'],
 ['What did the bee say to the rose?', 'Hi, bud.'],
 ['What did the appendix say to the kidney?', "The doctor's taking me out tonight."],
 ['What did the window say to the venetian blinds?', "If it wasn't for you it'd be curtains for me."],
 ['What did the doctor say to the sick orange?', 'Are you peeling well?'],
 ['What do you get if you cross a chicken with a banjo?', 'A self-plucking chicken.'],
 ['What do you get if you cross a hyena with a bouillon cube?', 'An animal that makes a laughing stock of itself.'],
 ['What do you get if you cross a rabbit with a spider?', 'A hare net.'],
 ['What do you get if you cross a germ with a comedian?', 'Sick jokes.'],
 ['What do you get if you cross a hyena with a mynah bird?', 'An animal that laughs at its own jokes.'],
 ['What do you get if you cross a railway engine with a stick of gum?', 'A chew-chew train.'],
 ['What would you get if you crossed an elephant with a computer?', 'A big know-it-all.'],
 ['What would you get if you crossed an elephant with a skunk?', 'A big stinker.'],
 ['Why did the mouse take a trip to outer space?', 'He wanted to find Pluto.']]
MovieHealLaughterMisses = ('hmm',
 'heh',
 'ha',
 'harr harr')
MovieHealLaughterHits1 = ('Ha Ha Ha',
 'Hee Hee',
 'Tee Hee',
 'Ha Ha')
MovieHealLaughterHits2 = ('BWAH HAH HAH!', 'HO HO HO!', 'HA HA HA!')
MovieSOSCallHelp = '%s HELP!'
MovieSOSWhisperHelp = '%s needs help in battle!'
MovieSOSObserverHelp = 'HELP!'
MovieNPCSOSGreeting = 'Hi %s! Glad to help!'
FrumpGreetings = ["I'm all in on this for a small loan of a million jellybeans.", 'Did one of you mention a wall?', "TOGETHER... WE WILL MAKE TOONTOWN GREAT AGAIN!!!", 'This is gonna be yuge.', "They are all filthy cogs, I'm sure some of them are great robots.", 'We are going to build a wall and make Loonyville pay for it!']
JakebooySOSGreetings = ["You called for some rakes?", "Rake 'em in, boys!", "This won't rake long!", "These cogs are about to have a Pounding Headrake!", "Why are you calling me? The rake is a lie.", "It's time to rake up!", "Let them eat rake!", "It's time to put the icing on the rake!", "It's time to rake up!", "I rake it that you need some help?", "It's time to rake them cogs pay!"]
JakebooySOSGoodbyes = ["So head on down to Jakes Rakes today!", "Rake it or leaf it!", "Rake ya later!", "Rake me up when september ends."]
AliceSOSLeave = "I'll be going back to my rabbit hole now."
AliceSOSGreeting = "Off with their heads!"
MovieNPCSOSGoodbye = 'See you later!'
MovieNPCSOSToonsHit = 'Toons Always Hit!'
MovieNPCSOSToonsHitS = 'Toons Always Hit\nFor One Round!'
MovieNPCSOSToonsHitP = 'Toons Always Hit\nFor %d Rounds!'
MovieNPCSOSCogsMiss = 'Cogs Always Miss!'
MovieNPCSOSCogsMissS = 'Cogs Always Miss\nFor One Round!'
MovieNPCSOSCogsMissP = 'Cogs Always Miss\n For %d Rounds!'
MovieNPCSOSRestockGags = 'Restocking %s gags!'
MovieNPCSOSHeal = 'Heal'
MovieNPCSOSTrap = 'Trap'
MovieNPCSOSLure = 'Lure'
MovieNPCSOSSound = 'Sound'
MovieNPCSOSThrow = 'Throw'
MovieNPCSOSSquirt = 'Squirt'
MovieNPCSOSDrop = 'Drop'
MovieNPCSOSZap = 'Zap'
MovieNPCSOSAll = 'All'
MoviePetSOSTrickFail = 'Sigh'
MoviePetSOSTrickSucceedBoy = 'Good boy!'
MoviePetSOSTrickSucceedGirl = 'Good girl!'
MovieSuitCancelled = 'CANCELLED\nCANCELLED\nCANCELLED'
CogHQBonus = '2x BONUS - Cog HQ!'
CogInvasionBonus = '2x BONUS - Cog Invasion!'
MegaBonus = '3x BONUS - MEGA MULTIPLIER!'
RewardPanelToonTasks = 'ToonTasks'
RewardPanelItems = 'Items Recovered'
RewardPanelMissedItems = 'Items Not Recovered'
RewardPanelQuestLabel = 'Quest %s'
RewardPanelCongratsStrings = ['Yeah!',
 'Congratulations!',
 'Wow!',
 'Cool!',
 'Awesome!',
 'Toon-tastic!']
RewardPanelNewGag = 'New %(gagName)s gag for %(avName)s!'
RewardPanelUberGag = '%(avName)s earned the %(gagName)s gag with %(exp)s experience points!'
RewardPanelEndTrack = 'Yay! %(avName)s has reached the end of the %(gagName)s Gag Track!'
RewardPanelPromotionPending = 'Pending promotion...'
RewardPanelMeritsMaxed = 'Maxed'
RewardPanelMeritBarLabels = ['Stock Options',
 'Subpoenas',
 'Cogbucks',
 'Merits',
 'Invoices']
RewardPanelMeritAlert = 'Ready for promotion!'
RewardPanelCogPart = 'You gained a Cog disguise part!'
RewardPanelPromotion = 'Ready for promotion in %s  track!'
RewardPanelSkip = 'Skip'
CheesyEffectDescriptions = [('Normal Toon', 'you will be normal'),
 ('Big head', 'Big head'),
 ('Small head', 'Small head'),
 ('Big legs', 'Big legs'),
 ('Small legs', 'Small legs'),
 ('Big toon', 'Big toon'),
 ('Small toon', 'Small toon'),
 ('Flat portrait', 'Flat portrait'),
 ('Flat profile', 'Flat profile'),
 ('Transparent', 'Transparent'),
 ('No color', 'No color'),
 ('Invisible toon', 'Invisible toon'),
 ('Wireframe', 'Wireframe')]
CheesyEffectIndefinite = 'You now have access to the %(effectName)s effect. You can choose it on in the "Items" page of your Shticker book!'
CheesyEffectMinutes = 'For the next %(time)s minutes, %(effectName)s%(whileIn)s.'
CheesyEffectHours = 'For the next %(time)s hours, %(effectName)s%(whileIn)s.'
CheesyEffectDays = 'For the next %(time)s days, %(effectName)s%(whileIn)s.'
CheesyEffectWhileYouAreIn = ' while you are in %s'
CheesyEffectExceptIn = ', except in %s'
CheesyEffectId2Name = {
 0: 'Normal Toon',
 1: 'Big Head',
 2: 'Small Head',
 3: 'Big Legs',
 4: 'Small Legs',
 5: 'Big Toon',
 6: 'Small Toon',
 7: 'Flat Portrait',
 8: 'Flat Profile',
 9: 'Transparent',
 10: 'No Color',
 11: 'Invisible',
 15: 'Green Toon',
 77: 'Wireframe'}
SuitFlunky = 'Flunky'
SuitPencilPusher = 'Pencil Pusher'
SuitYesman = 'Yesman'
SuitMicromanager = 'Micro\x03manager'
SuitDownsizer = 'Downsizer'
SuitHeadHunter = 'Head Hunter'
SuitCorporateRaider = 'Corporate Raider'
SuitTheBigCheese = 'The Big Cheese'
SuitColdCaller = 'Cold Caller'
SuitTelemarketer = 'Tele\x03marketer'
SuitNameDropper = 'Name Dropper'
SuitGladHander = 'Glad Hander'
SuitMoverShaker = 'Mover & Shaker'
SuitTwoFace = 'Two-Face'
SuitTheMingler = 'The Mingler'
SuitMrHollywood = 'Mr. Hollywood'
SuitShortChange = 'Short Change'
SuitPennyPincher = 'Penny Pincher'
SuitTightwad = 'Tightwad'
SuitBeanCounter = 'Bean Counter'
SuitNumberCruncher = 'Number Cruncher'
SuitMoneyBags = 'Money Bags'
SuitLoanShark = 'Loan Shark'
SuitRobberBaron = 'Robber Baron'
SuitConArtist = 'Con Artist'
SuitConnoisseur = 'Connoisseur'
SuitSwindler = 'The Swindler'
SuitMiddleman = 'Middleman'
SuitToxicManager = 'Toxic Manager'
SuitMagnate = 'Magnate'
SuitBigFish = 'Big Fish'
SuitHeadHoncho = 'Head Honcho'
SuitBottomFeeder = 'Bottom Feeder'
SuitBloodsucker = 'Blood\x03sucker'
SuitDoubleTalker = 'Double Talker'
SuitAmbulanceChaser = 'Ambulance Chaser'
SuitBackStabber = 'Back Stabber'
SuitSpinDoctor = 'Spin Doctor'
SuitLegalEagle = 'Legal Eagle'
SuitBigWig = 'Big Wig'
SuitFlunkyS = 'a Flunky'
SuitPencilPusherS = 'a Pencil Pusher'
SuitYesmanS = 'a Yesman'
SuitMicromanagerS = 'a Micromanager'
SuitDownsizerS = 'a Downsizer'
SuitHeadHunterS = 'a Head Hunter'
SuitCorporateRaiderS = 'a Corporate Raider'
SuitTheBigCheeseS = 'a The Big Cheese'
SuitColdCallerS = 'a Cold Caller'
SuitTelemarketerS = 'a Telemarketer'
SuitNameDropperS = 'a Name Dropper'
SuitGladHanderS = 'a Glad Hander'
SuitMoverShakerS = 'a Mover & Shaker'
SuitTwoFaceS = 'a Two-Face'
SuitTheMinglerS = 'a The Mingler'
SuitMrHollywoodS = 'a Mr. Hollywood'
SuitShortChangeS = 'a Short Change'
SuitPennyPincherS = 'a Penny Pincher'
SuitTightwadS = 'a Tightwad'
SuitBeanCounterS = 'a Bean Counter'
SuitNumberCruncherS = 'a Number Cruncher'
SuitMoneyBagsS = 'a Money Bags'
SuitLoanSharkS = 'a Loan Shark'
SuitRobberBaronS = 'a Robber Baron'
SuitConArtistS = 'a Con Artist'
SuitConnoisseurS = 'a Connoisseur'
SuitSwindlerS = 'a Swindler'
SuitMiddlemanS = 'a Middleman'
SuitToxicManagerS = 'a Toxic Manager'
SuitMagnateS = 'a Magnate'
SuitBigFishS = 'a Big Fish'
SuitHeadHonchoS = 'a Head Honcho'
SuitBottomFeederS = 'a Bottom Feeder'
SuitBloodsuckerS = 'a Bloodsucker'
SuitDoubleTalkerS = 'a Double Talker'
SuitAmbulanceChaserS = 'an Ambulance Chaser'
SuitBackStabberS = 'a Back Stabber'
SuitSpinDoctorS = 'a Spin Doctor'
SuitLegalEagleS = 'a Legal Eagle'
SuitBigWigS = 'a Big Wig'
SuitFlunkyP = 'Flunkies'
SuitPencilPusherP = 'Pencil Pushers'
SuitYesmanP = 'Yesmen'
SuitMicromanagerP = 'Micromanagers'
SuitDownsizerP = 'Downsizers'
SuitHeadHunterP = 'Head Hunters'
SuitCorporateRaiderP = 'Corporate Raiders'
SuitTheBigCheeseP = 'The Big Cheeses'
SuitColdCallerP = 'Cold Callers'
SuitTelemarketerP = 'Telemarketers'
SuitNameDropperP = 'Name Droppers'
SuitGladHanderP = 'Glad Handers'
SuitMoverShakerP = 'Movers & Shakers'
SuitTwoFaceP = 'Two-Faces'
SuitTheMinglerP = 'The Minglers'
SuitMrHollywoodP = 'Mr. Hollywoods'
SuitShortChangeP = 'Short Changes'
SuitPennyPincherP = 'Penny Pinchers'
SuitTightwadP = 'Tightwads'
SuitBeanCounterP = 'Bean Counters'
SuitNumberCruncherP = 'Number Crunchers'
SuitMoneyBagsP = 'Money Bags'
SuitLoanSharkP = 'Loan Sharks'
SuitRobberBaronP = 'Robber Barons'
SuitConArtistP = 'Con Artists'
SuitConnoisseurP = 'Connoisseurs'
SuitSwindlerP = 'Swindlers'
SuitMiddlemanP = 'Middlemen'
SuitToxicManagerP = 'Toxic Managers'
SuitMagnateP = 'Magnates'
SuitBigFishP = 'Big Fish'
SuitHeadHonchoP = 'Head Honchos'
SuitBottomFeederP = 'Bottom Feeders'
SuitBloodsuckerP = 'Bloodsuckers'
SuitDoubleTalkerP = 'Double Talkers'
SuitAmbulanceChaserP = 'Ambulance Chasers'
SuitBackStabberP = 'Back Stabbers'
SuitSpinDoctorP = 'Spin Doctors'
SuitLegalEagleP = 'Legal Eagles'
SuitBigWigP = 'Big Wigs'
SuitFaceoffDefaultTaunts = ['Boo!']
SuitAttackDefaultTaunts = ['Take that!', 'Take a memo on this!']
SuitAttackNames = {'AcidRain': 'Acid Rain!',
 'Audit': 'Audit!',
 'Bite': 'Bite!',
 'BounceCheck': 'Bounce Check!',
 'BrainStorm': 'Brain Storm!',
 'BuzzWord': 'Buzz Word!',
 'Calculate': 'Calculate!',
 'Canned': 'Canned!',
 'Chomp': 'Chomp!',
 'CigarSmoke': 'Cigar Smoke!',
 'ClipOnTie': 'Clip On Tie!',
 'Crunch': 'Crunch!',
 'Demotion': 'Demotion!',
 'Downsize': 'Downsize!',
 'DoubleTalk': 'Double Talk!',
 'EvictionNotice': 'Eviction Notice!',
 'EvilEye': 'Evil Eye!',
 'Filibuster': 'Filibuster!',
 'FillWithLead': 'Fill With Lead!',
 'FiveOClockShadow': "Five O'Clock Shadow!",
 'FingerWag': 'Finger Wag!',
 'Fired': 'Fired!',
 'FloodTheMarket': 'Flood The Market!',
 'FountainPen': 'Fountain Pen!',
 'FreezeAssets': 'Freeze Assets!',
 'Gavel': 'Gavel!',
 'GlowerPower': 'Glower Power!',
 'GuiltTrip': 'Guilt Trip!',
 'HalfWindsor': 'Half Windsor!',
 'HangUp': 'Hang Up!',
 'HeadShrink': 'Head Shrink!',
 'HotAir': 'Hot Air!',
 'Jargon': 'Jargon!',
 'Legalese': 'Legalese!',
 'Liquidate': 'Liquidate!',
 'MarketCrash': 'Market Crash!',
 'MumboJumbo': 'Mumbo Jumbo!',
 'ParadigmShift': 'Paradigm Shift!',
 'PeckingOrder': 'Pecking Order!',
 'PickPocket': 'Pick Pocket!',
 'PinkSlip': 'Pink Slip!',
 'PlayHardball': 'Play Hardball!',
 'PoundKey': 'Pound Key!',
 'PowerTie': 'Power Tie!',
 'PowerTrip': 'Power Trip!',
 'Quake': 'Quake!',
 'RazzleDazzle': 'Razzle Dazzle!',
 'RedTape': 'Red Tape!',
 'ReOrg': 'Re-Org!',
 'RestrainingOrder': 'Restraining Order!',
 'Rolodex': 'Rolodex!',
 'RubberStamp': 'Rubber Stamp!',
 'RubOut': 'Rub Out!',
 'Sacked': 'Sacked!',
 'SandTrap': 'Sand Trap!',
 'Schmooze': 'Schmooze!',
 'Shake': 'Shake!',
 'Shred': 'Shred!',
 'SongAndDance': 'Song And Dance!',
 'Spin': 'Spin!',
 'Synergy': 'Synergy!',
 'Tabulate': 'Tabulate!',
 'TeeOff': 'Tee Off!',
 'ThrowBook': 'Throw Book!',
 'Tremor': 'Tremor!',
 'Watercooler': 'Watercooler!',
 'Withdrawal': 'Withdrawal!',
 'WriteOff': 'Write Off!'}
SuitAttackTaunts = {'AcidRain': ["It's sulfur you.",
           "A little CO2 didn't hurt anybody, right?",
           'Environment, Shmenvironment.',
           "Today's Forecast: Rainy with a chance of dissolution.",
           'pHew! That was close!'],
 'Audit': ["I believe your books don't balance.",
           "Looks like you're in the red.",
           'Let me help you with your books.',
           'Your debit column is much too high.',
           "Let's check your assets.",
           'This will put you in debt.',
           "Let's take a close look at what you owe.",
           'This should drain your account.',
           'Time for you to account for your expenses.',
           "I've found an error in your books."],
 'Bite': ['Would you like a bite?',
          'Try a bite of this!',
          "You're biting off more than you can chew.",
          'My bite is bigger than my bark.',
          'Bite down on this!',
          'Watch out, I may bite.',
          "I don't just bite when I'm cornered.",
          "I'm just gonna grab a quick bite.",
          "I haven't had a bite all day.",
          'I just want a bite.  Is that too much to ask?'],
 'BounceCheck': ["Ah, too bad, you're funless.",
                 'You have a payment due.',
                 'I believe this check is yours.',
                 'You owed me for this.',
                 "I'm collecting on this debt.",
                 "This check isn't going to be tender.",
                 "You're going to be charged for this.",
                 'Check this out.',
                 'This is going to cost you.',
                 "I'd like to cash this in.",
                 "I'm just going to kick this back to you.",
                 'This is one sour note.',
                 "I'm deducting a service charge."],
 'BrainStorm': ['I forecast rain.',
                'Hope you packed your umbrella.',
                'I want to enlighten you.',
                'How about a few rain DROPS?',
                'Not so sunny now, are you Toon?',
                'Ready for a down pour?',
                "I'm going to take you by storm.",
                'I call this a lightning attack.',
                'I love to be a wet blanket.'],
 'BuzzWord': ['Pardon me if I drone on.',
              'Have you heard the latest?',
              'Can you catch on to this?',
              'See if you can hum this Toon.',
              'Let me put in a good word for you.',
              'I\'ll "B" perfectly clear.',
              'You should "B" more careful.',
              'See if you can dodge this swarm.',
              "Careful, you're about to get stung.",
              'Looks like you have a bad case of hives.'],
 'Calculate': ['These numbers do add up!',
               'Did you count on this?',
               "Add it up, you're going down.",
               'Let me help you add this up.',
               "It just doesn't add up!",
               'Did you register all your expenses?',
               "According to my calculations, you won't be around much longer.",
               "Here's the grand total.",
               'Wow, your bill is adding up.',
               'Try fiddling with these numbers!',
               Cogs + ': 1 Toons: 0'],
 'Canned': ['Do you like it out of the can?',
            '"Can" you handle this?',
            "This one's fresh out of the can!",
            'Ever been attacked by canned goods before?',
            "I'd like to donate this canned good to you!",
            'Get ready to "Kick the can"!',
            'You think you "can", you think you "can".',
            "I'll throw you in the can!",
            "I'm making me a can o' toon-a!",
            "You don't taste so good out of the can."],
 'Chomp': ['Take a look at these chompers!',
           'Chomp, chomp, chomp!',
           "Here's something to chomp on.",
           'Looking for something to chomp on?',
           "Why don't you chomp on this?",
           "I'm going to have you for dinner.",
           'I love to feed on Toons!'],
 'CigarSmoke': ['Gentlemen.',
                "It's a good day for me to have a smoke.",
                'Take a breath of this.',
                "It's tradition you know.",
                'Another day, another dollar spent.',
                'I always have the occasional cigar.',
                "I'll quit tomorrow, I swear.",
                "You can't even escape my secondhand smoke.",
                'These fumes are toxic.',
                'I need a good smoke.',
                'Smoking is a dirty habit.'],
 'ClipOnTie': ['Better dress for our meeting.',
               "You can't go OUT without your tie.",
               'The best dressed ' + Cogs + ' wear them.',
               'Try this on for size.',
               'You should dress for success.',
               'No tie, no service.',
               'Do you need help putting this on?',
               'Nothing says powerful like a good tie.',
               "Let's see if this fits.",
               'This is going to choke you up.',
               "You'll want to dress up before you go OUT.",
               "I think I'll tie you up."],
 'Crunch': ["Looks like you're in a crunch.",
            "It's crunch time!",
            "I'll give you something to crunch on!",
            'Crunch on this!',
            'I pack quite a crunch.',
            'Which do you prefer, smooth or crunchy?',
            "I hope you're ready for crunch time.",
            "It sounds like you're getting crunched!",
            "I'll crunch you like a can."],
 'Demotion': ["You're moving down the corporate ladder.",
              "I'm sending you back to the Mail Room.",
              'Time to turn in your nameplate.',
              "You're going down, clown.",
              "Looks like you're stuck.",
              "You're going nowhere fast.",
              "You're in a dead end position.",
              "You won't be moving anytime soon.",
              "You're not going anywhere.",
              'This will go on your permanent record.'],
 'Downsize': ['Come on down!',
              'Do you know how to get down?',
              "Let's get down to business.",
              "What's wrong? You look down.",
              'Going down?',
              "What's goin' down? You!",
              'Why pick on people my own size?',
              "Why don't I size you up, or should I say, down?",
              'Would you like a smaller size for just a quarter more?',
              'Try this on for size!',
              'You can get this in a smaller size.',
              'This attack is one size fits all!'],
 'EvictionNotice': ["It's moving time.",
                    'Pack your bags, Toon.',
                    'Time to make some new living arrangements.',
                    'Consider yourself served.',
                    "You're behind on your lease.",
                    'This will be extremely unsettling.',
                    "You're about to be uprooted.",
                    "I'm going to send you packing.",
                    "You're out of place.",
                    'Prepare to be relocated.',
                    "You're in a hostel position."],
 'EvilEye': ["I'm giving you the evil eye.",
             'Could you eye-ball this for me?',
             "Wait.  I've got something in my eye.",
             "I've got my eye on you!",
             'Could you keep an eye on this for me?',
             "I've got a real eye for evil.",
             "I'll poke you in the eye!",
             '"Eye" am as evil as they come!',
             "I'll put you in the eye of the storm!",
             "I'm rolling my eye at you."],
 'Filibuster': ["Shall I fill 'er up?",
                'This is going to take awhile.',
                'I could do this all day.',
                "I don't even need to take a breath.",
                'I keep going and going and going.',
                'I never get tired of this one.',
                'I can talk a blue streak.',
                'Mind if I bend your ear?',
                "I think I'll shoot the breeze.",
                'I can always get a word in edgewise.'],
 'FingerWag': ['I have told you a thousand times.',
               'Now see here Toon.',
               "Don't make me laugh.",
               "Don't make me come over there.",
               "I'm tired of repeating myself.",
               "I believe we've been over this.",
               'You have no respect for us ' + Cogs + '.',
               "I think it's time you pay attention.",
               'Blah, Blah, Blah, Blah, Blah.',
               "Don't make me stop this meeting.",
               'Am I going to have to separate you?',
               "We've been through this before."],
 'Fired': ['I hope you brought some marshmallows.',
           "It's going to get rather warm around here.",
           'This should take the chill out of the air.',
           "I hope you're cold blooded.",
           'Hot, hot and hotter.',
           'You better stop, drop, and roll!',
           "You're outta here.",
           'How does "well-done" sound?',
           'Can you say ouch?',
           'Hope you wore sunscreen.',
           'Do you feel a little toasty?',
           "You're going down in flames.",
           "You'll go out in a blaze.",
           "You're a flash in the pan.",
           'I think I have a bit of a flare about me.',
           "I just sparkle, don't I?",
           'Oh look, a crispy critter.',
           "You shouldn't run around half baked."],
 'FountainPen': ['This is going to leave a stain.',
                 "Let's ink this deal.",
                 'Be prepared for some permanent damage.',
                 "You're going to need a good dry cleaner.",
                 'You should change.',
                 'This fountain pen has such a nice font.',
                 "Here, I'll use my pen.",
                 'Can you read my writing?',
                 'I call this the plume of doom.',
                 "There's a blot on your performance.",
                 "Don't you hate when this happens?"],
 'FreezeAssets': ['Your assets are mine.',
                  'Do you feel a draft?',
                  "Hope you don't have plans.",
                  'This should keep you on ice.',
                  "There's a chill in the air.",
                  'Winter is coming early this year.',
                  'Are you feeling a little blue?',
                  'Let me crystallize my plan.',
                  "You're going to take this hard.",
                  'This should cause freezer burn.',
                  'I hope you like cold cuts.',
                  'This one will be cold.',
                  "I'm very cold blooded."],
 'GlowerPower': ['You looking at me?',
                 "I'm told I have very piercing eyes.",
                 'I like to stay on the cutting edge.',
                 "Jeepers, Creepers, don't you love my peepers?",
                 "Here's looking at you kid.",
                 "How's this for expressive eyes?",
                 'My eyes are my strongest feature.',
                 'The eyes have it.',
                 'Peeka-boo, I see you.',
                 'Look into my eyes...',
                 'Shall we take a peek at your future?'],
 'GuiltTrip': ["I'll lay a real guilt trip on you!",
               'Feeling guilty?',
               "It's all your fault!",
               'I always blame everything on you.',
               'Wallow in your own guilt!',
               "I'm never speaking to you again!",
               "You had better say you're sorry.",
               "I'm would forgive you in a million years!",
               'Are you ready for your trip?',
               'Call me when you get back from your trip.',
               'When do you get back from your trip?'],
 'HalfWindsor': ["This is the fanciest tie you'll ever see!",
                 'Try not to get too winded.',
                 "This isn't even half the trouble you're in.",
                 "You're lucky I don't have a whole windsor.",
                 "You can't afford this tie.",
                 "I bet you've never even SEEN a half windsor!",
                 'This tie is out of your league.',
                 "I shouldn't even waste this tie on you.",
                 "You're not even worth half of this tie!"],
 'HangUp': ["You've been disconnected.",
            'Good bye!',
            "It's time I end our connection.",
            "...and don't call back!",
            'Click!',
            'This conversation is over.',
            "I'm severing this link.",
            'I think you have a few hang ups.',
            "It appears you've got a weak link.",
            'Your time is up.',
            'I hope you receive this loud and clear.',
            'Thank you come again.',
            'You got the wrong number.'],
 'HeadShrink': ["Looks like you're seeing a shrink.",
                'Honey, I shrunk the toon.',
                "Hope this doesn't shrink your pride.",
                'Do you shrink in the wash?',
                'I shrink therefore I am.',
                "It's nothing to lose your head over.",
                'Are you going out of your head?',
                'Heads up! Or should I say, down.',
                'Objects may be larger than they appear.',
                'Good Toons come in small packages.'],
 'HotAir': ["We're having a heated discussion.",
            "You're experiencing a heat wave.",
            "I've reached my boiling point.",
            'This should cause some wind burn.',
            'I hate to grill you, but...',
            "Always remember, where there's smoke, there's fire.",
            "You're looking a little burned out.",
            'Another meeting up in smoke.',
            "Guess it's time to add fuel to the fire.",
            'Let me kindle a working relationship.',
            'I have some glowing remarks for you.',
            'Air Raid!!!'],
 'Jargon': ['What nonsense.',
            'See if you can make sense of this.',
            'I hope you get this loud and clear.',
            "Looks like I'm going to have to raise my voice.",
            'I insist on having my say.',
            "I'm very outspoken.",
            'I must pontificate on this subject.',
            'See, words can hurt you.',
            'Did you catch my meaning?',
            'Words, words, words, words, words.'],
 'Legalese': ['You must cease and desist.',
              'You will be defeated, legally speaking.',
              'Are you aware of the legal ramifications?',
              "You aren't above the law!",
              'There should be a law against you.',
              "There's no ex post facto with me!",
              "The opinions expressed in this attack are not those of Project Altis.",
              'We cannot be held responsible for damages suffered in this attack.',
              'Your results for this attack may vary.',
              'This attack is void where prohibited.',
              "You don't fit into my legal system!",
              "You can't handle the legal matters."],
 'Liquidate': ['I like to keep things fluid.',
               'Are you having some cash flow problems?',
               "I'll have to purge your assets.",
               'Time for you to go with the flow.',
               "Remember it's slippery when wet.",
               'Your numbers are running.',
               'You seem to be slipping.',
               "It's all crashing down on you.",
               "I think you're diluted.",
               "You're all washed up."],
 'MarketCrash': ["I'm going to crash your party.",
                 "You won't survive the crash.",
                 "I'm more than the market can bear.",
                 "I've got a real crash course for you!",
                 "Now I'll come crashing down.",
                 "I'm a real bull in the market.",
                 'Looks like the market is going down.',
                 'You had better get out quick!',
                 'Sell! Sell! Sell!',
                 'Shall I lead the recession?',
                 "Everybody's getting out, shouldn't you?"],
 'MumboJumbo': ['Let me make this perfectly clear.',
                "It's as simple as this.",
                "This is how we're going to do this.",
                'Let me supersize this for you.',
                'You might call this technobabble.',
                'Here are my five-dollar words.',
                'Boy, this is a mouth full.',
                'Some call me bombastic.',
                'Let me just interject this.',
                'I believe these are the right words.'],
 'ParadigmShift': ["Watch out! I'm rather shifty.",
                   'Prepare to have your paradigm shifted!',
                   "Isn't this an interesting paradigm.",
                   "You'll get shifted out of place.",
                   "I guess it's your shift now.",
                   'Your shift is up!',
                   "You've never shifted this much in your life.",
                   "I'm giving you the bad shift!",
                   'Look into my shifty eyes!'],
 'PeckingOrder': ["This one's for the birds.",
                  'Get ready for a bird bath.',
                  "Looks like you're going to hit a birdie.",
                  'Some think this attack is fowl.',
                  "You're on the bottom of the pecking order.",
                  'A bird in my hand is worth ten on your head!',
                  'Your order is up; the pecking order!',
                  "Why don't I peck on someone my own size? Nah.",
                  'Birds of a feather strike together.'],
 'PickPocket': ['Let me check your valuables.',
                "Hey, what's that over there?",
                'Like taking candy from a baby.',
                'What a steal.',
                "I'll hold this for you.",
                'Watch my hands at all times.',
                'The hand is quicker than the eye.',
                "There's nothing up my sleeve.",
                'The management is not responsible for lost items.',
                "Finder's keepers.",
                "You'll never see it coming.",
                'One for me, none for you.',
                "Don't mind if I do.",
                "You won't be needing this..."],
 'PinkSlip': ['Try not to slip up.',
              "Are you frightened? You've turned pink!",
              'This one will surely slip you up.',
              'Oops, I guess you slipped there, huh?',
              "Watch yourself, wouldn't want to slip!",
              "This one's slippery when wet.",
              "I'll just slip this one in.",
              "Don't mind if you slip by, do you?",
              "Pink isn't really your color.",
              "Here's your pink slip, you're outta here!"],
 'PlayHardball': ['So you wanna play hardball?',
                  "You don't wanna play hardball with me.",
                  'Batter up!',
                  'Hey batter, batter!',
                  "And here's the pitch...",
                  "You're going to need a relief pitcher.",
                  "I'm going to knock you out of the park.",
                  "Once you get hit, you'll run home.",
                  'This is your final inning!',
                  "You can't play with me!",
                  "I'll strike you out.",
                  "I'm throwing you a real curve ball!"],
 'PoundKey': ['Time to return some calls.',
              "I'd like to make a collect call.",
              "Ring-a-ling - it's for you!",
              "I've been wanting to drop a pound or two.",
              'I have a lot of clout.',
              'This may cause a slight pounding sensation.',
              "I'll just punch in this number.",
              'Let me call up a little surprise.',
              "I'll ring you up.",
              "O.K. Toon, it's the pound for you."],
 'PowerTie': ["I'll call later, you looked tied up.",
              'Are you ready to tie die?',
              "Ladies and gentlemen, it's a tie!",
              'You had better learn how to tie.',
              "I'll have you tongue-tied!",
              "This is the worst tie you'll ever get!",
              'Can you feel the power?',
              'My powers are far too great for you!',
              "I've got the power!",
              "By the powers vested in me, I'll tie you up."],
 'PowerTrip': ["Pack your bags, we're taking a little trip.",
               'Did you have a nice trip?',
               "Nice trip, I guess I'll see you next fall.",
               'How was your trip?',
               'Sorry to trip you up there!',
               'You look a little tripped up.',
               "Now you see who's in power!",
               'I am much more powerful than you.',
               "Who's got the power now?",
               "You can't fight the power.",
               'Power corrupts, especially in my hands!'],
 'Quake': ["Let's quake, rattle, and roll.",
           "I've got a whole lot of quakin' goin' on!",
           "I see you quakin' in your shoes.",
           "Here it comes, it's the big one!",
           "This one's off the Richter scale.",
           'Now the earth will quake!',
           "Hey, what's shakin'? You!",
           'Ever been in an earthquake?',
           "You're on shaky ground now!"],
 'RazzleDazzle': ['Read my lips.',
                  'How about these choppers?',
                  "Aren't I charming?",
                  "I'm going to wow you.",
                  'My dentist does excellent work.',
                  "Blinding aren't they?",
                  "Hard to believe these aren't real.",
                  "Shocking, aren't they?",
                  "I'm going to cap this off.",
                  'I floss after every meal.',
                  'Say Cheese!'],
 'RedTape': ['This should wrap things up.',
             "I'm going to tie you up for awhile.",
             "You're on a roll.",
             'See if you can cut through this.',
             'This will get sticky.',
             "Hope you're claustrophobic.",
             "I'll make sure you stick around.",
             'Let me keep you busy.',
             "Looks like you're in a sticky situation.",
             'Just try to unravel this.',
             'I want this meeting to stick with you.'],
 'ReOrg': ["You don't like the way I reorganized things!",
           'Perhaps a little reorganization is in order.',
           "You're not that bad, you just need to be reorganized.",
           'Do you like my organizational skills.',
           "I just thought I'd give things a new look.",
           'You need to get organized!',
           "You're looking a little disorganized.",
           'Hold on while I reorganize your thoughts.',
           "I'll just wait for you to get a little organized.",
           "You don't mind if I just reorganize a bit?"],
 'RestrainingOrder': ['You should show a little restraint.',
                      "I'm slapping you with a restraining order!",
                      "You can't come within five feet of me.",
                      'Perhaps you better keep your distance.',
                      'You should be restrained.',
                      Cogs + '!  Restrain that Toon!',
                      'Try and restrain yourself.',
                      "I hope I'm being too much of a restraint on you.",
                      'See if you can lift these restraints!',
                      "I'm ordering you to restrain!",
                      "Why don't we start with basic restraining?"],
 'Rolodex': ["Your card's in here somewhere.",
             "Here's the number for a pest exterminator.",
             'I want to give you my card.',
             "I've got your number right here.",
             "I've got you covered from a-z.",
             "You'll flip over this.",
             'Take this for a spin.',
             'Watch out for paper cuts.',
             "I'll let my fingers do the knocking.",
             'Is this how I can contact you?',
             'I want to make sure we stay in touch.'],
 'RubberStamp': ['I always make a good impression.',
                 "It's important to apply firm and even pressure.",
                 'A perfect imprint every time.',
                 'I want to stamp you out.',
                 'You must be RETURNED TO SENDER.',
                 "You've been CANCELLED.",
                 'You have a PRIORITY delivery.',
                 "I'll make sure you RECEIVED my message.",
                 "You're not going anywhere - you have POSTAGE DUE.",
                 "I'll need a response ASAP."],
 'RubOut': ['And now for my disappearing act.',
            "I sense I've lost you somewhere.",
            'I decided to leave you out.',
            'I always rub out all obstacles.',
            "I'll just erase this error.",
            'I can make any nuisance disappear.',
            'I like things neat and tidy.',
            'Please try and stay animated.',
            "Now I see you...  now I don't.",
            'This will cause some fading.',
            "I'm going to eliminate the problem.",
            'Let me take care of your problem areas.'],
 'Sacked': ["Looks like you're getting sacked.",
            "This one's in the bag.",
            "You've been bagged.",
            'Paper or plastic?',
            'My enemies shall be sacked!',
            'I hold the Toontown record in sacks per game.',
            "You're no longer wanted around here.",
            "Your time is up around here, you're being sacked!",
            'Let me bag that for you.',
            'No defense can match my sack attack!'],
 'Schmooze': ["You'll never see this coming.",
              'This will look good on you.',
              "You've earned this.",
              "I don't mean to gush.",
              'Flattery will get me everywhere.',
              "I'm going to pile it on now.",
              'Time to lay it on thick.',
              "I'm going to get on your good side.",
              'That deserves a good slap on the back.',
              "I'm going to ring your praises.",
              'I hate to knock you off your pedestal, but...'],
 'Shake': ["You're right on the epicenter.",
           "You're standing on a fault line.",
           "It's going to be a bumpy ride.",
           'I think of this as a natural disaster.',
           "It's a disaster of seismic proportions.",
           "This one's off the Richter scale.",
           'Time to duck and cover.',
           'You seem disturbed.',
           'Ready for a jolt?',
           "I'll have you shaken, not stirred.",
           'This will shake you up.',
           'I suggest a good escape plan.'],
 'Shred': ['I need to get rid of some hazardous waste.',
           "I'm increasing my throughput.",
           "I think I'll dispose of you right now.",
           'This will get rid of the evidence.',
           "There's no way to prove it now.",
           'See if you can put this back together.',
           'This should cut you down to size.',
           "I'm going to rip that idea to shreds.",
           "We don't want this to fall into the wrong hands.",
           'Easy come, easy go.',
           "Isn't this your last shred of hope?"],
 'SongAndDance': ['Whoa whoa whoa...',
                  'A-one! A-two! A skiddly-diddly-doo!',
                  "Don't trip up!",
                  "Think of this as a dance to the death.",
                  "It's like dreaming with your feet.",
                  'Never miss a chance to dance!',
                  'When you feel sad, dance!',
                  'I never dance to forget.'],
 'Spin': ['What do you say we go for a little spin?',
          'Do you use the spin cycle?',
          "This'll really make your head spin!",
          "Here's my spin on things.",
          "I'll take you for a spin.",
          "It's time to take a spin!",
          'How do you like to "spin" your time?',
          "Watch it.  Wouldn't want to spin out of control!",
          "Oh what a spin you're in!",
          'My attacks will make your head spin!'],
 'Synergy': ["I'm taking this to committee.",
             "Your project's been cancelled.",
             "Your budget's been cut.",
             "We're restructuring your division.",
             'I put it to a vote, and you lose.',
             'I just received the final approval.',
             'A good team can get rid of any problem.',
             "I'll get back to you on this.",
             "Let's get right to business.",
             'Consider this a Synergy crisis.'],
 'Tabulate': ["This doesn't add up.",
              'By my count, you lose.',
              "You're racking up quite a tab.",
              "I'll have you totaled in a moment.",
              'Are you ready for these numbers?',
              'Your bill is now due and payable.',
              'Time for the reckoning.',
              'I like to put things in order.',
              'And the tally is...',
              'These numbers should prove to be quite powerful.'],
 'TeeOff': ["You're not up to par.",
            'Fore!',
            "I'm getting teed off.",
            "Caddie, I'll need my driver!",
            'Just try and avoid this hazard.',
            'Swing!',
            'This is a sure hole in one.',
            "You're in my fairway.",
            'Notice my grip.',
            'Watch the birdie!',
            'Keep your eye on the ball!',
            'Mind if I play through?'],
 'ThrowBook': ['My book from Law School should help.',
               'You better have a good lawyer.',
               "I'll have to take legal action.",
               'Legal Eagle will be pleased to see this.',
               'Objection!',
               'Under article 14 subsection C...',
               'I see you have broken the law!',
               "It seems you don't understand the authority of law.",
               "I'll see you in court, Toon."],
 'Tremor': ['Did you feel that?',
            'Not afraid of a little tremor are you?',
            'A tremor is only the beginning.',
            'You look jittery.',
            "I'll shake things up a bit!",
            'Are you ready to rumble?',
            "What's wrong? You look shaken.",
            'Tremor with fear!',
            'Why are you tremoring with fear?'],
 'Watercooler': ['This ought to cool you off.',
                 "Isn't this refreshing?",
                 'I deliver.',
                 'Straight from the tap - into your lap.',
                 "What's the matter, it's just spring water.",
                 "Don't worry, it's purified.",
                 'Ah, another satisfied customer.',
                 "It's time for your daily delivery.",
                 "Hope your colors don't run.",
                 'Care for a drink?',
                 'It all comes out in the wash.',
                 "The drink's on you."],
 'Withdrawal': ["I believe you're overdrawn.",
                'I hope your balance is high enough for this.',
                'Take that, with interest.',
                'Your balance is dropping.',
                "You're going to need to make a deposit soon.",
                "You've suffered an economic collapse.",
                "I think you're in a slump.",
                'Your finances have taken a decline.',
                'I foresee a definite downturn.',
                "It's a reversal of fortune."],
 'WriteOff': ['Let me increase your losses.',
              "Let's make the best of a bad deal.",
              'Time to balance the books.',
              "This won't look good on your books.",
              "I'm looking for some dividends.",
              'You must account for your losses.',
              'You can forget about a bonus.',
              "I'll shuffle your accounts around.",
              "You're about to suffer some losses.",
              'This is going to hurt your bottom line.']}
BuildingWaitingForVictors = ('Waiting for other toons...',)
ElevatorHopOff = 'Hop off'
ElevatorStayOff = "If you hop off, you'll need to wait\nfor the elevator to leave or empty."
ElevatorLeaderOff = 'Only your leader can decide when to hop off.'
ElevatorHoppedOff = 'You need to wait for the next elevator.'
ElevatorMinLaff = 'You need %s laff points to ride this elevator.'
ElevatorHopOK = 'Okay'
ElevatorGroupMember = 'Only your group leader can\n decide when to board.'
KartMinLaff = 'You need %s laff points to ride this kart'
CogsIncExt = ', Inc.'
CogsIncModifier = '%s' + CogsIncExt
CogsInc = Cogs.upper() + CogsIncExt
CogdominiumsExt = ' Field Office'
Cogdominiums = Cog.upper() + CogdominiumsExt
DoorKnockKnock = 'Knock, knock.'
DoorWhosThere = "Who's there?"
DoorWhoAppendix = ' who?'
DoorNametag = 'Door'
FADoorCodes_UNLOCKED = None
FADoorCodes_TALK_TO_TOM = 'You need gags! Go talk to Tutorial Tom!'
FADoorCodes_DEFEAT_FLUNKY_HQ = 'Come back here when you have defeated the Flunky!'
FADoorCodes_TALK_TO_HQ = 'Go get your reward from HQ Harry!'
FADoorCodes_WRONG_DOOR_HQ = 'Wrong door! Take the other door to the playground!'
FADoorCodes_GO_TO_PLAYGROUND = 'Wrong way! You need to go to the playground!'
FADoorCodes_DEFEAT_FLUNKY_TOM = 'Walk up to that Flunky to battle him!'
FADoorCodes_TALK_TO_HQ_TOM = 'Go get your reward from Toon Headquarters!'
FADoorCodes_SUIT_APPROACHING = None
FADoorCodes_BUILDING_TAKEOVER = "Watch out! There's a Cog in there!"
FADoorCodes_SB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Sellbot Disguise first!\n\nBuild your Sellbot Disguise out of parts from the Factory."
FADoorCodes_CB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Cashbot Disguise first!\n\nBuild your Cashbot Disguise out of parts from the Mints."
FADoorCodes_LB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Lawbot Disguise first!\n\nBuild your Lawbot Disguise out of parts from the DA Offices."
FADoorCodes_BB_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Bossbot Disguise first!\n\nBuild your Bossbot Disguise out of parts from the Cog Golf Courses."
FADoorCodes_BD_DISGUISE_INCOMPLETE = "You'll get caught going in there as a Toon! You need to complete your Boardbot Disguise first!\n\nBuild your Boardbot Disguise out of parts from the Board Offices."
KnockKnockJokes = [['Who', "Bad echo in here, isn't there?"],
 ['Dozen', 'Dozen anybody want to let me in?'],
 ['Freddie', 'Freddie or not, here I come.'],
 ['Dishes', 'Dishes your friend, let me in.'],
 ['Wooden shoe', 'Wooden shoe like to know.'],
 ['Betty', "Betty doesn't know who I am."],
 ['Kent', 'Kent you tell?'],
 ['Noah', "Noah don't know who either."],
 ["I don't know", 'Neither do I, I keep telling you that.'],
 ['Howard', 'Howard I know?'],
 ['Emma', 'Emma so glad you asked me that.'],
 ['Auto', "Auto know, but I've forgotten."],
 ['Jess', 'Jess me and my shadow.'],
 ['One', 'One-der why you keep asking that?'],
 ['Alma', 'Alma not going to tell you!'],
 ['Zoom', 'Zoom do you expect?'],
 ['Amy', "Amy fraid I've forgotten."],
 ['Arfur', 'Arfur got.'],
 ['Ewan', 'No, just me'],
 ['Cozy', "Cozy who's knocking will you?"],
 ['Sam', 'Sam person who knocked on the door last time.'],
 ['Fozzie', 'Fozzie hundredth time, my name is ' + Flippy + '.'],
 ['Deduct', Donald + ' Deduct.'],
 ['Max', 'Max no difference, just open the door.'],
 ['N.E.', 'N.E. body you like, let me in.'],
 ['Amos', 'Amos-quito bit me.'],
 ['Alma', "Alma candy's gone."],
 ['Bruce', "I Bruce very easily, don't hit me."],
 ['Colleen', "Colleen up your room, it's filthy."],
 ['Elsie', 'Elsie you later.'],
 ['Hugh', 'Hugh is going to let me in?'],
 ['Hugo', "Hugo first - I'm scared."],
 ['Ida', 'Ida know.  Sorry!'],
 ['Isabel', 'Isabel on a bike really necessary?'],
 ['Joan', "Joan call us, we'll call you."],
 ['Kay', 'Kay, L, M, N, O, P.'],
 ['Justin', 'Justin time for dinner.'],
 ['Liza', 'Liza wrong to tell.'],
 ['Luke', 'Luke and see who it is.'],
 ['Mandy', "Mandy the lifeboats, we're sinking."],
 ['Max', 'Max no difference - just open the door!'],
 ['Nettie', 'Nettie as a fruitcake.'],
 ['Olivia', 'Olivia me alone!'],
 ['Oscar', 'Oscar stupid question, you get a stupid answer.'],
 ['Patsy', 'Patsy dog on the head, he likes it.'],
 ['Paul', "Paul hard, the door's stuck again."],
 ['Thea', 'Thea later, alligator.'],
 ['Tyrone', "Tyrone shoelaces, you're old enough."],
 ['Stella', 'Stella no answer at the door.'],
 ['Uriah', 'Keep Uriah on the ball.'],
 ['Dwayne', "Dwayne the bathtub.  I'm drowning."],
 ['Dismay', "Dismay be a joke, but it didn't make me laugh."],
 ['Ocelot', "Ocelot of questions, don't you?"],
 ['Thermos', 'Thermos be a better knock knock joke than this.'],
 ['Sultan', 'Sultan Pepper.'],
 ['Vaughan', 'Vaughan day my prince will come.'],
 ['Donald', 'Donald come baby, cradle and all.'],
 ['Lettuce', "Lettuce in, won't you?"],
 ['Ivor', 'Ivor sore hand from knocking on your door!'],
 ['Isabel', 'Isabel broken, because I had to knock.'],
 ['Heywood, Hugh, Harry', 'Heywood Hugh Harry up and open this door.'],
 ['Juan', "Juan of this days you'll find out."],
 ['Earl', 'Earl be glad to tell you if you open this door.'],
 ['Abbot', 'Abbot time you opened this door!'],
 ['Ferdie', 'Ferdie last time, open the door!'],
 ['Don', 'Don mess around, just open the door.'],
 ['Sis', 'Sis any way to treat a friend?'],
 ['Isadore', 'Isadore open or locked?'],
 ['Harry', 'Harry up and let me in!'],
 ['Theodore', "Theodore wasn't open so I knocked-knocked."],
 ['Ken', 'Ken I come in?'],
 ['Boo', "There's no need to cry about it."],
 ['You', 'You who!  Is there anybody there?'],
 ['Ice cream', "Ice cream if you don't let me in."],
 ['Sarah', "Sarah 'nother way into this building?"],
 ['Mikey', 'Mikey dropped down the drain.'],
 ['Doris', 'Doris jammed again.'],
 ['Yelp', 'Yelp me, the door is stuck.'],
 ['Scold', 'Scold outside.'],
 ['Diana', 'Diana third, can I have a drink please?'],
 ['Doris', 'Doris slammed on my finger, open it quick!'],
 ['Lettuce', 'Lettuce tell you some knock knock jokes.'],
 ['Izzy', 'Izzy come, izzy go.'],
 ['Omar', 'Omar goodness gracious - wrong door!'],
 ['Says', "Says me, that's who!"],
 ['Duck', "Just duck, they're throwing things at us."],
 ['Tank', "You're welcome."],
 ['Eyes', 'Eyes got loads more knock knock jokes for you.'],
 ['Pizza', 'Pizza cake would be great right now.'],
 ['Closure', 'Closure mouth when you eat.'],
 ['Harriet', "Harriet all my lunch, I'm starving."],
 ['Wooden', 'Wooden you like to know?'],
 ['Punch', 'Not me, please.'],
 ['Gorilla', 'Gorilla me a hamburger.'],
 ['Jupiter', "Jupiter hurry, or you'll miss the trolley."],
 ['Bertha', 'Happy Bertha to you!'],
 ['Cows', 'Cows go "moo" not "who."'],
 ['Tuna fish', "You can tune a piano, but you can't tuna fish."],
 ['Consumption', 'Consumption be done about all these knock knock jokes?'],
 ['Banana', 'Banana spilt so ice creamed.'],
 ['X', 'X-tremely pleased to meet you.'],
 ['Haydn', 'Haydn seek is fun to play.'],
 ['Rhoda', 'Rhoda boat as fast as you can.'],
 ['Quacker', "Quacker 'nother bad joke and I'm off!"],
 ['Nana', 'Nana your business.'],
 ['Ether', 'Ether bunny.'],
 ['Little old lady', "My, you're good at yodelling!"],
 ['Beets', 'Beets me, I forgot the joke.'],
 ['Hal', 'Halloo to you too!'],
 ['Sarah', 'Sarah doctor in the house?'],
 ['Aileen', 'Aileen Dover and fell down.'],
 ['Atomic', 'Atomic ache'],
 ['Agatha', 'Agatha headache.  Got an aspirin?'],
 ['Stan', "Stan back, I'm going to sneeze."],
 ['Hatch', 'Bless you.'],
 ['Ida', "It's not Ida who, it's Idaho."],
 ['Zippy', 'Mrs. Zippy.'],
 ['Yukon', 'Yukon go away and come back another time.']]
SharedChatterGreetings = ['Hi, %!',
 'Yoo-hoo %, nice to see you.',
 "I'm glad you're here today!",
 'Well, hello there, %.']
SharedChatterComments = ["That's a great name, %.",
 'I like your name.',
 'Watch out for the ' + Cogs + '.',
 'Looks like the trolley is coming!',
 'I need to play a trolley game to get some pies!',
 'Sometimes I play trolley games just to eat the fruit pie!',
 'Whew, I just stopped a bunch of ' + Cogs + '. I need a rest!',
 'Yikes, some of those ' + Cogs + ' are big guys!',
 "You look like you're having fun.",
 "Oh boy, I'm having a good day.",
 "I like what you're wearing.",
 "I think I'll go fishing this afternoon.",
 'Have fun in my neighborhood.',
 'I hope you are enjoying your stay in Toontown!',
 "I heard it's snowing at the Brrrgh.",
 'Have you ridden the trolley today?',
 'I like to meet new people.',
 'Wow, there are lots of ' + Cogs + ' in the Brrrgh.',
 'I love to play tag. Do you?',
 'Trolley games are fun to play.',
 'I like to make people laugh.',
 "It's fun helping my friends.",
 "A-hem, are you lost?  Don't forget your map is in your shticker Book.",
 'Try not to get tied up in the ' + Cogs + "' Red Tape.",
 'I hear ' + Daisy + ' has planted some new flowers in her garden.',
 'If you press the Page Up key, you can look up!',
 'If you help take over Cog buildings, you can earn a bronze star!',
 'If you press the Tab key, you can see different views of your surroundings!',
 'If you press the Ctrl key, you can jump!']
SharedChatterGoodbyes = ['I have to go now, bye!',
 "I think I'll go play a trolley game.",
 "Well, so long. I'll be seeing you, %!",
 "I'd better hurry and get to work stopping those " + Cogs + '.',
 "It's time for me to get going.",
 'Sorry, but I have to go.',
 'Good-bye.',
 'See you later, %!',
 "I think I'm going to go practice tossing cupcakes.",
 "I'm going to join a group and stop some " + Cogs + '.',
 'It was nice to see you today, %.',
 "I have a lot to do today. I'd better get busy."]
MickeyChatter = (['Welcome to ' + lToontownCentral + '.', 'Hi, my name is ' + Mickey + ". What's yours?"], ['Hey, have you seen ' + Donald + '?',
  "I'm going to go watch the fog roll in at " + lDonaldsDock + '.',
  'If you see my pal ' + Goofy + ', say hi to him for me.',
  'I hear ' + Daisy + ' has planted some new flowers in her garden.'], ["I'm going to MelodyLand to see " + Minnie + '!',
  "Gosh, I'm late for my date with " + Minnie + '!',
  "Looks like it's time for " + Pluto + "'s dinner.",
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "It's time for a nap. I'm going to Dreamland."])
WinterMickeyCChatter = (["Hi, I'm Merry Mickey!",
  'Welcome to Tinseltown... I mean, Toontown!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Golly, these halls sure are decked!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Just look at those tree lights! What a sight!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Not a creature is stirring, except this mouse!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'I love this time of year!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  "I'm feeling jolly, how about you?",
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Know any good carols?',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  'Oh boy! I love Winter Holiday!',
  'Sing your seasonal cheer at Joy Buzzers to the World and Joy is sure to return the favor!',
  "I think I'll trade my gloves for mittens!"], ['Have a happy Winter Holiday!',
  'Warm wishes to you!',
  'Shucks, sorry you have to go. So long!',
  "I'm going caroling with Minnie!"])
ValentinesMickeyChatter = (["Hi, I'm Mickey!",
  'Welcome to ValenToontown Central!',
  "Happy ValenToon's Day!",
  "Happy ValenToon's Day, %"], ['Love is in the air! And butterflies!',
  'Those hearts are good for Laff boosts!',
  'I hope Minnie likes what I got her!',
  "The Cattlelog has lots of ValenToon's Day gifts!",
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I'm taking Minnie out to the Kooky Cafe!",
  'Will Minnie want chocolates or flowers?'], ['I loved having you visit!', "Tell Minnie I'll pick her up soon!"])
WinterMickeyDChatter = (["Hi, I'm Merry Mickey!",
  'Welcome to Tinseltown... I mean, Toontown!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['Golly, these halls sure are decked!',
  'Just look at those tree lights! What a sight!',
  'Not a creature is stirring, except this mouse!',
  'I love this time of year!',
  "I'm feeling jolly, how about you?",
  'Know any good carols?',
  'Oh boy! I love Winter Holiday!',
  "I think I'll trade my gloves for mittens!"], ['Have a happy Winter Holiday!',
  'Warm wishes to you!',
  'Shucks, sorry you have to go. So long!',
  "I'm going caroling with Minnie!"])
VampireMickeyChatter = (['Welcome to ' + lToontownCentral + '.',
  'Hi, my name is ' + Mickey + ". What's yours?",
  'Happy Halloween!',
  'Happy Halloween, %!',
  'Welcome to Tombtown... I mean Toontown!'], ['If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "It's fun to dress up for Halloween!",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Do you like my costume?',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  '%, watch out for Bloodsucker Cogs!',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "Aren't the Halloween decorations great?",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Beware of black cats!',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Did you see the Toon with the pumpkin head?',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Boo!  Did I scare you?',
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "Don't forget to brush your fangs!",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "I'm a vampire, but not a Bloodsucker!",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  "I hope you're enjoying our Halloween fun!",
  'If you think playing tricks is All Fun and Games, go see Lazy Hal for a treat!',
  'Vampires are really popular this year!'], ["I'm going to check out the cool Halloween decorations.",
  "I'm going to MelodyLand to surprise " + Minnie + '!',
  "I'm going to sneak up on another Toon!  Shhh!",
  "I'm going trick-or-treating!",
  'Shhh, sneak with me.'])
FieldOfficeMickeyChatter = ['Have you heard about the new Mover & Shaker Field Offices?']
MinnieChatter = (['Welcome to Melodyland.', 'Hi, my name is ' + Minnie + ". What's yours?"], ['The hills are alive with the sound of music!',
  'You have a cool outfit, %.',
  'Hey, have you seen ' + Mickey + '?',
  'If you see my friend ' + Goofy + ', say hi to him for me.',
  'Wow, there are lots of ' + Cogs + ' near ' + Donald + "'s Dreamland.",
  "I heard it's foggy at the " + lDonaldsDock + '.',
  'Be sure and try the maze in ' + lDaisyGardens + '.',
  "I think I'll go catch some tunes.",
  'Hey %, look at that over there.',
  'I love the sound of music.',
  "I bet you didn't know Melodyland is also called TuneTown!  Hee Hee!",
  'I love to play the Matching Game. Do you?',
  'I like to make people giggle.',
  'Boy, trotting around in heels all day is hard on your feet!',
  'Nice shirt, %.',
  'Is that a Jellybean on the ground?'], ["Gosh, I'm late for my date with %s!" % Mickey, "Looks like it's time for %s's dinner." % Pluto, "It's time for a nap. I'm going to Dreamland."])
WinterMinnieCChatter = (["Hi, I'm Merry Minnie!",
  'Welcome to the land of carols!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ["You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Belt out a tune, Toon!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Show us how to croon, Toon!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Can you carry a melody here in Melodyland?',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Those lamps look warm in their scarves!',
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  "The sing's the thing!",
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  "I'll always like you, for better or verse!",
  "You'll get more than a Shave and a Haircut For a Song if you carol to Barbara Seville!",
  'Everything looks better with a wreath!'], ['Have a fun Winter Holiday!', 'Happy Trails!', 'Mickey is taking me caroling!'])
WinterMinnieDChatter = (["Hi, I'm Merry Minnie!",
  'Welcome to the land of carols!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Belt out a tune, Toon!',
  'Show us how to croon, Toon!',
  'Can you carry a melody here in Melodyland?',
  'Those lamps look warm in their scarves!',
  "The sing's the thing!",
  "You can't go wrong with a song!",
  "I'll always like you, for better or verse!",
  'Everything looks better with a wreath!'], ['Have a fun Winter Holiday!', 'Happy Trails!', 'Mickey is taking me caroling!'])
ValentinesMinnieChatter = (["Hello, I'm Minnie!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %"], ['I hope Mickey got me chocolates or flowers!',
  'Those hearts are good for Laff boosts!',
  'I want to go to a ValenToon Party!',
  'I hope Mickey takes me to the Kooky Cafe!',
  'Mickey is such a good ValenToon!',
  'What did you get your ValenToon?',
  "Mickey has never missed a ValenToon's Day!"], ['It was sweet having you visit!'])
WitchMinnieChatter = (['Welcome to Magicland... I mean Melodyland!',
  "Hi, my name is Magic Minnie! What's yours?",
  "Hello, I think you're enchanting!",
  'Happy Halloween!',
  'Happy Halloween, %!'], ['I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  "It's a magical day, don't you think?",
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Now where did I put my spell book',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Abra-Cadabra!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Toontown looks positively spooky today!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Are you seeing stars too?',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Purple is really my color!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'I hope your Halloween is bewitching!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'Beware of musical spiders!',
  'I hear Tabitha has treats for Really Kool Katz who can play tricks!',
  'I hope you are enjoying our Halloween fun!'], ["I'm going to disappear now!", 'Time for me to vanish!', 'Mickey is taking me Trick-or-Treating!'])
FieldOfficeMinnieChatter = ['Everyone is talking about the new Mover & Shaker Field Offices!']
DaisyChatter = (['Welcome to my garden!', "Hello, I'm " + Daisy + ". What's your name?", "It's so nice to see you %!"], ['My prize winning flower is at the center of the garden maze.',
  'I just love strolling through the maze.',
  "I haven't seen " + Goofy + ' all day.',
  'I wonder where ' + Goofy + ' is.',
  'Have you seen ' + Donald + "? I can't find him anywhere.",
  'If you see my friend ' + Minnie + ', please say "Hello" to her for me.',
  'The better gardening tools you have the better plants you can grow.',
  'There are far too many ' + Cogs + ' near ' + lDonaldsDock + '.',
  'Watering your garden every day keeps your plants happy.',
  'To grow a Pink Daisy plant a yellow and red Jellybean together.',
  'Yellow daisies are easy to grow, just plant a yellow Jellybean.',
  'If you see sand under a plant it needs water or it will wilt!'], ["I'm going to Melody Land to see %s!" % Minnie,
  "I'm late for my picnic with %s!" % Donald,
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "Oh, I'm a little sleepy. I think I'll go to Dreamland."])
ValentinesDaisyChatter = (["Hi, I'm Daisy!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %"], ["I hope Donald doesn't get me another Amore Eel!",
  'Donald is taking me out to the Deep-see Diner!',
  'I certainly have enough roses!',
  'Those hearts are good for Laff boosts!',
  "I'd love to go to a ValenToon's Day party!",
  'This is the garden where love grows!',
  "Donald better not sleep through ValenToon's Day again!",
  'Maybe Donald and I can double-date with Mickey and Minnie!'], ["Tell Donald I'll be waiting for him!", "Have a nice ValenToon's Day!"])
WinterDaisyCChatter = (['Welcome to the only garden that grows in the winter!', 'Happy Winter Holiday!', 'Happy Winter Holiday, %!'], ['Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'My garden needs more mistletoe!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'I need to plant holly for next year!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  "I'm going to ask Goofy to build me a gingerbread house!",
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'Those lights on the lamps are lovely!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'That is some jolly holly!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'My snowman keeps melting!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'That duck is decked out!',
  'Shoshanna at Pine Needle Crafts is a real sap for songs, so why not craft her a carol?',
  'I grew all these lights myself!'], ['Have a jolly Winter Holiday!',
  'Happy planting!',
  'Tell Donald to stop by with presents!',
  'Donald is taking me caroling!'])
WinterDaisyDChatter = (['Welcome to the only garden that grows in the winter!', 'Happy Winter Holiday!', 'Happy Winter Holiday, %!'], ['My garden needs more mistletoe!',
  'I need to plant holly for next year!',
  "I'm going to ask Goofy to build me a gingerbread house!",
  'Those lights on the lamps are lovely!',
  'That is some jolly holly!',
  'My snowman keeps melting!',
  'That duck is decked out!',
  'I grew all these lights myself!'], ['Have a jolly Winter Holiday!',
  'Happy planting!',
  'Tell Donald to stop by with presents!',
  'Donald is taking me caroling!'])
HalloweenDaisyChatter = (['Welcome to Daisy Ghosts... I mean Gardens!', 'Happy Halloween!', 'Happy Halloween, %!'], ['Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Wanna dance?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  "I'm a duck with a poodle skirt!",
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'The pirate tree needs water.',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Trick-or-Tree!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Do you notice anything strange about the trees?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'I should grow some pumpkins!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'WHO notices something different about the lamps?',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Halloween really grows on me!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'Twig-or-Treat!',
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  "Owl bet you didn't notice the spooky lamps!",
  'Visit my friend Leif Pyle if you have a trick and Rake Inn the treats!',
  'I hope you are enjoying our Halloween fun!'], ['Donald is taking me Trick-or-Treating!', "I'm going to check out the fun Halloween decorations."])
FieldOfficeDaisyChatter = ['Those Mover & Shaker Field Offices are popping up like weeds!']
ChipChatter = (['Welcome to %s!' % lOutdoorZone,
  "Hello, I'm " + Chip + ". What's your name?",
  "No, I'm " + Chip + '.',
  "It's so nice to see you %!",
  'We are Chip and Dale!'], ['I like golf.', 'We have the best acorns in Toontown.', 'The golf holes with volcanoes are the most challenging for me.'], ["We're going to the " + lTheBrrrgh + ' and play with %s.' % Pluto,
  "We'll visit %s and fix him." % Donald,
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "Oh, I'm a little sleepy. I think I'll go to Dreamland."])
ValentinesChipChatter = (["I'm Chip!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["What did you get me for ValenToon's Day, Dale?",
  'Those hearts are good for Laff boosts!',
  'Will you be my ValenToon, Dale?',
  "What did you get the Cogs for ValenToon's Day?",
  "I love ValenToon's Day!"], ['Come back any time!'])
WinterChipChatter = (['Happy Winter Holiday!', 'Dressed as chipmunks!', 'Happy Winter Holiday, %!'], ['Happy Winter Holiday, Dale!',
  'All this water could freeze any minute!',
  'We should switch the golf balls with snowballs!',
  'If only chipmunks knew how to sing!',
  'Did you remember to store nuts for the winter?',
  'Did you get the Cogs a present?'], ['Go nuts this Winter Holiday!', 'Have a joyful winter Holiday!'])
HalloweenChipChatter = (['Play some MiniGhoul... I mean Golf!', 'Happy Halloween!', 'Happy Halloween, %!'], ["We're nuts about Halloween!",
  "You're under arrest",
  "You can't outrun the long arm of the law",
  "I'm a Bobby!",
  'I hope you are enjoying our Halloween fun!',
  'Play golf and get a Howl-In-One.',
  'Candy corns are sweeter than acorns.',
  'I hope you are enjoying our Halloween fun!'], ['%, watch out for Bloodsucker Cogs!'])
DaleChatter = (["It's so nice to see you %!",
  "Hello, I'm " + Dale + ". What's your name?",
  "Hi I'm " + Chip + '.',
  'Welcome to %s!' % lOutdoorZone,
  'We are Chip and Dale!'], ['I like picnics.', 'Acorns are tasty, try some.', 'Those windmills can be hard too.'], ['Hihihi ' + Pluto + ' is fun to play with.',
  "Yeah, let's fix %s." % Donald,
  'A swim sounds refreshing.',
  "I'm getting tired and could use a nap."])
ValentinesDaleChatter = (["I'm Dale!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ['Same thing as last year. Nothing!',
  'I miss the nuts!',
  'Will you be my ValenToon, Chip?',
  'A pie in the face',
  "Yeah, it's all right."], ['Come back any time!'])
WinterDaleChatter = (['Merry chipmunks!',
  "Hi, we're two merry elves!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Happy Winter Holiday, Chip!',
  'Better not be on the geyser when it happens!',
  'And the golf clubs with icicles!',
  'Whoever heard of singing chipmunks?',
  'I told YOU to do that!',
  'Yes, a cream pie!'], ['And bring some back for us!', 'Have a joyful Winter Holiday!'])
HalloweenDaleChatter = (['Happy Halloween, %!', 'Play some MiniGhoul... I mean Golf!', 'Happy Halloween!'], ["We're nuts about Halloween!",
  'Great, I could use a rest!',
  'But your arms are short!',
  'I thought you were a Chip!',
  'Play golf and get a Howl-In-One',
  'Candy corns are sweeter than acorns.',
  'I hope you are enjoying our Halloween fun!'], ['%, watch out for Bloodsucker Cogs!'])
GoofyChatter = (['Welcome to ' + lDaisyGardens + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %!"], ['Boy it sure is easy to get lost in the garden maze!',
  'Be sure and try the maze here.',
  "I haven't seen " + Daisy + ' all day.',
  'I wonder where ' + Daisy + ' is.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
  'It looks like ' + Daisy + ' has planted some new flowers in her garden.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!"], ["I'm going to Melody Land to see %s!" % Mickey,
  "Gosh, I'm late for my game with %s!" % Donald,
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "It's time for a nap. I'm going to Dreamland."])
WinterGoofyChatter = (["I'm Goofy about the holidays!",
  'Welcome to Snowball Speedway!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Who needs reindeer when you have a fast kart?',
  'Gawrsh! Is it Winter Holiday already?',
  'I need my earmuffs!',
  "I haven't done any shopping yet!",
  "Don't drive your kart on ice!",
  'Seems like it was Winter Holiday only a year ago!',
  'Treat your kart to a present and spruce it up!',
  'These karts are better than any old sleigh!'], ['Have a cheery Winter Holiday!', 'Drive safe, now!', 'Watch out for flying reindeer!'])
ValentinesGoofyChatter = (["I'm Goofy about ValenToon's Day!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["Gawrsh! Is it ValenToon's Day already?",
  'I LOVE kart racing!',
  'Be sweet to each other out there!',
  'Show your sweetie a new kart!',
  'Toons love their karts!',
  'Make some new friends on the track!'], ['Drive safe, now!', 'Show some love out there!'])
GoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.', 'Hi, my name is ' + Goofy + ". What's yours?", "Gawrsh, it's nice to see you %!"], ['Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!"], ["I'm going to Melody Land to see %s!" % Mickey,
  "Gosh, I'm late for my game with %s!" % Donald,
  "I think I'll go swimming at " + lDonaldsDock + '.',
  "It's time for a nap. I'm going to Dreamland."])
SuperGoofyChatter = (['Welcome to my Super Speedway!',
  "Hi, I'm Super Goof! What's your name?",
  'Happy Halloween!',
  'Happy Halloween, %!'], ['I am feeling kind of batty today!',
  'Anybody see my cape around? Oh, there it is!',
  "Gawrsh! I don't know my own strength!",
  'Did somebody call for a superhero?',
  "Beware Cogs, I'll save Halloween!",
  "There's nothing scarier than me in a kart!",
  "I bet you don't know who I am with this mask on!",
  "It's fun to dress up for Halloween!",
  'I hope you are enjoying our Halloween fun!'], ['Gotta fly!',
  'Hi-Ho and away I go!',
  "Should I fly or drive to Donald's Dock?",
  'Gawrsh, have a Happy Halloween!'])
DonaldChatter = (['Welcome to Dreamland.', "Hi, my name is %s. What's yours?" % Donald], ['Sometimes this place gives me the creeps.',
  'Be sure and try the maze in ' + lDaisyGardens + '.',
  "Oh boy, I'm having a good day.",
  'Hey, have you seen ' + Mickey + '?',
  'If you see my buddy ' + Goofy + ', say hi to him for me.',
  "I think I'll go fishing this afternoon.",
  'Wow, there are lots of ' + Cogs + ' at ' + lDonaldsDock + '.',
  "Hey, didn't I take you on a boat ride at " + lDonaldsDock + '?',
  "I haven't seen " + Daisy + ' all day.',
  'I hear ' + Daisy + ' has planted some new flowers in her garden.',
  'Quack.'], ["I'm going to Melody Land to see %s!" % Minnie,
  "Gosh, I'm late for my date with %s!" % Daisy,
  "I think I'll go swimming at my dock.",
  "I think I'll take my boat for a spin at my dock."])
WinterDreamlandCChatter = (["Hi, I'm Dozing Donald!",
  'Welcome to Holiday Dreamland!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'I wish I was nestled all snug in my bed!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I'm dreaming of a white Toontown!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'I meant to leave out milk and cookies!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'When I wake up, I better see lots of presents!',
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I hope I don't sleep through the holidays!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  "I love a long winter's nap!",
  'Willow says that learning a little Sleep Voice Training is a real present, sing her a tune and find out why!',
  'The trees on the streets are covered in night lights!'], ['To all, a good night!', 'Sweet dreams!', 'When I wake up I am going caroling!'])
WinterDreamlandDChatter = (["Hi, I'm Dozing Donald!",
  'Welcome to Holiday Dreamland!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['I wish I was nestled all snug in my bed!',
  "I'm dreaming of a white Toontown!",
  'I meant to leave out milk and cookies!',
  'When I wake up, I better see lots of presents!',
  "I hope I don't sleep through the holidays!",
  "I love a long winter's nap!",
  'The trees on the streets are covered in night lights!'], ['To all, a good night!', 'Sweet dreams!', 'When I wake up I am going caroling!'])
HalloweenDreamlandChatter = (['Happy Halloween!', 'Happy Halloween, %!', "Hi, I'm FrankenDonald!"], ['If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'Am I awake or dreaming?',
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "I'm so scared, I can't fall asleep!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'So this is what Dreamland looks like!',
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "Boy, I'm sleepy!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  "I hope I don't sleep through Halloween this year!",
  'If you can play a trick on my friend Max, then you can Relax To The Max with a treat!',
  'I hope you are enjoying our Halloween fun!'], ['Sleep with the lights on tonight!', 'When I wake up, I am going Trick-or-Treating!'])
ValentinesDreamlandChatter = (["Hello, I'm (yawn) Donald!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["I hope I don't sleep through ValenToon's Day!",
  "I'm dreaming of Daisy!",
  "I had a nightmare that I missed ValenToon's Day!",
  'Those hearts are good for Laff boosts!',
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I couldn't dream of a nicer holiday than ValenToon's Day!",
  'I love sleeping!'], ['Nite-nite!', "Wake me when it's ValenToon's Day!"])
FieldOfficeDreamlandChatter = ['I dreamed about something called a Field Office...']
HalloweenDonaldChatter = (['Welcome to my Halloween harbor!',
  'Come aboard, if you have treats!',
  'Happy Halloween!',
  'Happy Halloween, %!'], ['If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I'm dressed as a sailor!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'Pumpkins make great lanterns!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I've never seen palm trees with hairy legs before!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "Maybe I'll be a pirate next Halloween!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I think the best treats are starfish!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  "I'll take you Trick-or-Treating around the harbor!",
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I hope those spiders stay in the trees!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'What do you call a ghost in the water? A BOO-y!',
  'If playing tricks is making you feel Rudderly Ridiculous, then go see Rudy for a treat!',
  'I hope you are enjoying our Halloween fun!'], ['Set sail for scares!', 'Happy haunting!', "I'm going to check out the spooky Halloween decorations."])
ValentinesDonaldChatter = (["Ahoy, I'm Donald!", "Happy ValenToon's Day!", "Happy ValenToon's Day, %!"], ["Was I supposed to take Daisy somewhere for ValenToon's Day?",
  "Just once more around the dock, then I'll get Daisy something.",
  "What would Daisy like for ValenToon's Day?",
  'Those hearts in the water are good for Laff boosts!',
  "Throw a ValenToon's Day party!",
  'Show the Cogs you love them with a pie in the face!',
  "I'll have to catch an Amore Eel for Daisy!"], ['Aloha!', 'Give the Cogs my best!'])
WinterDonaldCChatter = (["Welcome to Donald's Boat and Sleigh Dock!",
  'All aboard for the Winter Holiday cruise!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'How do you like my duck-orations?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'What is snow doing on the lamp posts?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'This water better not ice over!',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'How did they get the lights up in those trees?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'This boat is better than a sleigh! or is it?',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  "I don't need reindeer to pull this boat!",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  "I'm glad I'm not a turkey this time of year!",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  'My present to you? Free boat rides!',
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!',
  "I hope I don't get a lump of coal again!",
  'I hear that Dante has Gifts With A Porpoise, share a song and he may have a gift for you too!'], ['All ashore for holiday fun!', 'Remember to tip your boat driver on the way out!', 'Enjoy your holiday!'])
WinterDonaldDChatter = (["Welcome to Donald's Boat and Sleigh Dock!",
  'All aboard for the Winter Holiday cruise!',
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %!'], ['How do you like my duck-orations?',
  'What is snow doing on the lamp posts?',
  'This water better not ice over!',
  'How did they get the lights up in those trees?',
  'This boat is better than a sleigh! or is it?',
  "I don't need reindeer to pull this boat!",
  "I'm glad I'm not a turkey this time of year!",
  'My present to you? Free boat rides!',
  "I hope I don't get a lump of coal again!"], ['All ashore for holiday fun!', 'Remember to tip your boat driver on the way out!', 'Enjoy your holiday!'])
WesternPlutoChatter = (["Boo! Don't be scared, it's just me ... Pluto!", 'Happy Halloween, pardner!', 'Happy Halloween, %!'], ["Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I do tricks for treats!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "Mickey's taking me Trick-or-Treating later!",
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'It feels more like Winter Holiday than Halloween!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "Bark! That's 'Trick-or-Treat' in dog!",
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I hope you are enjoying our Halloween fun!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  'I like to chase Black Cat Toons!',
  "Frosty Fred has treats for tricks, they make him feel like there's Snowplace Like Home!",
  "There's a snake in my boot!"], ["I'm going to go dig up a treat!", "I'm going to see if Mickey has some treats!", "I'm going to scare Donald!"])
WinterPlutoCChatter = (["Hi, I'm Pluto!",
  "Welcome to the Brrgh, where it's winter all year!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ["Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'I chewed on an icicle and got frost-bite!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'This is like living in a snow globe!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'I wish I was beside a warm fire!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  'Arf! Arf! I need a scarf!',
  "Eddie could use a good tune, because Snowman's Land is a lonely place for a Yeti!",
  "At least my nose isn't red and glowing!"], ['Have a fun Winter Holiday!', 'Come back any time you want snow!', 'Mickey is taking me caroling!'])
WinterPlutoDChatter = (["Hi, I'm Pluto!",
  "Welcome to the Brrgh, where it's winter all year!",
  'Happy Winter Holiday!',
  'Happy Winter Holiday, %'], ['I chewed on an icicle and got frost-bite!',
  'This is like living in a snow globe!',
  'I wish I was beside a warm fire!',
  'Arf! Arf! I need a scarf!',
  "At least my nose isn't red and glowing!"], ['Have a fun Winter Holiday!', 'Come back any time you want snow!', 'Mickey is taking me caroling!'])
AFMickeyChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to the Gardens! I'm " + Daisy + '!',
  "I'm " + Daisy + ', and I love to garden!',
  "April Toons' Week is the silliest week of the year!",
  "What, you've never seen a duck with mouse ears?",
  "Hi, I'm " + Daisy + '! Quack!',
  "It's tough quacking like a duck!",
  "I'm not feeling like myself today!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'Tell Mickey I said hi!'])
AFMinnieChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ['Welcome to ' + lTheBrrrgh + "! I'm " + Pluto + '!',
  "Hi, I'm " + Pluto + "! What's your name?",
  "What, you've never seen a dog with mouse ears?",
  "I'm not feeling like myself today!",
  "Does anyone have a doggie biscuit? I'm hungry!",
  'Bark! My name is ' + Pluto + '!',
  "Isn't this silly?",
  "Don't make me chase you around!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'I have to go chase cars now!  Bye!'])
AFDaisyChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ['Welcome to ' + lToontownCentral + "! I'm " + Mickey + ' Mouse!',
  "Hi, I'm " + Mickey + '! The happiest mouse in Toontown!',
  'If you see ' + Daisy + ', tell her ' + Mickey + ' said hi!',
  "What, you've never seen a mouse with feathers?",
  "Isn't this silly?",
  "I'm not feeling like myself today!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ['Bye! Tell them ' + Mickey + ' sent you!', 'If you go to ' + lDaisyGardens + ', say hi to her for me!'])
AFGoofySpeedwayChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to Dreamland! I'm " + Donald + '!',
  "Hello, I'm " + Donald + '! Is it nap time yet?',
  'A duck needs his beauty rest, you know!',
  "What, you've never seen a duck with dog ears?",
  'Gawrsh! I mean -- Quack!',
  'This would make a great race track ... um, I mean place to nap!',
  "I'm not feeling like myself today!",
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ['If you see ' + Goofy + ', tell him ' + Donald + ' says hi!', 'Bye, and good night!'])
AFDonaldChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to the Speedway! I'm " + Goofy + '!',
  "I'm " + Goofy + ", and I'm dreaming I'm " + Donald + '!',
  "I've heard of sleep walking, but sleep kart driving?",
  'Gawrsh!  It sure is silly being ' + Goofy + '!',
  'How can I watch the races with my eyes closed?',
  'I better grab a nap before my next race!',
  "April Toons' Week is the silliest week of the year!",
  "I'm not feeling like myself today!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'I need to work on my karts!  Bye!'])
AFDonaldDockChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Everybody gets April Toons' Week off but me!",
  "I'm the only one who has to work this week!",
  'I only get time off when I sleep!',
  'All my friends are pretending to be somebody else!',
  'Round and round in this boat, all day long!',
  'I heard Daisy is pretending to be Mickey!',
  "The silliest week of the year, and I'm missing it!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'Play a joke on the Cogs for me!'])
AFPlutoChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Welcome to Melodyland!  I'm " + Minnie + '!',
  'Hi, my name is ' + Minnie + ' Mouse!',
  "I'm as happy as a mouse can be!",
  "What, you've never seen a mouse with dog ears?",
  'I love when ' + Mickey + ' and I go for walks!',
  'What, you never heard a mouse talk before?',
  "April Toons' Week is the silliest week of the year!",
  'Have you heard your Doodle talk yet?',
  'Gravity has taken a holiday at the Estates!'], ["Have a wacky April Toons' Week!", 'If you see ' + Pluto + ', tell him ' + Minnie + ' says hi!'])
AFChipChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Hi, I'm " + Dale + '!',
  'How are you today, ' + Chip + '?',
  'I always thought you were ' + Dale + ', ' + Chip + '.',
  "You're sure you're " + Chip + ' and not ' + Dale + ', ' + Chip + '?',
  "April Toons' Week is the silliest week of the year!"], ['Bye from ' + Chip + ' and ' + Dale + '!'])
AFDaleChatter = (["Happy April Toons' Week!", "Happy April Toons' Week, %!"], ["Hi, I'm " + Chip + '!',
  'Very well ' + Dale + ', thanks!',
  "Nope, I'm " + Chip + ', ' + Dale + '.',
  'Yes, ' + Dale + ", I'm " + Chip + ', not ' + Dale + '.',
  'It sure is, ' + Chip + '! I mean, ' + Dale + '.'], ['Or ' + Dale + ' and ' + Chip + '!'])
CLGoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.',
  'Hi, my name is ' + Goofy + ". What's yours?",
  "Gawrsh, it's nice to see you %!",
  "Hi there!  Pardon my dusty clothes I've been busy fixin' that broken Leaderboard."], ['We better get this Leaderboard working soon, Grand Prix Weekend is coming up!',
  "Does anybody want to buy a slightly used kart? It's only been through the Leaderboard once!",
  'Grand Prix Weekend is coming, better get to practicing.',
  'Grand Prix Weekend will be here on Friday, May 22 through Monday, May 25!',
  "I'm gonna need a ladder to get that kart down.",
  'That Toon really wanted to get on the Leaderboard!',
  'Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '?',
  'If you see my friend ' + Mickey + ', say hi to him for me.',
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!"], ['I better go get my kart a new paint job for the upcoming Grand Prix Weekend.',
  "Gosh, I better get workin' on this broken Leaderboard!",
  "Hope I'll see y'all on Grand Prix Weekend!  Goodbye!",
  "It's time for a nap. I'm going to Dreamland to dream about winnin' the Grand Prix."])
GPGoofySpeedwayChatter = (['Welcome to ' + lGoofySpeedway + '.',
  'Welcome to Grand Prix Weekend!',
  'Hi, my name is ' + Goofy + ". What's yours?",
  "Gawrsh, it's nice to see you %!"], ['Are you excited about the Grand Prix Weekend?',
  'Grand Prix Weekend really drives up those scores!',
  'Get more tickets by racing practice laps.',
  "Gawrsh, you're a fast racer!",
  'Boy, I saw a terrific race earlier.',
  'Watch out for banana peels on the race track!',
  'Have you upgraded your kart lately?',
  'We just got in some new rims at the kart shop.',
  'Hey, have you seen ' + Donald + '? He said he was gonna come watch the Grand Prix!',
  'If you see my friend ' + Mickey + ", tell him he's missing some great racing!",
  "D'oh! I forgot to fix " + Mickey + "'s breakfast!",
  'Gawrsh there sure are a lot of ' + Cogs + ' near ' + lDonaldsDock + '.',
  'At the Brrrgh branch of my Gag Shop, Hypno-Goggles are on sale for only 1 Jellybean!',
  "Goofy's Gag Shops offer the best jokes, tricks, and funnybone-ticklers in all of Toontown!",
  "At Goofy's Gag Shops, every pie in the face is guaranteed to make a laugh or you get your Jellybeans back!"], ['Good luck in the Grand Prix!',
  "I'm going to catch the next race in the Grand Prix!",
  'Gawrsh I think the next race is about to start!',
  'Gosh, I better go check on the new Leaderboard and make sure it is working right!'])
SillyPhase1Chatter = ["If you haven't seen the Silly Meter, head to Toon Hall!",
 'Toontown is getting sillier by the day!',
 "Cause silly surges in battle to boost Toontown's silly levels!",
 'Objects on the street are starting to animate!',
 'I saw a fire hydrant on Silly Street move!']
SillyPhase2Chatter = ['Silly levels are still rising!',
 'The Silly Meter has climbed higher and gotten crazier!',
 'Someone saw a trash can moving on Maple Street!',
 'A lot of hydrants on Silly Street have come alive!',
 'A mailbox on Lighthouse Lane has gone nuts!',
 'Go see the Silly Meter in Toon Hall!',
 'Keep causing those silly surges!']
SillyPhase3Chatter = ['The Cogs hate how silly Toontown is becoming!',
 'Keep a sharp eye out for Cog Invasions!',
 'Cog Invasions have caused the silly levels to drop!',
 'The Silly Meter went down after the Cog Invasions!',
 'Every street of Toontown has animated objects now!',
 'Toontown is sillier than ever!']
SillyPhase4Chatter = ['Fire hydrants make your Squirt Gags squirtier!',
 'Mail Boxes give your Throw Gags a special delivery!',
 'Those crazy Trash Cans can help boost your Toon-up!',
 'Objects on the street can help you in battle!',
 "I just know we'll get the Silly Meter back up soon!",
 'Enjoy the sillier Toontown!']
for chatter in [MickeyChatter,
 DonaldChatter,
 MinnieChatter,
 GoofyChatter]:
    chatter[0].extend(SharedChatterGreetings)
    chatter[1].extend(SharedChatterComments)
    chatter[2].extend(SharedChatterGoodbyes)

BoringTopic = 'Boring'
EmceeDialoguePhase1Topic = 'EmceeDialoguePhase1'
EmceeDialoguePhase2Topic = 'EmceeDialoguePhase2'
EmceeDialoguePhase3Topic = 'EmceeDialoguePhase3'
EmceeDialoguePhase3_5Topic = 'EmceeDialoguePhase3.5'
EmceeDialoguePhase4Topic = 'EmceeDialoguePhase4'
EmceeDialoguePhase5Topic = 'EmceeDialoguePhase5'
EmceeDialoguePhase6Topic = 'EmceeDialoguePhase6'
AprilToonsPhasePreTopTopic = 'AprilToonsPhasePreTopTopic'
AprilToonsPhaseTopTopic = 'AprilToonsPhaseTopTopic'
AprilToonsExtPhaseTopTopic = 'AprilToonsExtPhaseTopTopic'
AprilToonsPhasePostTopTopic = 'AprilToonsPhasePostTopTopic'
toontownDialogues = {BoringTopic: {(1, 2018): ['Hello Albert', 'It looks like the sillyness levels are rising', 'Yes and dont forget April Toons!'],
               (2, 2019): ['Hello Newton', 'Yes I wonder how much the parties are contributing to all this'],
               (3, 2020): ['Why hello there Albert and Newton', 'Halloween was pretty silly too!']},
 AprilToonsPhasePreTopTopic: {(1, 2020): ['Gadzooks! The Silly Meter has come back to life!',
                                          "It's rising every day, and will reach the top soon!",
                                          'When it does, something silly is sure to happen!',
                                          'So get ready to get ridiculous!']},
 AprilToonsPhaseTopTopic: {(1, 2020): ['The Silly Meter has hit the top!',
                                       'Doodles are talking, Estates are bouncy!',
                                       "There's only one thing to say\xe2\x80\xa6",
                                       'HAPPY APRIL TOONS!']},
 AprilToonsExtPhaseTopTopic: {(1, 2020): ['The Silly Meter has hit the top!', 'Doodles are talking, Estates are bouncy!']},
 AprilToonsPhasePostTopTopic: {(1, 2020): ['April Toons is over!',
                                           "It's time for us to return to our lab.",
                                           'But when things get REALLY crazy again\xe2\x80\xa6',
                                           'The Silly Meter will return!']},
 EmceeDialoguePhase1Topic: {(1, 2020): ['Fellow Toons, this is the Silly Meter!',
                                        "It is tracking Toontown's rising silly levels...",
                                        'Which are causing objects on the street to animate!',
                                        'And YOU can help push these levels higher!',
                                        'Battle Cogs to cause Silly Surges...',
                                        'Make Toontown sillier than ever...',
                                        "And let's watch the world come alive!",
                                        "Now I'll repeat what I said, but only once more."]},
 EmceeDialoguePhase2Topic: {(1, 2020): ['Good Gag work, Toons!',
                                        "You're keeping those silly levels rising...",
                                        'And Toontown is getting sillier every day!',
                                        'Fire hydrants, trash cans, and mailboxes are springing to life...',
                                        'Making the world more animated than ever!',
                                        "You know the Cogs aren't happy about this...",
                                        'But Toons sure are!']},
 EmceeDialoguePhase3Topic: {(1, 2020): ['Gadzooks! The Silly Meter is even crazier than expected!',
                                        'Your Silly Surges are working wonders...',
                                        'And Toontown is getting more animated every day!',
                                        'Keep up the good Gag work...',
                                        'And lets see how silly we can make Toontown!',
                                        "You know the Cogs aren't happy about what's going on...",
                                        'But Toons sure are!']},
 EmceeDialoguePhase3_5Topic: {(1, 2020): ['YOU DID IT TOONS!',
                                          'You brought the streets of Toontown to life!',
                                          'You deserve a reward!',
                                          'Enter the code SILLYMETER in your Shticker Book...',
                                          '...to get a Silly Meter T-Shirt!']},
 EmceeDialoguePhase4Topic: {(1, 2020): ['Attention all Toons!',
                                        'The sudden Cog invasions have been an unhappy event.',
                                        'As a result, silly levels have rapidly fallen...',
                                        'And no new objects are coming to life.',
                                        'But those that have are very thankful...',
                                        "So perhaps they'll find a way to show their appreciation!",
                                        'Stay Tooned!']},
 EmceeDialoguePhase5Topic: {(1, 2020): ['Attention all Toons!',
                                        'The Cog invasions have been an unhappy event.',
                                        'As a result, silly levels have rapidly fallen...',
                                        'And no new objects are coming to life.',
                                        'But those that have are very thankful...',
                                        'And are showing their appreciation by helping in battle!',
                                        'We may hold off the Cogs yet, so keep up the fight!']},
 EmceeDialoguePhase6Topic: {(1, 2020): ['Congratulations Toons!',
                                        'You all succesfully held off the Cog Invasions...',
                                        'With a little help from our newly animated friends...',
                                        'And brought Toontown back to its usual silly self!',
                                        'We hope to get the Silly Meter rising again soon...',
                                        'So in the meantime, keep up the Cog fight...',
                                        'And enjoy the silliest place ever, Toontown!']}}
FriendsListPanelNewFriend = 'New Friend'
FriendsListPanelSecrets = 'True Friend'
FriendsListPanelOnlineFriends = 'ONLINE TOON\nFRIENDS'
FriendsListPanelAllFriends = 'ALL TOON\nFRIENDS'
FriendsListPanelIgnoredFriends = 'IGNORED\nTOONS'
FriendsListPanelPets = 'NEARBY\nPETS'
FriendsListPanelPlayers = 'ALL PLAYER\nFRIENDS'
FriendsListPanelOnlinePlayers = 'ONLINE PLAYER\nFRIENDS'
FriendsListPanelLocal = 'NEARBY\nTOONS'
FriendInviterClickToon = 'Click on the toon you would like to make friends with.\n\n(You have %s friends)'
FriendInviterToon = 'Toon'
FriendInviterThatToon = 'That toon'
FriendInviterPlayer = 'Player'
FriendInviterThatPlayer = 'That player'
FriendInviterBegin = 'What type of friend would you like to make?'
FriendInviterToonFriendInfo = 'A friend only in Toontown'
FriendInviterPlayerFriendInfo = 'A friend across the Project Altis network'
FriendInviterToonTooMany = 'You have too many toon friends to add another one now. You will have to remove some toon friends if you want to make friends with %s. You could also try making player friends them.'
FriendInviterPlayerTooMany = 'You have too many player friends to add another one now. You will have to remove some player friends if you want to make friends with %s. You could also try making toon friends with them.'
FriendInviterToonAlready = '%s is already your toon friend.'
FriendInviterPlayerAlready = '%s is already your player friend.'
FriendInviterStopBeingToonFriends = 'Stop being toon friends'
FriendInviterStopBeingPlayerFriends = 'Stop being player friends'
FriendInviterEndFriendshipToon = 'Are you sure you want to stop being toon friends with %s?'
FriendInviterEndFriendshipPlayer = 'Are you sure you want to stop being player friends with %s?'
FriendInviterRemainToon = '\n(You will still be toon friends with %s)'
FriendInviterRemainPlayer = '\n(You will still be player friends with %s)'
DownloadForceAcknowledgeVerbList = ['painted',
 'unpacked',
 'unfolded',
 'drawn',
 'inflated',
 'built']
DownloadForceAcknowledgeMsg = 'Sorry, the %(phase)s area is still being %(verb)s, and will be ready for you in a minute.'
TeaserTop = ''
TeaserBottom = ''
TeaserDefault = ',\nyou need to become a Member.\n\nJoin us!'
TeaserOtherHoods = 'For unlimited adventures in all 6 neighborhoods'
TeaserTypeAName = 'Type in your favorite name for your Toon!'
TeaserSixToons = 'To play more than one Toon'
TeaserClothing = 'To buy items from the Cattlelog \nto customize your toon'
TeaserCogHQ = 'To access awesome Cog HQs'
TeaserSecretChat = 'To use the True Friends Chat feature'
TeaserSpecies = 'To pick this type of Toon'
TeaserFishing = 'To fish in all 6 neighborhoods'
TeaserGolf = 'To play Toon MiniGolf'
TeaserParties = 'To plan a party'
TeaserSubscribe = 'Subscribe'
TeaserContinue = 'Return To Game'
TeaserEmotions = 'To make your Toon more expressive'
TeaserKarting = 'To access unlimited Kart Racing'
TeaserKartingAccessories = 'To customize your Kart'
TeaserGardening = 'To continue gardening at your Toon Estate'
TeaserHaveFun = 'Have more fun!'
TeaserJoinUs = 'Join us!'
TeaserPlantGags = 'To plant these gags'
TeaserPickGags = 'To pick these gags'
TeaserRestockGags = 'To restock these gags'
TeaserGetGags = 'To get these gags'
TeaserUseGags = 'To use these gags'
TeaserMinigames = TeaserOtherHoods
TeaserQuests = TeaserOtherHoods
TeaserOtherGags = TeaserOtherHoods
TeaserTricks = TeaserOtherHoods
LauncherPhaseNames = {0: 'Initialization',
 1: 'Panda',
 2: 'Engine',
 3: 'Make-A-Toon',
 3.5: 'Toontorial',
 4: 'Playground',
 5: 'Streets',
 5.5: 'Estates',
 6: 'Neighborhoods I',
 7: Cog + ' Buildings',
 8: 'Neighborhoods II',
 9: Sellbot + ' HQ',
 10: Cashbot + ' HQ',
 11: Lawbot + ' HQ',
 12: Bossbot + ' HQ',
 13: 'Parties'}
LauncherProgress = '%(name)s (%(current)s of %(total)s)'
LauncherStartingMessage = "Starting Project Altis... "
LauncherDownloadFile = 'Downloading update for ' + LauncherProgress + '...'
LauncherDownloadFileBytes = 'Downloading update for ' + LauncherProgress + ': %(bytes)s'
LauncherDownloadFilePercent = 'Downloading update for ' + LauncherProgress + ': %(percent)s%%'
LauncherDecompressingFile = 'Decompressing update for ' + LauncherProgress + '...'
LauncherDecompressingPercent = 'Decompressing update for ' + LauncherProgress + ': %(percent)s%%'
LauncherExtractingFile = 'Extracting update for ' + LauncherProgress + '...'
LauncherExtractingPercent = 'Extracting update for ' + LauncherProgress + ': %(percent)s%%'
LauncherPatchingFile = 'Applying update for ' + LauncherProgress + '...'
LauncherPatchingPercent = 'Applying update for ' + LauncherProgress + ': %(percent)s%%'
LauncherConnectProxyAttempt = 'Connecting to Project Altis: %s (proxy: %s) attempt: %s'
LauncherConnectAttempt = 'Connecting to Project Altis: %s attempt %s'
LauncherDownloadServerFileList = 'Updating Project Altis...'
LauncherCreatingDownloadDb = 'Updating Project Altis...'
LauncherDownloadClientFileList = 'Updating Project Altis...'
LauncherFinishedDownloadDb = 'Updating Project Altis... '
LauncherStartingGame = 'Starting Project Altis...'
LauncherRecoverFiles = 'Updating Project Altis. Recovering files...'
LauncherCheckUpdates = 'Checking for updates for ' + LauncherProgress
LauncherVerifyPhase = 'Updating Project Altis...'
LoadingDownloadWatcherUpdate = 'Loading %s'
AvatarChoiceMakeAToon = 'Make A\nToon'
AvatarChoicePlayThisToon = 'Play\nThis Toon'
AvatarChoiceSelectThisToon = 'Select\nThis Toon'
AvatarChoiceSubscribersOnly = 'Subscribe'
AvatarChoiceDelete = 'Delete'
AvatarChoiceDeleteConfirm = 'This will delete %s forever.'
AvatarChoiceNameRejected = 'Name\nRejected'
AvatarChoiceNameApproved = 'Name\nApproved!'
AvatarChoiceNameReview = 'Under\nReview'
AvatarChoiceNameYourToon = 'Name\nYour Toon!'
AvatarChoiceDeletePasswordText = 'Careful! This will delete %s forever.  To delete this Toon, enter your password.'
AvatarChoiceDeleteConfirmText = 'Careful! This will delete %(name)s forever.  If you are sure you want to do this, type "%(confirm)s" and click OK.'
AvatarChoiceDeleteConfirmUserTypes = 'delete'
AvatarChoiceDeletePasswordTitle = 'Delete Toon?'
AvatarChoicePassword = 'Password'
AvatarChoiceDeletePasswordOK = lOK
AvatarChoiceDeletePasswordCancel = lCancel
AvatarChoiceDeleteWrongPassword = 'That password does not seem to match.  To delete this Toon, enter your password.'
AvatarChoiceDeleteWrongConfirm = 'You didn\'t type the right thing.  To delete %(name)s, type "%(confirm)s" and click OK.  Do not type the quotation marks.  Click Cancel if you have changed your mind.'
AvatarChooserPickAToon = 'Pick  A  Toon  To  Play'
AvatarChooserQuit = lQuit
DateOfBirthEntryMonths = ['Jan',
 'Feb',
 'Mar',
 'Apr',
 'May',
 'Jun',
 'Jul',
 'Aug',
 'Sep',
 'Oct',
 'Nov',
 'Dec']
DateOfBirthEntryDefaultLabel = 'Date of Birth'
CertPageTitle = 'Beta Certificates'
PhotoPageNoName = 'Unnamed'
PhotoPageUnknownName = 'Unknown'
PhotoPageAddName = 'Add Caption'
PhotoPageAddNamePanel = 'Add a Caption to this Snapshot:'
PhotoPageDelete = 'Are you sure you want to delete'
PhotoPageConfirm = 'Yep!'
PhotoPageCancel = lCancel
PhotoPageClose = lClose
PhotoPageDirectory = 'Open Folder'
CertPageInfo = "You can view any beta certificates you have won in game here! If you wish to redeem one, take a screenshot of the certificate. Don't try to use a certificate more than once, we will know!"
AchievePageTitle = 'Achievements\n(Coming Soon)'
BuildingPageTitle = 'Buildings\n(Coming Soon)'
InventoryPageTitle = 'Gags'
InventoryPageDeleteTitle = 'DELETE GAGS'
InventoryPageTrackFull = 'You have all the gags in the %s track.'
InventoryPagePluralPoints = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s points.'
InventoryPageSinglePoint = 'You will get a new\n%(trackName)s gag when you\nget %(numPoints)s more %(trackName)s point.'
InventoryPageNoAccess = 'You do not have access to the %s track yet.'
AchievementsPageTitle = 'Achievements'

# Stats Page
StatsPageTitle = "Toon Stats"

StatsList = [
"Cogs defeated: %s",
"Buildings Saved: %s",
"Elite Cogs defeated: %s",
"Friends made: %s",
"Current friends: %s",
"Tasks completed: %s",
"VPs defeated: %s",
"CFOs defeated: %s",
"CJs defeated: %s",
"CEOs defeated: %s",
"??? defeated: %s",
"Times went sad: %s",
"Items purchased: %s",
"Fish caught: %s",
"Trolley games played: %s",
"Gags used: %s",
"Treasures collected: %s",
"Jellybeans spent: %s",
"Jellybeans earned: %s",
"SOS Cards used: %s",
"Unites used: %s",
"Summons used: %s",
"Fires used: %s",
"Factories defeated: %s",
"Mints defeated: %s",
"District Attorney Offices defeated: %s",
"Cog Golf Courses defeated: %s",
"??? defeated: %s"
]

EarnedAchievement = 'You earned an achievement!'

LockedAchievement = 'ACHIEVEMENT LOCKED'

AchievementCategories = [
 "Friends",
 "Catalog",
 "Trolley",
 "Cogs",
 "Gags",
 "Fishing",
 "Visit",
 "Special"]
Achievements = [
 "You've Got a Friend In Me!",
 "I'm In a Clique!",
 "Popular Toon in Town!",
 "Shipping and Handling is Free!",
 "Impulse Buyer!",
 "Regular Customer!",
 "Clarabelle's on Speed-dial!",
 "Choo Choo!",
 "That's-a Spicy Meatball!",
 "Counter-offer!",
 "Closed Lost!",
 "Breaking the Bank!",
 "Robbing the Bank!",
 "First Case!",
 "The Prosecution does not Rest!",
 "Demoted!",
 "Corporate Restructuring!",
 "Take a seat.",
 "All in favor?",
 "Closed Win!",
 "Buying the Bank!",
 "Per Curiam!",
 "You're the Boss!",
 "Motion Carried!",
 "It Tickles!",
 "You'll Slip and Slide on This!",
 "Attractive Personality!",
 "Professional Noisemaker!",
 "Shock and Awe!",
 "Heads up!",
 "How Did Island Here?",
 "Do You See What I Ski?",
 "Stay Composed!",
 "Don't be Such a Pansy!",
 "Make Like a Tree and Leaf!",
 "Grand Prix-ce of Cake!",
 "Counting Sheep!",
 "Welcome to the Club!",
 "The Sales Floor!",
 "Not the Mint I was Talking About!",
 "Justice Second!",
 "Board Yet?",
 "First Encounter!",
 "Ten Tin Suits!",
 "I'm 40% Corporate!",
 "Saving the Streets!",
 "Corporate Conundrum!",
 "Toontastic Takeover!",
 "Cog-Crusher!",
 "You Can Make a Fishstick With That!",
 "The Reel Deal!",
 "Not Bad, Cod Do Better!",
 "You're Krilling it!",
 "Sole of a Fisherman!",
 "Stand-up Comedian!",
 "You Just Activated my Trap Card!",
 "VERY Attractive Personality!",
 "Shrill of the Fight!",
 "You Underestimate My Flour!",
 "Go With the Flow!",
 "1.21 Gigawatts!",
 "I Missed the Minor Chord!",
 "Never gets old!",
 "Where Have you Bean All my Life?",
 "Viva la Resistance!",
 "Fun for Everyone!",
 "Minigame Mania!",
 "Frequent Rider!",
 "Solo Salesman!",
 "I Knead that Dough!",
 "Ace Attorney!",
 "Good Fore-Sight!",
 "Board of Director!",
 "Appraised!",
 "Depreciation!",
 "Evicted!",
 "Forclosure!",
 "Deed to the City!",
 "Shutting down the Factory!",
 "Plant Shutdown!",
 "Seizing the Means of Production!",
 "Loose Change!",
 "Making it Rain!",
 "Making it Pour!",
 "Corporate Espionage!",
 "Extradition!",
 "Legal Breakdown!",
 "Round of Putt-Putt!",
 "Country Club Regular!",
 "Tiger Woods!",
 "Board?",
 "I'd Like to Make a Proposal!",
 "Motion Acknowledged!"
]
AchievementsDesc = ("Make a friend",
 "Make 10 friends",
 "Make 50 friends",
 "Purchase an item from the cattlelog",
 "Purchase 10 items from the cattlelog",
 "Purchase 50 items from the cattlelog",
 "Purchase 100 items from the cattlelog",
 "Ride the trolley",
 "Visit Loopy's Balls",
 "Defeat the VP",
 "Defeat 10 VPs",
 "Defeat the CFO",
 "Defeat 10 CFOs",
 "Defeat the CJ",
 "Defeat 10 CJs",
 "Defeat the CEO",
 "Defeat 10 CEOs",
 "Defeat the Chairman",
 "Defeat 10 Chairmen",
 "Reach level 50 Sellbot Suit",
 "Reach level 50 Cashbot Suit",
 "Reach level 50 Lawbot Suit",
 "Reach level 50 Bossbot Suit",
 "Reach level 50 Boardbot Suit",
 "Unlock the TOON-UP gag track.",
 "Unlock the TRAP gag track.",
 "Unlock the LURE gag track.",
 "Unlock the SOUND gag track.",
 "Unlock the ZAP gag track.",
 "Unlock the DROP gag track.",
 "Visit Donald's Dock.",
 "Visit The Brrrrgh.",
 "Visit Minnie's Melodyland.",
 "Visit Daisy Gardens.",
 "Visit Acorn Acres.",
 "Visit Goofy Speedway.",
 "Visit Donald's Dreamland.",
 "Visit Bossbot HQ.",
 "Visit Sellbot HQ.",
 "Visit Cashbot HQ.",
 "Visit Lawbot HQ.",
 "Visit Boardbot HQ.",
 "Destroy 1 cog.",
 "Destroy 10 cogs.",
 "Destroy 100 cogs.",
 "Destroy 1,000 cogs.",
 "Destroy 10,000 cogs.",
 "Destroy 100,000 cogs.",
 "Destroy 1,000,000 cogs.",
 "Catch 1 fish.",
 "Catch 10 fish.",
 "Catch 100 fish.",
 "Catch 1,000 fish.",
 "Catch 10,000 fish.",
 "Max the TOON-UP gag track.",
 "Max the TRAP gag track.",
 "Max the LURE gag track.",
 "Max the SOUND gag track.",
 "Max the THROW gag track.",
 "Max the SQUIRT gag track.",
 "Max the ZAP gag track.",
 "Max the DROP gag track.",
 "Humor Sofie Squirt with a stale joke.",
 "Buy a doodle.",
 "Join the Resistance.",
 "Ride the trolley 10 times.",
 "Ride the trolley 50 times.",
 "Ride the trolley 100 times.",
 "Solo the VP.",
 "Solo the CFO.",
 "Solo the CJ.",
 "Solo the CEO.",
 "Solo the Chairman.",
 "Reclaim a Cog building.",
 "Reclaim 10 Cog buildings.",
 "Reclaim 50 Cog buildings.",
 "Reclaim 100 Cog buildings.",
 "Reclaim 250 Cog buildings.",
 "Defeat a Factory.",
 "Defeat 10 Factories.",
 "Defeat 50 Factories.",
 "Defeat a Mint.",
 "Defeat 10 Mints.",
 "Defeat 50 Mints.",
 "Defeat a District Attorney's Office.",
 "Defeat 10 District Attorney's Offices.",
 "Defeat 50 District Attorney's Offices.",
 "Defeat a Cog Golf Course.",
 "Defeat 10 Cog Golf Courses.",
 "Defeat 50 Cog Golf Courses.",
 "Defeat a Board Office.",
 "Defeat 10 Board Offices.",
 "Defeat 50 Board Offices.")
NPCFriendPageTitle = 'SOS Toons'
PartyDateFormat = '%(mm)s %(dd)d, %(yyyy).4d'
PartyTimeFormat = '%d:%.2d %s'
PartyTimeFormatMeridiemAM = 'am'
PartyTimeFormatMeridiemPM = 'pm'
PartyCanStart = "It's Party Time, click Start Party in your Shticker Book Hosting page!"
PartyHasStartedAcceptedInvite = '%s party has started!  Click the host then "Go To Party" in the Shticker Book Invites page.'
PartyHasStartedNotAcceptedInvite = '%s party has started! You can still go to it by teleporting to the host.'
EventsPageName = 'Events'
EventsPageCalendarTabName = 'Calendar'
EventsPageCalendarTabParty = 'Party'
EventsPageToontownTimeIs = 'TOONTOWN TIME IS'
EventsPageConfirmCancel = 'If you cancel, you will get a %d%% refund. Are you sure you want to cancel your party?'
EventsPageCancelPartyResultOk = 'Your party was cancelled and you got %d Jellybeans back!'
EventsPageCancelPartyResultError = 'Sorry, your party was not cancelled.'
EventsPageCancelPartyAlreadyRefunded = 'Your party was never started. Check your mailbox for your refund!'
EventsPageTooLateToStart = 'Sorry, it is too late to start your party. You can cancel it and plan another one.'
EventsPagePublicPrivateChange = "Changing your party's privacy setting..."
EventsPagePublicPrivateNoGo = "Sorry, you can't change your party's privacy setting right now."
EventsPagePublicPrivateAlreadyStarted = "Sorry, your party has already started, so you can't change your party's privacy setting."
EventsPageHostTabName = 'Hosting'
EventsPageHostTabTitle = 'My Next Party'
EventsPageHostTabTitleNoParties = 'No Parties'
EventsPageHostTabDateTimeLabel = 'You are having a party on %s at %s Toontown Time.'
EventsPageHostingTabNoParty = 'Go to a playground\nParty Gate to plan\nyour own party!'
EventsPageHostTabPublicPrivateLabel = 'This party is:'
EventsPageHostTabToggleToPrivate = 'Private'
EventsPageHostTabToggleToPublic = 'Public'
EventsPageHostingTabGuestListTitle = 'Guests'
EventsPageHostingTabActivityListTitle = 'Activities'
EventsPageHostingTabDecorationsListTitle = 'Decorations'
EventsPageHostingTabPartiesListTitle = 'Hosts'
EventsPageHostTabCancelButton = 'Cancel Party'
EventsPageGoButton = 'Start\nParty!'
EventsPageGoBackButton = 'Party\nNow!'
EventsPageInviteGoButton = 'Go to\nParty!'
EventsPageUnknownToon = 'Unknown Toon'
EventsPageInvitedTabName = 'Invitations'
EventsPageInvitedTabTitle = 'Party Invitations'
EventsPageInvitedTabInvitationListTitle = 'Invitations'
EventsPageInvitedTabActivityListTitle = 'Activities'
EventsPageInvitedTabTime = '%s %s Toontown Time'
EventsPageNewsTabName = 'News'
EventsPageNewsTabTitle = 'News'
EventsPageNewsDownloading = 'Retrieving News...'
EventsPageNewsUnavailable = 'Chip and Dale played with the printing press. News not available.'
EventsPageNewsPaperTitle = 'TOONTOWN TIMES'
EventsPageNewsLeftSubtitle = 'Still only 1 Jellybean'
EventsPageNewsRightSubtitle = 'Established toon-thousand nine'
NewsPageName = 'News'
NewsPageImportError = 'Whoops! There is an issue loading the "Toon News ... for the Amused!" Please check back later.'
NewsPageDownloadingNewsSubstr = 'Stay Tooned, while we bring you the latest issue of the \n"Toon News ... for the Amused!"'
NewsPageDownloadingNews0 = NewsPageDownloadingNewsSubstr + ' %s%% Complete.'
NewsPageDownloadingNews1 = NewsPageDownloadingNewsSubstr + ' %s%% Complete..'
NewsPageDownloadingNews2 = NewsPageDownloadingNewsSubstr + ' %s%% Complete...'
NewsPageErrorDownloadingFile = 'Whoops! Page %s is missing from "Toon News ... for the Amused!" Please check back later.'
NewsPageErrorDownloadingFileCanStillRead = 'Whoops! Page %s \nis missing from the "Toon News ... for the Amused!" \nTurn the page to continue, while we work to get this page back.'
NewsPageNoIssues = 'Whoops! The "Toon News ... for the Amused!" has gone missing! \nStay Tooned ... while we work to bring the news back!'
IssueFrameThisWeek = 'this week'
IssueFrameLastWeek = 'last week'
IssueFrameWeeksAgo = '%d weeks ago'
SelectedInvitationInformation = '%s is having a party on %s at %s Toontown Time.'
PartyPlannerNextButton = 'Continue'
PartyPlannerPreviousButton = 'Back'
PartyPlannerWelcomeTitle = 'Toontown Party Planner'
PartyPlannerInstructions = 'Hosting your own party is a lot of fun!\nStart planning with the arrows at the bottom!'
PartyPlannerDateTitle = 'Pick A Day For Your Party'
PartyPlannerTimeTitle = 'Pick A Time For Your Party'
PartyPlannerGuestTitle = 'Choose Your Guests'
PartyPlannerEditorTitle = 'Design Your Party\nPlace Activities and Decorations'
PartyPlannerConfirmTitle = 'Choose Invitations To Send'
PartyPlannerConfirmTitleNoFriends = 'Double Check Your Party'
PartyPlannerTimeToontown = 'Toontown'
PartyPlannerTimeTime = 'Time'
PartyPlannerTimeRecap = 'Party Date and Time'
PartyPlannerPartyNow = 'As Soon As Possible'
PartyPlannerTimeToontownTime = 'Toontown Time:'
PartyPlannerTimeLocalTime = 'Party Local Time : '
PartyPlannerPublicPrivateLabel = 'This party will be:'
PartyPlannerPublicDescription = 'Any Toon\ncan come!'
PartyPlannerPrivateDescription = 'Only\nInvited Toons\ncan come!'
PartyPlannerPublic = 'Public'
PartyPlannerPrivate = 'Private'
PartyPlannerCheckAll = 'Check\nAll'
PartyPlannerUncheckAll = 'Uncheck\nAll'
PartyPlannerDateText = 'Date'
PartyPlannerTimeText = 'Time'
PartyPlannerTTTimeText = 'Toontown Time'
PartyPlannerEditorInstructionsIdle = 'Click on the Party Activity or Decoration you would like to purchase.'
PartyPlannerEditorInstructionsClickedElementActivity = 'Click Buy or Drag the Activity Icon onto the Party Grounds Map'
PartyPlannerEditorInstructionsClickedElementDecoration = 'Click Buy or Drag the Decoration onto the Party Grounds Map'
PartyPlannerEditorInstructionsDraggingActivity = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsDraggingDecoration = 'Drag the Activity onto the Party Grounds Map.'
PartyPlannerEditorInstructionsPartyGrounds = 'Click and Drag items to move them around the Party Grounds Map'
PartyPlannerEditorInstructionsTrash = 'Drag an Activity or Decoration here to remove it.'
PartyPlannerEditorInstructionsNoRoom = 'There is no room to place that activity.'
PartyPlannerEditorInstructionsRemoved = '%(removed)s removed since %(added)s was added.'
PartyPlannerBeans = 'beans'
PartyPlannerTotalCost = 'Total Cost:\n%d beans'
PartyPlannerSoldOut = 'SOLD OUT'
PartyPlannerBuy = 'BUY'
PartyPlannerPaidOnly = 'MEMBERS ONLY'
PartyPlannerPartyGrounds = 'PARTY GROUNDS MAP'
PartyPlannerOkWithGroundsLayout = 'Are you done moving your Party Activities and Decorations around the Party Grounds Map?'
PartyPlannerChooseFutureTime = 'Please choose a time in the future.'
PartyPlannerInviteButton = 'Send Invites'
PartyPlannerInviteButtonNoFriends = 'Plan Party'
PartyPlannerBirthdayTheme = 'Birthday'
PartyPlannerGenericMaleTheme = 'Star'
PartyPlannerGenericFemaleTheme = 'Flower'
PartyPlannerRacingTheme = 'Racing'
PartyPlannerValentoonsTheme = 'ValenToons'
PartyPlannerVictoryPartyTheme = 'Victory'
PartyPlannerWinterPartyTheme = 'Winter'
PartyPlannerGuestName = 'Guest Name'
PartyPlannerClosePlanner = 'Close Planner'
PartyPlannerConfirmationAllOkTitle = 'Congratulations!'
PartyPlannerConfirmationAllOkText = 'Your party has been created and your invitations sent out.\nThanks!'
PartyPlannerConfirmationAllOkTextNoFriends = 'Your party has been created!\nThanks!'
PartyPlannerConfirmationErrorTitle = 'Oops.'
PartyPlannerConfirmationValidationErrorText = 'Sorry, there seems to be a problem\nwith that party.\nPlease go back and try again.'
PartyPlannerConfirmationDatabaseErrorText = "Sorry, I couldn't record all your information.\nPlease try again later.\nDon't worry, no beans were lost."
PartyPlannerConfirmationTooManyText = 'Sorry, you are already hosting a party.\nIf you want to plan another party, please\ncancel your current party.'
PartyPlannerInvitationThemeWhatSentence = 'You are invited to my %s party! %s!'
PartyPlannerInvitationThemeWhatSentenceNoFriends = 'I am hosting a %s party! %s!'
PartyPlannerInvitationThemeWhatActivitiesBeginning = 'It will have '
PartyPlannerInvitationWhoseSentence = '%s Party'
PartyPlannerInvitationTheme = 'Theme'
PartyPlannerInvitationWhenSentence = 'It will be on %s,\nat %s Toontown Time.\nHope you can make it!'
PartyPlannerInvitationWhenSentenceNoFriends = 'It will be on %s,\nat %s Toontown Time.\nToontastic!'
PartyPlannerComingSoon = 'Coming Soon'
PartyPlannerCantBuy = "Can't Buy"
PartyPlannerGenericName = 'Party Planner'
PartyJukeboxOccupied = 'Someone else is using the jukebox. Try again later.'
PartyJukeboxNowPlaying = 'The song you chose is now playing on the jukebox!'
MusicEncntrGeneralBg = 'Encounter With Cogs'
MusicTcSzActivity = 'Toontorial Medley'
MusicTcSz = 'Strolling Along'
MusicCreateAToon = 'The New Toon in Town'
MusicTtpaTheme = 'The Project Altis Theme'
MusicTtTheme = 'The Toontown Theme'
MusicMinigameRace = 'Slow and Steady'
MusicMgPairing = 'Remember Me?'
MusicTcNbrhood = 'Toontown Central'
MusicMgDiving = 'Treasure Lullaby'
MusicMgCannonGame = 'Fire the Cannons!'
MusicMgTwodgame = 'Running Toon'
MusicMgCogthief = 'Catch That Cog!'
MusicMgTravel = 'Traveling Music'
MusicMgTugOWar = 'Tug-of-War'
MusicMgVine = 'The Jungle Swing'
MusicMgIcegame = 'Slippery Situation'
MusicMgToontag = 'Minigame Medley'
MusicMMatchBg2 = 'Jazzy Minnie'
MusicMgTarget = "Soarin' Over Toontown"
MusicFfSafezone = 'The Funny Farm'
MusicDdSz = 'Waddling Way'
MusicMmNbrhood = "Minnie's Melodyland"
MusicGzPlaygolf = "Let's Play Golf!"
MusicGsSz = 'Goofy Speedway'
MusicOzSz = "Chip n' Dale's Acres"
MusicGsRaceCc = 'Downtown Driving'
MusicGsRaceSs = 'Ready, Set, Go!'
MusicGsRaceRr = 'Route 66'
MusicGzSz = 'The Putt-Putt Polka'
MusicMmSz = 'Dancing in the Streets'
MusicMmSzActivity = 'Here Comes Treble'
MusicDdNbrhood = "Donald's Dock"
MusicGsKartshop = 'Mr. Goofywrench'
MusicDdSzActivity = 'Sea Shanty'
MusicEncntrGeneralBgIndoor = 'Building Excitement'
MusicTakeOnMe = "Take on meeeee! (Take me on) Take me onnnnn! (Take on me) I'll be gone in a day or TWOOOOOOOOOOOOOOOOO!"
MusicTtElevator = 'Going Up?'
MusicEncntrToonWinningIndoor = 'Toons Unite!'
MusicEncntrGeneralSuitWinningIndoor = 'Cog-tastrophe!'
MusicTbNbrhood = 'The Brrrgh'
MusicDlNbrhood = "Donald's Dreamland"
MusicDlSzActivity = 'Counting Sheep'
MusicDgSz = 'Waltz of the Flowers'
MusicDlSz = 'Sleepwalking'
MusicTbSzActivity = 'Snow Problem'
MusicTbSz = 'Shiver and Shimmy'
MusicDgNbrhood = "Daisy's Garden"
MusicEncntrHallOfFame = 'The Hall of Fame'
MusicEncntrSuitHqNbrhood = 'Dollars and Cents'
MusicChqFactBg = 'Cog Factory'
MusicCoghqFinale = 'Triumph of the Toons'
MusicEncntrToonWinning = 'Cashing In!'
MusicEncntrSuitWinning = 'Selling You Short'
MusicEncntrHeadSuitTheme = 'The Big Boss'
MusicCashbotMintTheme = 'The Mints'
MusicEncntrCFOCraneTheme = 'Metal Clanks, Metal Clangs'
MusicLbJurybg = 'Court is in Session'
MusicLbCourtyard = 'Balancing Act'
MusicBossbotEntryV1 = 'Here We Are'
MusicBossbotFactoryV1 = 'Cog Waltz'
MusicBossbotFactoryV2 = 'Foreshadowed Lands'
MusicBossbotFactoryV3 = 'Dreaded Anticipation'
MusicBossbotCeoV1 = 'Bossing You Around'
MusicBossbotCeoV2 = 'A Battle To The End'
MusicPartyOriginalTheme = 'Party Time'
MusicPartyPolkaDance = 'Party Polka'
MusicPartySwingDance = 'Party Swing'
MusicPartyWaltzDance = 'Party Waltz'
MusicPartyGenericThemeJazzy = 'Party Jazz'
MusicPartyGenericTheme = 'Party Jingle'
JukeboxAddSong = 'Add\nSong'
JukeboxReplaceSong = 'Replace\nSong'
JukeboxQueueLabel = 'Playing Next:'
JukeboxSongsLabel = 'Pick a Song:'
JukeboxClose = 'Done'
JukeboxCurrentlyPlaying = 'Currently Playing'
JukeboxCurrentlyPlayingNothing = 'Jukebox is paused.'
JukeboxCurrentSongNothing = 'Add a song to the playlist!'
PartyOverWarningNoName = 'The party has ended! Thanks for coming!'
PartyOverWarningWithName = '%s party has ended! Thanks for coming!'
PartyCountdownClockText = 'Time\n\nLeft'
PartyTitleText = '%s Party'
PartyActivityConjunction = ', and'
PartyActivityNameDict = {0: {'generic': 'Jukebox',
     'invite': 'a Jukebox',
     'editor': 'Jukebox',
     'description': 'Listen to music with your own jukebox!'},
 1: {'generic': 'Party Cannons',
     'invite': 'Party Cannons',
     'editor': 'Cannons',
     'description': 'Fire yourself out of the cannons and into fun!'},
 2: {'generic': 'Trampoline',
     'invite': 'Trampoline',
     'editor': 'Trampoline',
     'description': 'Collect Jellybeans and bounce the highest!'},
 3: {'generic': 'Party Catch',
     'invite': 'Party Catch',
     'editor': 'Party Catch',
     'description': 'Catch fruit to win beans! Dodge those anvils!'},
 4: {'generic': 'Dance Floor\n10 moves',
     'invite': 'a 10 move Dance Floor',
     'editor': 'Dance Floor - 10',
     'description': 'Show off all 10 of your moves, toon style!'},
 5: {'generic': 'Party Tug-of-War',
     'invite': 'Party Tug-of-War',
     'editor': 'Tug-of-War',
     'description': 'Up to 4 on 4 toon tugging craziness!'},
 6: {'generic': 'Party Fireworks',
     'invite': 'Party Fireworks',
     'editor': 'Fireworks',
     'description': 'Launch your very own fireworks show!'},
 7: {'generic': 'Party Clock',
     'invite': 'a Party Clock',
     'editor': 'Party Clock',
     'description': 'Counts down the time left in your party.'},
 8: {'generic': 'Deluxe Jukebox',
     'invite': 'a deluxe jukebox',
     'editor': 'Deluxe Jukebox',
     'description': 'Your own deluxe jukebox with double the tunes for double the deal!'},
 9: {'generic': 'Dance Floor\n20 moves',
     'invite': 'a 20 move Dance Floor',
     'editor': 'Dance Floor - 20',
     'description': 'Show off all 20 of your moves, toon style!'},
 10: {'generic': 'Cog-O-War',
      'invite': 'Cog-O-War',
      'editor': 'Cog-O-War',
      'description': 'The team vs. team game of Cog splatting!'},
 11: {'generic': 'Cog Trampoline',
      'invite': 'Cog Trampoline',
      'editor': 'Cog Trampoline',
      'description': "Jump on a Cog's face!"},
 12: {'generic': 'Present Catch',
      'invite': 'Present Catch',
      'editor': 'Present Catch',
      'description': 'Catch presents to win beans! Dodge those anvils!'},
 13: {'generic': 'Holiday Trampoline',
      'invite': 'Holiday Trampoline',
      'editor': 'Holiday Trampoline',
      'description': 'Jump if you love Winter Holidays!'},
 14: {'generic': 'Holiday Cog-O-War',
      'invite': 'Holiday Cog-O-War',
      'editor': 'Holiday Cog-O-War',
      'description': 'The team vs. team game of Cog splattering!'},
 15: {'generic': 'Dance Floor\n10 moves',
      'invite': 'a 10 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 10',
      'description': 'Get your ValenToon Groove On!'},
 16: {'generic': 'Dance Floor\n20 moves',
      'invite': 'a 20 move ValenToons Dance Floor',
      'editor': 'Dance Floor - 20',
      'description': 'Get your ValenToon Groove On!'},
 17: {'generic': 'Jukebox\n20 songs',
      'invite': 'a 20 song Valentoons Jukebox',
      'editor': 'Jukebox - 20',
      'description': 'Nothing sets the mood like music!'},
 18: {'generic': 'Jukebox\n40 songs',
      'invite': 'a 40 song Valentoons jukebox',
      'editor': 'Jukebox - 40',
      'description': 'Nothing sets the mood like music!'},
 19: {'generic': 'Trampoline',
      'invite': 'ValenToons Trampoline',
      'editor': 'Trampoline',
      'description': "Jump to your heart's content!"}}
PartyDecorationNameDict = {0: {'editor': 'Balloon Anvil',
     'description': 'Try to keep the fun from floating away!'},
 1: {'editor': 'Party Stage',
     'description': 'Balloons, stars, what else could you want?'},
 2: {'editor': 'Party Bow',
     'description': 'Wrap up the fun!'},
 3: {'editor': 'Cake',
     'description': 'Delicious.'},
 4: {'editor': 'Party Castle',
     'description': "A Toon's home is his castle."},
 5: {'editor': 'Gift Pile',
     'description': 'Gifts for every Toon!'},
 6: {'editor': 'Streamer Horn',
     'description': 'This horn is a hoot! Streamers!'},
 7: {'editor': 'Party Gate',
     'description': 'Multi-colored and crazy!'},
 8: {'editor': 'Noise Makers',
     'description': 'Tweeeeet!'},
 9: {'editor': 'Pinwheel',
     'description': 'Colorful twirling for everyone!'},
 10: {'editor': 'Gag Globe',
      'description': 'Gag and star globe designed by Olivea'},
 11: {'editor': 'Bean Banner',
      'description': 'A Jellybean banner designed by Cassidy'},
 12: {'editor': 'Gag Cake',
      'description': 'A Topsy Turvy gag cake designed by Felicia'},
 13: {'editor': "Cupid's Heart",
      'description': 'Ready...Aim...\nValenToons!'},
 14: {'editor': 'Candy Hearts\n Banner',
      'description': "Who doesn't love candy hearts?"},
 15: {'editor': 'Flying Heart',
      'description': 'This heart is getting carried away!'},
 16: {'editor': 'Victory Bandstand',
      'description': 'All our new friends are ready to dance!'},
 17: {'editor': 'Victory Banner',
      'description': 'Not just a normal banner!'},
 18: {'editor': 'Confetti Cannons',
      'description': 'BOOM! Confetti! Fun!'},
 19: {'editor': 'Cog & Doodle',
      'description': "Ouch! That's gotta hurt."},
 20: {'editor': 'Cog Flappy Man',
      'description': 'A Cog full of hot air, what a shock!'},
 21: {'editor': 'Cog Ice Cream',
      'description': 'A Cog looking his best.'},
 22: {'editor': 'CogCicle',
      'description': 'A Cog looking his holiday best.'},
 23: {'editor': 'Holiday Bandstand',
      'description': 'Everyone loves a Holiday Party!'},
 24: {'editor': 'Chilly Cog',
      'description': "Ouch! That's gotta hurt."},
 25: {'editor': 'Snowman',
      'description': "So cool, he's hot!"},
 26: {'editor': 'SnowDoodle',
      'description': 'His only trick is being cold!'},
 27: {'editor': 'ValenToons Anvil',
      'description': "We've got your heart on a string!"}}
ActivityLabel = 'Cost - Activity Name'
PartyDoYouWantToPlan = 'Would you like to plan a new party right now?'
PartyPlannerOnYourWay = 'Have fun planning your party!'
PartyPlannerMaybeNextTime = 'Maybe next time.  Have a good day!'
PartyPlannerHostingTooMany = 'You can only host one party at a time, sorry.'
PartyPlannerOnlyPaid = 'Only paid toons can host a party, sorry.'
PartyPlannerNpcComingSoon = 'Parties are coming soon! Try again later.'
PartyPlannerNpcMinCost = 'It costs a minimum of %d Jellybeans to plan a party.'
PartyHatPublicPartyChoose = 'Do you want to go to the 1st available public party?'
PartyGateTitle = 'Public Parties'
PartyGateGoToParty = 'Go to\nParty!'
PartyGatePartiesListTitle = 'Hosts'
PartyGatesPartiesListToons = 'Toons'
PartyGatesPartiesListActivities = 'Activities'
PartyGatesPartiesListMinLeft = 'Minutes Left'
PartyGateLeftSign = 'Come On In!'
PartyGateRightSign = 'Public Parties Here!'
PartyGatePartyUnavailable = 'Sorry. That party is no longer available.'
PartyGatePartyFull = 'Sorry. That party is full.'
PartyGateInstructions = 'Click on a host, then click on "Go to Party"'
PartyActivityWaitingForOtherPlayers = 'Waiting for other players to join the party game...'
PartyActivityPleaseWait = 'Please wait...'
DefaultPartyActivityTitle = 'Party Game Title'
DefaultPartyActivityInstructions = 'PartyGame Instructions'
PartyOnlyHostLeverPull = 'Only the host can start this activity. Sorry.'
PartyActivityDefaultJoinDeny = 'You cannot join this activity right now. Sorry.'
PartyActivityDefaultExitDeny = 'You cannot leave this activity right now. Sorry.'
PartyJellybeanRewardOK = 'OK'
PartyCatchActivityTitle = 'Party Catch Activity'
PartyCatchActivityInstructions = "Catch as many pieces of fruit as you can. Try not to 'catch' any %(badThing)s!"
PartyCatchActivityFinishPerfect = 'PERFECT GAME!'
PartyCatchActivityFinish = 'Good Game!'
PartyCatchActivityExit = 'EXIT'
PartyCatchActivityApples = 'apples'
PartyCatchActivityOranges = 'oranges'
PartyCatchActivityPears = 'pears'
PartyCatchActivityCoconuts = 'coconuts'
PartyCatchActivityWatermelons = 'watermelons'
PartyCatchActivityPineapples = 'pineapples'
PartyCatchActivityAcorns = 'acorn'
PartyCatchActivityAnvils = 'anvils'
PartyCatchStarted = 'The game has started. Go play it.'
PartyCatchCannotStart = 'The game could not start right now.'
PartyCatchRewardMessage = 'Pieces of fruit caught: %s\n\nJellybeans earned: %d'
WinterPartyCatchActivityInstructions = "Catch as many presents as you can. Try not to 'catch' any %(badThing)s!"
WinterPartyCatchRewardMessage = 'Presents caught: %s\n\nJellybeans earned: %s'
PartyDanceActivityTitle = 'Party Dance Floor'
PartyDanceActivityInstructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 10 dance moves available. Can you find them all?'
PartyDanceActivity20Title = 'Party Dance Floor'
PartyDanceActivity20Instructions = 'Combine 3 or more ARROW KEY patterns to do dance moves! There are 20 dance moves available. Can you find them all?'
DanceAnimRight = 'Right'
DanceAnimReelNeutral = 'The Fishertoon'
DanceAnimConked = 'The Headbob'
DanceAnimHappyDance = 'The Happy Dance'
DanceAnimConfused = 'Very Dizzy'
DanceAnimWalk = 'Walking on the Moon'
DanceAnimJump = 'The Jump!'
DanceAnimFirehose = 'The Firetoon'
DanceAnimShrug = 'Who Knows?'
DanceAnimSlipForward = 'The Fall'
DanceAnimSadWalk = 'Tired'
DanceAnimWave = 'Hello Goodbye'
DanceAnimStruggle = 'The Shuffle Hop'
DanceAnimRunningJump = 'The Running Toon'
DanceAnimSlipBackward = 'The Backfall'
DanceAnimDown = 'Down'
DanceAnimUp = 'Up'
DanceAnimGoodPutt = 'The Putt'
DanceAnimVictory = 'The Victory Dance'
DanceAnimPush = 'The Mimetoon'
DanceAnimAngry = "Rock n' Roll"
DanceAnimLeft = 'Left'
PartyCannonActivityTitle = 'Party Cannons'
PartyCannonActivityInstructions = 'Hit the clouds to change their color and bounce in the air! While IN THE AIR, you can USE THE ARROW KEYS to GLIDE.'
PartyCannonResults = 'You collected %d jelly beans!\n\nNumber of Clouds Hit: %d'
FireworksActivityInstructions = 'Look up using the "Page Up" key to see better.'
FireworksActivityBeginning = 'Party fireworks are about to start! Enjoy the show!'
FireworksActivityEnding = 'Hope you enjoyed the show!'
PartyFireworksAlreadyActive = 'The fireworks show has already started.'
PartyFireworksAlreadyDone = 'The fireworks show is over.'
PartyTrampolineJellyBeanTitle = 'Jelly Beans Trampoline'
PartyTrampolineTricksTitle = 'Tricks Trampoline'
PartyTrampolineActivityInstructions = 'Use the Control key to jump.\n\nJump when your Toon is at its lowest point on the trampoline to jump higher.'
PartyTrampolineActivityOccupied = 'Trampoline in use.'
PartyTrampolineQuitEarlyButton = 'Hop Off'
PartyTrampolineBeanResults = 'You collected %d jelly beans.'
PartyTrampolineBonusBeanResults = 'You collected %d jelly beans, plus %d more for getting the Big Bean. '
PartyTrampolineTopHeightResults = 'Your top height was %d ft.'
PartyTrampolineTimesUp = "Time's Up"
PartyTrampolineReady = 'Ready...'
PartyTrampolineGo = 'Go!'
PartyTrampolineBestHeight = 'Best Height So Far:\n%s\n%d ft'
PartyTrampolineNoHeightYet = 'How high\ncan you jump?'
PartyTrampolineGetHeight = '%d ft'
PartyTeamActivityForMorePlural = 's'
PartyTeamActivityForMore = 'Waiting  for  %d  player%s\non  each  side...'
PartyTeamActivityForMoreWithBalance = 'Waiting  for  %d  more  player%s...'
PartyTeamActivityWaitingForOtherPlayers = 'Waiting  for  other  players...'
PartyTeamActivityWaitingToStart = 'Starting  in...'
PartyTeamActivityExitButton = 'Hop Off'
PartyTeamActivitySwitchTeamsButton = 'Switch\nTeams'
PartyTeamActivityWins = '%s team wins!'
PartyTeamActivityLocalAvatarTeamWins = 'Your team won!'
PartyTeamActivityGameTie = "It's a tie!"
PartyTeamActivityJoinDenied = "Sorry, you can't join %s at this time."
PartyTeamActivityExitDenied = 'Sorry, you are unable to leave %s at this time.'
PartyTeamActivitySwitchDenied = "Sorry, you cant's switch teams at this time."
PartyTeamActivityTeamFull = 'Sorry, that team is already full!'
PartyTeamActivityRewardMessage = 'You got %d Jellybeans. Good job!'
PartyCogTeams = ('Blue', 'Orange')
PartyCogRewardMessage = 'Your Score: %d\n'
PartyCogRewardBonus = '\nYou got %d additional Jellybean%s because your team won!'
PartyCogJellybeanPlural = 's'
PartyCogSignNote = 'HI-SCORE\n%s\n%d'
PartyCogTitle = 'Cog-O-War'
PartyCogInstructions = 'Throw pies at cogs to push them away from your team. ' + "When time's up, the team with most cogs on the other side wins!" + '\n\nThrow with the CONTROL KEY. Move with the ARROW KEYS.'
PartyCogDistance = '%d ft'
PartyCogTimeUp = "Time's up!"
PartyCogGuiScoreLabel = 'SCORE'
PartyCogGuiPowerLabel = 'POWER'
PartyCogGuiSpamWarning = 'Hold CONTROL for more power!'
PartyCogBalanceBar = 'BALANCE'
PartyTugOfWarReady = 'Ready...'
PartyTugOfWarGo = 'GO!'
PartyTugOfWarGameEnd = 'Good  game!'
PartyTugOfWarTitle = 'Party Tug-of-War'
CalendarShowAll = 'Show All'
CalendarShowOnlyHolidays = 'Show Only Holidays'
CalendarShowOnlyParties = 'Show Only Parties'
CalendarEndsAt = 'Ends at '
CalendarStartedOn = 'Started on '
CalendarEndDash = 'End-'
CalendarEndOf = 'End of '
CalendarPartyGetReady = 'Get ready!'
CalendarPartyGo = 'Go party!'
CalendarPartyFinished = "It's over..."
CalendarPartyCancelled = 'Cancelled.'
CalendarPartyNeverStarted = 'Never Started.'
NPCFriendPanelRemaining = '%d Remaining'
MapPageTitle = 'Map'
MapPageBackToPlayground = 'Back to Playground'
MapPageBackToCogHQ = 'Back to Cog Headquarters'
MapPageGoHome = 'Go Home'
MapPageYouAreHere = 'You are in: %s\n%s'
MapPageYouAreAtHome = 'You are at\nyour estate'
MapPageYouAreAtSomeonesHome = 'You are at %s estate'
MapPageGoTo = 'Go To\n%s'
OptionsPageTitle = 'Options'
OptionsPageSpecial = 'Advanced'
OptionsTabTitle = 'Options\n& Codes'
OptionsPagePurchase = 'Subscribe'
OptionsPageLogout = 'Logout'
OptionsPageExitToontown = 'Exit Toontown'
OptionsPageMusic = 'Music:'
OptionsPageSFX = 'Sound Effects:'
OptionsPageToonChatSoundsOnLabel = 'Type Chat Sounds are on.'
OptionsPageToonChatSoundsOffLabel = 'Type Chat Sounds are off.'
OptionsPageFriendsEnabledLabel = 'Accepting new friend requests.'
OptionsPageFriendsDisabledLabel = 'Not accepting friend requests.'
OptionsPageWhisperEnabledLabel = 'Allowing whispers from anyone.'
OptionsPageWhisperDisabledLabel = 'Allowing whispers from friends only.'
OptionsPageSpeedChatStyleLabel = 'SpeedChat Color'
OptionsPageDisplayWindowed = 'windowed'
OptionsPageSelect = 'Select'
OptionsPageToggleOn = 'Turn On'
OptionsPageToggleOff = 'Turn Off'
OptionsPageChange = 'Change'
OptionsPageDisplaySettings = 'Display: %(screensize)s, %(api)s'
OptionsPageDisplaySettingsNoApi = 'Display: %(screensize)s'
OptionsPageExitConfirm = 'Exit Toontown?'
CodePageTitle = 'Codes'
ItemsPageTitle = 'Items'
ItemsPageNametagStyle = 'Nametag Style'
ItemsPageFishingRods = "Fishing Rod"
ItemsPageCheesyEffect = "Cheesy Effect"
DisplaySettingsTitle = 'Display Settings'
DisplaySettingsIntro = 'The following settings are used to configure the way Toontown is displayed on your computer.  It is usually unnecessary to adjust these unless you are experiencing a problem.'
DisplaySettingsIntroSimple = 'You may adjust the screen resolution to a higher value to improve the clarity of text and graphics in Toontown, but depending on your graphics card, some higher values may make the game run less smoothly or may not work at all.'
DisplaySettingsApi = 'Graphics API:'
DisplaySettingsResolution = 'Resolution:'
DisplaySettingsWindowed = 'In a window'
DisplaySettingsFullscreen = 'Full screen'
DisplaySettingsApply = 'Apply'
DisplaySettingsCancel = lCancel
DisplaySettingsApplyWarning = 'When you press OK, the display settings will change.  If the new configuration does not display properly on your computer, the display will automatically return to its original configuration after %s seconds.'
DisplaySettingsAccept = 'Press OK to keep the new settings, or Cancel to revert.  If you do not press anything, the settings will automatically revert back in %s seconds.'
DisplaySettingsRevertUser = 'Your previous display settings have been restored.'
DisplaySettingsRevertFailed = 'The selected display settings do not work on your computer.  Your previous display settings have been restored.'
OptionsPageCodesTab = 'Enter Code'
CdrPageTitle = 'Enter a Code'
CdrInstructions = 'Enter your code to receive a special item in your mailbox.'
CdrResultSuccess = 'Congratulations! Check your mailbox to claim your item!'
CdrResultInvalidCode = "You've entered an invalid code. Please check the code and try again."
CdrResultIneligibleCode = "You are not eligible for this code!"
CdrResultExpiredCode = "We're sorry. This code has expired."
CdrResultUnknownError = "We're sorry. This code cannot be applied to your Toon."
CdrResultMailboxFull = 'Your mailbox is full. Please remove an item, then enter your code again.'
CdrResultAlreadyInMailbox = "You've already received this item. Check your mailbox to confirm."
CdrResultAlreadyInQueue = 'Your item is on its way. Check your mailbox in a few minutes to receive it.'
CdrResultAlreadyInCloset = "You've already received this item. Check your closet to confirm."
CdrResultAlreadyBeingWorn = "You've already received this item, and you are wearing it!"
CdrResultAlreadyReceived = "You've already received this item."
CdrResultTooManyFails = "We're sorry. You've tried to enter an incorrect code too many times. Please try again after some time."
CdrResultServiceUnavailable = "We're sorry. This feature is temporarily unavailable. Please try again during your next login."
CdrResultClosetFull = 'Your closet is full. Please remove an item, then enter your code again.'
CdrResultTrunkFull = 'Your trunk is full. Please remove an item, then enter your code again.'
InsomniaReusableCodes = 'If you are using an Insomnia 60 code, keep it! You can reuse the code when beta comes along!'
TrackPageTitle = 'Gag Track Training'
TrackPageShortTitle = 'Gag Training'
TrackPageSubtitle = 'Training Points:'
TrackPageUnlocked = 'UNLOCKED'
TrackPageProgress = '%s/2 POINTS TO UNLOCK'
TrackPageHints = ['First of 2 pieces of the gag training reel, get both to unlock the gag track!', 'Last piece of the gag training reel, get both to unlock the gag track!', 'Adds a 20% self heal bonus to Toon-up gags.', '???', '???',
 'First of 2 pieces of the gag training reel, get both to unlock the gag track!', 'Last piece of the gag training reel, get both to unlock the gag track!', 'Adds a 10% chance to not use a Trap gag.', '???', '???',
 'First of 2 pieces of the gag training reel, get both to unlock the gag track!', 'Last piece of the gag training reel, get both to unlock the gag track!', 'Adds an additional round of stun to Lure gags.', '???', '???',
 'First of 2 pieces of the gag training reel, get both to unlock the gag track!', 'Last piece of the gag training reel, get both to unlock the gag track!', 'All Sound gags get a bonus damage equal to 1/2 the highest level cog in the battle.', '???', '???',
 'First of 2 pieces of the gag training reel, get both to unlock the gag track!', 'Last piece of the gag training reel, get both to unlock the gag track!', 'Adds a 10% damage bonus to Throw gags.', '???', '???',
 'First of 2 pieces of the gag training reel, get both to unlock the gag track!', 'Last piece of the gag training reel, get both to unlock the gag track!', 'Adds an extra round of soak to Squirt gags, as well as giving a -20 defense debuff to the cog, as long as the cog is soaked.', '???', '???',
 'First of 2 pieces of the gag training reel, get both to unlock the gag track!', 'Last piece of the gag training reel, get both to unlock the gag track!', 'Increases the chance for Zap gags to cause a shortcircuit by 1.5x (50%).', '???', '???',
 'First of 2 pieces of the gag training reel, get both to unlock the gag track!', 'Last piece of the gag training reel, get both to unlock the gag track!', 'Adds a 20% accuracy bonus to Drop gags.', '???', '???']
TrackPageUpgrade = 'Training Point Use'
TrackPageAckTakeback = 'You are about to allocate a training point into the %(track)s gag track, you can take the training point back IF you have only allocated one point into the track. Once the second point is allocated, you can no longer take those points back! Are you sure you want to use your training point?'
TrackPageAckPrestige = 'You are about to allocate a training point into the %(track)s gag track, it will add the following bonus:\n\n%(bonus)s\n\nThis third training point is not permanent, but it isn\'t cheap to buy back! Are you sure you want to upgrade %(track)s?'
QuestPageToonTasks = 'ToonTasks'
QuestPageChoose = 'Choose'
QuestPageLocked = 'Locked'
QuestPageDestination = '%s\n%s\n%s'
QuestPageNameAndDestination = '%s\n%s\n%s\n%s'
QuestPosterHQOfficer = lHQOfficerM
QuestPosterHQBuildingName = lToonHQ
QuestPosterHQStreetName = 'Any Street'
QuestPosterHQLocationName = 'Any Neighborhood'
QuestPosterTailor = 'Tailor'
QuestPosterTailorBuildingName = 'Clothing Store'
QuestPosterTailorStreetName = 'Any Playground'
QuestPosterTailorLocationName = 'Any Neighborhood'
QuestPosterPlayground = 'In the playground'
QuestPosterAtHome = 'At your home'
QuestPosterInHome = 'In your home'
QuestPosterOnPhone = 'On your phone'
QuestPosterEstate = 'At your estate'
QuestPosterAnywhere = 'Anywhere'
QuestPosterAuxTo = 'to:'
QuestPosterAuxFrom = 'from:'
QuestPosterAuxFor = 'for:'
QuestPosterAuxOr = 'or:'
QuestPosterAuxReturnTo = 'Return to:'
QuestPosterLocationIn = ' in '
QuestPosterLocationOn = ' in '
QuestPosterFun = 'Just for fun!'
QuestPosterExp = 'Experience: '
QuestPosterFishing = 'GO FISHING'
QuestPosterComplete = 'COMPLETE'
QuestPosterConfirmDelete = 'Are you sure you want to delete this ToonTask?'
QuestPosterDeleteBtn = 'Delete'
QuestPosterDialogYes = 'Delete'
QuestPosterDialogNo = 'Cancel'
ShardPageTitle = 'Districts'
ShardPageHelpIntro = 'Each District is a copy of the Toontown world.'
ShardPageHelpWhere = '  You are currently in the "%s" District.'
ShardPageHelpWelcomeValley = '  You are currently in the "Welcome Valley" District, within "%s".'
ShardPageHelpMove = '  To move to a new District, click on its name.'
ShardPagePopulationTotal = 'Total Toontown Population:\n%d'
ShardPageScrollTitle = 'Name            Population'
ShardPageLow = 'Quiet'
ShardPageMed = 'Ideal'
ShardPageHigh = 'Full'
ShardPageChoiceReject = 'Sorry, that district is full. Please try another one.'
SuitPageTitle = 'Cog Gallery'
SuitPageMystery = DialogQuestion + DialogQuestion + DialogQuestion
SuitPageQuota = '%s of %s'
SuitPageCogRadar = '%s present'
SuitPageBuildingRadarS = '%s building'
SuitPageBuildingRadarP = '%s buildings'
DisguisePageTitle = Cog + ' Disguise'
DisguisePageMeritAlert = 'Ready for\npromotion!'
DisguisePageCogLevel = 'Level %s'
DisguisePageMeritFull = 'Full'
FishPageTitle = 'Fishing'
FishPageTitleTank = 'Fish Bucket'
FishPageTitleCollection = 'Fish Album'
FishPageTitleTrophy = 'Fishing Trophies'
FishPageWeightStr = 'Weight: '
FishPageWeightLargeS = '%d lb. '
FishPageWeightLargeP = '%d lbs. '
FishPageWeightSmallS = '%d oz.'
FishPageWeightSmallP = '%d oz.'
FishPageWeightConversion = 16
FishPageValueS = 'Value: %d Jellybean'
FishPageValueP = 'Value: %d Jellybeans'
FishPageCollectedTotal = 'Fish Species Collected: %d of %d'
FishPageRodInfo = '%s Rod\n%d - %d Pounds'
FishPageTankTab = 'Bucket'
FishPageCollectionTab = 'Album'
FishPageTrophyTab = 'Trophies'
FishPickerTotalValue = 'Bucket: %s / %s\nValue: %d Jellybeans'
UnknownFish = '???'
FishingRod = '%s Rod'
FishingRodNameDict = {0: 'Twig',
 1: 'Bamboo',
 2: 'Hardwood',
 3: 'Steel',
 4: 'Gold'}
FishTrophyNameDict = {0: 'Guppy',
 1: 'Minnow',
 2: 'Fish',
 3: 'Flying Fish',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
GardenPageTitle = 'Gardening'
GardenPageTitleBasket = 'Flower Basket'
GardenPageTitleCollection = 'Flower Album'
GardenPageTitleTrophy = 'Gardening Trophies'
GardenPageTitleSpecials = 'Gardening Specials'
GardenPageBasketTab = 'Basket'
GardenPageCollectionTab = 'Album'
GardenPageTrophyTab = 'Trophies'
GardenPageSpecialsTab = 'Specials'
GardenPageCollectedTotal = 'Flower Varieties Collected: %d of %d'
GardenPageValueS = 'Value: %d Jellybean'
GardenPageValueP = 'Value: %d Jellybeans'
FlowerPickerTotalValue = 'Basket: %s / %s\nValue: %d Jellybeans'
GardenPageShovelInfo = '%s Shovel: %d / %d\n'
GardenPageWateringCanInfo = '%s Watering Can: %d / %d'
FlowerPageWeightConversion = 1
FlowerPageWeightLargeP = 'Large P'
FlowerPageWeightLargeS = 'LargeS '
FlowerPageWeightSmallP = 'SmallP '
FlowerPageWeightSmallS = 'SmallS '
FlowerPageWeightStr = 'Weight: %s'
KartPageTitle = 'Karts'
KartPageTitleCustomize = 'Kart Customizer'
KartPageTitleRecords = 'Personal Best Records'
KartPageTitleTrophy = 'Racing Trophies'
KartPageCustomizeTab = 'Customize'
KartPageRecordsTab = 'Records'
KartPageTrophyTab = 'Trophy'
KartPageTrophyDetail = 'Trophy %s : %s'
KartPageTickets = 'Tickets : '
KartPageConfirmDelete = 'Delete Accessory?'
KartShtikerDelete = 'Delete'
KartShtikerSelect = 'Select a Category'
KartShtikerNoAccessories = 'No Accessories Owned'
KartShtikerBodyColors = 'Kart Colors'
KartShtikerAccColors = 'Accessory Colors'
KartShtikerEngineBlocks = 'Hood Accessories'
KartShtikerSpoilers = 'Trunk Accessories'
KartShtikerFrontWheelWells = 'Front Wheel Accessories'
KartShtikerBackWheelWells = 'Back Wheel Accessories'
KartShtikerRims = 'Rim Accessories'
KartShtikerDecals = 'Decal Accessories'
KartShtikerBodyColor = 'Kart Color'
KartShtikerAccColor = 'Accessory Color'
KartShtikerEngineBlock = 'Hood'
KartShtikerSpoiler = 'Trunk'
KartShtikerFrontWheelWell = 'Front Wheel'
KartShtikerBackWheelWell = 'Back Wheel'
KartShtikerRim = 'Rim'
KartShtikerDecal = 'Decal'
KartShtikerDefault = 'Default %s'
KartShtikerNo = 'No %s Accessory'
QuestChoiceGuiCancel = lCancel
TrackChoiceGuiChoose = 'Choose'
TrackChoiceGuiRandom = "I'm feeling lucky"
TrackChoiceGuiAreYouSure = 'Are you sure?'
TrackChoiceGuiCancel = lCancel
TrackChoiceGuiHEAL = 'Toonup lets you heal other Toons in battle.'
TrackChoiceGuiTRAP = 'Traps are powerful gags that must be used with Lure.'
TrackChoiceGuiLURE = 'Use Lure to stun Cogs or draw them into traps.'
TrackChoiceGuiSOUND = 'Sound gags affect all Cogs, but are not very powerful.'
TrackChoiceGuiZAP = 'Zap gags are weak, but when paired with squirt, they can shortcircuit a cog and deal 2x damage.'
TrackChoiceGuiDROP = 'Drop gags do lots of damage, but are not very accurate.'
EmotePageTitle = 'Expressions / Emotions'
EmotePageDance = 'You have built the following dance sequence:'
EmoteJump = 'Jump'
EmoteDance = 'Dance'
EmoteHappy = 'Happy'
EmoteSad = 'Sad'
EmoteAnnoyed = 'Annoyed'
EmoteSleep = 'Sleepy'
TIPPageTitle = 'TIP'
SuitBaseNameWithLevel = '%(name)s\n%(dept)s\nLevel %(level)s'
HealthForceAcknowledgeMessage = 'You cannot leave the playground until your Laff meter is smiling!'
InventoryTotalGags = 'Total gags\n%d / %d'
InventroyPinkSlips = '%s Pink Slips'
InventroyPinkSlip = '1 Pink Slip'
InventoryDelete = 'DELETE'
InventoryDeleteAll = 'DELETE ALL'
InventoryDeleteConfirm = "Are you sure you want to delete all your gags? Don't worry, your level 7 gags will be safe"
InventoryDone = 'DONE'
InventoryDeleteHelp = 'Click on a gag to DELETE it.'
InventorySkillCredit = 'Skill credit: %s'
InventorySkillCreditNone = 'Skill credit: None'
InventoryDetailAmount = '%(numItems)s / %(maxItems)s'
InventoryDetailData = 'Accuracy: %(accuracy)s\n%(damageString)s: %(damage)d%(bonus)s\n%(singleOrGroup)s'
InventoryDetailDataExtra = 'Accuracy: %(accuracy)s\n%(damageString)s: %(damage)d%(bonus)s\n%(singleOrGroup)s\n%(extra)s'
TrapExtraText = '+10% chance to save gag'
SoundExtraText = '(+Varies)'
HealExtraText = '%(heal)s self'
ZapExtraText = 'Fry Chance: %s'
InventoryTrackExp = '%(curExp)s / %(nextExp)s'
InventoryUberTrackExp = '%(nextExp)s to Go!'
InventoryGuestExp = 'Guest Limit'
GuestLostExp = 'Over Guest Limit'
InventoryAffectsOneCog = 'Affects: One ' + Cog
InventoryAffectsOneToon = 'Affects: One Toon'
InventoryAffectsAllToons = 'Affects: All Toons'
InventoryAffectsAllCogs = 'Affects: All ' + Cogs
InventoryHealString = 'Toon-up'
InventoryDamageString = 'Damage'
InventoryLureString = 'Rounds active'
InventorySquirtRoundsString = 'Rounds soaked: %s'
InventoryBattleMenu = 'BATTLE MENU'
InventoryRun = 'RUN'
InventorySOS = 'SOS'
InventoryPass = 'PASS'
InventoryFire = 'FIRE'
InventoryLevelsShow = 'SHOW LEVELS'
InventoryLevelsHide = 'HIDE LEVELS'
InventoryClickToAttack = 'Click a\ngag to\nattack'
InventoryDamageBonus = '(+%d)'
InventoryDamageBonusString = '(+%s)'
NPCForceAcknowledgeMessage = "You must visit the bank before leaving.\n\n\n\n\n\n\n\n\nYou can find the bank next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage2 = 'You must return to Toon Headquarters before leaving.\n\n\n\n\n\n\n\n\n\nToon Headquarters is located near the center of the playground.'
NPCForceAcknowledgeMessage3 = "Remember to visit Banker Bob.\n\n\n\n\n\n\n\nYou can find the bank next to Goofy's Gag Shop."
NPCForceAcknowledgeMessage4 = 'Looks like you found Banker Bob! Great work!\n\n\n\n\n\n\n\n\n\nNow report back to Toon Headquarters.'
NPCForceAcknowledgeMessage5 = "Don't forget your ToonTask!\n\n\n\n\n\n\n\n\n\n\nYou can find Cogs to defeat on the other side of tunnels like this."
NPCForceAcknowledgeMessage6 = 'Great job defeating those Cogs!\n\n\n\n\n\n\n\n\nHead back to Toon Headquarters as soon as possible.'
NPCForceAcknowledgeMessage7 = "Don't forget to make a friend!\n\n\n\n\n\n\nClick on another player and use the New Friend button."
NPCForceAcknowledgeMessage8 = 'Great! You made a new friend!\n\n\n\n\n\n\n\n\nYou should go back at Toon Headquarters now.'
NPCForceAcknowledgeMessage9 = 'Good job using the phone!\n\n\n\n\n\n\n\n\nReturn to Toon Headquarters to claim your reward.'
ToonSleepString = '. . . ZZZ . . .'
MovieTutorialReward1 = 'You received 1 Throw point! When you get 10, you will get a new gag!'
MovieTutorialReward2 = 'You received 1 Squirt point! When you get 10, you will get a new gag!'
MovieTutorialReward3 = 'Good job! You completed your first ToonTask!'
MovieTutorialReward4 = 'Go to Toon Headquarters for your reward!'
MovieTutorialReward5 = 'Have fun!'
BattleGlobalTracks = ['toon-up',
 'trap',
 'lure',
 'sound',
 'throw',
 'squirt',
 'zap',
 'drop']
BattleGlobalNPCTracks = ['restock', 'toons hit', 'cogs miss']
BattleGlobalAvPropStrings = (('Feather',
  'Megaphone',
  'Lipstick',
  'Bamboo Cane',
  'Pixie Dust',
  'Juggling Balls',
  'High Dive'),
 ('Banana Peel',
  'Rake',
  'Marbles',
  'Quicksand',
  'Trapdoor',
  'TNT',
  'Railroad'),
 ('$1 bill',
  'Small Magnet',
  '$5 bill',
  'Big Magnet',
  '$10 bill',
  'Hypno-goggles',
  'Presentation'),
 ('Bike Horn',
  'Whistle',
  'Bugle',
  'Aoogah',
  'Elephant Trunk',
  'Foghorn',
  'Opera Singer'),
 ('Cupcake',
  'Fruit Pie Slice',
  'Cream Pie Slice',
  'Whole Fruit Pie',
  'Whole Cream Pie',
  'Birthday Cake',
  'Wedding Cake'),
 ('Squirting Flower',
  'Glass of Water',
  'Squirt Gun',
  'Seltzer Bottle',
  'Fire Hose',
  'Storm Cloud',
  'Geyser'),
 ('Joybuzzer',
  'Carpet',
  'Balloon',
  'Kart Battery',
  'Tazer',
  'Tesla Coil',
  'Lightning'),
 ('Flower Pot',
  'Sandbag',
  'Anvil',
  'Big Weight',
  'Safe',
  'Grand Piano',
  'Toontanic'))
BattleGlobalAvPropStringsSingular = (('a Feather',
  'a Megaphone',
  'a Lipstick',
  'a Bamboo Cane',
  'a Pixie Dust',
  'a set of Juggling Balls',
  'a High Dive'),
 ('a Banana Peel',
  'a Rake',
  'a set of Marbles',
  'a patch of Quicksand',
  'a Trapdoor',
  'a TNT',
  'a Railroad'),
 ('a $1 bill',
  'a Small Magnet',
  'a $5 bill',
  'a Big Magnet',
  'a $10 bill',
  'a pair of Hypno-goggles',
  'a Presentation'),
 ('a Bike Horn',
  'a Whistle',
  'a Bugle',
  'an Aoogah',
  'an Elephant Trunk',
  'a Foghorn',
  'an Opera Singer'),
 ('a Cupcake',
  'a Fruit Pie Slice',
  'a Cream Pie Slice',
  'a Whole Fruit Pie',
  'a Whole Cream Pie',
  'a Birthday Cake',
  'a Wedding Cake'),
 ('a Squirting Flower',
  'a Glass of Water',
  'a Squirt Gun',
  'a Seltzer Bottle',
  'a Fire Hose',
  'a Storm Cloud',
  'a Geyser'),
 ('a Joybuzzer',
  'a Carpet',
  'a Balloon',
  'a Kart Battery',
  'a Tazer',
  'a Tesla Coil',
  'Lightning'),
 ('a Flower Pot',
  'a Sandbag',
  'an Anvil',
  'a Big Weight',
  'a Safe',
  'a Grand Piano',
  'the Toontanic'))
BattleGlobalAvPropStringsPlural = (('Feathers',
  'Megaphones',
  'Lipsticks',
  'Bamboo Canes',
  'Pixie Dusts',
  'sets of Juggling Balls',
  'High Dives'),
 ('Banana Peels',
  'Rakes',
  'sets of Marbles',
  'patches of Quicksand',
  'Trapdoors',
  'TNTs',
  'Railroads'),
 ('$1 bills',
  'Small Magnets',
  '$5 bills',
  'Big Magnets',
  '$10 bills',
  'pairs of Hypno-goggles',
  'Presentations'),
 ('Bike Horns',
  'Whistles',
  'Bugles',
  'Aoogahs',
  'Elephant Trunks',
  'Foghorns',
  'Opera Singers'),
 ('Cupcakes',
  'Fruit Pie Slices',
  'Cream Pie Slices',
  'Whole Fruit Pies',
  'Whole Cream Pies',
  'Birthday Cakes',
  'Wedding cakes'),
 ('Squirting Flowers',
  'Glasses of Water',
  'Squirt Guns',
  'Seltzer Bottles',
  'Fire Hoses',
  'Storm Clouds',
  'Geysers'),
 ('Joybuzzers',
  'Carpets',
  'Balloons',
  'Kart Batteries',
  'Tazers',
  'Tesla Coils',
  'Lightning'),
 ('Flower Pots',
  'Sandbags',
  'Anvils',
  'Big Weights',
  'Safes',
  'Grand Pianos',
  'Oceanliners'))
BattleGlobalAvTrackAccStrings = ('Medium',
 'Perfect',
 'Low',
 'High',
 'Medium',
 'High',
 'Very Low',
 'Low')
BattleGlobalLureAccLow = 'Low'
BattleGlobalLureAccMedium = 'Medium'
AttackMissed = 'MISSED'
NPCCallButtonLabel = 'CALL'
LoaderLabel = 'Loading Project Altis...'
StarringIn = 'Starring In...'
HeadingToHood = 'Loading %(hood)s...'
HeadingToYourEstate = 'Loading your estate...'
HeadingToEstate = "Loading %s's estate..."
HeadingToFriend = "Loading your %s's friend's estate..."
HeadingToPlayground = 'Loading the Playground...'
HeadingToStreet = 'Loading %(street)s...'
TownBattleRun = 'Run all the way back to the playground?'
TownBattleChooseAvatarToonTitle = 'WHICH TOON?'
TownBattleChooseAvatarCogTitle = 'WHICH ' + Cog.upper() + '?'
TownBattleChooseAvatarBack = 'BACK'
FireCogTitle = 'PINK SLIPS LEFT:%s\nFIRE WHICH COG?'
FireCogLowTitle = 'PINK SLIPS LEFT:%s\nNOT ENOUGH SLIPS!'
TownBattleSOSNoFriends = 'No friends to call!'
TownBattleSOSWhichFriend = 'Call which friend?'
TownBattleSOSNPCFriends = 'Rescued Toons'
TownBattleSOSBack = 'BACK'
TownBattleToonSOS = 'SOS'
TownBattleToonFire = 'Fire'
TownBattleUndecided = '?'
TownBattleHealthText = '%(hitPoints)s/%(maxHit)s'
TownBattleWaitTitle = 'Waiting for\nother players...'
TownSoloBattleWaitTitle = 'Please wait...'
TownBattleWaitBack = 'BACK'
TownBattleSOSPetSearchTitle = 'Searching for doodle\n%s...'
TownBattleSOSPetInfoTitle = '%s is %s'
TownBattleSOSPetInfoOK = lOK
TrolleyHFAMessage = 'You may not board the trolley until your Laff meter is smiling.'
TrolleyTFAMessage = 'You may not board the trolley until ' + Mickey + ' says so.'
TrolleyHopOff = 'Hop off'
FishingExit = 'Exit'
FishingCast = 'Cast'
FishingAutoReel = 'Auto Reel'
FishingItemFound = 'You caught:'
FishingCrankTooSlow = 'Too\nslow'
FishingCrankTooFast = 'Too\nfast'
FishingFailure = "You didn't catch anything!"
FishingFailureTooSoon = "Don't start to reel in the line until you see a nibble.  Wait for your float to bob up and down rapidly!"
FishingFailureTooLate = 'Be sure to reel in the line while the fish is still nibbling!'
FishingFailureAutoReel = "The auto-reel didn't work this time.  Turn the crank by hand, at just the right speed, for your best chance to catch something!"
FishingFailureTooSlow = 'You turned the crank too slowly.  Some fish are faster than others.  Try to keep the speed bar centered!'
FishingFailureTooFast = 'You turned the crank too quickly.  Some fish are slower than others.  Try to keep the speed bar centered!'
FishingOverTankLimit = 'Your fish bucket is full. Go sell your fish to the Pet Shop and come back.'
FishingBroke = 'You do not have any more Jellybeans for bait! Ride the trolley or sell fish to the Pet Shop Clerks to earn more Jellybeans.'
FishingHowToFirstTime = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it now!'
FishingHowToFailed = 'Click and drag down from the Cast button. The farther down you drag, the stronger your cast will be. Adjust your angle to hit the fish targets.\n\nTry it again now!'
FishingBootItem = 'An old boot'
BetaCertificateItem = 'A Project Altis Beta Certificate'
FishingJellybeanItem = '%s Jellybeans'
FishingNewEntry = 'New Species!'
FishingNewRecord = 'New Record!'
FishPokerCashIn = 'Cash In\n%s\n%s'
FishPokerLock = 'Lock'
FishPokerUnlock = 'Unlock'
FishPoker5OfKind = '5 of a Kind'
FishPoker4OfKind = '4 of a Kind'
FishPokerFullHouse = 'Full House'
FishPoker3OfKind = '3 of a Kind'
FishPoker2Pair = '2 Pair'
FishPokerPair = 'Pair'
TutorialGreeting1 = 'Hello %s! Welcome to Toontown!'
TutorialGreeting2 = 'As you may know, we are a small town on the Toontown Mainland.'
TutorialGreeting3 = 'However, everything hasn\'t always been slapstick and seltzer in Toontown...'
TutorialGreeting4 = 'After the E.R.A.S.E.R., things have been a little more dreary.'
TutorialGreeting5 = 'Though, I have a good feeling about you!'
TutorialGreeting6 = 'Alright, so where to start... OH! I got it!'
TutorialGreeting7 = 'Use the arrow keys to move. Then come over and talk to me!'
TutorialSuit1 = 'You must be the new kid on the block.'
TutorialSuitTaunt = {'s': "I'm gonna send chills down your spine.", 'm': "I'll make short work of you.", 'l': 'Time for a feeding frenzy!', 'c': "Schools in session, and you're about to flunk out.", 'g': 'Ze idea is zat you vill lose!'} 
TutorialMickeyWelcome = 'Welcome to Toontown!'
TutorialFlippyIntro = 'Let me introduce you to my friend %s...' % Flippy
TutorialFlippyHi = 'Hi, %s!'
TutorialQT1 = 'You can talk by using this.'
TutorialQT2 = 'You can talk by using this.\nClick it, then choose "Hi".'
TutorialChat1 = 'You can talk using either of these buttons.'
TutorialChat2 = 'The blue button lets you chat with the keyboard.'
TutorialChat3 = "Be careful!  Most other players won't understand what you say you when you use the keyboard."
TutorialChat4 = 'The green button opens the %s.'
TutorialChat5 = 'Everyone can understand you if you use the %s.'
TutorialChat6 = 'Try saying "Hi".'
TutorialBodyClick1 = 'Very good!'
TutorialBodyClick2 = 'Pleased to meet you! Want to be friends?'
TutorialBodyClick3 = 'To make friends with %s, click on him...' % Flippy
TutorialHandleBodyClickSuccess = 'Good Job!'
TutorialHandleBodyClickFail = 'Not quite. Try clicking right on %s...' % Flippy
TutorialFriendsButton = "Now click the 'Friends' button under %s's picture in the right hand corner." % Flippy
TutorialHandleFriendsButton = "And then click on the 'Yes' button.."
TutorialOK = lOK
TutorialYes = lYes
TutorialNo = lNo
TutorialFriendsPrompt = 'Would you like to make friends with %s?' % Flippy
TutorialFriendsPanelMickeyChat = "%s has agreed to be your friend. Click 'Ok' to finish up." % Flippy
TutorialFriendsPanelYes = '%s said yes!' % Flippy
TutorialFriendsPanelNo = "That's not very friendly!"
TutorialFriendsPanelCongrats = 'Congratulations! You made your first friend.'
TutorialFlippyChat1 = 'Come see me when you are ready for your first ToonTask!'
TutorialFlippyChat2 = "I'll be in ToonHall!"
TutorialAllFriendsButton = 'You can view all your friends by clicking the friends button. Try it out...'
TutorialEmptyFriendsList = "Right now your list is empty because %s isn't a real player." % Flippy
TutorialCloseFriendsList = "Click the 'Close'\nbutton to make the\nlist go away"
TutorialShtickerButton = 'The button in the lower, right corner opens your Shticker Book. Try it...'
TutorialBook1 = 'The book contains lots of useful information like this map of Toontown.'
TutorialBook2 = 'You can also check the progress of your ToonTasks.'
TutorialBook3 = 'When you are done click the book button again to make it close'
TutorialLaffMeter1 = 'You will also need this...'
TutorialLaffMeter2 = "You will also need this...\nIt's your Laff meter."
TutorialLaffMeter3 = 'When ' + Cogs + ' attack you, it gets lower.'
TutorialLaffMeter4 = 'When you are in playgrounds like this one, it goes back up.'
TutorialLaffMeter5 = 'When you complete ToonTasks, you will get rewards, like increasing your Laff limit.'
TutorialLaffMeter6 = 'Be careful! If the ' + Cogs + ' defeat you, you will lose all your gags.'
TutorialLaffMeter7 = 'To get more gags, play trolley games.'
TutorialTrolley1 = 'Follow me to the trolley!'
TutorialTrolley2 = 'Hop on board!'
TutorialBye1 = 'Play some games!'
TutorialBye2 = 'Play some games!\nBuy some gags!'
TutorialBye3 = 'Go see %s when you are done!' % Flippy
TutorialForceAcknowledgeMessage = 'You are going the wrong way! Go find %s!' % Mickey
PetTutorialTitle1 = 'The Doodle Panel'
PetTutorialTitle2 = 'Doodle SpeedChat'
PetTutorialTitle3 = 'Doodle Cattlelog'
PetTutorialNext = 'Next Page'
PetTutorialPrev = 'Previous Page'
PetTutorialDone = 'Done'
PetTutorialPage1 = 'Click on a Doodle to display the Doodle panel.  From here you can feed, scratch, and call the Doodle.'
PetTutorialPage2 = "Use the new 'Pets' area in the SpeedChat menu to get a Doodle to do a trick.  If he does it, reward him and he'll get better!"
PetTutorialPage3 = "Purchase new Doodle tricks from Clarabelle's Cattlelog.  Better tricks give better Toon-Ups!"

def getPetGuiAlign():
    from pandac.PandaModules import TextNode
    return TextNode.ACenter


GardenTutorialTitle1 = 'Gardening'
GardenTutorialTitle2 = 'Flowers'
GardenTutorialTitle3 = 'Trees'
GardenTutorialTitle4 = 'How-to'
GardenTutorialTitle5 = 'Statues'
GardenTutorialNext = 'Next Page'
GardenTutorialPrev = 'Previous Page'
GardenTutorialDone = 'Done'
GardenTutorialPage1 = 'Toon up your Estate with a garden!  You can plant flowers, grow trees, harvest super-powerful gags, and decorate with statues!'
GardenTutorialPage2 = 'Flowers are finicky and require unique Jellybean recipes. Once grown, put them in the wheelbarrow to sell them and work toward Laff boosts!'
GardenTutorialPage3 = 'Use a gag from your inventory to plant a tree.  After a few days, that gag will do more damage!  Remember to keep it healthy or the damage boost will go away.'
GardenTutorialPage4 = 'Walk up to these spots to plant, water, dig up or harvest your garden.'
GardenTutorialPage5 = "Statues can be purchased in Clarabelle's Cattlelog. Increase your skill to unlock the more extravagant statues!"
PlaygroundDeathAckMessage = TheCogs + ' took all your gags!\n\nYou are sad. You may not leave the playground until you are happy.'
ForcedLeaveFactoryAckMsg = 'The ' + Foreman + ' was defeated before you could reach him. You did not recover any Cog parts.'
ForcedLeaveMintAckMsg = 'The Mint Floor Supervisor was defeated before you could reach him. You did not recover any Cogbucks.'
HeadingToFactoryTitle = '%s'
ForemanConfrontedMsg = '%s is battling the ' + Foreman + '!'
MintBossConfrontedMsg = '%s is battling the Supervisor!'
StageBossConfrontedMsg = '%s is battling the Clerk!'
BoardOfficeBossConfrontedMsg = '%s is battling the Executive Board Member!'
stageToonEnterElevator = '%s \nhas entered the elevator'
ForcedLeaveStageAckMsg = 'The Clerk was defeated before you could reach him. You did not recover any Subpoenas.'
MinigameWaitingForOtherPlayers = 'Waiting for other players to join...'
MinigamePleaseWait = 'Please wait...'
DefaultMinigameTitle = 'Minigame Title'
DefaultMinigameInstructions = 'Minigame Instructions'
HeadingToMinigameTitle = '%s'
MinigamePowerMeterLabel = 'Power Meter'
MinigamePowerMeterTooSlow = 'Too\nslow'
MinigamePowerMeterTooFast = 'Too\nfast'
MinigameTemplateTitle = 'Minigame Template'
MinigameTemplateInstructions = 'This is a template minigame. Use it to create new minigames.'
CannonGameTitle = 'Cannon Game'
CannonGameInstructions = 'Shoot your toon into the water tower as quickly as you can. Use the mouse or the arrow keys to aim the cannon. Be quick and win a big reward for everyone!'
CannonGameReward = 'REWARD'
TwoDGameTitle = 'Toon Escape'
TwoDGameInstructions = 'Escape from the ' + Cog + ' den as soon as you can. Use arrow keys to run/jump and Ctrl to squirt a ' + Cog + '. Collect ' + Cog + ' treasures to gain even more points.'
TwoDGameElevatorExit = 'EXIT'
TugOfWarGameTitle = 'Tug-of-War'
TugOfWarInstructions = "Alternately tap the left and right arrow keys just fast enough to line up the green bar with the red line. Don't tap them too slow or too fast, or you'll end up in the water!"
TugOfWarGameGo = 'GO!'
TugOfWarGameReady = 'Ready...'
TugOfWarGameEnd = 'Good game!'
TugOfWarGameTie = 'You tied!'
TugOfWarPowerMeter = 'Power meter'
PatternGameTitle = 'Match Tubby'
PatternGameInstructions = 'Sir Tubby Cheezyfish will show you a dance sequence. ' + 'Try to repeat Sir Tubby Cheezyfish\'s dance just the way you see it using the arrow keys!'
PatternGameWatch = 'Watch these dance steps...'
PatternGameGo = 'GO!'
PatternGameRight = 'Good, %s!'
PatternGameWrong = 'Oops!'
PatternGamePerfect = 'That was perfect, %s!'
PatternGameBye = 'Thanks for playing!'
PatternGameWaitingOtherPlayers = 'Waiting for other players...'
PatternGamePleaseWait = 'Please wait...'
PatternGameFaster = 'You were\nfaster!'
PatternGameFastest = 'You were\nthe fastest!'
PatternGameYouCanDoIt = 'Come on!\nYou can do it!'
PatternGameOtherFaster = '\nwas faster!'
PatternGameOtherFastest = '\nwas the fastest!'
PatternGameGreatJob = 'Great Job!'
PatternGameRound = 'Round %s!'
PatternGameImprov = 'You did great!  Now Improv!'
RaceGameTitle = 'Race Game'
RaceGameInstructions = 'Click a number. Choose wisely! You only advance if no one else picked the same number.'
RaceGameWaitingChoices = 'Waiting for other players to choose...'
RaceGameCardText = '%(name)s draws: %(reward)s'
RaceGameCardTextBeans = '%(name)s receives: %(reward)s'
RaceGameCardTextHi1 = '%(name)s is one Fabulous Toon!'
RaceGameForwardOneSpace = ' forward 1 space'
RaceGameForwardTwoSpaces = ' forward 2 spaces'
RaceGameForwardThreeSpaces = ' forward 3 spaces'
RaceGameBackOneSpace = ' back 1 space'
RaceGameBackTwoSpaces = ' back 2 spaces'
RaceGameBackThreeSpaces = ' back 3 spaces'
RaceGameOthersForwardThree = ' all others forward \n3 spaces'
RaceGameOthersBackThree = 'all others back \n3 spaces'
RaceGameInstantWinner = 'Instant Winner!'
RaceGameJellybeans2 = '2 Jellybeans'
RaceGameJellybeans4 = '4 Jellybeans'
RaceGameJellybeans10 = '10 Jellybeans!'
RingGameTitle = 'Ring Game'
RingGameInstructionsSinglePlayer = 'Try to swim through as many of the %s rings as you can.  Use the arrow keys to swim.'
RingGameInstructionsMultiPlayer = 'Try to swim through the %s rings.  Other players will try for the other colored rings.  Use the arrow keys to swim.'
RingGameMissed = 'MISSED'
RingGameGroupPerfect = 'GROUP\nPERFECT!!'
RingGamePerfect = 'PERFECT!'
RingGameGroupBonus = 'GROUP BONUS'
ColorRed = 'red'
ColorGreen = 'green'
ColorOrange = 'orange'
ColorPurple = 'purple'
ColorWhite = 'white'
ColorBlack = 'black'
ColorYellow = 'yellow'
DivingGameTitle = 'Treasure Dive'
DivingInstructionsSinglePlayer = 'Treasures will appear at the bottom of the lake.  Use the arrow keys to swim.  Avoid the fish and get the treasures up to the boat!'
DivingInstructionsMultiPlayer = 'Treasures will appear at the bottom of the lake.  Use the arrow keys to swim.  Work together to get the treasures up to the boat!'
DivingGameTreasuresRetrieved = 'Treasures Retrieved'
TargetGameTitle = 'Toon Slingshot'
TargetGameInstructionsSinglePlayer = 'Use your umbrella to land on the targets. The smaller the target, the more Jellybeans you get!'
TargetGameInstructionsMultiPlayer = 'Use your umbrella to land on the targets. The smaller the target, the more Jellybeans you get!'
TargetGameBoard = 'Round %s - Keeping Best Score'
TargetGameCountdown = 'Forced launch in %s seconds'
TargetGameCountHelp = 'Pound left and right arrows for power, stop to launch'
TargetGameFlyHelp = 'Press down to open umbrella'
TargetGameFallHelp = 'Use the arrow keys to land on target'
TargetGameBounceHelp = ' Bouncing can knock you off target'
PhotoGameScoreTaken = '%s: %s\nYou: %s'
PhotoGameScoreBlank = 'Score: %s'
PhotoGameScoreOther = '\n%s'
PhotoGameScoreYou = '\nBest Bonus!'
TagGameTitle = 'Tag Game'
TagGameInstructions = 'Collect the treasures. You cannot collect treasure when you are IT!'
TagGameYouAreIt = 'You Are IT!'
TagGameSomeoneElseIsIt = '%s is IT!'
MazeGameTitle = 'Maze Game'
MazeGameInstructions = 'Collect the treasures. Try to get them all, but look out for the ' + Cogs + '!'
CatchGameTitle = 'Catching Game'
CatchGameInstructions = 'Catch as many %(fruit)s as you can. Watch out for the ' + Cogs + ", and try not to 'catch' any %(badThing)s!"
CatchGamePerfect = 'PERFECT!'
CatchGameApples = 'apples'
CatchGameOranges = 'oranges'
CatchGamePears = 'pears'
CatchGameCoconuts = 'coconuts'
CatchGameWatermelons = 'watermelons'
CatchGamePineapples = 'pineapples'
CatchGameAcorns = 'acorns'
CatchGameAnvils = 'anvils'
PieTossGameTitle = 'Pie Toss Game'
PieTossGameInstructions = 'Toss pies at the targets.'
PhotoGameInstructions = 'Capture photos matching the toons shown at the bottom. Aim the camera with the mouse, and left click to take a picture. Press Ctrl to zoom in/out, and look around with the arrow keys.  Pictures with higher ratings get more points!'
PhotoGameTitle = 'Photo Fun'
PhotoGameFilm = 'FILM'
PhotoGameScore = 'Team Score: %s\n\nBest Photos: %s\n\nTotal Score: %s'
CogThiefGameTitle = 'Cog Thief'
CogThiefGameInstructions = 'Stop these Cogs from stealing our Gags! Press the Control key to throw pies. But be careful... they have a tendancy to explode!'
CogThiefBarrelsSaved = '%(num)d Barrels\nSaved!'
CogThiefBarrelSaved = '%(num)d Barrel\nSaved!'
CogThiefNoBarrelsSaved = 'No Barrels\nSaved'
CogThiefPerfect = 'PERFECT!'
MinigameRulesPanelPlay = 'PLAY'
MinigameRulesPanelSkip = 'SKIP'
GagShopName = "Goofy's Gag Shop"
GagShopPlayAgain = 'PLAY\nAGAIN'
GagShopBackToPlayground = 'EXIT BACK TO\nPLAYGROUND'
GagShopYouHave = 'You have %s Jellybeans to spend'
GagShopYouHaveOne = 'You have 1 Jellybean to spend'
GagShopTooManyProps = 'Sorry, you have too many props'
GagShopDoneShopping = 'DONE\nSHOPPING'
GagShopTooManyOfThatGag = 'Sorry, you have enough %s already'
GagShopInsufficientSkill = 'You do not have enough skill for that yet'
GagShopNotEnoughJellybeans = 'You do not have enough Jellybeans for that gag'
GagShopYouPurchased = 'You purchased %s'
GagShopOutOfJellybeans = 'Sorry, you are all out of Jellybeans!'
GagShopWaitingOtherPlayers = 'Waiting for other players...'
GagShopPlayerDisconnected = '%s has disconnected'
GagShopPlayerExited = '%s has exited'
GagShopPlayerPlayAgain = 'Play Again'
GagShopPlayerBuying = 'Buying'
PopupTouchControls = 'You are using the \1textShadow\1EXPERIMENTAL\2 touch controls. These are very early in development and may be buggy. Please report any issues to the team. Thanks, and enjoy Project Altis!'
PopupAlphaDisclaimer = '\1textShadow\1Disclaimer:\2\nThis is an BETA build of Project Altis! Things that are in game may be subject to change! There is some incomplete content as well, so stay tooned for the updated content! Thanks for participating in Project Altis\' Beta!'
QuitConfirm = 'Are you sure you want to quit?'
PlayGame = 'Pick-A-Toon'
DiscordButton = 'News'
CreditsButton = 'Credits'
GenderShopQuestionMickey = 'To make a boy toon, click on me!'
GenderShopQuestionMinnie = 'To make a girl toon, click on me!'
GenderShopFollow = 'Follow me!'
GenderShopSeeYou = 'See you later!'
GenderShopBoyButtonText = 'Boy'
GenderShopGirlButtonText = 'Girl'
BodyShopHead = 'Head'
BodyShopBody = 'Body'
BodyShopLegs = 'Legs'
ColorShopToon = 'Toon Color'
ColorShopHead = 'Head'
ColorShopBody = 'Body'
ColorShopLegs = 'Legs'
ColorShopParts = 'Multi Color'
ColorShopAll = 'Single Color'
ColorShopPicker = "Color Picker"
ColorShopBasic = "Basic Picker"
ClothesShopShorts = 'Shorts'
ClothesShopShirt = 'Shirts'
ClothesShopBottoms = 'Bottoms'
ClothesShopShirtsStyle = 'Shirts Style'
ClothesShopShirtsColor = 'Shirts Color'
ClothesShopShortsStyle = 'Shorts Style'
ClothesShopShortsColor = 'Shorts Color'
ClothesShopBottomsStyle = 'Bottoms Style'
ClothesShopBottomsColor = 'Bottoms Color'
PromptTutorial = "Congratulations!!\nYou are Toontown's newest citizen!\n\nWould you like to continue to the Toontorial or teleport directly to Toontown Central?"
MakeAToonSkipTutorial = 'Skip Toontorial'
MakeAToonEnterTutorial = 'Enter Toontorial'
MakeAToonDone = 'Done'
MakeAToonCancel = lCancel
MakeAToonNext = lNext
MakeAToonLast = 'Back'
CreateYourToon = 'Click the arrows to create your toon.'
CreateYourToonTitle = 'Choose  Boy  or  Girl'
ShapeYourToonTitle = 'Choose  Your  Type'
PaintYourToonTitle = 'Choose  Your  Color'
PickClothesTitle = 'Choose  Your  Clothes'
PickStatusTitle = 'Choose  Your  Statuses'
PickStartTitle = 'Choose  Your  Starting  Playground'
NameToonTitle = 'Choose  Your  Name'
UberTitles = ['Normal', '15 Laff', '25 Laff', '34 Laff']
UberInfos = ['Your average run of the mill toon, they have no laff limits! Great for players who want to play traditionally.',
 '15 laff ubers can NEVER GAIN ANY LAFF POINTS.',
 '25 laff ubers can gain up to 10 extra laff points from their base laff. Once they reach 25 laff, they can NEVER GAIN ANY MORE LAFF POINTS.',
 '34 laff ubers can gain up to 19 extra laff points from their base laff. Once they reach 34 laff, they can NEVER GAIN ANY MORE LAFF POINTS.']
CreateYourToonHead = "Click the 'head' arrows to pick different animals."
MakeAToonClickForNextScreen = 'Click the arrow below to go to the next screen.'
PickClothes = 'Click the arrows to pick clothes!'
PaintYourToon = 'Click the arrows to paint your toon!'
MakeAToonYouCanGoBack = 'You can go back to change your body too!'
MakeAFunnyName = 'Choose a funny name for your toon with my Pick-A-Name game!'
MustHaveAFirstOrLast1 = "Your toon should have a first or last name, don't you think?"
MustHaveAFirstOrLast2 = "Don't you want your toon to have a first or last name?"
ApprovalForName1 = "That's it, your toon deserves a great name!"
ApprovalForName2 = 'Toon names are the best kind of names!'
MakeAToonLastStep = 'Last step before going to Toontown!'
PickANameYouLike = 'Pick a name you like!'
TitleCheckBox = 'Title'
FirstCheckBox = 'First'
LastCheckBox = 'Last'
RandomButton = 'Random'
ShuffleButton = 'Shuffle'
NameShopSubmitButton = 'Submit'
TypeANameButton = 'Type-A-Name'
TypeAName = "Don't like these names?\nClick here -->"
PickAName = 'Try the PickAName game!\nClick here -->'
PickANameButton = 'Pick-A-Name'
RejectNameText = 'That name is not allowed. Please try again.'
WaitingForNameSubmission = 'Submitting your name...'
PetNameMaster = 'PetNameMasterEnglish.txt'
PetNameIndexMAX = 2713
PetshopUnknownName = 'Name: ???'
PetshopDescGender = 'Gender:\t%s'
PetshopDescCost = 'Cost:\t%s Jellybeans'
PetshopDescTrait = 'Traits:\t%s'
PetshopDescStandard = 'Standard'
PetshopCancel = lCancel
PetshopSell = 'Sell Fish'
PetshopAdoptAPet = 'Adopt a Doodle'
PetshopReturnPet = 'Return your Doodle'
PetshopAdoptConfirm = 'Adopt %s for %d Jellybeans?'
PetshopGoBack = 'Go Back'
PetshopAdopt = 'Adopt'
PetshopReturnConfirm = 'Return %s?'
PetshopReturn = 'Return'
PetshopChooserTitle = "TODAY'S DOODLES"
PetshopGoHomeText = 'Would you like to go to your estate to play with your new Doodle?'
NameShopNameMaster = 'NameMasterEnglish.txt'
NameShopPay = 'Subscribe'
NameShopPlay = 'Free Trial'
NameShopOnlyPaid = 'Only paid users\nmay name their Toons.\nUntil you subscribe\nyour name will be\n'
NameShopContinueSubmission = 'Continue Submission'
NameShopChooseAnother = 'Choose Another Name'
NameShopToonCouncil = 'The Toon Council\nwill review your\nname.  ' + 'Review may\ntake a few days.\nWhile you wait\nyour name will be\n '
PleaseTypeName = 'Please type your name:'
AllNewNames = 'All new names must be\napproved by the Toon Council.'
NameMessages = 'Be creative, and remember:\nno NPC names, please.'
NameShopNameRejected = 'The name you\nsubmitted has\nbeen rejected.'
NameShopNameAccepted = 'Congratulations!\nThe name you\nsubmitted has\nbeen accepted!'
NoPunctuation = "You can't use punctuation marks in your name!"
PeriodOnlyAfterLetter = 'You can use a period in your name, but only after a letter.'
ApostropheOnlyAfterLetter = 'You can use an apostrophe in your name, but only after a letter.'
NoNumbersInTheMiddle = 'Numeric digits may not appear in the middle of a word.'
ThreeWordsOrLess = 'Your name must be three words or fewer.'
CopyrightedNames = ('mickey',
 'mickey mouse',
 'mickeymouse',
 'minnie',
 'minnie mouse',
 'minniemouse',
 'donald',
 'donald duck',
 'donaldduck',
 'pluto',
 'goofy')
NumToColor = ['White',
 'Peach',
 'Bright Red',
 'Red',
 'Maroon',
 'Sienna',
 'Brown',
 'Tan',
 'Coral',
 'Orange',
 'Yellow',
 'Cream',
 'Citrine',
 'Lime',
 'Sea Green',
 'Green',
 'Light Blue',
 'Aqua',
 'Blue',
 'Periwinkle',
 'Royal Blue',
 'Slate Blue',
 'Purple',
 'Lavender',
 'Pink',
 'Plum',
 'Black',
 'Rose Pink',
 'Ice Blue',
 'Mint Green',
 'Emerald',
 'Teal',
 'Apricot',
 'Amber',
 'Crimson',
 'Dark Green',
 'Steel Blue',
 'ToonFest Blue',
 'Mountain Green',
 'Icy Blue',
 'Desert Sand',
 'Mint',
 'Charcoal',
 'Hot Pink',
 'Honey Mustard',
 'Gray',
 'Neon Orange',
 'Sapphire',
 'Crimson',
 'Emerald',
 'Bronze',
 'African Violet',
 'Magenta',
 'Medium Purple',
 'Ivory',
 'Thistle',
 'Spring Green',
 'Goldenrod',
 'Cadium Yellow',
 'Peach Puff',
 'Toony Teal',
 'Salmon',
 'Banana Yellow',
 'Dim Gray',
 'Gold']
AnimalToSpecies = {'dog': 'Dog',
 'cat': 'Cat',
 'mouse': 'Mouse',
 'horse': 'Horse',
 'rabbit': 'Rabbit',
 'duck': 'Duck',
 'monkey': 'Monkey',
 'bear': 'Bear',
 'pig': 'Pig',
 'deer': 'Deer',
 'beaver': 'Beaver',
 'alligator': 'Alligator',
 'fox': 'Fox',
 'bat': 'Bat',
 'raccoon': 'Raccoon'}
AllSpecies = ('Dog', 'Cat', 'Horse', 'Mouse', 'Rabbit', 'Duck', 'Monkey', 'Bear', 'Pig', 'Deer', 'Beaver', 'Alligator', 'Fox', 'Bat', 'Raccoon')
NameTooLong = 'That name is too long. Please try again.'
ToonAlreadyExists = 'You already have a toon named %s!'
NameAlreadyInUse = 'That name is already used!'
EmptyNameError = 'You must enter a name first.'
NameError = 'Sorry.  That name will not work.'
NCTooShort = 'That name is too short.'
NCNoDigits = 'Your name cannot contain numbers.'
NCNeedLetters = 'Each word in your name must contain some letters.'
NCNeedVowels = 'Each word in your name must contain some vowels.'
NCAllCaps = 'Your name cannot be all capital letters.'
NCMixedCase = 'That name has too many capital letters.'
NCBadCharacter = "Your name cannot contain the character '%s'"
NCGeneric = 'Sorry, that name will not work.'
NCTooManyWords = 'Your name cannot be more than four words long.'
NCDashUsage = "Dashes may only be used to connect two words together (like in 'Boo-Boo')."
NCCommaEdge = 'Your name may not begin or end with a comma.'
NCCommaAfterWord = 'You may not begin a word with a comma.'
NCCommaUsage = 'That name does not use commas properly. Commas must join two words together, like in the name "Dr. Quack, MD". Commas must also be followed by a space.'
NCPeriodUsage = 'That name does not use periods properly. Periods are only allowed in words like "Mr.", "Mrs.", "J.T.", etc.'
NCApostrophes = 'That name has too many apostrophes.'
RemoveTrophy = lToonHQ + ': ' + TheCogs + ' took over one of the buildings you rescued!'
STOREOWNER_TOOKTOOLONG = 'Need more time to think?'
STOREOWNER_GOODBYE = 'See you later!'
STOREOWNER_NEEDJELLYBEANS = 'You need to ride the Trolley to get some Jellybeans.'
STOREOWNER_GREETING = 'Choose what you want to buy.'
STOREOWNER_BROWSING = 'You can browse, but you need a clothing ticket to buy.'
STOREOWNER_BROWSING_JBS = 'You can browse, but you need at least 200 Jellybeans to buy.'
STOREOWNER_NOCLOTHINGTICKET = 'You need a clothing ticket to shop for clothes.'
STOREOWNER_NOFISH = 'Come back here to sell fish to the Pet Shop for Jellybeans.'
STOREOWNER_THANKSFISH = 'Thanks! The Pet Shop will love these. Bye!'
STOREOWNER_THANKSFISH_PETSHOP = 'These are some fine specimens! Thanks.'
STOREOWNER_PETRETURNED = "Don't worry.  We'll find a good home for your Doodle."
STOREOWNER_PETADOPTED = 'Congratulations on purchasing a Doodle! You can play with your new friend at your estate.'
STOREOWNER_PETCANCELED = 'Remember, if you see a Doodle you like, make sure to adopt him before someone else does!'
STOREOWNER_NOROOM = 'Hmm...you might want to make room in your closet before you buy new clothes.\n'
STOREOWNER_CONFIRM_LOSS = 'Your closet is full.  You will lose the clothes you were wearing.'
STOREOWNER_OK = lOK
STOREOWNER_CANCEL = lCancel
STOREOWNER_TROPHY = 'Wow! You collected %s of %s fish. That deserves a trophy and a Laff boost!'
STOREOWNER_BANKING = 'Welcome to The Toontown Bank! How may I help you?'
STOREOWNER_ROD_BUY = 'Congratulations on your new fishing rod! You can access it from the \'Items\' page of your shtiker book!'
STOREOWNER_BUCKET_BUY = 'Congratulations on your new fishing bucket! Your bucket has been automatically upgraded.'
SuitInvasionBegin1 = lToonHQ + ': A Cog invasion has begun!!!'
SuitInvasionBegin2 = lToonHQ + ': %s have taken over Toontown!!!'
SuitInvasionEnd1 = lToonHQ + ': The %s invasion has ended!!!'
SuitInvasionEnd2 = lToonHQ + ': The Toons have saved the day once again!!!'
SuitInvasionUpdate1 = lToonHQ + ': Keep it up, Toons!!!'
SuitInvasionUpdate2 = lToonHQ + ': The Cogs appear to be decreasing in numbers!!!'
SuitInvasionBulletin1 = lToonHQ + ': There is a Cog invasion in progress!!!'
SuitInvasionBulletin2 = lToonHQ + ': %s have taken over Toontown!!!'
SkelecogInvasionBegin1 = lToonHQ + ": Hmm... We're getting a strange reading over here..."
SkelecogInvasionBegin2 = lToonHQ + ': The Cog factories are running out of parts to build new Cogs!'
SkelecogInvasionBegin3 = lToonHQ + ': Skelecogs have taken over Toontown!!!'
SkelecogInvasionEnd1 = lToonHQ + ': The Skelecog invasion has ended!!!'
SkelecogInvasionEnd2 = lToonHQ + ': The Toons have saved the day once again!!!'
SkelecogInvasionBulletin1 = lToonHQ + ': There is a Cog invasion in progress!!!'
SkelecogInvasionBulletin2 = lToonHQ + ': The Cog factories are running out of parts to build new Cogs!'
SkelecogInvasionBulletin3 = lToonHQ + ': Skelecogs have taken over Toontown!!!'
WaiterInvasionBegin1 = lToonHQ + ': It appears that the C.E.O. has fired all his waiters...'
WaiterInvasionBegin2 = lToonHQ + ': The unemployed waiters are invading Toontown!!!'
WaiterInvasionEnd1 = lToonHQ + ': The unemployed waiters have been defeated!!!'
WaiterInvasionEnd2 = lToonHQ + ': The Toons have saved the day once again!!!'
WaiterInvasionBulletin1 = lToonHQ + ': There is a Cog invasion in progress!!!'
WaiterInvasionBulletin2 = lToonHQ + ': The C.E.O. has fired all of his waiters!!!'
WaiterInvasionBulletin3 = lToonHQ + ": The unemployed waiters are invading Toontown!!!"
V2InvasionBegin1 = lToonHQ + ": Yikes!!! This isn't good, Toons!"
V2InvasionBegin2 = lToonHQ + ': A major firmware update has been released to the Cogs!!!'
V2InvasionBegin3 = lToonHQ + ': Version 2.0 Cogs have taken over Toontown!!!'
V2InvasionEnd1 = lToonHQ + ': The version 2.0 Cog invasion has ended!!!'
V2InvasionEnd2 = lToonHQ + ': The Toons have saved the day once again!!!'
V2InvasionBulletin1 = lToonHQ + ': There is a Cog invasion in progress!!!'
V2InvasionBulletin2 = lToonHQ + ': A major firmware update has been released to the Cogs!!!'
V2InvasionBulletin3 = lToonHQ + ': Version 2.0 Cogs have taken over Toontown!!!'
SuitMegaInvasionBegin1 = lToonHQ + ': A MEGA invasion has begun!!!'
SuitMegaInvasionBegin2 = lToonHQ + ': %s have taken over Toontown!!!'
SuitMegaInvasionEnd1 = lToonHQ + ': The %s MEGA invasion has ended!!!'
SuitMegaInvasionEnd2 = lToonHQ + ': The Toons have saved the day once again!!!'
SuitMegaInvasionUpdate1 = lToonHQ + ': Bulletin incoming, Toons!!!'
SuitMegaInvasionUpdate2 = lToonHQ + ': There are still a ton of cogs, but keep it up!!!'
LeaderboardTitle = 'Toon Platoon'
QuestScriptTutorialMickey_1 = 'Toontown has a new citizen! Do you have some extra gags?'
QuestScriptTutorialMickey_2 = 'Sure, %s!'
QuestScriptTutorialMickey_3 = 'Tutorial Tom will tell you all about the Cogs.\x07Gotta go!'
QuestScriptTutorialMickey_4 = "Hello, new citizen! Welcome to Toontown! Come over here so I can tell you what's been going on in town recently. Use the arrow keys to move."
QuestScriptTutorialMinnie_1 = 'Toontown has a new citizen! Do you have some extra gags?'
QuestScriptTutorialMinnie_2 = 'Sure, %s!'
QuestScriptTutorialMinnie_3 = 'Tutorial Tom will tell you all about the Cogs.\x07Gotta go!'
QuestScript101_1 = 'These are Cogs. They are robots that are trying to take over Toontown.'
QuestScript101_2 = 'There are many different kinds of Cogs and...'
QuestScript101_3 = '...they turn happy Toon buildings...'
QuestScript101_4 = '...into ugly Cog buildings!'
QuestScript101_5 = "But Cogs can't take a joke!"
QuestScript101_6 = 'A good gag will stop them.'
QuestScript101_7 = 'There are lots of gags, but take these to start.'
QuestScript101_8 = 'Oh! You also need a Laff meter!'
QuestScript101_9 = "If your Laff meter gets too low, you'll be sad!"
QuestScript101_10 = 'A happy Toon is a healthy Toon!'
QuestScript101_11 = "OH NO! There's a Cog outside my shop!"
QuestScript101_12 = 'HELP ME, PLEASE! Defeat that Cog!'
QuestScript101_13 = 'Here is your first ToonTask!'
QuestScript101_14 = 'Hurry up! Go defeat that Cog!'

QuestScript110_1 = 'Good work defeating that Cog. Let me give you a Shticker Book...'
QuestScript110_2 = 'The book is full of good stuff.'
QuestScript110_3 = "Open it, and I'll show you."
QuestScript110_4 = "The map shows where you've been."
QuestScript110_5 = 'Turn the page to see your gags...'
QuestScript110_6 = 'Uh oh! You have no gags! I will assign you a task.'
QuestScript110_7 = 'Turn the page to see your tasks.'
QuestScript110_8 = 'You\'ll need a way to get beans.'
QuestScript110_9 = 'Luckily, Banker Bob knows a thing or two on how to earn some!'
QuestScript110_10 = 'Now, close the book and find the bank!'
QuestScript110_11 = 'When Bob is finished with you, please return to the Toon HQ.'

QuestScriptTutorialBlocker_1 = 'Why, hello there!'
QuestScriptTutorialBlocker_2 = 'Hello?'
QuestScriptTutorialBlocker_3 = "Oh! You don't know how to use SpeedChat!"
QuestScriptTutorialBlocker_4 = 'Click on the button to say something.'
QuestScriptTutorialBlocker_5 = 'Very good!\x07Where you are going there are many Toons to talk to.'
QuestScriptTutorialBlocker_6 = "If you want to chat with other Toons using the keyboard, there's another button you can use."
QuestScriptTutorialBlocker_7 = "It's called the SpeedChat Plus button. You need to turn on Speedchat Plus in your Account Manager on the Project Altis Website to use it."
QuestScriptTutorialBlocker_8 = 'Good luck! See you later!'

QuestScriptGagShop_1 = 'Welcome to the Gag Shop!'
QuestScriptGagShop_1a = 'This is where Toons come to buy gags to use against the Cogs.'
QuestScriptGagShop_3 = 'To buy gags, click on the gag buttons. Try getting some now!'
QuestScriptGagShop_4 = 'Good! You can use these gags in battle against the Cogs.'
QuestScriptGagShop_5 = "Here's a peek at the advanced throw and squirt gags..."
QuestScriptGagShop_6 = "When you're done buying gags, click this button to return to the Playground."
QuestScriptGagShop_7 = 'Normally you can use this button to play another Trolley Game...'
QuestScriptGagShop_8 = "...but there's no time for another game right now. You're needed in Toon HQ!"

QuestScript120_1 = "Ah, yes. You need to earn beans, don't you?\x07One way toons can earn their beans is through riding the trolley."
QuestScript120_2 = 'Once you ride the trolley, please return to me.\x07You should have enough beans to purchase more gags once you\'re done.'

QuestScript121_1 = "Another way you can earn beans is through fishings.\x07Why not go catch two fish and then return to me? Just so you get the hang of it.\x07However, you do need beans with you in order to fish."

QuestScript130_1 = 'Great job fishing!\x07Now, return to the Toon Headquarters.'
QuestScript131_1 = 'Oh, thanks for the chalk.\x07What?!?\x07Those Cogs stole my blackboard. Defeat Cogs to find my stolen blackboard.\x07When you find it, bring it back to me.'

QuestScript140_1 = 'Good job finding the trolley!\x07By the way, I have this friend, Librarian Larry, who is quite a book worm.\x07I picked this book up for him last time I was over in ' + lDonaldsDock + '.\x07Could you take it over to him, he is usually in the Library.'
QuestScript141_1 = 'Oh, yes, this book almost completes my collection.\x07Let me see...\x07Uh oh...\x07Now where did I put my glasses?\x07I had them just before those Cogs took over my building.\x07Defeat Cogs to find my stolen glasses.\x07When you find them, bring them back to me for a reward.'
QuestScript145_1 = 'I see you had no problem with Bob!\x07Listen, the Cogs have stolen our blackboard eraser.\x07Go into the streets and fight Cogs until you recover the eraser.\x07To reach the streets go through one of the tunnels like this:'
QuestScript145_2 = "When you find our eraser, bring it back here.\x07Don't forget, if you need gags, ride the trolley.\x07Also, if you need to recover Laff points, collect ice cream cones in the Playground."

QuestScript150_1 = 'Great work!\x07Toontown is more fun when you have friends!'
QuestScript150_2 = 'To make friends, find another player, and use the New Friend button.'
QuestScript150_3 = 'Once you have made a friend, come back here.'
QuestScript150_4 = 'Some tasks are too difficult to do alone!'

QuestScript600_1 = "Welcome to Toontown: Project Altis!"
QuestScript600_2 = "There are many shop keepers out there who will require your help."
QuestScript600_3 = "Those toons send help requests here to the Toon HQ, where we give the job to toons like you."
QuestScript600_4 = "Jester Chester can help you get used to this habbit."
QuestScript600_5 = "He can be found at Jest for Laughs on Loopy Lane."
QuestScript600_6 = "Have fun in Toontown: Project Altis!"

QuestScript10301_1 = "Welcome to Loopy's Balls!"
QuestScript10301_2 = "We sell the freshest swedish meatballs in all of Toontown!"
QuestScript10301_3 = "What would you like to order?"
QuestScript10301_4 = "Meatballs! A Fan favorite. Great choice! Let me just check in with Jimmy."
QuestScript10301_5 = "JIMMY!!"
QuestScript10301_6 = "Oh, That's right."
QuestScript10301_7 = "Jimmy was loafing around earlier so I tossed him in the pond."
QuestScript10301_8 = "Can you be a darling and go fish him out and bring him back for me?"

MissingKeySanityCheck = 'Ignore me'
SellbotBossName = 'Senior V. P.'
CashbotBossName = 'C. F. O.'
LawbotBossName = 'Chief Justice'
BoardbotBossName = 'Chairman'
BossCogNameWithDept = '%(name)s\n%(dept)s'
BossCogPromoteDoobers = 'You are hereby promoted to full-fledged %s.  Congratulations!'
BossCogDoobersAway = {'s': 'Go!  And make that sale!'}
BossCogWelcomeToons = 'Welcome, new Cogs!'
BossCogPromoteToons = 'You are hereby promoted to full-fledged %s.  Congratu--'
CagedToonInterruptBoss = 'Hey! Hiya! Hey over there!'
CagedToonRescueQuery = 'So, did you Toons come to rescue me?'
BossCogDiscoverToons = 'Huh?  Toons!  In disguise!'
BossCogAttackToons = 'Attack!!'
CagedToonDrop = ["Great job!  You're wearing him down!",
 "Keep after him!  He's on the run!",
 'You guys are doing great!',
 "Fantastic!  You've almost got him now!"]
CagedToonPrepareBattleTwo = "Look out, he's trying to get away!\x07Help me, everyone--get up here and stop him!"
CagedToonPrepareBattleThree = "Hooray, I'm almost free!\x07Now you need to attack the V.P. Cog directly.\x07I've got a whole bunch of pies you can use!\x07Jump up and touch the bottom of my cage and I'll give you some pies.\x07Press the Delete key to throw pies once you've got them!"
BossBattleNeedMorePies = 'You need to get more pies!'
BossBattleHowToGetPies = 'Jump up to touch the cage to get pies.'
BossBattleHowToThrowPies = 'Press the Delete key to throw pies!'
CagedToonYippee = 'Yippee!'
CagedToonThankYou = "It's great to be free!\x07Thanks for all your help!\x07I am in your debt.\x07Here's my card. If you ever need a hand in battle, give a shout!\x07Just click on your SOS button."
CagedToonLevelPromotion = "\x07Say--that V.P. Cog left behind your promotion papers.\x07I'll file them for you on the way out, so you'll get your promotion!"
CagedToonSuitPromotion = "\x07It seems like you've reached the highest level you can for a %s.\x07You can continue upgrading your Cog suit through the disguise page in your Shticker Book.\x07Along with getting a new Cog suit, you will also get a 1 point Laff boost!"
CagedToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07Cogs don't get promoted higher than that.\x07You can now start upgrading your v2.0 suit, however, you can only promote this suit in hard mode bosses or higher."
CagedToonLastRevivePromotion = "\x07Wow, you've reached level %s on your v2.0 Cog suit!\x07Cogs don't get promoted higher than that, at all.\x07You are now at the top of the corporate ladder, well, a step below the boss cogs.\x07You are the highest level cog that is promoted through the boss cogs! Thank you, for coming back to save more toons!\x07And with this, I award you your final laff point for your cog disguise."
CagedToonHPBoost = "\x07You've rescued a lot of Toons from this HQ.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
CagedToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CagedToonGoodbye = 'See ya!'
CagedToonBattleThree = {10: 'Nice jump, %(toon)s.  Here are some pies!',
 11: 'Hi, %(toon)s!  Have some pies!',
 12: "Hey there, %(toon)s!  You've got some pies now!",
 20: 'Hey, %(toon)s!  Jump up to my cage and get some pies to throw!',
 21: 'Hi, %(toon)s!  Use the Ctrl key to jump up and touch my cage!',
 100: 'Press the Delete key to throw a pie.',
 101: 'The blue power meter shows how high your pie will go.',
 102: 'First try to lob a pie inside his undercarriage to gum up his works.',
 103: 'Wait for the door to open, and throw a pie straight inside.',
 104: "When he's dizzy, hit him in the face or chest to knock him back!",
 105: "You'll know you've got a good hit when you see the splat in color.",
 106: 'If you hit a Toon with a pie, it gives that Toon a Laff point!'}
CagedToonBattleThreeMaxGivePies = 12
CagedToonBattleThreeMaxTouchCage = 21
CagedToonBattleThreeMaxAdvice = 106
CashbotBossHadEnough = "That's it.  I've had enough of these pesky Toons!"
CashbotBossOuttaHere = "I've got a train to catch!"
ResistanceToonName = 'Mata Hairy'
ResistanceToonCongratulations = "You did it!  Congratulations!\x07You're an asset to the Resistance!\x07Here's a special phrase you can use in a tight spot:\x07%s\x07When you say it, %s.\x07But you can only use it once, so choose that time well!"
ResistanceToonToonupInstructions = 'all the Toons near you will gain %s Laff points'
ResistanceToonToonupAllInstructions = 'all the Toons near you will gain full Laff points'
ResistanceToonMoneyInstructions = 'all the Toons near you will gain %s Jellybeans'
ResistanceToonMoneyAllInstructions = 'all the Toons near you will fill their Jellybean jars'
ResistanceToonRestockInstructions = 'all the Toons near you will restock their "%s" gags'
ResistanceToonRestockAllInstructions = 'all the Toons near you will restock all their gags'
ResistanceToonBonusUnites = '\x07Since you have continued your efforts against the C.F.O. and progressed your cog disguise, you have been awarded %d extra unites!'
ResistanceToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
ResistanceToonLevelPromotion = "\x07Say--that C.F.O. Cog left behind your promotion papers.\x07I'll file them for you on the way out, so you'll get your promotion!"
ResistanceToonSuitPromotion = "\x07It seems like you've reached the highest level you can for a %s.\x07You can continue upgrading your Cog suit through the disguise page in your Shticker Book.\x07Along with getting a new Cog suit, you will also get a 1 point Laff boost!"
ResistanceToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07I'm pretty sure Cogs don't get promoted higher than that.\x07You can begin upgrading your V2.0 Cog Suit, through hard mode bosses!"
ResistanceToonLastRevivePromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07I'm pretty sure Cogs don't get promoted higher than that.\x07You have really went above and beyond the call of duty!\x07And with this, I grant you your last Cog Disguise laff boost!"
ResistanceToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
CashbotBossCogAttack = 'Get them!!!'
ResistanceToonWelcome = 'Hey, you made it!  Follow me to the main vault before the C.F.O. finds us!'
ResistanceToonTooLate = "Blast it!  We're too late!"
CashbotBossDiscoverToons1 = 'Ah-HAH!'
CashbotBossDiscoverToons2 = 'I thought I smelled something a little toony in here!  Imposters!'
ResistanceToonKeepHimBusy = "Keep him busy!  I'm going to set a trap!"
ResistanceToonFollowHim = 'Come on toons! Follow that bag of bolts!'
CashbotBossTrapped = "I've got you right where I want you now, toons."
CashbotBossCogAgain = 'Err, again...'
ResistanceToonCraneInstructions1 = 'Control a magnet by stepping up to a podium.'
ResistanceToonCraneInstructions2 = 'Use the arrow keys to move the crane, and press the Ctrl key to grab an object.'
ResistanceToonCraneInstructions3 = "Grab a safe with a magnet and knock the C.F.O.'s safe-ty helmet off."
ResistanceToonCraneInstructions4 = 'Once his helmet is gone, grab a disabled goon and hit him in the head!'
ResistanceToonGetaway = 'Eek!  Gotta run!'
CashbotCraneLeave = 'Leave Crane'
CashbotCraneAdvice = 'Use the arrow keys to move the overhead crane.'
CashbotMagnetAdvice = 'Hold down the control key to pick things up.'
CashbotCraneLeaving = 'Leaving crane'
MintElevatorRejectMessage = 'You cannot enter the Mints until you have completed your %s Cog Suit.'
BossElevatorRejectMessage = 'You cannot board this elevator until you have earned a promotion.'
NotYetAvailable = 'This elevator is not yet available.'
SellbotRentalSuitMessage = "Wear this Rental Suit so you can get close enough to the VP to attack.\n\nYou won't earn merits or promotions, but you can rescue a Toon for an SOS reward!"
SellbotCogSuitNoMeritsMessage = "Your Sellbot Disguise will get you in, but since you don't have enough merits, you won't earn a promotion.\n\nIf you rescue the trapped Toon, you will earn an SOS Toon reward!"
SellbotCogSuitHasMeritsMessage = "It's Operation: Storm Sellbot!\n\nBring 5 or more Rental Suit Toons with you to defeat the VP and earn credit towards a reward!"
FurnitureTypeName = 'Furniture'
PaintingTypeName = 'Painting'
ClothingTypeName = 'Clothing'
ChatTypeName = 'SpeedChat Phrase'
EmoteTypeName = 'Acting Lessons'
BeanTypeName = 'Jellybeans'
PoleTypeName = 'Fishing Pole'
WindowViewTypeName = 'Window View'
PetTrickTypeName = 'Doodle Training'
GardenTypeName = 'Garden Supplies'
RentalTypeName = 'Rental Item'
GardenStarterTypeName = 'Gardening Kit'
NametagTypeName = 'Name tag'
AccessoryTypeName = 'Accessory'
InteriorLayoutTypeName = "Interior Layout"
CatalogItemTypeNames = {0: 'INVALID_ITEM',
 1: FurnitureTypeName,
 2: ChatTypeName,
 3: ClothingTypeName,
 4: EmoteTypeName,
 5: 'WALLPAPER',
 6: 'Window View',
 7: 'FLOORING',
 8: 'MOULDING',
 9: 'WAINSCOTING',
 10: PoleTypeName,
 11: PetTrickTypeName,
 12: BeanTypeName,
 13: GardenTypeName,
 14: RentalTypeName,
 15: GardenStarterTypeName,
 16: NametagTypeName,
 17: 'TOON_STATUE',
 18: 'ANIMATED FURNITURE',
 19: AccessoryTypeName,
 20: InteriorLayoutTypeName}
InteriorLayoutNames = ["Default Layout", "Layout 2", "Layout 3", "Layout 4"]
HatStylesDescriptions = {'hbb1': 'Green Baseball Cap',
 'kmh1': 'Mouskateer',
 'hbb2': 'Blue Baseball Cap',
 'hbb3': 'Orange Baseball Cap',
 'hsf1': 'Beige Safari Hat',
 'hsf2': 'Brown Safari Hat',
 'hsf3': 'Green Safari Hat',
 'hrb1': 'Pink Bow',
 'hrb2': 'Red Bow',
 'hrb3': 'Purple Bow',
 'hht1': 'Pink Heart',
 'hht2': 'Yellow Heart',
 'htp1': 'Black Top Hat',
 'htp2': 'Blue Top Hat',
 'hav1': 'Anvil Hat',
 'hfp1': 'Flower Hat',
 'hsg1': 'Sandbag Hat',
 'hwt1': 'Weight Hat',
 'hfz1': 'Fez Hat',
 'hgf1': 'Golf Hat',
 'hpt1': 'Party Hat',
 'hpt2': 'Toon Party Hat',
 'hpb1': 'Fancy Hat',
 'hcr1': 'Crown',
 'hcw1': 'Cowboy Hat',
 'hpr1': 'Pirate Hat',
 'hpp1': 'Propeller Hat',
 'hfs1': 'Fishing Hat',
 'hsb1': 'Sombrero Hat',
 'hst1': 'Straw Hat',
 'hsu1': 'Sun Hat',
 'hrb4': 'Yellow Bow',
 'hrb5': 'Checker Bow',
 'hrb6': 'Light Red Bow',
 'hrb7': 'Rainbow Bow',
 'hat1': 'Antenna Thingy',
 'hhd1': 'Beehive Hairdo',
 'hbw1': 'Bowler Hat',
 'hch1': 'Chef Hat',
 'hdt1': 'Detective Hat',
 'hft1': 'Fancy Feathers Hat',
 'hfd1': 'Fedora',
 'hmk1': "Mickey's Band Hat",
 'hft2': 'Feather Headband',
 'hhd2': 'Pompadour Hairdo',
 'hpc1': 'Princess Hat',
 'hrh1': 'Archer Hat',
 'hhm1': 'Roman Helmet',
 'hat2': 'Spider Antenna Thingy',
 'htr1': 'Tiara',
 'hhm2': 'Viking Helmet',
 'hwz1': 'Witch Hat',
 'hwz2': 'Wizard Hat',
 'hhm3': 'Conquistador Helmet',
 'hhm4': 'Firefighter Helmet',
 'hfp2': 'Anti-Cog Control Hat',
 'hhm5': 'Miner Hat',
 'hnp1': 'Napoleon Hat',
 'hpc2': 'Pilot Cap',
 'hph1': 'Cop Hat',
 'hwg1': 'Rainbow Wacky Wig',
 'hbb4': 'Yellow Baseball Cap',
 'hbb5': 'Red Baseball Cap',
 'hbb6': 'Aqua Baseball Cap',
 'hsl1': 'Sailor Hat',
 'hfr1': 'Samba Hat',
 'hby1': 'Bobby Hat',
 'hrb8': 'Pink Dots Bow',
 'hjh1': 'Jester Hat',
 'hbb7': 'Purple Baseball Cap',
 'hrb9': 'Green Checker Bow',
 'hwt2': 'Winter Hat',
 'hhw1': 'Bandana',
 'hhw2': 'Toonosaur Hat',
 'hob1': 'Jamboree Hat',
 'hbn1': 'Bird Hat by Brianna'}
GlassesStylesDescriptions = {'grd1': 'Round Glasses',
 'gmb1': 'White Mini Blinds',
 'gnr1': 'Purple Narrow Glasses',
 'gst1': 'Yellow Star Glasses',
 'g3d1': 'Movie Glasses',
 'gav1': 'Aviator',
 'gce1': 'Cateye Glasses',
 'gdk1': 'Nerd Glasses',
 'gjo1': 'Celebrity Shades',
 'gsb1': 'Scuba Mask',
 'ggl1': 'Goggles',
 'ggm1': 'Groucho Glasses',
 'ghg1': 'Heart Glasses',
 'gie1': 'Bug Eye Glasses',
 'gmt1': 'Black Secret ID Mask',
 'gmt2': 'Blue Secret ID Mask',
 'gmt3': 'Blue Carnivale Mask',
 'gmt4': 'Purple Carnivale Mask',
 'gmt5': 'Aqua Carnivale Mask',
 'gmn1': 'Monocle',
 'gmo1': 'Smooch Glasses',
 'gsr1': 'Square Frame Glasses',
 'ghw1': 'Skull Eyepatch',
 'ghw2': 'Gem Eyepatch',
 'ghw3': "Limey's Eyepatch",
 'gag1': 'Alien Eyes by Alexandra'}
BackpackStylesDescriptions = {'bpb1': 'Blue Backpack',
 'bpb2': 'Orange Backpack',
 'bpb3': 'Purple BackPack',
 'bpd1': 'Red Dot Backpack',
 'bpd2': 'Yellow Dot Backpack',
 'bwg1': 'Bat Wings',
 'bwg2': 'Bee Wings',
 'bwg3': 'DragonFly Wings',
 'bst1': 'Scuba Tank',
 'bfn1': 'Shark Fin',
 'baw1': 'White Angel Wings',
 'baw2': 'Rainbow Angel Wings',
 'bwt1': 'Toys Backpack',
 'bwg4': 'Butterfly Wings',
 'bwg5': 'Pixie Wings',
 'bwg6': 'Dragon Wings',
 'bjp1': 'Jet Pack',
 'blg1': 'Bug Backpack',
 'bsa1': 'Plush Bear Pack',
 'bwg7': 'Bird wings',
 'bsa2': 'Plush Cat Pack',
 'bsa3': 'Plush Dog Pack',
 'bap1': 'Airplane Wings',
 'bhw1': 'Pirate Sword',
 'bhw2': 'Super Toon Cape',
 'bhw3': 'Vampire Cape',
 'bhw4': 'Toonosaur Backpack',
 'bob1': 'Jamboree Pack',
 'bfg1': 'Gag Attack Pack',
 'bfl1': 'Cog Pack by Savanah'}
ShoesStylesDescriptions = {'sat1': 'Green Athletic Shoes',
 'sat2': 'Red Athletic Shoes',
 'smb1': 'Green Toon Boots',
 'scs1': 'Green Sneakers',
 'swt1': 'Wingtips',
 'smj1': 'Black Fancy Shoes',
 'sdk1': 'Boat Shoes',
 'sat3': 'Yellow Athletic Shoes',
 'scs2': 'Black Sneakers',
 'scs3': 'White Sneakers',
 'scs4': 'Pink Sneakers',
 'scb1': 'Cowboy Boots',
 'sfb1': 'Purple Boots',
 'sht1': 'Green Hi Top Sneakers',
 'smj2': 'Brown Fancy Shoes',
 'smj3': 'Red Fancy Shoes',
 'ssb1': 'Red Super Toon Boots',
 'sts1': 'Green Tennis Shoes',
 'sts2': 'Pink Tennis Shoes',
 'scs5': 'Red Sneakers',
 'smb2': 'Aqua Toon Boots',
 'smb3': 'Brown Toon Boots',
 'smb4': 'Yellow Toon Boots',
 'sfb2': 'Blue Square Boots',
 'sfb3': 'Green Hearts Boots',
 'sfb4': 'Grey Dots Boots',
 'sfb5': 'Orange Stars Boots',
 'sfb6': 'Pink Stars Boots',
 'slf1': 'Loafers',
 'smj4': 'Purple Fancy Shoes',
 'smt1': 'Motorcycle Boots',
 'sox1': 'Oxfords',
 'srb1': 'Pink Rain Boots',
 'sst1': 'Jolly Boots',
 'swb1': 'Beige Winter Boots',
 'swb2': 'Pink Winter Boots',
 'swk1': 'Work Boots',
 'scs6': 'Yellow Sneakers',
 'smb5': 'Pink Toon Boots',
 'sht2': 'Pink Hi Top Sneakers',
 'srb2': 'Red Dots Rain Boots',
 'sts3': 'Purple Tennis Shoes',
 'sts4': 'Violet Tennis Shoes',
 'sts5': 'Yellow Tennis Shoes',
 'srb3': 'Blue Rain Boots',
 'srb4': 'Yellow Rain Boots',
 'sat4': 'Black Athletic Shoes',
 'shw1': 'Pirate Shoes',
 'shw2': 'Toonosaur Feet'}
AccessoryNamePrefix = {0: 'hat unisex ',
 1: 'glasses unisex ',
 2: 'backpack unisex ',
 3: 'shoes unisex ',
 4: 'hat boy ',
 5: 'glasses boy ',
 6: 'backpack boy ',
 7: 'shoes boy ',
 8: 'hat girl ',
 9: 'glasses girl ',
 10: 'backpack girl ',
 11: 'shoes girl '}
AwardManagerAccessoryNames = {}
AccessoryTypeNames = {}
for accessoryId in CatalogAccessoryItemGlobals.AccessoryTypes.keys():
    accessoryInfo = CatalogAccessoryItemGlobals.AccessoryTypes[accessoryId]
    if accessoryInfo[0] % 4 == 0:
        accessoryStyleDescription = HatStylesDescriptions
    elif accessoryInfo[0] % 4 == 1:
        accessoryStyleDescription = GlassesStylesDescriptions
    elif accessoryInfo[0] % 4 == 2:
        accessoryStyleDescription = BackpackStylesDescriptions
    else:
        accessoryStyleDescription = ShoesStylesDescriptions
    if accessoryInfo[3]:
        AwardManagerAccessoryNames[accessoryId] = AccessoryNamePrefix[accessoryInfo[0]] + accessoryStyleDescription[accessoryInfo[1]]
    AccessoryTypeNames[accessoryId] = accessoryStyleDescription[accessoryInfo[1]]

ShirtStylesDescriptions = {'bss1': 'solid',
 'bss2': 'single stripe',
 'bss3': 'collar',
 'bss4': 'double stripe',
 'bss5': 'multiple stripes',
 'bss6': 'collar w/ pocket',
 'bss7': 'hawaiian',
 'bss8': 'collar w/ 2 pockets',
 'bss9': 'bowling shirt',
 'bss10': 'vest (special)',
 'bss11': 'collar w/ ruffles',
 'bss12': 'soccer jersey (special)',
 'bss13': 'lightning bolt (special)',
 'bss14': 'jersey 19 (special)',
 'bss15': 'guayavera',
 'gss1': 'girl solid',
 'gss2': 'girl single stripe',
 'gss3': 'girl collar',
 'gss4': 'girl double stripes',
 'gss5': 'girl collar w/ pocket',
 'gss6': 'girl flower print',
 'gss7': 'girl flower trim (special)',
 'gss8': 'girl collar w/ 2 pockets',
 'gss9': 'girl denim vest (special)',
 'gss10': 'girl peasant',
 'gss11': 'girl peasant w/ mid stripe',
 'gss12': 'girl soccer jersey (special)',
 'gss13': 'girl hearts',
 'gss14': 'girl stars (special)',
 'gss15': 'girl flower',
 'c_ss1': 'yellow hooded - Series 1',
 'c_ss2': 'yellow with palm tree - Series 1',
 'c_ss3': 'purple with stars - Series 2',
 'c_bss1': 'blue stripes (boys only) - Series 1',
 'c_bss2': 'orange (boys only) - Series 1',
 'c_bss3': 'lime green with stripe (boys only) - Series 2',
 'c_bss4': 'red kimono with checkerboard (boys only) - Series 2',
 'c_gss1': 'girl blue with yellow stripes (girls only) - Series 1',
 'c_gss2': 'girl pink and beige with flower (girls only) - Series 1',
 'c_gss3': 'girl Blue and gold with wavy stripes (girls only) - Series 2',
 'c_gss4': 'girl Blue and pink with bow (girls only) - Series 2',
 'c_gss5': 'girl Aqua kimono white stripe (girls only) - UNUSED',
 'c_ss4': 'Tie dye shirt (boys and girls) - Series 3',
 'c_ss5': 'light blue with blue and white stripe (boys only) - Series 3',
 'c_ss6': 'cowboy shirt 1 : Series 4',
 'c_ss7': 'cowboy shirt 2 : Series 4',
 'c_ss8': 'cowboy shirt 3 : Series 4',
 'c_ss9': 'cowboy shirt 4 : Series 4',
 'c_ss10': 'cowboy shirt 5 : Series 4',
 'c_ss11': 'cowboy shirt 6 : Series 4',
 'hw_ss1': 'Halloween Ghost',
 'hw_ss2': 'Halloween Pumpkin',
 'hw_ss3': 'Halloween Vampire',
 'hw_ss4': 'Halloween Turtle',
 'hw_ss5': 'Halloween Bee',
 'hw_ss6': 'Halloween Pirate',
 'hw_ss7': 'Halloween SuperToon',
 'hw_ss8': 'Halloween Vampire NoCape',
 'hw_ss9': 'Halloween Dinosaur',
 'wh_ss1': 'Winter Holiday 1',
 'wh_ss2': 'Winter Holiday 2',
 'wh_ss3': 'Winter Holiday 3',
 'wh_ss4': 'Winter Holiday 4',
 'vd_ss1': 'girl Valentines day, pink with red hearts (girls)',
 'vd_ss2': 'Valentines day, red with white hearts',
 'vd_ss3': 'Valentines day, white with winged hearts (boys)',
 'vd_ss4': ' Valentines day, pink with red flamed heart',
 'vd_ss5': '2009 Valentines day, white with red cupid',
 'vd_ss6': '2009 Valentines day, blue with green and red hearts',
 'vd_ss7': '2010 Valentines day, red with white wings',
 'sd_ss1': "St Pat's Day, four leaf clover shirt",
 'sd_ss2': "St Pat's Day, pot o gold shirt",
 'sd_ss3': 'Ides of March greenToon shirt',
 'tc_ss1': 'T-Shirt Contest, Fishing Vest',
 'tc_ss2': 'T-Shirt Contest, Fish Bowl',
 'tc_ss3': 'T-Shirt Contest, Paw Print',
 'tc_ss4': 'T-Shirt Contest, Backpack',
 'tc_ss5': 'T-Shirt Contest, Lederhosen ',
 'tc_ss6': 'T-Shirt Contest, Watermelon  ',
 'tc_ss7': 'T-Shirt Contest, Race Shirt',
 'j4_ss1': 'July 4th, Flag',
 'j4_ss2': 'July 4th, Fireworks',
 'c_ss12': 'Catalog series 7, Green w/ yellow buttons',
 'c_ss13': 'Catalog series 7, Purple w/ big flower',
 'pj_ss1': 'Blue Banana Pajama shirt',
 'pj_ss2': 'Red Horn Pajama shirt',
 'pj_ss3': 'Purple Glasses Pajama shirt',
 'sa_ss1': 'Award Striped Shirt',
 'sa_ss2': 'Award Fishing Shirt 1',
 'sa_ss3': 'Award Fishing Shirt 2',
 'sa_ss4': 'Award Gardening Shirt 1',
 'sa_ss5': 'Award Gardening Shirt 2',
 'sa_ss6': 'Award Party Shirt 1',
 'sa_ss7': 'Award Party Shirt 2',
 'sa_ss8': 'Award Racing Shirt 1',
 'sa_ss9': 'Award Racing Shirt 2',
 'sa_ss10': 'Award Summer Shirt 1',
 'sa_ss11': 'Award Summer Shirt 2',
 'sa_ss12': 'Award Golf Shirt 1',
 'sa_ss13': 'Award Golf Shirt 2',
 'sa_ss14': 'Award Halloween Bee Shirt',
 'sa_ss15': 'Award Halloween SuperToon Shirt',
 'sa_ss16': 'Award Matathon Shirt 1',
 'sa_ss17': 'Award Save Building Shirt 1',
 'sa_ss18': 'Award Save Building Shirt 2',
 'sa_ss19': 'Award Toontask Shirt 1',
 'sa_ss20': 'Award Toontask Shirt 2',
 'sa_ss21': 'Award Trolley Shirt 1',
 'sa_ss22': 'Award Trolley Shirt 2',
 'sa_ss23': 'Award Winter Shirt 1',
 'sa_ss24': 'Award Halloween Skeleton Shirt',
 'sa_ss25': 'Award Halloween Spider Shirt',
 'sa_ss26': 'Award Most Cogs Defeated Shirt',
 'sa_ss27': 'Award Most V.P.s Defeated Shirt',
 'sa_ss28': 'Award Sellbot Smasher Shirt',
 'sa_ss29': 'Award Most C.J.s Defeated Shirt',
 'sa_ss30': 'Award Lawbot Smasher Shirt',
 'sa_ss31': 'Award Racing Shirt 3',
 'sa_ss32': 'Award Fishing Shirt 4',
 'sa_ss33': 'Award Golf Shirt 3',
 'sa_ss34': 'Award Most Cogs Defeated Shirt 2',
 'sa_ss35': 'Award Racing Shirt 4',
 'sa_ss36': 'Award Save Building Shirt 3',
 'sa_ss37': 'Award Trolley Shirt 3',
 'sa_ss38': 'Award Fishing Shirt 5',
 'sa_ss39': 'Award Golf Shirt 4',
 'sa_ss40': 'Award Halloween Witchy Moon Shirt',
 'sa_ss41': 'Award Winter Holiday Sled Shirt',
 'sa_ss42': 'Award Halloween Batty Moon Shirt',
 'sa_ss43': 'Award Winter Holiday Mittens Shirt',
 'sa_ss44': 'Award Fishing Shirt 6',
 'sa_ss45': 'Award Fishing Shirt 7',
 'sa_ss46': 'Award Golf Shirt 5',
 'sa_ss47': 'Award Racing Shirt 5',
 'sa_ss48': 'Award Racing Shirt 6',
 'sa_ss49': 'Award Most Cogs Defeated shirt 3',
 'sa_ss50': 'Award Most Cogs Defeated shirt 4',
 'sa_ss51': 'Award Trolley shirt 4',
 'sa_ss52': 'Award Trolley shirt 5',
 'sa_ss53': 'Award Save Building Shirt 4',
 'sa_ss54': 'Award Save Building Shirt 5',
 'sa_ss55': 'Award Anniversary',
 'sc_1': 'Scientist top 1',
 'sc_2': 'Scientist top 2',
 'sc_3': 'Scientist top 3',
 'sil_1': 'Silly Mailbox Shirt',
 'sil_2': 'Silly Trash Can Shirt',
 'sil_3': 'Loony Labs Shirt',
 'sil_4': 'Silly Hydrant Shirt',
 'sil_5': 'Sillymeter Whistle Shirt',
 'sil_6': 'Silly Cog-Crusher Shirt',
 'sil_7': 'Victory Party Shirt 1',
 'sil_8': 'Victory Party Shirt 2',
 'emb_us1': 'placeholder emblem shirt 1',
 'emb_us2': 'placeholder emblem shirt 2',
 'emb_us3': 'placeholder emblem shirt 3',
 'sb_1': 'Sellbot Icon Shirt',
 'lb_1': 'Lawbot Icon Shirt',
 'jb_1': 'Jellybean Shirt',
 'jb_2': 'Doodle Shirt',
 'ugcms': 'Get Connected Mover & Shaker'}
BottomStylesDescriptions = {'bbs1': 'plain w/ pockets',
 'bbs2': 'belt',
 'bbs3': 'cargo',
 'bbs4': 'hawaiian',
 'bbs5': 'side stripes (special)',
 'bbs6': 'soccer shorts',
 'bbs7': 'side flames (special)',
 'bbs8': 'denim',
 'vd_bs1': 'Valentines shorts',
 'vd_bs2': 'Green with red heart',
 'vd_bs3': 'Blue denim with green and red heart',
 'c_bs1': 'Orange with blue side stripes',
 'c_bs2': 'Blue with gold cuff stripes',
 'c_bs5': 'Green stripes - series 7',
 'sd_bs1': 'St. Pats leprechaun shorts',
 'sd_bs2': 'Ides of March greenToon shorts',
 'pj_bs1': 'Blue Banana Pajama pants',
 'pj_bs2': 'Red Horn Pajama pants',
 'pj_bs3': 'Purple Glasses Pajama pants',
 'wh_bs1': 'Winter Holiday Shorts Style 1',
 'wh_bs2': 'Winter Holiday Shorts Style 2',
 'wh_bs3': 'Winter Holiday Shorts Style 3',
 'wh_bs4': 'Winter Holiday Shorts Style 4',
 'hw_bs1': 'Halloween Bee Shorts male',
 'hw_bs2': 'Halloween Pirate Shorts male',
 'hw_bs5': 'Halloween SuperToon Shorts male',
 'hw_bs6': 'Halloween Vampire NoCape Shorts male',
 'hw_bs7': 'Halloween Dinosaur Shorts male',
 'sil_bs1': 'Silly Cog-Crusher Shorts',
 'gsk1': 'solid',
 'gsk2': 'polka dots (special)',
 'gsk3': 'vertical stripes',
 'gsk4': 'horizontal stripe',
 'gsk5': 'flower print',
 'gsk6': '2 pockets (special) ',
 'gsk7': 'denim skirt',
 'gsh1': 'plain w/ pockets',
 'gsh2': 'flower',
 'gsh3': 'denim shorts',
 'c_gsk1': 'blue skirt with tan border and button',
 'c_gsk2': 'purple skirt with pink and ribbon',
 'c_gsk3': 'teal skirt with yellow and star',
 'vd_gs1': 'red skirt with hearts',
 'vd_gs2': 'Pink flair skirt with polka hearts',
 'vd_gs3': 'Blue denim skirt with green and red heart',
 'c_gsk4': 'rainbow skirt - Series 3',
 'sd_gs1': 'St. Pats day shorts',
 'sd_gs2': 'Ides of March greenToon skirt',
 'c_gsk5': 'Western skirts 1',
 'c_gsk6': 'Western skirts 2',
 'c_bs3': 'Western shorts 1',
 'c_bs4': 'Western shorts 2',
 'j4_bs1': 'July 4th shorts',
 'j4_gs1': 'July 4th Skirt',
 'c_gsk7': 'Blue with flower - series 7',
 'pj_gs1': 'Blue Banana Pajama pants',
 'pj_gs2': 'Red Horn Pajama pants',
 'pj_gs3': 'Purple Glasses Pajama pants',
 'wh_gsk1': 'Winter Holiday Skirt Style 1',
 'wh_gsk2': 'Winter Holiday Skirt Style 2',
 'wh_gsk3': 'Winter Holiday Skirt Style 3',
 'wh_gsk4': 'Winter Holiday Skirt Style 4',
 'sa_bs1': 'Award Fishing Shorts',
 'sa_bs2': 'Award Gardening Shorts',
 'sa_bs3': 'Award Party Shorts',
 'sa_bs4': 'Award Racing Shorts',
 'sa_bs5': 'Award Summer Shorts',
 'sa_bs6': 'Award Golf Shorts 1',
 'sa_bs7': 'Award Halloween Bee Shorts',
 'sa_bs8': 'Award Halloween SuperToon Shorts',
 'sa_bs9': 'Award Save Building Shorts 1',
 'sa_bs10': 'Award Trolley Shorts 1',
 'sa_bs11': 'Award Halloween Spider Shorts',
 'sa_bs12': 'Award Halloween Skeleton Shorts',
 'sa_bs13': 'Award Sellbot Smasher Shorts male',
 'sa_bs14': 'Award Lawbot Smasher Shorts male',
 'sa_bs15': 'Award Racing Shorts 1',
 'sa_bs16': 'Award Golf Shorts 3',
 'sa_bs17': 'Award Racing Shorts 4',
 'sa_bs18': 'Award Golf Shorts 4',
 'sa_bs19': 'Award Golf Shorts 5',
 'sa_bs20': 'Award Racing Shorts 5',
 'sa_bs21': 'Award Racing Shorts 6',
 'sa_gs1': 'Award Fishing Skirt',
 'sa_gs2': 'Award Gardening Skirt',
 'sa_gs3': 'Award Party Skirt',
 'sa_gs4': 'Award Racing Skirt',
 'sa_gs5': 'Award Summer Skirt',
 'sa_gs6': 'Award Golf Skirt 1',
 'sa_gs7': 'Award Halloween Bee Skirt',
 'sa_gs8': 'Award Halloween SuperToon Skirt',
 'sa_gs9': 'Award Save Building Skirt 1',
 'sa_gs10': 'Award Trolley Skirt 1',
 'sa_gs11': 'Award Halloween Skeleton Skirt',
 'sa_gs12': 'Award Halloween Spider Skirt',
 'sa_gs13': 'Award Sellbot Smasher Shorts female',
 'sa_gs14': 'Award Lawbot Smasher Shorts female',
 'sa_gs15': 'Award Racing Skirt 1',
 'sa_gs16': 'Award Golf Skirt 2',
 'sa_gs17': 'Award Racing Skirt 4',
 'sa_gs18': 'Award Golf Skirt 3',
 'sa_gs19': 'Award Golf Skirt 4',
 'sa_gs20': 'Award Racing Skirt 5',
 'sa_gs21': 'Award Racing Skirt 6',
 'sc_bs1': 'Scientist bottom male 1',
 'sc_bs2': 'Scientist bottom male 2',
 'sc_bs3': 'Scientist bottom male 3',
 'sc_gs1': 'Scientist bottom female 1',
 'sc_gs2': 'Scientist bottom female 2',
 'sc_gs3': 'Scientist bottom female 3',
 'sil_bs1': 'Silly Cog-Crusher Shorts male',
 'sil_gs1': 'Silly Cog-Crusher Shorts female',
 'hw_bs3': 'Halloween Vampire Shorts male',
 'hw_gs3': 'Halloween Vampire Shorts female',
 'hw_bs4': 'Halloween Turtle Shorts male',
 'hw_gs4': 'Halloween Turtle Shorts female',
 'hw_gs1': 'Halloween Bee Shorts female',
 'hw_gs2': 'Halloween Pirate Shorts female',
 'hw_gs5': 'Halloween SuperToon Shorts female',
 'hw_gs6': 'Halloween Vampire NoCape Shorts female',
 'hw_gs7': 'Halloween Dinosaur Shorts female',
 'hw_gsk1': 'Halloween Pirate Skirt'}
AwardMgrBoy = 'boy'
AwardMgrGirl = 'girl'
AwardMgrUnisex = 'unisex'
AwardMgrShorts = 'shorts'
AwardMgrSkirt = 'skirt'
AwardMgrShirt = 'shirt'
SpecialEventMailboxStrings = {1: 'A special item from the Toon Council just for you!',
 2: "Here is your Melville's Fishing Tournament prize! Congratulations!",
 3: "Here is your Billy Budd's Fishing Tournament prize! Congratulations!",
 4: 'Here is your Acorn Acres April Invitational prize! Congratulations!',
 5: 'Here is your Acorn Acres C.U.P. Championship prize! Congratulations!',
 6: 'Here is your Gift-Giving Extravaganza prize! Congratulations!',
 7: "Here is your Top Toons New Year's Day Marathon prize! Congratulations!",
 8: 'Here is your Perfect Trolley Games Weekend prize! Congratulations!',
 9: 'Here is your Trolley Games Madness prize! Congratulations!',
 10: 'Here is your Grand Prix Weekend prize! Congratulations!',
 11: 'Here is your ToonTask Derby prize! Congratulations!',
 12: 'Here is your Save a Building Marathon prize! Congratulations!',
 13: 'Here is your Most Cogs Defeated Tournament prize! Congratulations!',
 14: 'Here is your Most V.P.s Defeated Tournament prize! Congratulations!',
 15: 'Here is your Operation: Storm Sellbot prize! Congratulations!',
 16: 'Here is your Most C.J.s Defeated Tournament prize! Congratulations!',
 17: 'Here is your Operation: Lawbots Lose prize! Congratulations!',
 18: 'Here is your Operation: Crash Cashbots prize! Congratulations!',
 19: 'Here is your Operation: Blast Bossbots prize! Congratulations!',
 20: 'Here is your Most C.E.O.s Defeated Tournament prize! Congratulations!'}
RentalHours = 'Hours'
RentalOf = 'Of'
RentalCannon = 'Cannons!'
RentalGameTable = 'Game Table!'
EstateCannonGameEnd = 'The Cannon Game rental is over.'
GameTableRentalEnd = 'The Game Table rental is over.'
MessageConfirmRent = 'Begin rental? Cancel to save the rental for later'
MessageConfirmGarden = 'Are you sure you want to start a garden?'
NametagPaid = 'Citizen Name Tag'
NametagAction = 'Action Name Tag'
NametagFrilly = 'Frilly Name Tag'
FurnitureYourOldCloset = 'your old wardrobe'
FurnitureYourOldBank = 'your old bank'
FurnitureYourOldTrunk = 'your old trunk'
TrunkHatGUI = 'Hats'
TrunkGlassesGUI = 'Glasses'
TrunkBackpackGUI = 'Backpacks'
TrunkShoesGUI = 'Shoes'
ChatItemQuotes = '"%s"'
FurnitureNames = {100: 'Armchair',
 105: 'Armchair',
 110: 'Chair',
 120: 'Desk Chair',
 130: 'Log Chair',
 140: 'Lobster Chair',
 145: 'Lifejacket Chair',
 150: 'Saddle Stool',
 160: 'Native Chair',
 170: 'Cupcake Chair',
 200: 'Bed',
 205: 'Bed',
 210: 'Bed',
 220: 'Bathtub Bed',
 230: 'Leaf Bed',
 240: 'Boat Bed',
 250: 'Cactus Hammock',
 260: 'Ice Cream Bed',
 270: "Olivia Erin & Cat's Bed",
 300: 'Player Piano',
 310: 'Pipe Organ',
 400: 'Fireplace',
 410: 'Fireplace',
 420: 'Round Fireplace',
 430: 'Fireplace',
 440: 'Apple Fireplace',
 450: "Erin's Fireplace",
 460: "Erin's Lit Fireplace",
 470: 'Lit Fireplace',
 480: 'Round Lit Fireplace',
 490: 'Lit Fireplace',
 491: 'Lit Fireplace',
 492: 'Apple Lit Fireplace',
 500: 'Wardrobe',
 502: '15 item Wardrobe',
 504: '20 item Wardrobe',
 506: '25 item Wardrobe',
 508: '50 item Wardrobe',
 510: 'Wardrobe',
 512: '15 item Wardrobe',
 514: '20 item Wardrobe',
 516: '25 item Wardrobe',
 518: '50 item Wardrobe',
 600: 'Short Lamp',
 610: 'Tall Lamp',
 620: 'Table Lamp',
 625: 'Table Lamp',
 630: 'Daisy Lamp',
 640: 'Daisy Lamp',
 650: 'Jellyfish Lamp',
 660: 'Jellyfish Lamp',
 670: 'Cowboy Lamp',
 680: 'Candle',
 681: 'Lit Candle',
 700: 'Cushioned Chair',
 705: 'Cushioned Chair',
 710: 'Couch',
 715: 'Couch',
 720: 'Hay Couch',
 730: 'Shortcake Couch',
 800: 'Desk',
 810: 'Log Desk',
 900: 'Umbrella Stand',
 910: 'Coat Rack',
 920: 'Trash Can',
 930: 'Red Mushroom',
 940: 'Yellow Mushroom',
 950: 'Coat Rack',
 960: 'Barrel Stand',
 970: 'Cactus Plant',
 980: 'Teepee',
 990: "Juliette's Fan",
 1000: 'Large Rug',
 1010: 'Round Rug',
 1015: 'Round Rug',
 1020: 'Small Rug',
 1030: 'Leaf Mat',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Display Cabinet',
 1110: 'Display Cabinet',
 1120: 'Tall Bookcase',
 1130: 'Low Bookcase',
 1140: 'Sundae Chest',
 1200: 'End Table',
 1210: 'Small Table',
 1215: 'Small Table',
 1220: 'Coffee Table',
 1230: 'Coffee Table',
 1240: "Snorkeler's Table",
 1250: 'Cookie Table',
 1260: 'Bedroom Table',
 1300: '20000 Bean Bank',
 1310: '25000 Bean Bank',
 1320: '30000 Bean Bank',
 1330: '35000 Bean Bank',
 1340: '40000 Bean Bank',
 1350: '45000 Bean Bank',
 1399: 'Telephone',
 1400: 'Cezanne Toon',
 1410: 'Flowers',
 1420: 'Modern Mickey',
 1430: 'Rembrandt Toon',
 1440: 'Toonscape',
 1441: "Whistler's Horse",
 1442: 'Toon Star',
 1443: 'Not a Pie',
 1450: 'Mickey and Minnie',
 1500: 'Radio',
 1510: 'Radio',
 1520: 'Radio',
 1530: 'Television',
 1600: 'Short Vase',
 1610: 'Tall Vase',
 1620: 'Short Vase',
 1630: 'Tall Vase',
 1640: 'Short Vase',
 1650: 'Short Vase',
 1660: 'Coral Vase',
 1661: 'Shell Vase',
 1670: 'Rose Vase',
 1680: 'Rose Watercan',
 1700: 'Popcorn Cart',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Washing Machine',
 1800: 'Fish Bowl',
 1810: 'Fish Bowl',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'Hanging Horns',
 1930: 'Simple Sombrero',
 1940: 'Fancy Sombrero',
 1950: 'Dream Catcher',
 1960: 'Horseshoe',
 1970: 'Bison Portrait',
 2000: 'Candy Swing Set',
 2010: 'Cake Slide',
 3000: 'Banana Split Tub',
 4000: 'Boy Trunk',
 4010: 'Girl Trunk',
 10000: 'Short Pumpkin',
 10010: 'Tall Pumpkin',
 10020: 'Winter Tree',
 10030: 'Winter Wreath'}
AwardManagerFurnitureNames = {100: 'Armchair A - Series 1',
 105: 'Armchair A - Series 7',
 110: 'Chair - Series 1',
 120: 'Desk Chair - Series 2',
 130: 'Log Chair - Series 2',
 140: 'Lobster Chair - Series 3',
 145: 'Lifejacket Chair - Series 3',
 150: 'Saddle Stool - Series 4',
 160: 'Native Chair - Series 4',
 170: 'Cupcake Chair - Series 6',
 200: "Bed Boy's bed - Initial Furniture",
 205: "Bed Boy's bed Series 7",
 210: "Bed Girl's bed - Series 1",
 220: 'Bathtub Bed',
 230: 'Leaf Bed',
 240: 'Boat Bed',
 250: 'Cactus Hammock',
 260: 'Ice Cream Bed',
 270: "Olivia Erin & Cat's Bed - Trolley Bed",
 300: 'Player Piano',
 310: 'Pipe Organ',
 400: 'Fireplace - Square Fireplace Initial Furniture',
 410: 'Fireplace - Girly Fireplace Series 1',
 420: 'Round Fireplace',
 430: 'Fireplace - bug room series 2',
 440: 'Apple Fireplace',
 450: "Erin's Fireplace - coral",
 460: "Erin's Lit Fireplace - coral",
 470: 'Lit Fireplace - square fireplace with fire',
 480: 'Round Lit Fireplace',
 490: 'Lit Fireplac - girl fireplace with firee',
 491: 'Lit Fireplace - bug room fireplace',
 492: 'Apple Lit Fireplace',
 500: 'boy Wardrobe - 10 items initial',
 502: 'boy 15 item Wardrobe',
 504: 'boy 20 item Wardrobe',
 506: 'boy 25 item Wardrobe',
 508: 'boy 50 item Wardrobe',
 510: 'girl Wardrobe -  10 items initial',
 512: 'girl 15 item Wardrobe',
 514: 'girl 20 item Wardrobe',
 516: 'girl 25 item Wardrobe',
 518: 'girl 50 item Wardrobe',
 600: 'Short Lamp',
 610: 'Tall Lamp',
 620: 'Table Lamp - Series 1',
 625: 'Table Lamp - Series 7',
 630: 'Daisy Lamp 1',
 640: 'Daisy Lamp 2',
 650: 'Jellyfish Lamp 1',
 660: 'Jellyfish Lamp 2',
 670: 'Cowboy Lamp',
 680: 'Candle',
 681: 'Lit Candle',
 700: 'Cushioned Chair - Series 1',
 705: 'Cushioned Chair - Series 7',
 710: 'Couch - series 1',
 715: 'Couch - series 7',
 720: 'Hay Couch',
 730: 'Shortcake Couch',
 800: 'Desk',
 810: 'Log Desk',
 900: 'Umbrella Stand',
 910: 'Coat Rack - series 1',
 920: 'Trash Can',
 930: 'Red Mushroom',
 940: 'Yellow Mushroom',
 950: 'Coat Rack - underwater',
 960: 'Barrel Stand',
 970: 'Cactus Plant',
 980: 'Teepee',
 990: "Juliette's Fan - gag fan",
 1000: 'Large Rug',
 1010: 'Round Rug - Series 1',
 1015: 'Round Rug - Series 7',
 1020: 'Small Rug',
 1030: 'Leaf Mat',
 1040: 'Presents',
 1050: 'Sled',
 1100: 'Display Cabinet - Red',
 1110: 'Display Cabinet - Yellow',
 1120: 'Tall Bookcase',
 1130: 'Low Bookcase',
 1140: 'Sundae Chest',
 1200: 'End Table',
 1210: 'Small Table - series 1 ',
 1215: 'Small Table - series 7',
 1220: 'Coffee Table sq',
 1230: 'Coffee Table bw',
 1240: "Snorkeler's Table",
 1250: 'Cookie Table',
 1260: 'Bedroom Table',
 1300: '1000 Bean Bank',
 1310: '2500 Bean Bank',
 1320: '5000 Bean Bank',
 1330: '7500 Bean Bank',
 1340: '10000 Bean Bank',
 1350: '12000 Bean Bank',
 1399: 'Telephone',
 1400: 'Cezanne Toon',
 1410: 'Flowers',
 1420: 'Modern Mickey',
 1430: 'Rembrandt Toon',
 1440: 'Toonscape',
 1441: "Whistler's Horse",
 1442: 'Toon Star',
 1443: 'Not a Pie',
 1450: 'Mickey and Minnie',
 1500: 'Radio A series 2',
 1510: 'Radio B series 1',
 1520: 'Radio C series 2',
 1530: 'Television',
 1600: 'Short Vase A',
 1610: 'Tall Vase A',
 1620: 'Short Vase B',
 1630: 'Tall Vase B',
 1640: 'Short Vase C',
 1650: 'Short Vase D',
 1660: 'Coral Vase',
 1661: 'Shell Vase',
 1670: 'Rose Vase',
 1680: 'Rose Watercan',
 1700: 'Popcorn Cart',
 1710: 'Ladybug',
 1720: 'Fountain',
 1725: 'Washing Machine',
 1800: 'Fish Bowl skull',
 1810: 'Fish Bowl lizard',
 1900: 'Swordfish',
 1910: 'Hammerhead',
 1920: 'Hanging Horns',
 1930: 'Simple Sombrero',
 1940: 'Fancy Sombrero',
 1950: 'Dream Catcher',
 1960: 'Horseshoe',
 1970: 'Bison Portrait',
 2000: 'Candy Swing Set',
 2010: 'Cake Slide',
 3000: 'Banana Split Tub',
 4000: 'Boy Trunk',
 4010: 'Girl Trunk',
 10000: 'Short Pumpkin',
 10010: 'Tall Pumpkin',
 10020: 'Winter Tree',
 10030: 'Winter Wreath'}
ClothingArticleNames = ('Shirt',
 'Shirt',
 'Shirt',
 'Shorts',
 'Shorts',
 'Skirt',
 'Shorts')
ClothingTypeNames = {1001: 'Ghost Shirt',
 1002: 'Pumpkin Shirt',
 1112: 'Bee Shirt',
 1113: 'Pirate Shirt',
 1114: 'Super Toon Shirt',
 1115: 'Vampire Shirt',
 1116: 'Toonosaur Shirt',
 1117: 'Bee Shorts',
 1118: 'Pirate Shorts',
 1119: 'Super Toon Shorts',
 1120: 'Vampire Shorts',
 1121: 'Toonosaur Shorts',
 1122: 'Bee Shorts',
 1123: 'Pirate Shorts',
 1124: 'Super Toon Shorts',
 1125: 'Vampire Shorts',
 1126: 'Toonosaur Shorts',
 1127: 'Pirate Skirt',
 1304: "O'Shirt",
 1305: "O'Shorts",
 1306: "O'Skirt",
 1400: "Matthew's Shirt",
 1401: "Jessica's Shirt",
 1402: "Marissa's Shirt",
 1600: 'Trap Outfit',
 1601: 'Sound Outfit',
 1602: 'Lure Outfit',
 1603: 'Trap Outfit',
 1604: 'Sound Outfit',
 1605: 'Lure Outfit',
 1606: 'Trap Outfit',
 1607: 'Sound Outfit',
 1608: 'Lure Outfit',
 1723: 'Bee Shirt',
 1724: 'SuperToon Shirt',
 1734: 'Bee Shorts',
 1735: 'SuperToon Shorts',
 1739: 'Bee Skirt',
 1740: 'SuperToon Skirt',
 1743: 'Skeleton Shirt',
 1744: 'Spider Shirt',
 1745: 'Spider Shorts',
 1746: 'Skeleton Shorts',
 1747: 'Skeleton Skirt',
 1748: 'Spider Skirt',
 1749: 'Silly Mailbox Shirt',
 1750: 'Silly Trash Can Shirt',
 1751: 'Loony Labs Shirt',
 1752: 'Silly Hydrant Shirt',
 1753: 'Silly Meter Shirt',
 1754: 'Cog-Crusher Shirt',
 1755: 'Cog-Crusher Shorts',
 1756: 'Cog-Crusher Shorts',
 1757: 'Victory Party Shirt',
 1758: 'Relaxed Victory Shirt',
 1763: 'Smashed Sellbot Shirt',
 1764: 'Most V.P.s Defeated Shirt',
 1765: 'Sellbot Smasher Shirt',
 1766: 'Sellbot Smasher Shorts',
 1767: 'Sellbot Smasher Shorts',
 1768: 'Jellybean Bank Shirt',
 1769: 'Doodle Shirt',
 1770: 'Vampire Shirt',
 1771: 'Turtle Shirt',
 1772: 'Vampire Shorts',
 1773: 'Vampire Shorts',
 1774: 'Turtle Shorts',
 1775: 'Turtle Shorts',
 1776: 'Get Connected Mover & Shaker Shirt',
 1777: 'Smashed Lawbot Shirt',
 1778: 'Most C.J.s Defeated Shirt',
 1779: 'Lawbot Smasher Shirt',
 1780: 'Lawbot Smasher Shorts',
 1781: 'Lawbot Smasher Shorts',
 1782: 'Racing Shirt 3',
 1783: 'Racing Shorts 1',
 1784: 'Racing Skirt 1',
 1801: 'Batty Moon Shirt',
 1802: 'Mittens Shirt'}
AccessoryArticleNames = ('Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes',
 'Hat',
 'Glasses',
 'Backpack',
 'Shoes')
SurfaceNames = ('Wallpaper',
 'Moulding',
 'Flooring',
 'Wainscoting',
 'Border')
WallpaperNames = {1000: 'Parchment',
 1100: 'Milan',
 1200: 'Dover',
 1300: 'Victoria',
 1400: 'Newport',
 1500: 'Pastoral',
 1600: 'Harlequin',
 1700: 'Moon',
 1800: 'Stars',
 1900: 'Flowers',
 2000: 'Spring Garden',
 2100: 'Formal Garden',
 2200: 'Race Day',
 2300: 'Touchdown!',
 2400: 'Cloud 9',
 2500: 'Climbing Vine',
 2600: 'Springtime',
 2700: 'Kokeshi',
 2800: 'Posies',
 2900: 'Angel Fish',
 3000: 'Bubbles',
 3100: 'Bubbles',
 3200: 'Go Fish',
 3300: 'Stop Fish',
 3400: 'Sea Horse',
 3500: 'Sea Shells',
 3600: 'Underwater',
 3700: 'Boots',
 3800: 'Cactus',
 3900: 'Cowboy Hat',
 10100: 'Cats',
 10200: 'Bats',
 11000: 'Snowflakes',
 11100: 'Hollyleaf',
 11200: 'Snowman',
 12000: 'ValenToons',
 12100: 'ValenToons',
 12200: 'ValenToons',
 12300: 'ValenToons',
 13000: 'Shamrock',
 13100: 'Shamrock',
 13200: 'Rainbow',
 13300: 'Shamrock'}
FlooringNames = {1000: 'Hardwood Floor',
 1010: 'Carpet',
 1020: 'Diamond Tile',
 1030: 'Diamond Tile',
 1040: 'Grass',
 1050: 'Beige Bricks',
 1060: 'Red Bricks',
 1070: 'Square Tile',
 1080: 'Stone',
 1090: 'Boardwalk',
 1100: 'Dirt',
 1110: 'Wood Tile',
 1120: 'Tile',
 1130: 'Honeycomb',
 1140: 'Water',
 1150: 'Beach Tile',
 1160: 'Beach Tile',
 1170: 'Beach Tile',
 1180: 'Beach Tile',
 1190: 'Sand',
 10000: 'Ice Cube',
 10010: 'Igloo',
 11000: 'Shamrock',
 11010: 'Shamrock'}
MouldingNames = {1000: 'Knotty',
 1010: 'Painted',
 1020: 'Dental',
 1030: 'Flowers',
 1040: 'Flowers',
 1050: 'Ladybug',
 1060: 'ValenToons',
 1070: 'Beach',
 1080: 'Winter Lights 1',
 1085: 'Winter Lights 2',
 1090: 'Winter Lights 3',
 1100: "ValenToon's Cupid",
 1110: "ValenToon's Heart 1",
 1120: "ValenToon's Heart 2"}
WainscotingNames = {1000: 'Painted',
 1010: 'Wood Panel',
 1020: 'Wood',
 1030: 'ValenToons',
 1040: 'Underwater'}
WindowViewNames = {10: 'Large Garden',
 20: 'Wild Garden',
 30: 'Greek Garden',
 40: 'Cityscape',
 50: 'Wild West',
 60: 'Under the Sea',
 70: 'Tropical Island',
 80: 'Starry Night',
 90: 'Tiki Pool',
 100: 'Frozen Frontier',
 110: 'Farm Country',
 120: 'Native Camp',
 130: 'Main Street'}
SpecialEventNames = {1: 'Generic Award',
 2: "Melville's Fishing Tournament",
 3: "Billy Budd's Fishing Tournament",
 4: 'Acorn Acres April Invitational',
 5: 'Acorn Acres C.U.P. Championship',
 6: 'Gift-Giving Extravaganza',
 7: "Top Toons New Year's Day Marathon",
 8: 'Perfect Trolley Games Weekend',
 9: 'Trolley Games Madness',
 10: 'Grand Prix Weekend',
 11: 'ToonTask Derby',
 12: 'Save a Building Marathon',
 13: 'Most Cogs Defeated',
 14: 'Most V.P.s Defeated',
 15: 'Operation Storm Sellbot Event',
 16: 'Most C.J.s Defeated',
 17: 'Operation Lawbots Lose Event',
 18: 'Operation Blast Bossbots Event',
 19: 'Operation Crash Cashbots Event'}
NewCatalogNotify = 'There are new items available to order at your phone!'
NewDeliveryNotify = 'A new delivery has just arrived at your mailbox!'
CatalogNotifyFirstCatalog = 'Your first cattlelog has arrived!  You may use this to order new items for yourself or for your house.'
CatalogNotifyNewCatalog = 'Your cattlelog #%s has arrived!  You can go to your phone to order items from this cattlelog.'
CatalogNotifyNewCatalogNewDelivery = 'A new delivery has arrived at your mailbox!  Also, your cattlelog #%s has arrived!'
CatalogNotifyNewDelivery = 'A new delivery has arrived at your mailbox!'
CatalogNotifyNewCatalogOldDelivery = 'Your cattlelog #%s has arrived, and there are still items waiting in your mailbox!'
CatalogNotifyOldDelivery = 'There are still items waiting in your mailbox for you to pick up!'
CatalogNotifyInstructions = 'Click the "Go home" button on the map page in your Shticker Book, then walk up to the phone inside your house.'
CatalogNewDeliveryButton = 'New\nDelivery!'
CatalogNewCatalogButton = 'New\nCattlelog'
CatalogSaleItem = 'Sale!  '
DistributedMailboxEmpty = 'Your mailbox is empty right now.  Come back here to look for deliveries after you place an order from your phone!'
DistributedMailboxWaiting = 'Your mailbox is empty right now, but the package you ordered is on its way.  Check back later!'
DistributedMailboxReady = 'Your ordeer has arrived!'
DistributedMailboxNotOwner = 'Sorry, this is not your mailbox.'
DistributedPhoneEmpty = "You can use any phone to order special items for you and your house.  New items will become available to order over time.\n\nYou don't have any items available to order right now, but check back later!"
DistributedPhoneNoHouse = 'You must have a house to use the catalog!'
Clarabelle = 'Clarabelle'
MailboxExitButton = 'Close Mailbox'
MailboxAcceptButton = 'Take this item'
MailBoxDiscard = 'Discard this item'
MailboxAcceptInvite = 'Accept this invite'
MailBoxRejectInvite = 'Reject this invite'
MailBoxDiscardVerify = 'Are you sure you want to Discard %s?'
MailBoxRejectVerify = 'Are you sure you want to Reject %s?'
MailboxOneItem = 'Your mailbox contains 1 item.'
MailboxNumberOfItems = 'Your mailbox contains %s items.'
MailboxGettingItem = 'Taking %s from mailbox.'
MailboxGiftTag = 'Gift From: %s'
MailboxGiftTagAnonymous = 'Anonymous'
MailboxItemNext = 'Next\nItem'
MailboxItemPrev = 'Previous\nItem'
MailboxDiscard = 'Discard'
MailboxReject = 'Reject'
MailboxLeave = 'Keep'
CatalogCurrency = 'beans'
CatalogHangUp = 'Hang Up'
CatalogNew = 'NEW'
CatalogBackorder = 'BACKORDER'
CatalogLoyalty = 'SPECIAL'
CatalogEmblem = 'EMBLEM'
CatalogPagePrefix = 'Page'
CatalogGreeting = "Hello! Thanks for calling Clarabelle's Cattlelog. Can I help you?"
CatalogGoodbyeList = ['Bye now!',
 'Call back soon!',
 'Thanks for calling!',
 'Ok, bye now!',
 'Bye!']
CatalogHelpText1 = 'Turn the page to see items for sale.'
CatalogSeriesLabel = 'Series %s'
CatalogGiftFor = 'Buy Gift for:'
CatalogGiftTo = 'To: %s'
CatalogGiftToggleOn = 'Stop Gifting'
CatalogGiftToggleOff = 'Buy Gifts'
CatalogGiftToggleWait = 'Trying!...'
CatalogGiftToggleNoAck = 'Unavailable'
CatalogPurchaseItemAvailable = 'Congratulations on your new purchase!  You can start using it right away.'
CatalogPurchaseGiftItemAvailable = 'Excellent!  %s can start using your gift right away.'
CatalogPurchaseItemOnOrder = 'Congratulations! Your purchase will be delivered to your mailbox soon.'
CatalogPurchaseGiftItemOnOrder = 'Excellent! Your gift to %s will be delivered to their mailbox.'
CatalogAnythingElse = 'Anything else I can get you today?'
CatalogPurchaseClosetFull = 'Your closet is full.  You may purchase this item anyway, but if you do you will need to delete something from your closet to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogPurchaseNoTrunk = 'In order to wear this item, you need to buy a trunk.\n\nDo you still want to purchase this item?'
CatalogPurchaseTrunkFull = 'Your trunk is full. If you purchase this item, you\xe2\x80\x99ll need to delete another item from your trunk to make more room.\n\nDo you still want to purchase this item?'
CatalogAcceptClosetFull = 'Your closet is full.  You must go inside and delete something from your closet to make room for this item before you can take it out of your mailbox.'
CatalogAcceptNoTrunk = "You don't have a trunk. You must buy a trunk before you can take this item out of your mailbox."
CatalogAcceptTrunkFull = 'Your trunk is full.  You must delete something from your trunk before you can take this item out of your mailbox.'
CatalogAcceptShirt = 'You are now wearing your new hat.  The hat you were wearing before has been moved to your trunk.'
CatalogAcceptShorts = 'You are now wearing your new shorts.  What you were wearing before has been moved to your closet.'
CatalogAcceptSkirt = 'You are now wearing your new skirt.  What you were wearing before has been moved to your closet.'
CatalogAcceptHat = 'You are now wearing your new hat.  The hat you were wearing before has been moved to your trunk.'
CatalogAcceptGlasses = 'You are now wearing your new glasses.  The glasses you were wearing before have been moved to your trunk.'
CatalogAcceptBackpack = 'You are now wearing your new backpack.  The backpack you were wearing before has been moved to your trunk.'
CatalogAcceptShoes = 'You are now wearing your new shoes.  The shoes you were wearing before have been moved to your trunk.'
CatalogAcceptPole = "You're now ready to go catch some bigger fish with your new pole!"
CatalogAcceptPoleUnneeded = 'You already have a better pole than this one!'
CatalogAcceptChat = 'You now have a new SpeedChat!'
CatalogAcceptEmote = 'You now have a new Emotion!'
CatalogAcceptBeans = 'You received some jelly beans!'
CatalogAcceptRATBeans = 'Your Toon recruit reward has arrived!'
CatalogAcceptPartyRefund = "Your party was never started. Here's your refund!"
CatalogAcceptNametag = 'Your new name tag has arrived!'
CatalogAcceptGarden = 'Your garden supplies have arrived!'
CatalogAcceptPet = 'You now have a new Pet Trick!'
CatalogPurchaseHouseFull = 'Your house is full.  You may purchase this item anyway, but if you do you will need to delete something from your house to make room for it when it arrives.\n\nDo you still want to purchase this item?'
CatalogAcceptHouseFull = 'Your house is full. You can not accept this item until you free up some room. Would you like to discard this item now?'
CatalogAcceptInAttic = 'Your new item is now in your attic.  You can put it in your house by going inside and clicking on the "Move Furniture" button.'
CatalogAcceptInAtticP = 'Your new items are now in your attic.  You can put them in your house by going inside and clicking on the "Move Furniture" button.'
CatalogPurchaseMailboxFull = "Your mailbox is full!  You can't purchase this item until you take some items out of your mailbox to make room."
CatalogPurchaseGiftMailboxFull = "%s's mailbox is full!  You can't purchase this item."
CatalogPurchaseOnOrderListFull = "You have too many items currently on order.  You can't order any more items until some of the ones you have already ordered arrive."
CatalogPurchaseGiftOnOrderListFull = '%s has too many items currently on order.'
CatalogPurchaseGeneralError = 'The item could not be purchased because of some internal game error: error code %s.'
CatalogPurchaseGiftGeneralError = 'The item could not be gifted to %(friend)s because of some internal game error: error code %(error)s.'
CatalogPurchaseGiftNotAGift = 'This item could not be sent to %s because it would be an unfair advantage.'
CatalogPurchaseGiftWillNotFit = "This item could not be sent to %s because it doesn't fit them."
CatalogPurchaseGiftLimitReached = "This item could not be sent to %s because they've already have it."
CatalogPurchaseGiftNotEnoughMoney = "This item could not be sent to %s because you can't afford it."
CatalogAcceptGeneralError = 'The item could not be removed from your mailbox because of some internal game error: error code %s.'
CatalogAcceptRoomError = "You don't have any place to put this. You'll have to get rid of something."
CatalogAcceptLimitError = "You already have as many of these as you can handle. You'll have to get rid of something."
CatalogAcceptFitError = "This won't fit you!"
CatalogAcceptInvalidError = 'This item has gone out of style!'
CatalogAcceptClosetError = 'You already have a bigger closet!'
MailboxOverflowButtonDicard = 'Discard'
MailboxOverflowButtonLeave = 'Leave'
HDMoveFurnitureButton = 'Move\nFurniture'
HDStopMoveFurnitureButton = 'Done\nMoving'
HDAtticPickerLabel = 'In the attic'
HDInRoomPickerLabel = 'In the room'
HDInTrashPickerLabel = 'In the trash'
HDDeletePickerLabel = 'Delete?'
HDInAtticLabel = 'Attic'
HDInRoomLabel = 'Room'
HDInTrashLabel = 'Trash'
HDToAtticLabel = 'Send\nto attic'
HDMoveLabel = 'Move'
HDRotateCWLabel = 'Rotate Right'
HDRotateCCWLabel = 'Rotate Left'
HDReturnVerify = 'Return this item to the attic?'
HDReturnFromTrashVerify = 'Return this item to the attic from the trash?'
HDDeleteItem = 'Click OK to send this item to the trash, or Cancel to keep it.'
HDNonDeletableItem = "You can't delete items of this type!"
HDNonDeletableBank = "You can't delete your bank!"
HDNonDeletableCloset = "You can't delete your wardrobe!"
HDNonDeletablePhone = "You can't delete your phone!"
HDNonDeletableTrunk = "You can't delete your trunk!"
HDNonDeletableNotOwner = "You can't delete %s's things!"
HDHouseFull = 'Your house is full.  You have to delete something else from your house or attic before you can return this item from the trash.'
HDHelpDict = {'DoneMoving': 'Finish room decorating.',
 'Attic': 'Show list of items in attic. The attic stores items that are not in your room.',
 'Room': 'Show list of items in room. Useful for finding lost items.',
 'Trash': 'Show items in trash. Oldest items are deleted after a while or when trash overflows.',
 'ZoomIn': 'Get a closer view of room.',
 'ZoomOut': 'Get a farther view of room.',
 'SendToAttic': 'Send the current furniture item to attic for storage.',
 'RotateLeft': 'Turn left.',
 'RotateRight': 'Turn right.',
 'DeleteEnter': 'Change to delete mode.',
 'DeleteExit': 'Exit delete mode.',
 'FurnitureItemPanelDelete': 'Send %s to trash.',
 'FurnitureItemPanelAttic': 'Place %s in room.',
 'FurnitureItemPanelRoom': 'Return %s to attic.',
 'FurnitureItemPanelTrash': 'Return %s to attic.'}
MessagePickerTitle = 'You have too many phrases. In order to purchase\n"%s"\n you must choose one to remove:'
MessagePickerCancel = lCancel
MessageConfirmDelete = 'Are you sure you want to remove "%s" from your SpeedChat menu?'
CatalogBuyText = 'Buy'
CatalogRentText = 'Rent'
CatalogGiftText = 'Gift'
CatalogOnOrderText = 'On Order'
CatalogPurchasedText = 'Already\nPurchased'
CatalogCurrent = 'Current'
CatalogGiftedText = 'Gifted\nTo You'
CatalogPurchasedGiftText = 'Already\nOwned'
CatalogMailboxFull = 'No Room'
CatalogNotAGift = 'Not a Gift'
CatalogNoFit = "Doesn't\nFit"
CatalogMembersOnly = 'Members\nOnly!'
CatalogSndOnText = 'Snd On'
CatalogSndOffText = 'Snd Off'
CatalogPurchasedMaxText = 'Already\nPurchased Max'
CatalogVerifyPurchase = 'Purchase %(item)s for %(price)s Jellybeans?'
CatalogVerifyPurchaseBeanSilverGold = 'Purchase %(item)s for %(price)s Jellybeans, %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanGold = 'Purchase %(item)s for %(price)s Jellybeans and %(gold)s gold emblems?'
CatalogVerifyPurchaseBeanSilver = 'Purchase %(item)s for %(price)s Jellybeans and %(silver)s silver emblems?'
CatalogVerifyPurchaseSilverGold = 'Purchase %(item)s for %(silver)s silver emblems and %(gold)s gold emblems?'
CatalogVerifyPurchaseSilver = 'Purchase %(item)s for %(silver)s silver emblems?'
CatalogVerifyPurchaseGold = 'Purchase %(item)s for %(gold)s gold emblems?'
CatalogVerifyRent = 'Rent %(item)s for %(price)s Jellybeans?'
CatalogVerifyGift = 'Purchase %(item)s for %(price)s Jellybeans as a gift for %(friend)s?'
CatalogOnlyOnePurchase = 'You may only have one of these items at a time.  If you purchase this one, it will replace %(old)s.\n\nAre you sure you want to purchase %(item)s for %(price)s Jellybeans?'
CatalogExitButtonText = 'Hang Up'
CatalogCurrentButtonText = 'To Current Items'
CatalogPastButtonText = 'To Past Items'
TutorialHQOfficerName = 'HQ Harry'
NPCToonNames = {20000: 'Tutorial Tom',
 998: 'Talkative Tyler',
 999: 'Toon Tailor',
 1000: lToonHQ,
 20001: Flippy,
 2001: Flippy,
 2002: 'Banker Bob',
 2003: 'Professor Pete',
 2004: 'Tammy',
 2005: 'Librarian Larry',
 2006: 'Clark',
 2011: 'Clara',
 2007: lHQOfficerM,
 2008: lHQOfficerM,
 2009: lHQOfficerF,
 2010: lHQOfficerF,
 2012: 'Freddy',
 2018: 'Duff..err..TIP Man',
 2013: 'Poppy',
 2014: 'Peppy',
 2015: 'Pappy',
 2016: 'Pumpkin',
 2017: 'Polly',
 2018: 'Doctor Surlee',
 2019: 'Doctor Dimm',
 2020: 'Professor Prepostera',
 2021: 'Yin',
 2022: 'Yang',
 2101: 'Dentist Daniel',
 2102: 'Sheriff Sherry',
 2103: 'Sneezy Kitty',
 2104: lHQOfficerM,
 2105: lHQOfficerM,
 2106: lHQOfficerF,
 2107: lHQOfficerF,
 2108: 'Canary Coalmine',
 2109: 'Sir Babbles A Lot',
 2110: 'Bill Board',
 2111: 'Dancing Diego',
 2112: 'Dr. Tom',
 2113: 'Rollo The Amazing',
 2114: 'Roz Berry',
 2115: 'Patty Papercut',
 2116: 'Bruiser McDougal',
 2117: 'Ma Putrid',
 2118: 'Jesse Jester',
 2119: 'Honey Haha',
 2120: 'Professor Binky',
 2121: 'Madam Chuckle',
 2122: 'Harry Ape',
 2123: 'Spamonia Biggles',
 2124: 'T.P. Rolle',
 2125: 'Lazy Hal',
 2126: 'Professor Guffaw',
 2127: 'Woody Nickel',
 2128: 'Loony Louis',
 2129: 'Frank Furter',
 2130: 'Joy Buzzer',
 2131: 'Feather Duster',
 2132: 'Daffy Don',
 2133: 'Dr. Euphoric',
 2134: 'Silent Simone',
 2135: 'Mary',
 2136: 'Sal Snicker',
 2137: 'Happy Heikyung',
 2138: 'Muldoon',
 2139: 'Dan Dribbles',
 2140: 'Billy',
 2201: 'Postmaster Pete',
 2202: 'Shirley U. Jest',
 2203: lHQOfficerM,
 2204: lHQOfficerM,
 2205: lHQOfficerF,
 2206: lHQOfficerF,
 2207: 'Will Wiseacre',
 2208: 'Sticky Lou',
 2209: 'Charlie Chortle',
 2210: 'Tee Hee',
 2211: 'Sally Spittake',
 2212: 'Weird Warren',
 2213: 'Lucy Tires',
 2214: 'Sam Stain',
 2215: 'Sid Seltzer',
 2216: 'Nona Seeya',
 2217: 'Sharky Jones',
 2218: 'Fanny Pages',
 2219: 'Chef Knucklehead',
 2220: 'Rick Rockhead',
 2221: 'Clovinia Cling',
 2222: 'Shorty Fuse',
 2223: 'Sasha Sidesplitter',
 2224: 'Smokey Joe',
 2225: 'Droopy',
 2226: 'Inky Ivon',
 2301: 'Dr. Pulyurleg',
 2302: 'Professor Wiggle',
 2303: 'Nurse Nancy',
 2304: lHQOfficerM,
 2305: lHQOfficerM,
 2306: lHQOfficerF,
 2307: lHQOfficerF,
 2308: 'Nancy Gas',
 2309: 'Big Bruce',
 2311: 'Franz Neckvein',
 2312: 'Dr. Sensitive',
 2313: 'Lucy Shirtspot',
 2314: 'Ned Slinger',
 2315: 'Chewy Morsel',
 2316: 'Cindy Sprinkles',
 2318: 'Tony Maroni',
 2319: 'Zippy',
 2320: 'Crunchy Alfredo',
 2321: 'Punchy',
 2322: 'Jester Chester',
 2323: 'Loopy Goopy Googlenerd',
 2401: 'Oily Oswald',
 2402: 'Louise Connection',
 2403: 'Wacky Wally',
 2404: 'Rancid Robert',
 2405: 'Limey',
 2406: 'Al Hare-ington',
 2407: "Good Ol' Honkin' Sally",
 2408: 'P.I. Multiply',
 2409: 'Bookworm Bork',
 2410: 'Professor Proton',
 2411: 'B.R. Bea',
 2412: 'Chef Foolery',
 2413: 'R.E. Versed',
 2414: 'Roy',
 2415: 'Pants On Fire',
 2416: 'Liar Liar',
 1001: 'Will',
 1002: 'Bill',
 1003: lHQOfficerM,
 1004: lHQOfficerF,
 1005: lHQOfficerM,
 1006: lHQOfficerF,
 1007: 'Longjohn Leroy',
 1008: 'Furball',
 1009: 'Barky',
 1010: 'Purr',
 1011: 'Bloop',
 1012: 'Pickles',
 1013: 'Patty',
 1101: 'Billy Budd',
 1102: 'Captain Carl',
 1103: 'Fishy Frank',
 1104: 'Doctor Squall',
 1105: 'Admiral Hook',
 1106: 'Mrs. Starch',
 1107: 'Cal Estenicks',
 1108: lHQOfficerM,
 1109: lHQOfficerF,
 1110: lHQOfficerM,
 1111: lHQOfficerF,
 1112: 'Gary Glubglub',
 1113: 'Lisa Luff',
 1114: 'Charlie Chum',
 1115: 'Sheila Squid, Atty',
 1116: 'Barnacle Bessie',
 1117: 'Captain Yucks',
 1118: 'Choppy McDougal',
 1121: 'Linda Landlubber',
 1122: 'Salty Stan',
 1123: 'Electra Eel',
 1124: 'Flappy Docksplinter',
 1125: 'Eileen Overboard',
 1126: 'Barney',
 1201: 'Barnacle Barbara',
 1202: 'Art',
 1203: 'Ahab',
 1204: 'Rocky Shores',
 1205: lHQOfficerM,
 1206: lHQOfficerF,
 1207: lHQOfficerM,
 1208: lHQOfficerF,
 1209: 'Professor Plank',
 1210: 'Gang Wei',
 1211: 'Wynn Bag',
 1212: 'Toby Tonguestinger',
 1213: 'Dante Dolphin',
 1214: 'Gusty Kate',
 1215: 'Dinah Down',
 1216: 'Rod Reel',
 1217: 'CC Weed',
 1218: 'Pacific Tim',
 1219: 'Brian Beachead',
 1220: 'Carla Canal',
 1221: 'Blisters McKee',
 1222: 'Shep Ahoy',
 1223: 'Sid Squid',
 1224: 'Emily Eel',
 1225: 'Bonzo Bilgepump',
 1226: 'Heave Ho',
 1227: 'Coral Reef',
 1228: 'Reed',
 1301: 'Alice',
 1302: 'Melville',
 1303: 'Claggart',
 1304: 'Svetlana',
 1305: lHQOfficerM,
 1306: lHQOfficerF,
 1307: lHQOfficerM,
 1308: lHQOfficerF,
 1309: 'Seafoam',
 1310: 'Ted Tackle',
 1311: 'Topsy Turvey',
 1312: 'Ethan Keel',
 1313: 'William Wake',
 1314: 'Rusty Ralph',
 1315: 'Doctor Drift',
 1316: 'Wilma Wobble',
 1317: 'Paula Pylon',
 1318: 'Captain Jack Harrow',
 1319: 'Davey Drydock',
 1320: 'Ted Calm',
 1321: 'Dinah Docker',
 1322: 'Whoopie Cushion',
 1323: 'Stinky Ned',
 1324: 'Pearl Diver',
 1325: 'Ned Setter',
 1326: 'Felicia Chips',
 1327: 'Cindy Splat',
 1328: 'Fred Flounder',
 1329: 'Shelly Seaweed',
 1330: 'Porter Hole',
 1331: 'Rudy Rudder',
 1332: 'Shane',
 1400: 'Edgar Allen Pole',
 1401: 'Sir C. Saw',
 1402: 'Helpful Hurley',
 1403: 'Chef Shea',
 1404: 'Professor Pearl',
 1405: 'Greggory Goggles',
 1406: 'N.D. Skye',
 1407: lHQOfficerM,
 1408: lHQOfficerM,
 1409: lHQOfficerF,
 1410: lHQOfficerF,
 1411: 'Crafty Clyde',
 1412: 'T. Shirley',
 1413: 'Eugene',
 1414: 'Captain Cheesy',
 1415: 'Smirky Bumberpop',
 1416: 'Chef Chip',
 1417: 'Postmaster Paul',
 1418: 'A.R. Ming',
 1419: 'Ree Pare',
 3001: 'Betty Freezes',
 3002: lHQOfficerM,
 3003: lHQOfficerF,
 3004: lHQOfficerM,
 3005: lHQOfficerM,
 3006: 'Lenny',
 3007: 'Penny',
 3008: 'Warren Bundles',
 3009: 'Frizzy',
 3010: 'Skip',
 3011: 'Dip',
 3012: 'Kipp',
 3013: 'Pete',
 3014: 'Penny',
 3101: 'Mr. Cow',
 3102: 'Auntie Freeze',
 3103: 'Fred',
 3104: 'Bonnie',
 3105: 'Frosty Freddy',
 3106: 'Gus Gooseburger',
 3107: 'Patty Passport',
 3108: 'Toboggan Ted',
 3109: 'Kate',
 3110: 'Chicken Boy',
 3111: 'Snooty Sinjin',
 3112: 'Lil Oldman',
 3113: 'Hysterical Harry',
 3114: 'Henry the Hazard',
 3115: lHQOfficerM,
 3116: lHQOfficerF,
 3117: lHQOfficerM,
 3118: lHQOfficerM,
 3119: 'Creepy Carl',
 3120: 'Mike Mittens',
 3121: 'Joe Shockit',
 3122: 'Lucy Luge',
 3123: 'Frank Lloyd Ice',
 3124: 'Lance Iceberg',
 3125: 'Colonel Crunchmouth',
 3126: 'Colestra Awl',
 3127: 'Ifalla Yufalla',
 3128: 'Sticky George',
 3129: 'Baker Bridget',
 3130: 'Sandy',
 3131: 'Lazy Lorenzo',
 3132: 'Ashy',
 3133: 'Dr. Friezeframe',
 3134: 'Lounge Lassard',
 3135: 'Soggy Nell',
 3136: 'Happy Sue',
 3137: 'Mr. Freeze',
 3138: 'Chef Bumblesoup',
 3139: 'Granny Icestockings',
 3140: 'Lucille',
 3201: 'Aunt Arctic',
 3202: 'Shakey',
 3203: 'Walt',
 3204: 'Dr. Ivanna Cee',
 3205: 'Bumpy Noggin',
 3206: 'Vidalia VaVoom',
 3207: 'Dr. Mumbleface',
 3208: 'Grumpy Phil',
 3209: 'Giggles McGhee',
 3210: 'Simian Sam',
 3211: 'Fanny Freezes',
 3212: 'Frosty Fred',
 3213: lHQOfficerM,
 3214: lHQOfficerF,
 3215: lHQOfficerM,
 3216: lHQOfficerM,
 3217: 'Sweaty Pete',
 3218: 'Blue Lou',
 3219: 'Tom Tandemfrost',
 3220: 'Mr. Sneeze',
 3221: 'Nelly Snow',
 3222: 'Mindy Windburn',
 3223: 'Chappy',
 3224: 'Freida Frostbite',
 3225: 'Blake Ice',
 3226: 'Santa Paws',
 3227: 'Solar Ray',
 3228: 'Wynne Chill',
 3229: 'Hernia Belt',
 3230: 'Balding Benjy',
 3231: 'Choppy',
 3232: 'Albert',
 3301: 'Paisley Patches',
 3302: 'Bjorn Bord',
 3303: 'Dr. Peepers',
 3304: 'Eddie the Yeti',
 3305: 'Mack Ramay',
 3306: 'Paula Behr',
 3307: 'Fredrica',
 3308: 'Donald Frump',
 3309: 'Bootsy',
 3310: 'Professor Flake',
 3311: 'Connie Ferris',
 3312: 'March Harry',
 3313: lHQOfficerM,
 3314: lHQOfficerF,
 3315: lHQOfficerM,
 3316: lHQOfficerF,
 3317: 'Kissy Krissy',
 3318: 'Johnny Cashmere',
 3319: 'Sam Stetson',
 3320: 'Fizzy Lizzy',
 3321: 'Pickaxe Paul',
 3322: 'Flue Lou',
 3323: 'Dallas Borealis',
 3324: 'Snaggletooth Stu',
 3325: 'Groovy Garland',
 3326: 'Blanche',
 3327: 'Chuck Roast',
 3328: 'Shady Sadie',
 3329: 'Treading Ed',
 3401: 'Xanon',
 3402: 'Olive',
 3403: 'Auntie Art',
 3404: 'Chilly',
 3405: 'Toony',
 3406: 'Nate Happening',
 3407: 'Ice Day',
 3408: 'Polar Brrr',
 3409: "Feelin' Frosty",
 3410: "North 'N South",
 3411: 'Gunther',
 3412: 'Dr. Buck',
 3413: 'Freezy Pete',
 3414: 'Dr. Nerve',
 3415: 'Cold Cuts',
 3416: 'Frost',
 4001: 'Molly Molloy',
 4002: lHQOfficerM,
 4003: lHQOfficerF,
 4004: lHQOfficerF,
 4005: lHQOfficerF,
 4006: 'Doe',
 4007: 'Ray',
 4008: 'Harmony',
 4009: 'Fanny',
 4010: 'Chris',
 4011: 'Neil',
 4012: 'Westin Girl',
 4013: 'Preston',
 4014: 'Penelope',
 4101: 'Tom',
 4102: 'Fifi',
 4103: 'Dr. Fret',
 4104: lHQOfficerM,
 4105: lHQOfficerF,
 4106: lHQOfficerF,
 4107: lHQOfficerF,
 4108: 'Cleff',
 4109: 'Carlos',
 4110: 'Metra Gnome',
 4111: 'Tom Hum',
 4112: 'Fa',
 4113: 'Madam Manners',
 4114: 'Offkey Eric',
 4115: 'Barbara Seville',
 4116: 'Piccolo',
 4117: 'Mandy Lynn',
 4118: 'Attendant Abe',
 4119: 'Moe Zart',
 4120: 'Viola Padding',
 4121: 'Gee Minor',
 4122: 'Minty Bass',
 4123: 'Lightning Ted',
 4124: 'Riff Raff',
 4125: 'Melody Wavers',
 4126: 'Mel Canto',
 4127: 'Happy Feet',
 4128: 'Luciano Scoop',
 4129: 'Tootie Twostep',
 4130: 'Metal Mike',
 4131: 'Abraham Armoire',
 4132: 'Lowdown Sally',
 4133: 'Scott Poplin',
 4134: 'Disco Dave',
 4135: 'Sluggo Songbird',
 4136: 'Patty Pause',
 4137: 'Tony Deff',
 4138: 'Cliff Cleff',
 4139: 'Harmony Swell',
 4140: 'Clumsy Ned',
 4141: 'Jed',
 4201: 'Tina',
 4202: 'Barry',
 4203: 'Lumber Jack',
 4204: lHQOfficerM,
 4205: lHQOfficerF,
 4206: lHQOfficerF,
 4207: lHQOfficerF,
 4208: 'Hedy',
 4209: 'Corny Canter',
 4211: 'Carl Concerto',
 4212: 'Detective Dirge',
 4213: 'Fran Foley',
 4214: 'Tina Toehooks',
 4215: 'Tim Tailgater',
 4216: 'Gummy Whistle',
 4217: 'Handsome Anton',
 4218: 'Wilma Wind',
 4219: 'Sid Sonata',
 4220: 'Curtis Finger',
 4221: 'Moe Madrigal',
 4222: 'John Doe',
 4223: 'Penny Prompter',
 4224: 'Jungle Jim',
 4225: 'Holly Hiss',
 4226: 'Thelma Throatreacher',
 4227: 'Quiet Francesca',
 4228: 'August Winds',
 4229: 'June Loon',
 4230: 'Julius Wheezer',
 4231: 'Steffi Squeezebox',
 4232: 'Hedly Hymn',
 4233: 'Charlie Carp',
 4234: 'Leed Guitar',
 4235: 'Larry',
 4301: 'Yuki',
 4302: 'Anna',
 4303: 'Leo',
 4304: lHQOfficerM,
 4305: lHQOfficerF,
 4306: lHQOfficerF,
 4307: lHQOfficerF,
 4308: 'Tabitha',
 4309: 'Marshall',
 4310: 'Martha Mopp',
 4311: 'Sea Shanty',
 4312: 'Moe Saj',
 4313: 'Dumb Dolph',
 4314: 'Dana Dander',
 4315: 'Karen Clockwork',
 4316: 'Tim Tango',
 4317: 'Stubby Toe',
 4318: 'Bob Marlin',
 4319: 'Rinky Dink',
 4320: 'Cammy Coda',
 4321: 'Luke Lute',
 4322: 'Randy Rythm',
 4323: 'Hanna Hogg',
 4324: 'Ellie',
 4325: 'Banker Bran',
 4326: 'Fran Fret',
 4327: 'Flim Flam',
 4328: 'Wagner',
 4329: 'Telly Prompter',
 4330: 'Quentin',
 4331: 'Mellow Costello',
 4332: 'Ziggy',
 4333: 'Harry',
 4334: 'Fast Freddie',
 4335: 'Walden',
 4400: 'Rocky',
 4401: 'Nurse Marie',
 4402: 'Tune A. Fish',
 4403: 'Leo Pulseman',
 4404: 'Remote',
 4405: 'Susan Soprano',
 4406: 'Kazoo Kid',
 4407: 'Annie Airhead',
 4408: 'Barry B.',
 4409: 'Peter Plunger',
 5001: lHQOfficerM,
 5002: lHQOfficerM,
 5003: lHQOfficerF,
 5004: lHQOfficerF,
 5005: 'Peaches',
 5006: 'Herb',
 5007: 'Bonnie Blossom',
 5008: 'Flora',
 5009: 'Bo Tanny',
 5010: 'Tom A. Dough',
 5011: 'Doug Wood',
 5012: 'Pierce',
 5013: 'Peggy',
 5101: 'Artie',
 5102: 'Susan',
 5103: 'Bud',
 5104: 'Flutterby',
 5105: 'Jack',
 5106: 'Barber Bjorn',
 5107: 'Postman Felipe',
 5108: 'Innkeeper Janet',
 5109: lHQOfficerM,
 5110: lHQOfficerM,
 5111: lHQOfficerF,
 5112: lHQOfficerF,
 5113: 'Dr. Spud',
 5114: 'Wilt',
 5115: 'Honey Dew',
 5116: 'Vegetable Vern',
 5117: 'Petal',
 5118: 'Pop Corn',
 5119: 'Barry Medly',
 5120: 'Gopher',
 5121: 'Paula Peapod',
 5122: 'Leif Pyle',
 5123: 'Diane Vine',
 5124: 'Soggy Bottom',
 5125: 'Sanjay Splash',
 5126: 'Madam Mum',
 5127: 'Polly Pollen',
 5128: 'Shoshanna Sap',
 5129: 'Sally',
 5201: 'Jake',
 5202: 'Cynthia',
 5203: 'Lisa',
 5204: 'Bert',
 5205: 'Dan D. Lion',
 5206: 'Vine Green',
 5207: 'Sofie Squirt',
 5208: 'Samantha Spade',
 5209: lHQOfficerM,
 5210: lHQOfficerM,
 5211: lHQOfficerF,
 5212: lHQOfficerF,
 5213: 'Big Galoot',
 5214: 'Itchie Bumps',
 5215: 'Tammy Tuber',
 5216: 'Stinky Jim',
 5217: 'Greg Greenethumb',
 5218: 'Rocky Raspberry',
 5219: 'Lars Bicep',
 5220: 'Lacy Underalls',
 5221: 'Pink Flamingo',
 5222: 'Whiny Wilma',
 5223: 'Wet Will',
 5224: 'Uncle Bumpkin',
 5225: 'Pamela Puddle',
 5226: 'Pete Moss',
 5227: 'Begonia Biddlesmore',
 5228: 'Digger Mudhands',
 5229: 'Lily',
 5301: lHQOfficerM,
 5302: lHQOfficerM,
 5303: lHQOfficerM,
 5304: lHQOfficerM,
 5305: 'Crystal',
 5306: 'S. Cargo',
 5307: 'Fun Gus',
 5308: 'Naggy Nell',
 5309: 'Ro Maine',
 5310: 'Timothy',
 5311: 'Judge McIntosh',
 5312: 'Eugene',
 5313: 'Coach Zucchini',
 5314: 'Aunt Hill',
 5315: 'Uncle Mud',
 5316: 'Uncle Spud',
 5317: 'Detective Lima',
 5318: 'Caesar',
 5319: 'Rose',
 5320: 'April',
 5321: 'Professor Ivy',
 5322: 'Rose',
 5400: 'Dr. Vine',
 5401: 'Gamby Lure',
 5402: 'Mr. Orange',
 5403: 'Flora',
 5404: 'Psy Kick',
 5405: 'Postmaster Parker',
 5406: 'I.C. Hue',
 5407: 'Officer Bork',
 5408: 'G. Arden',
 5409: 'Jackson Woods',
 5410: "Bunnysius O'Hare",
 5411: 'Law N. Mower',
 5412: 'Gus',
 5413: 'Blue Beary',
 5414: 'Speedy Herb',
 5415: 'Sunny Jim',
 5416: 'Cool Ray',
 5417: 'Bruce',
 5418: lHQOfficerF,
 5419: lHQOfficerM,
 5420: lHQOfficerM,
 5421: lHQOfficerF,
 6001: 'Peanut',
 6002: 'Chestnut',
 6003: 'Coconut',
 6004: 'Rick',
 6005: 'Rebecca',
 6006: 'Randy',
 6007: 'Rory',
 6008: 'Park',
 6009: 'Bark',
 6010: 'Tim',
 6011: 'Norman',
 6101: 'Ried Solocup',
 6102: 'Dr. Vert',
 6103: 'Chet Ter',
 6104: 'Tolkein A Hiking',
 6105: 'Blue Funk',
 6106: 'Coach GaZebo',
 6107: 'Leafy',
 6108: 'Maple Oak',
 6109: 'Tinothy',
 6110: 'Dennis Willow',
 6111: 'Humid Henry',
 6112: 'Sir Wippy Roastenbottom',
 6113: 'Forrest Fire',
 6114: 'Problematic Pete',
 6115: 'Jack',
 6201: 'Summer Wear',
 6202: 'Nathaniel Cawthorn',
 6203: 'Professor Pi',
 6204: 'Farmer Lyndon',
 6205: 'Dr, Love',
 6206: 'Tropical Tom',
 6207: 'Hazel Linden',
 6208: 'Postmaster Paul',
 6209: 'Spruce Hairtune',
 6210: 'Dr. Fields',
 6211: 'Elwood Elis',
 6212: 'Nat R.L. Remedy',
 6213: 'Colorful Monkey',
 6214: 'Charlie Doggenbottom',
 6215: 'Fifer Pig',
 6216: 'Builder Bob',
 6217: 'Fern Oakdale ',
 6218: 'Mirror Slav Lajcak',
 6301: 'Jake, King of Estates',
 6302: 'Madam Macadamia',
 6303: 'Duke Lancelot',
 6304: 'Rustle Oak',
 6305: 'Hanniball',
 6306: 'Judge Judybeans',
 6307: 'Covfefe',
 6308: 'Professor W. Willows',
 6309: 'Mother Wood',
 6310: "Randy O' Keel",
 6311: 'Nutty Ned',
 6312: 'Enraged Elizabeth',
 6313: 'Relaxed Roger',
 6314: 'Vincent Vacation',
 6315: 'Bees-In-My-Eyes Johnson',
 6316: 'Awkward Adam',
 6316: 'Awkward Adam',
 6317: 'Nutty Nathan',
 6318: 'Irritable Ivy',
 6401: 'Irritable Ivy',
 6402: 'Alvin',
 6403: 'Undeer Cover',
 6404: 'Under Read-It',
 6405: 'Father Fred',
 6406: 'Burt Embers',
 6407: 'Bannini',
 6408: 'Gregg Mendel',
 6409: 'Mechanic Mike',
 6410: 'Sir Tubby Cheezyfish',
 6411: 'Buzz',
 6412: 'Seargent Arms',
 6413: 'Walnut William',
 6414: 'Driver Dennis',
 6415: 'Stan',
 6416: 'T. P. Papre',
 6417: 'T. Spoon',
 6418: 'Sweet Sally',
 6419: 'Gopher Gold',
 6420: 'Smokey',
 8001: 'Graham Pree',
 8002: 'Ivona Race',
 8003: 'Anita Winn',
 8004: 'Phil Errup',
 9001: "Snoozin' Susan",
 9002: 'Sleeping Tom',
 9003: 'Drowsy Dennis',
 9004: lHQOfficerF,
 9005: lHQOfficerF,
 9006: lHQOfficerM,
 9007: lHQOfficerM,
 9008: 'Jill',
 9009: 'Phil',
 9010: 'Worn Out Waylon',
 9011: 'Freud',
 9012: 'Sarah Snuze',
 9013: 'Kat Knap',
 9014: 'R. V. Winkle',
 9015: 'Pebbles',
 9016: 'Pearl',
 9101: 'Ed',
 9102: 'Big Mama',
 9103: 'P.J.',
 9104: 'Sweet Slumber',
 9105: 'Professor Yawn',
 9106: 'Max',
 9107: 'Snuggles',
 9108: 'Winky Wilbur',
 9109: 'Dreamy Daphne',
 9110: 'Kathy Nip',
 9111: 'Powers Erge',
 9112: 'Lullaby Lou',
 9113: 'Jacques Clock',
 9114: 'Smudgy Mascara',
 9115: 'Babyface MacDougal',
 9116: 'Dances with Sheep',
 9117: 'Afta Hours',
 9118: 'Starry Knight',
 9119: 'Rocco',
 9120: 'Sarah Slumber',
 9121: 'Serena Shortsheeter',
 9122: 'Puffy Ayes',
 9123: 'Teddy Blair',
 9124: 'Nina Nitelight',
 9125: 'Dr. Bleary',
 9126: 'Wyda Wake',
 9127: 'Tabby Tucker',
 9128: "Hardy O'Toole",
 9129: 'Bertha Bedhog',
 9130: 'Charlie Chamberpot',
 9131: 'Susan Siesta',
 9132: lHQOfficerF,
 9133: lHQOfficerF,
 9134: lHQOfficerF,
 9135: lHQOfficerF,
 9136: 'Taylor',
 9201: 'Bernie Sandals',
 9202: 'Orville',
 9203: 'Nat',
 9204: 'Claire de Loon',
 9205: 'Zen Glen',
 9206: 'Skinny Ginny',
 9207: 'Jane Drain',
 9208: 'Drowsy Dave',
 9209: 'Dr. Floss',
 9210: 'Master Mike',
 9211: 'Dawn',
 9212: 'Moonbeam',
 9213: 'Rooster Rick',
 9214: 'Dr. Blinky',
 9215: 'Rip',
 9216: 'Cat',
 9217: 'Lawful Linda',
 9218: 'Waltzing Matilda',
 9219: 'The Countess',
 9220: 'Grumpy Gordon',
 9221: 'Zari',
 9222: 'Cowboy George',
 9223: 'Mark the Lark',
 9224: 'Sandy Sandman',
 9225: 'Fidgety Bridget',
 9226: 'William Teller',
 9227: 'Bed Head Ted',
 9228: 'Whispering Willow',
 9229: 'Rose Petals',
 9230: 'Tex',
 9231: 'Harry Hammock',
 9232: 'Honey Moon',
 9233: lHQOfficerM,
 9234: lHQOfficerM,
 9235: lHQOfficerM,
 9236: lHQOfficerM,
 9237: 'Jung',
 9301: 'Phil Bettur',
 9302: 'Emma Phatic',
 9303: 'GiggleMesh',
 9304: 'Anne Ville',
 9305: 'Bud Erfingerz',
 9306: 'J.S. Bark',
 9307: 'Bea Sharpe',
 9308: 'Otto Toon',
 9309: 'Al Capella',
 9310: 'Des Traction',
 9311: 'Dee Version',
 9312: 'Bo Nanapeel',
 7001: 'N. Prisoned',
 7002: 'R.E. Leaseme',
 7003: 'Lemmy Owte',
 7004: 'T. Rapped',
 7005: 'Little Helphere',
 7006: 'Gimmy Ahand',
 7007: 'Dewin Tymme',
 7008: 'Ima Cagedtoon',
 7009: 'Jimmy Thelock',
 91917: 'Prince Frizzy',
 91918: 'Squeaker',
 91919: 'Sir Tubby Cheezyfish',
 91920: 'Jakebooy',
 91925: 'Ask Alice'}
zone2TitleDict = {2513: ('Toon Hall', ''),
 2514: ('Toontown Bank', ''),
 2516: ('Toontown School House', ''),
 2518: ('Toontown Library', ''),
 2519: ('Gag Shop', ''),
 2520: (lToonHQ, ''),
 2521: ('Clothing Shop', ''),
 2522: ('Pet Shop', ''),
 2601: ('All Smiles Tooth Repair', ''),
 2602: ('', ''),
 2603: ('One-Liner Miners', ''),
 2604: ('Hogwash & Dry', ''),
 2605: ('Toontown Sign Factory', ''),
 2606: ('', ''),
 2607: ('Jumping Beans', ''),
 2610: ('Dr. Tom Foolery', ''),
 2611: ('', ''),
 2616: ("Weird Beard's Disguise Shop", ''),
 2617: ('Silly Stunts', ''),
 2618: ('All That Razz', ''),
 2621: ('Paper Airplanes', ''),
 2624: ('Happy Hooligans', ''),
 2625: ('House of Bad Pies', ''),
 2626: ("Jesse's Joke Repair", ''),
 2629: ("The Laughin' Place", ''),
 2632: ('Clown Class', ''),
 2633: ('Tee-Hee Tea Shop', ''),
 2638: ('Toontown Playhouse', ''),
 2639: ('Monkey Tricks', ''),
 2643: ('Canned Bottles', ''),
 2644: ('Impractical Jokes', ''),
 2649: ('All Fun and Games Shop', ''),
 2652: ('', ''),
 2653: ('', ''),
 2654: ('Laughing Lessons', ''),
 2655: ('Funny Money Savings & Loan', ''),
 2656: ('Used Clown Cars', ''),
 2657: ("Frank's Pranks", ''),
 2659: ('Joy Buzzers to the World', ''),
 2660: ('Tickle Machines', ''),
 2661: ('Daffy Taffy', ''),
 2662: ('Dr. I.M. Euphoric', ''),
 2663: ('Toontown Cinerama', ''),
 2664: ('The Merry Mimes', ''),
 2665: ("Mary's Go Around Travel Company", ''),
 2666: ('Laughing Gas Station', ''),
 2667: ('Happy Times', ''),
 2669: ("Muldoon's Maroon Balloons", ''),
 2670: ('Soup Forks', ''),
 2671: ('', ''),
 2701: ('', ''),
 2704: ('Movie Multiplex', ''),
 2705: ("Wiseacre's Noisemakers", ''),
 2708: ('Blue Glue', ''),
 2711: ('Toontown Post Office', ''),
 2712: ('Chortle Cafe', ''),
 2713: ('Laughter Hours Cafe', ''),
 2714: ('Kooky CinePlex', ''),
 2716: ('Soup and Crack Ups', ''),
 2717: ('Bottled Cans', ''),
 2720: ('Crack Up Auto Repair', ''),
 2725: ('', ''),
 2727: ('Seltzer Bottles and Cans', ''),
 2728: ('Vanishing Cream', ''),
 2729: ('14 Karat Goldfish', ''),
 2730: ('News for the Amused', ''),
 2731: ('', ''),
 2732: ('Spaghetti and Goofballs', ''),
 2733: ('Cast Iron Kites', ''),
 2734: ('Suction Cups and Saucers', ''),
 2735: ('The Kaboomery', ''),
 2739: ("Sidesplitter's Mending", ''),
 2740: ('Used Firecrackers', ''),
 2741: ("Loopy's Balls", ''),
 2742: ('', ''),
 2743: ('Ragtime Dry Cleaners', ''),
 2744: ('', ''),
 2747: ('Visible Ink', ''),
 2748: ('Jest for Laughs', ''),
 2801: ('Sofa Whoopee Cushions', ''),
 2802: ('Inflatable Wrecking Balls', ''),
 2803: ('The Karnival Kid', ''),
 2804: ('Dr. Pulyurleg, Chiropractor', ''),
 2805: ('', ''),
 2809: ('The Punch Line Gym', ''),
 2814: ('Toontown Theatre', ''),
 2818: ('The Flying Pie', ''),
 2821: ('', ''),
 2822: ('Rubber Chicken Sandwiches', ''),
 2823: ('Sundae Funnies Ice Cream', ''),
 2824: ('Punchline Movie Palace', ''),
 2829: ('Phony Baloney', ''),
 2830: ("Zippy's Zingers", ''),
 2831: ("Professor Wiggle's House of Giggles", ''),
 2832: ('', ''),
 2833: ('', ''),
 2834: ('Funny Bone Emergency Room', ''),
 2836: ('', ''),
 2837: ('Hardy Harr Seminars', ''),
 2839: ('Barely Palatable Pasta', ''),
 2841: ('', ''),
 2901: ('Gasonline', ''),
 2902: ('Wacky Way Wonderworld', ''),
 2903: ('Toon Mobile', ''),
 2904: ('Pies Are Squared', ''),
 2905: ('Wacky Way-ving Inflatable Arm Flailing Tube Man', ''),
 2907: ('A Gaggle of Gags', ''),
 2908: ('Dogs of Wisdom', ''),
 2909: ('The Circuit Breaker', ''),
 2910: ('', ''),
 2911: ('Recessed is in Session', ''),
 2914: ('Lying Birthday Cakes', ''),
 2915: ('No, the Building Beside Me is Telling the Truth', ''),
 2916: ('The Building Beside Me is Lying to you', ''),
 2917: ('The Mehvie Theatre', ''),
 2919: ("Roy's Kones", ''),
 2920: ('Topsy Turvey Tailors', ''),
 2922: ('Slip and Slide', ''),
 2923: ("Limey's Limes", ''),
 1506: ('Gag Shop', ''),
 1507: ('Toon Headquarters', ''),
 1508: ('Clothing Shop', ''),
 1510: ('', ''),
 1602: ('Used Life Preservers', ''),
 1604: ('Wet Suit Dry Cleaners', ''),
 1606: ("Hook's Clock Repair", ''),
 1608: ("Luff 'N Stuff", ''),
 1609: ('Every Little Bait', ''),
 1612: ('Dime & Quarterdeck Bank', ''),
 1613: ('Squid Pro Quo, Attorneys at Law', ''),
 1614: ('Trim the Nail Boutique', ''),
 1615: ("Yacht's All, Folks!", ''),
 1616: ("Blackbeard's Beauty Parlor", ''),
 1617: ('Out to See Optics', ''),
 1619: ('Disembark! Tree Surgeons', ''),
 1620: ('From Fore to Aft', ''),
 1621: ('Poop Deck Gym', ''),
 1622: ('Bait and Switches Electrical Shop', ''),
 1624: ('Soles Repaired While U Wait', ''),
 1626: ('Salmon Chanted Evening Formal Wear', ''),
 1627: ("Billy Budd's Big Bargain Binnacle Barn", ''),
 1628: ('Piano Tuna', ''),
 1629: ('', ''),
 1701: ('Buoys and Gulls Nursery School', ''),
 1703: ('Wok the Plank Chinese Food', ''),
 1705: ('Sails for Sale', ''),
 1706: ('Peanut Butter and Jellyfish', ''),
 1707: ('Gifts With a Porpoise', ''),
 1709: ('Windjammers and Jellies', ''),
 1710: ('Barnacle Bargains', ''),
 1711: ('Deep Sea Diner', ''),
 1712: ('Able-Bodied Gym', ''),
 1713: ("Art's Smart Chart Mart", ''),
 1714: ("Reel 'Em Inn", ''),
 1716: ('Mermaid Swimwear', ''),
 1717: ('Be More Pacific Ocean Notions', ''),
 1718: ('Run Aground Taxi Service', ''),
 1719: ("Duck's Back Water Company", ''),
 1720: ('The Reel Deal', ''),
 1721: ('All For Nautical', ''),
 1723: ("Squid's Seaweed", ''),
 1724: ("That's  a Moray!", ''),
 1725: ("Ahab's Prefab Sea Crab Center", ''),
 1726: ('Root Beer Afloats', ''),
 1727: ('This Oar That', ''),
 1728: ('Good Luck Horseshoe Crabs', ''),
 1729: ('', ''),
 1802: ('Nautical But Nice', ''),
 1804: ('Mussel Beach Gymnasium', ''),
 1805: ('Tackle Box Lunches', ''),
 1806: ('Cap Size Hat Store', ''),
 1807: ('Keel Deals', ''),
 1808: ('Knots So Fast', ''),
 1809: ('Rusty Buckets', ''),
 1810: ('Anchor Management', ''),
 1811: ("What's Canoe With You?", ''),
 1813: ('Pier Pressure Plumbing', ''),
 1814: ('The Yo Ho Stop and Go', ''),
 1815: ("What's Up, Dock?", ''),
 1818: ('Seven Seas Cafe', ''),
 1819: ("Docker's Diner", ''),
 1820: ('Hook, Line, and Sinker Prank Shop', ''),
 1821: ("King Neptoon's Cannery", ''),
 1823: ('The Clam Bake Diner', ''),
 1824: ('Dog Paddles', ''),
 1825: ('Wholly Mackerel! Fish Market', ''),
 1826: ("Claggart's Clever Clovis Closet", ''),
 1828: ("Alice's Ballast Palace", ''),
 1829: ('Seagull Statue Store', ''),
 1830: ('Lost and Flounder', ''),
 1831: ('Kelp Around the House', ''),
 1832: ("Melville's Massive Mizzenmast Mart", ''),
 1833: ('This Transom Man Custom Tailored Suits', ''),
 1834: ('Rudderly Ridiculous!', ''),
 1835: ('', ''),
 1903: ("Poetic Fishing Rods", ''),
 1904: ('Seaside Seasaws', ''),
 1905: ('I See Seafood', ''),
 1906: ('School of Fish Tutoring', ''),
 1908: ('Be Pacific! Customer Support', ''),
 1909: ('Goggle Defogers', ''),
 1910: ('Island, You Land! Airplanes', ''),
 1911: ('Seacastle Contractors', ''),
 1912: ('Manatee Shirts', ''),
 1913: ('Burger King Crabs', ''),
 1914: ("Sailor Don't Sail! Boating Equipment", ''),
 1915: ("Salty Smirky's Seriously Salty Seafood Shop", ''),
 1922: (lToonHQ, ''),
 1924: ("Fish and Chips on Ships", ''),
 1925: ('Pelican Package Company', ''),
 1926: ('Sad Vacant Building', ''),
 1927: ('Swordfish Armor and Weaponry', ''),
 1929: ('Flounder and Sink Ship Repair', ''),
 4503: ('Gag Shop', ''),
 4504: ('Toon Headquarters', ''),
 4506: ('Clothing Shop', ''),
 4508: ('', ''),
 4603: ("Tom-Tom's Drums", ''),
 4604: ('In Four-Four Time', ''),
 4605: ("Fifi's Fiddles", ''),
 4606: ('Casa De Castanets', ''),
 4607: ('Catchy Toon Apparel', ''),
 4609: ('Do, Rae, Me Piano Keys', ''),
 4610: ('Please Refrain', ''),
 4611: ('Tuning Forks and Spoons', ''),
 4612: ("Dr. Fret's Dentistry", ''),
 4614: ('Shave and a Haircut for a Song', ''),
 4615: ("Piccolo's Pizza", ''),
 4617: ('Happy Mandolins', ''),
 4618: ('Rests Rooms', ''),
 4619: ('More Scores', ''),
 4622: ('Chin Rest Pillows', ''),
 4623: ('Flats Sharpened', ''),
 4625: ('Tuba Toothpaste', ''),
 4626: ('Notations', ''),
 4628: ('Accidental Insurance', ''),
 4629: ("Riff's Paper Plates", ''),
 4630: ('Music Is Our Forte', ''),
 4631: ('Canto Help You', ''),
 4632: ('Dance Around the Clock Shop', ''),
 4635: ('Tenor Times', ''),
 4637: ('For Good Measure', ''),
 4638: ('Hard Rock Shop', ''),
 4639: ('Four Score Antiques', ''),
 4641: ('Blues News', ''),
 4642: ('Ragtime Dry Cleaners', ''),
 4645: ('Club 88', ''),
 4646: ('', ''),
 4648: ('Carry a Toon Movers', ''),
 4649: ('', ''),
 4652: ('Full Stop Shop', ''),
 4653: ('', ''),
 4654: ('Pitch Perfect Roofing', ''),
 4655: ("The Treble Chef's Cooking School", ''),
 4656: ('', ''),
 4657: ('Barbershop Quartet', ''),
 4658: ('Plummeting Pianos', ''),
 4659: ('', ''),
 4701: ('The Schmaltzy Waltz School of Dance', ''),
 4702: ('Timbre! Equipment for the Singing Lumberjack', ''),
 4703: ('I Can Handel It!', ''),
 4704: ("Tina's Concertina Concerts", ''),
 4705: ('Zither Here Nor There', ''),
 4707: ("Doppler's Sound Effects Studio", ''),
 4709: ('On Ballet! Climbing Supplies', ''),
 4710: ('Hurry Up, Slow Polka! School of Driving', ''),
 4712: ('C-Flat Tire Repair', ''),
 4713: ('B-Sharp Fine Menswear', ''),
 4716: ('Four-Part Harmonicas', ''),
 4717: ('Sonata Your Fault! Discount Auto Insurance', ''),
 4718: ('Chopin Blocks and Other Kitchen Supplies', ''),
 4719: ('Madrigal Motor Homes', ''),
 4720: ('Name That Toon', ''),
 4722: ('Overture Understudies', ''),
 4723: ('Haydn Go Seek Playground Supplies', ''),
 4724: ('White Noise for Girls and Boys', ''),
 4725: ('The Baritone Barber', ''),
 4727: ('Vocal Chords Braided', ''),
 4728: ("Sing Solo We Can't Hear You", ''),
 4729: ('Double Reed Bookstore', ''),
 4730: ('Lousy Lyrics', ''),
 4731: ('Toon Tunes', ''),
 4732: ('Etude Brute? Theatre Company', ''),
 4733: ('', ''),
 4734: ('', ''),
 4735: ('Accordions, If You Want In, Just Bellow!', ''),
 4736: ('Her and Hymn Wedding Planners', ''),
 4737: ('Harp Tarps', ''),
 4738: ('Canticle Your Fancy Gift Shop', ''),
 4739: ('', ''),
 4801: ("Marshall's Stacks", ''),
 4803: ('What a Mezzo! Maid Service', ''),
 4804: ('Mixolydian Scales', ''),
 4807: ('Relax the Bach', ''),
 4809: ("I Can't Understanza!", ''),
 4812: ('', ''),
 4817: ('The Ternary Pet Shop', ''),
 4819: ("Yuki's Ukeleles", ''),
 4820: ('', ''),
 4821: ("Anna's Cruises", ''),
 4827: ('Common Time Watches', ''),
 4828: ("Schumann's Shoes for Men", ''),
 4829: ("Pachelbel's Canonballs", ''),
 4835: ('Ursatz for Kool Katz', ''),
 4836: ('Reggae Regalia', ''),
 4838: ('Kazoology School of Music', ''),
 4840: ('Coda Pop Musical Beverages', ''),
 4841: ('Lyre, Lyre, Pants on Fire!', ''),
 4842: ('The Syncopation Corporation', ''),
 4843: ('', ''),
 4844: ('Con Moto Cycles', ''),
 4845: ("Ellie's Elegant Elegies", ''),
 4848: ('Lotsa Lute Savings & Loan', ''),
 4849: ('', ''),
 4850: ('The Borrowed Chord Pawn Shop', ''),
 4852: ('Flowery Flute Fleeces', ''),
 4853: ("Leo's Fenders", ''),
 4854: ("Wagner's Vocational Violin Videos", ''),
 4855: ('The Teli-Caster Network', ''),
 4856: ('', ''),
 4862: ("Quentin's Quintessen\x03tial Quadrilles", ''),
 4867: ("Mr. Costello's Yellow Cellos", ''),
 4868: ('', ''),
 4870: ("Ziggy's Zoo of Zigeuner\x03musik", ''),
 4871: ("Harry's House of Harmonious Humbuckers", ''),
 4872: ("Fast Freddie's Fretless Fingerboards", ''),
 4873: ('', ''),
 4903: ("Rock 'N'Roll Geologists", ''),
 4905: ('Pipe Organs Medical Facilities', ''),
 4906: ("Remote's Notes", ''),
 4907: ('Bass Fishing And Tuning', ''),
 4908: ('Soprano Street Pianos', ''),
 4909: ('Leo Pulseman', ''),
 4910: ('Bagpipe Plumbing Agency', ''),
 4911: ('You On Kazoo', ''),
 4912: ('Bee Flat Exterminators', ''),
 4913: ('The Air Horn Refillery', ''),
 5501: ('Gag Shop', ''),
 5502: (lToonHQ, ''),
 5503: ('Clothing Shop', ''),
 5505: ('', ''),
 5601: ('Eye of the Potato Optometry', ''),
 5602: ("Artie Choke's Neckties", ''),
 5603: ('Lettuce Alone', ''),
 5604: ('Cantaloupe Bridal Shop', ''),
 5605: ('Vege-tables and Chairs', ''),
 5606: ('Petals', ''),
 5607: ('Compost Office', ''),
 5608: ('Mom and Pop Corn', ''),
 5609: ('Berried Treasure', ''),
 5610: ("Black-eyed Susan's Boxing Lessons", ''),
 5611: ("Gopher's Gags", ''),
 5613: ('Crop Top Barbers', ''),
 5615: ("Bud's Bird Seed", ''),
 5616: ('Dew Drop Inn', ''),
 5617: ("Flutterby's Butterflies", ''),
 5618: ("Peas and Q's", ''),
 5619: ("Jack's Beanstalks", ''),
 5620: ('Rake It Inn', ''),
 5621: ('Grape Expectations', ''),
 5622: ('Petal Pusher Bicycles', ''),
 5623: ('Bubble Bird Baths', ''),
 5624: ("Mum's the Word", ''),
 5625: ('Leaf It Bees', ''),
 5626: ('Pine Needle Crafts', ''),
 5627: ('', ''),
 5701: ('From Start to Spinach', ''),
 5702: ("Jake's Rakes", ''),
 5703: ("Photo Cynthia's Camera Shop", ''),
 5704: ('Lisa Lemon Used Cars', ''),
 5705: ('Poison Oak Furniture', ''),
 5706: ('14 Carrot Jewelers', ''),
 5707: ('Musical Fruit', ''),
 5708: ("We'd Be Gone Travel Agency", ''),
 5709: ('Astroturf Mowers', ''),
 5710: ('Tuft Guy Gym', ''),
 5711: ('Garden Hosiery', ''),
 5712: ('Silly Statues', ''),
 5713: ('Trowels and Tribulations', ''),
 5714: ('Spring Rain Seltzer Bottles', ''),
 5715: ('Hayseed News', ''),
 5716: ('Take It or Leaf It Pawn Shop', ''),
 5717: ('The Squirting Flower', ''),
 5718: ('The Dandy Lion Exotic Pets', ''),
 5719: ('Trellis the Truth! Private Investi\x03gators', ''),
 5720: ('Vine and Dandy Menswear', ''),
 5721: ('Root 66 Diner', ''),
 5725: ('Barley, Hops, and Malt Shop', ''),
 5726: ("Bert's Dirt", ''),
 5727: ('Gopher Broke Savings & Loan', ''),
 5728: ('', ''),
 5802: (lToonHQ, ''),
 5804: ('Just Vase It', ''),
 5805: ('Snail Mail', ''),
 5809: ('Fungi Clown School', ''),
 5810: ('Honeydew This', ''),
 5811: ('Lettuce Inn', ''),
 5815: ('Grass Roots', ''),
 5817: ('Apples and Oranges', ''),
 5819: ('Green Bean Jeans', ''),
 5821: ('Squash and Stretch Gym', ''),
 5826: ('Ant Farming Supplies', ''),
 5827: ('Dirt. Cheap.', ''),
 5828: ('Couch Potato Furniture', ''),
 5830: ('Spill the Beans', ''),
 5833: ('The Salad Bar', ''),
 5835: ('Flower Bed and Breakfast', ''),
 5836: ("April's Showers and Tubs", ''),
 5837: ('School of Vine Arts', ''),
 5903: ("I'm Feeling Vine! Chiropractors", ''),
 5904: ('Hedge Your Bets!', ''),
 5909: ("Orange's Door Hinges", ''),
 5910: ("Gus' Fungus Funhouse", ''),
 5911: ("Flora's Flowers", ''),
 5912: ("Palm Tree Fortunes", ''),
 5914: ("Rainbow Sightseeings", ''),
 5915: ('Seed and Send Post Office', ''),
 5917: ('Garden Patrol', ''),
 5919: ("Garden's Awaiting", ''),
 5920: ("Campfire Firewood", ''),
 5921: ("O'Hare Air", ''),
 5922: ('Mow Jellybeans, Mow Problems', ''),
 5923: ('A Bushel Of Berries Fruit Shop', ''),
 5924: ('Hybrid Karts and Plants', ''),
 5926: ('Solar Powered Gardens', ''),
 5927: ("Cool Ray's Rad-ish Makeovers", ''),
 5929: (lToonHQ, ''),
 9501: ('Lullaby Library', ''),
 9503: ('The Snooze Bar', ''),
 9504: ('Gag Shop', ''),
 9505: (lToonHQ, ''),
 9506: ('Clothing Shop', ''),
 9508: ('', ''),
 6503: ('Clothing Shop', ''),
 6505: ('Gag Shop', ''),
 6506: ('', ''),
 6508: (lToonHQ, ''),
 6603: ('Wild Animals Party Supplies', ''),
 6604: ('Evergreen? Greening Rehabilitation', ''),
 6605: ('Cheese and Hammock', ''),
 6606: ('Hiking, Biking, and Sightseeing', ''),
 6607: ("The Skunk's Funk", ''),
 6608: ('Hut Hut Hike', ''),
 6611: ('Bark! Pet Tree Training', ''),
 6613: ('Doors for the Outdoors', ''),
 6614: ('Fine Woods and Canned Goods', ''),
 6616: ('Tents for Rent', ''),
 6618: ("Humid Henry's Humming Humidifiers", ''),
 6619: ('Marshmallows Extra Burnt', ''),
 6620: ('Firefly Firefighters', ''),
 6621: ("I'm Stumped! Problem Solvers", ''),
 6622: ('Acorn on the Cob', ''),
 6701: ('Spruce Up Tuxedos and Gowns', ''),
 6704: ('Rooster Alarm Clocks', ''),
 6705: ('Sine and Cosine Tanning Supplies', ''),
 6706: ('Acorn Fields Farming Supplies', ''),
 6707: ('Tree Hugging Dating Service', ''),
 6708: ('Pecan Colada', ''),
 6709: ('Cedar Sightseers', ''),
 6710: ('Acrescent the Mail', ''),
 6711: ('Pecan You Surveilence Systems', ''),
 6712: ('Acre for Sickness Medical Center', ''),
 6713: ('Tree Rings Jewelery', ''),
 6714: ('Woodside Pharamacy', ''),
 6715: ('Antlers for Monkeys and Deer Alike!', ''),
 6716: ("I've Gone Chestnuts! Therapy", ''),
 6717: ("Three Lil' Pigs Straw Brick and Wood", ''),
 6718: ('Walnut Built Yet Home Construction', ''),
 6719: ('Cypress and Clean Dry', ''),
 6720: ('Hiberunited Nations', ''),
 6816: ('Cashew! Tissue Company', ''),
 6817: ('Deer and Doe Construction Co.', ''),
 6818: ('Acorns for Acres', ''),
 6819: ('Elementree Savings and Loan', ''),
 6821: ('Golf Balls Fore Sale', ''),
 6823: ("Willow's Weeping Wood Emporium", ''),
 6824: ('Childwood Daycare', ''),
 6825: ('Rowan a Boat Shipyard', ''),
 6826: ('The Nuthouse', ''),
 6827: ('WHAT THE SHELL?!?', ''),
 6828: ('What a Releaf! Day Spa', ''),
 6829: ('Cashew Later!', ''),
 6831: ('Real Fake Outdoors', ''),
 6832: ("Tree's a Crowd", ''),
 6833: ('Go Nuts!', ''),
 6834: ('Wood You Not?', ''),
 6835: ("Covfefe's Coffee Shop", ''),
 6836: ('Lawn and Order', ''),
 6901: ('Did Nut See That Coming', ''),
 6902: ('Chipmunks with Funk', ''),
 6903: ('Undeer Cover Investigators', ''),
 6904: ('Hivemind', ''),
 6905: ("Chip off the ol' Munk", ''),
 6906: ('Burn Tree-tment Center', ''),
 6907: ("Bannini's Paninis", ''),
 6908: ('Munks', ''),
 6909: ("Nuts n' Bolts", ''),
 6910: ('Cheezy Fish Bites', ''),
 6911: ("Buzz's Beekeeping", ''),
 6913: ('Bomb-shell Heavy Artillery', ''),
 6914: ('Toons in a Nutshell', ''),
 6915: ('Driving Me Nuts!', ''),
 6916: ('Fine Pines', ''),
 6917: ('Nature Calls! Toilet-trees', ''),
 6918: ('Wooden Spoons for Half of a Dubloon!', ''),
 6919: ('Leaf it, Bee!', ''),
 6920: ('Burrow Bikes', ''),
 6921: ("Smokey's Smoking Rehab", ''),
 9601: ('Snuggle Inn', ''),
 9602: ('Forty Winks for the Price of Twenty', ''),
 9604: ("Ed's Red Bed Spreads", ''),
 9605: ('Cloud Nine Design', ''),
 9607: ("Big Mama's Bahama Pajamas", ''),
 9608: ('Cat Nip for Cat Naps', ''),
 9609: ('Deep Sleep for Cheap', ''),
 9613: ('Clock Cleaners', ''),
 9616: ('Lights Out Electric Co.', ''),
 9617: ('Crib Notes - Music to Sleep By', ''),
 9619: ('Relax to the Max', ''),
 9620: ("PJ's Taxi Service", ''),
 9622: ('Sleepy Time Pieces', ''),
 9625: ('Curl Up Beauty Parlor', ''),
 9626: ('Bed Time Stories', ''),
 9627: ('The Sleepy Teepee', ''),
 9628: ('Call It a Day Calendars', ''),
 9629: ('Silver Lining Jewelers', ''),
 9630: ('Rock to Sleep Quarry', ''),
 9631: ('Down Time Watch Repair', ''),
 9633: ('The Dreamland Screening Room', ''),
 9634: ('Mind Over Mattress', ''),
 9636: ('Insomniac Insurance', ''),
 9639: ('House of Hibernation', ''),
 9640: ('Nightstand Furniture Company', ''),
 9642: ('Sawing Wood Slumber Lumber', ''),
 9643: ('Shut-Eye Optometry', ''),
 9644: ('Pillow Fights Nightly', ''),
 9645: ('The All Tucked Inn', ''),
 9647: ('Make Your Bed! Hardware Store', ''),
 9649: ('Snore or Less', ''),
 9650: ('Crack of Dawn Repairs', ''),
 9651: ('For Richer or Snorer', ''),
 9652: ('', ''),
 9703: ('Fly By Night Travel Agency', ''),
 9704: ('Night Owl Pet Shop', ''),
 9705: ('Asleep At The Wheel Car Repair', ''),
 9706: ('Tooth Fairy Dentistry', ''),
 9707: ("Dawn's Yawn & Garden Center", ''),
 9708: ('Bed Of Roses Florist', ''),
 9709: ('Pipe Dream Plumbers', ''),
 9710: ('REM Optometry', ''),
 9711: ('Wake-Up Call Phone Company', ''),
 9712: ("Counting Sheep - So You Don't Have To!", ''),
 9713: ('Wynken, Blynken & Nod, Attorneys at Law', ''),
 9714: ('Dreamboat Marine Supply', ''),
 9715: ('First Security Blanket Bank', ''),
 9716: ('Wet Blanket Party Planners', ''),
 9717: ("Baker's Dozin' Doughnuts", ''),
 9718: ("Sandman's Sandwiches", ''),
 9719: ('Armadillo Pillow Company', ''),
 9720: ('Talking In Your Sleep Voice Training', ''),
 9721: ('Snug As A Bug Rug Dealer', ''),
 9722: ('Dream On Talent Agency', ''),
 9725: ("Cat's Pajamas", ''),
 9727: ('You Snooze, You Lose', ''),
 9736: ('Dream Jobs Employment Agency', ''),
 9737: ("Waltzing Matilda's Dance School", ''),
 9738: ('House of Zzzzzs', ''),
 9740: ('Hit The Sack Fencing School', ''),
 9741: ("Don't Let The Bed Bugs Bite Exterminators", ''),
 9744: ("Rip Van Winkle's Wrinkle Cream", ''),
 9752: ('Midnight Oil & Gas Company', ''),
 9753: ("Moonbeam's Ice Creams", ''),
 9754: ('Sleepless in the Saddle All Night Pony Rides', ''),
 9755: ('Bedknobs & Broomsticks Movie House', ''),
 9756: ('', ''),
 9759: ('Sleeping Beauty Parlor', ''),
 3507: ('Gag Shop', ''),
 3508: (lToonHQ, ''),
 3509: ('Clothing Shop', ''),
 3511: ('', ''),
 3601: ('Northern Lights Electric Company', ''),
 3602: ("Nor'easter Bonnets", ''),
 3605: ('', ''),
 3607: ('The Blizzard Wizard', ''),
 3608: ('Nothing to Luge', ''),
 3610: ("Mike's Massive Mukluk Mart", ''),
 3611: ("Mr. Cow's Snow Plows", ''),
 3612: ('Igloo Design', ''),
 3613: ('Ice Cycle Bikes', ''),
 3614: ('Snowflakes Cereal Company', ''),
 3615: ('Fried Baked Alaskas', ''),
 3617: ('Cold Air Balloon Rides', ''),
 3618: ('Snow Big Deal! Crisis Management', ''),
 3620: ('Skiing Clinic', ''),
 3621: ('The Melting Ice Cream Bar', ''),
 3622: ('', ''),
 3623: ('The Mostly Toasty Bread Company', ''),
 3624: ('Subzero Sandwich Shop', ''),
 3625: ("Auntie Freeze's Radiator Supply", ''),
 3627: ('St. Bernard Kennel Club', ''),
 3629: ('Pea Soup Cafe', ''),
 3630: ('Icy London, Icy France Travel Agency', ''),
 3634: ('Easy Chair Lifts', ''),
 3635: ('Used Firewood', ''),
 3636: ('Affordable Goosebumps', ''),
 3637: ("Kate's Skates", ''),
 3638: ('Toboggan or Not Toboggan', ''),
 3641: ("Fred's Red Sled Beds", ''),
 3642: ('Eye of the Storm Optics', ''),
 3643: ('Snowball Hall', ''),
 3644: ('Melted Ice Cubes', ''),
 3647: ('The Sanguine Penguin Tuxedo Shop', ''),
 3648: ('Instant Ice', ''),
 3649: ('Hambrrrgers', ''),
 3650: ('Antarctic Antiques', ''),
 3651: ("Frosty Freddy's Frozen Frankfurters", ''),
 3653: ('Ice House Jewelry', ''),
 3654: ('', ''),
 3702: ('Winter Storage', ''),
 3703: ('', ''),
 3705: ('Icicles Built for Two', ''),
 3706: ("Shiverin' Shakes Malt Shop", ''),
 3707: ('Snowplace Like Home', ''),
 3708: ("Pluto's Place", ''),
 3710: ('Dropping Degrees Diner', ''),
 3711: ('', ''),
 3712: ('Go With the Floe', ''),
 3713: ('Chattering Teeth, Subzero Dentist', ''),
 3715: ("Aunt Arctic's Soup Shop", ''),
 3716: ('Road Salt and Pepper', ''),
 3717: ('Juneau What I Mean?', ''),
 3718: ('Designer Inner Tubes', ''),
 3719: ('Ice Cube on a Stick', ''),
 3721: ("Noggin's Toboggan Bargains", ''),
 3722: ('Snow Bunny Ski Shop', ''),
 3723: ("Shakey's Snow Globes", ''),
 3724: ('The Chattering Chronicle', ''),
 3725: ('You Sleigh Me', ''),
 3726: ('Solar Powered Blankets', ''),
 3728: ('Lowbrow Snowplows', ''),
 3729: ('', ''),
 3730: ('Snowmen Bought & Sold', ''),
 3731: ('Portable Fireplaces', ''),
 3732: ('The Frozen Nose', ''),
 3734: ('Icy Fine, Do You? Optometry', ''),
 3735: ('Polar Ice Caps', ''),
 3736: ('Diced Ice at a Nice Price', ''),
 3737: ('Downhill Diner', ''),
 3738: ("Heat-Get It While It's Hot", ''),
 3739: ('', ''),
 3801: ('Toon HQ', ''),
 3806: ('Alpine Chow Line', ''),
 3807: ('Used Groundhog Shadows', ''),
 3808: ('The Sweater Lodge', ''),
 3809: ('Ice Saw It Too', ''),
 3810: ('A Better Built Quilt', ''),
 3811: ('Your Snow Angel', ''),
 3812: ('Mittens for Kittens', ''),
 3813: ("Snowshoes You Can't Refuse", ''),
 3814: ('Malt in Your Mouth Soda Fountain', ''),
 3815: ('The Toupee Chalet', ''),
 3816: ('Just So Mistletoe', ''),
 3817: ('Winter Wonderland Walking Club', ''),
 3818: ('The Shovel Hovel', ''),
 3819: ('Clean Sweep Chimney Service', ''),
 3820: ('Snow Whitening', ''),
 3821: ('Hibernation Vacations', ''),
 3823: ('Precipitation Foundation', ''),
 3824: ('Open Fire Chestnut Roasting', ''),
 3825: ('Cool Cat Hats', ''),
 3826: ('Oh My Galoshes!', ''),
 3827: ('Choral Wreaths', ''),
 3828: ("Snowman's Land", ''),
 3829: ('Pinecone Zone', ''),
 3830: ('Wait and See Goggle Defogging', ''),
 3901: ("Xanon's Xylophones", ''),
 3902: ("Olive the Other Reindeer", ''),
 3903: ("Ant-Art-Ica Art Academy", ''),
 3904: ("Avalanchovies Fish Market", ''),
 3905: ("Frosted Flakes", ''),
 3906: ("Snow Way in Hail", ''),
 3907: ("Ice to Meet You!", ''),
 3908: ("Polar Panels", ''),
 3909: ("The Cold Shoulder", ''),
 3910: ("Polar Opposites", ''),
 3911: ("Central Parka", ''),
 3912: ("Frostbite Dentistry", ''),
 3913: ("B-Ice-Cycles", ''),
 3914: ("Brain Freeze Neurology", ''),
 3915: ("Sub Zero Deli", ''),
 3916: ("Frost Come, Frost Serve", '')}
ClosetTimeoutMessage = 'Sorry, you ran out\n of time.'
ClosetNotOwnerMessage = "This isn't your closet, but you may try on the clothes."
ClosetPopupOK = lOK
ClosetPopupCancel = lCancel
ClosetDiscardButton = 'Remove'
ClosetAreYouSureMessage = 'You have deleted some clothes.  Do you really want to delete them?'
ClosetYes = lYes
ClosetNo = lNo
ClosetVerifyDelete = 'Really delete %s?'
ClosetShirt = 'this shirt'
ClosetShorts = 'these shorts'
ClosetSkirt = 'this skirt'
ClosetDeleteShirt = 'Delete\nshirt'
ClosetDeleteShorts = 'Delete\nshorts'
ClosetDeleteSkirt = 'Delete\nskirt'
TrunkNotOwnerMessage = "This isn't your trunk, but you may try on the accessories."
TrunkNotPaidMessage = 'Only Paid Members can wear accessories, but you may try them on.'
TrunkAreYouSureMessage = 'You have deleted some accessories.  Do you really want to delete them?'
TrunkHat = 'this hat'
TrunkGlasses = 'these glasses'
TrunkBackpack = 'this backpack'
TrunkShoes = 'these shoes'
TrunkDeleteHat = 'Delete\nhat'
TrunkDeleteGlasses = 'Delete\nglasses'
TrunkDeleteBackpack = 'Delete\nbackpack'
TrunkDeleteShoes = 'Delete\nshoes'
EstateOwnerLeftMessage = "Sorry, the owner of this estate left.  You'll be sent to the playground in %s seconds"
EstatePopupOK = lOK
EstateTeleportFailed = "Couldn't go home. Try again!"
EstateTeleportFailedNotFriends = "Sorry, %s is in a toon's estate that you are not friends with."
EstateTargetGameStart = 'The Toon-up Target game has started!'
EstateTargetGameInst = "The more you hit the red target, the more you'll get Tooned up."
EstateTargetGameEnd = 'The Toon-up Target game is now over...'
AvatarsHouse = '%s\n House'
BankGuiCancel = lCancel
BankGuiOk = lOK
DistributedBankNoOwner = 'Sorry, this is not your bank.'
DistributedBankNotOwner = 'Sorry, this is not your bank.'
FishGuiCancel = lCancel
FishGuiOk = 'Sell All'
FishTankValue = 'Hi, %(name)s! You have %(num)s fish in your bucket worth a total of %(value)s Jellybeans. Do you want to sell them all?'
FishItemBuyPageTitle = 'Would you like to upgrade your fishing rod or your bucket today?'
FishRodBuy = 'Would you like to buy the %(type)s rod for %(beans)s jellybeans?'
FishBucketBuy = 'Would you like to upgrade your fishing bucket capacity by 10 for %s jellybeans?'
FishPurchase = 'Purchase'
FlowerGuiCancel = lCancel
FlowerGuiOk = 'Sell All'
FlowerBasketValue = '%(name)s, you have %(num)s flowers in your basket worth a total of %(value)s Jellybeans. Do you want to sell them all?'

def GetPossesive(name):
    if name[-1:] == 's':
        possesive = name + "'"
    else:
        possesive = name + "'s"
    return possesive


PetTrait2descriptions = {'hungerThreshold': ('Always Hungry',
                     'Often Hungry',
                     'Sometimes Hungry',
                     'Rarely Hungry'),
 'boredomThreshold': ('Always Bored',
                      'Often Bored',
                      'Sometimes Bored',
                      'Rarely Bored'),
 'angerThreshold': ('Always Grumpy',
                    'Often Grumpy',
                    'Sometimes Grumpy',
                    'Rarely Grumpy'),
 'forgetfulness': ('Always Forgets',
                   'Often Forgets',
                   'Sometimes Forgets',
                   'Rarely Forgets'),
 'excitementThreshold': ('Very Calm',
                         'Pretty Calm',
                         'Pretty Excitable',
                         'Very Excitable'),
 'sadnessThreshold': ('Always Sad',
                      'Often Sad',
                      'Sometimes Sad',
                      'Rarely Sad'),
 'restlessnessThreshold': ('Always Restless',
                           'Often Restless',
                           'Sometimes Restless',
                           'Rarely Restless'),
 'playfulnessThreshold': ('Rarely Playful',
                          'Sometimes Playful',
                          'Often Playful',
                          'Always Playful'),
 'lonelinessThreshold': ('Always Lonely',
                         'Often Lonely',
                         'Sometimes Lonely',
                         'Rarely Lonely'),
 'fatigueThreshold': ('Always Tired',
                      'Often Tired',
                      'Sometimes Tired',
                      'Rarely Tired'),
 'confusionThreshold': ('Always Confused',
                        'Often Confused',
                        'Sometimes Confused',
                        'Rarely Confused'),
 'surpriseThreshold': ('Always Surprised',
                       'Often Surprised',
                       'Sometimes Surprised',
                       'Rarely Surprised'),
 'affectionThreshold': ('Rarely Affectionate',
                        'Sometimes Affectionate',
                        'Often Affectionate',
                        'Always Affectionate')}
FireworksInstructions = lToonHQ + ': Hit the "Page Up" key to see the show!'
startFireworksResponse = "Usage: startFireworksShow ['num']\n                                         'num' = %s - New Years\n                                         %s - Party Summer \n                                         %s - 4th of July"
FireworksJuly4Beginning = lToonHQ + ': Welcome to summer fireworks! Enjoy the show!'
FireworksJuly4Ending = lToonHQ + ': Hope you enjoyed the show! Have a great summer!'
FireworksNewYearsEveBeginning = lToonHQ + ': Happy New Year! Enjoy the fireworks show, sponsored by Flippy!'
FireworksNewYearsEveEnding = lToonHQ + ': Hope you enjoyed the show! Have a Toontastic New Year!'
FireworksComboBeginning = lToonHQ + ': Enjoy lots of Laffs with Toon fireworks!'
FireworksComboEnding = lToonHQ + ': Thank you, Toons! Hope you enjoyed the show!'
BlockerTitle = 'LOADING TOONTOWN...'
BlockerLoadingTexts = ['Rewriting history',
 'Baking pie crusts',
 'Heating pie filling',
 'Loading Doodle chow',
 'Stringing Jungle Vines',
 'Uncaging those spiders who crawl down jungle vines',
 'Planting squirting flower seeds',
 'Stretching trampolines',
 'Herding pigs',
 "Tweaking 'SPLAT' sounds",
 'Cleaning Hypno-glasses',
 'Unbottling ink for Toon News',
 'Clipping TNT fuses',
 "Setting up 'Under Construction' sign in Acorn Acres",
 'Waking Donald Duck',
 'Teaching new moves to dancing fire hydrants',
 'Binding Shticker Books',
 'Analyzing quacks',
 'Harvesting Jellybean pods',
 'Emptying fish buckets',
 'Corralling trashcan trash',
 'Spreading Cog grease',
 'Polishing kart trophies',
 'Balancing scale for weighing 1 Ton weights',
 'Practicing Victory Dances',
 'Preparing wackiness',
 'Testing white gloves',
 'Bending underwater rings',
 'Spooling red tape',
 'Freezing Brrrgh ice',
 'Tuning falling pianos']
TIP_NONE = 0
TIP_GENERAL = 1
TIP_STREET = 2
TIP_MINIGAME = 3
TIP_COGHQ = 4
TIP_ESTATE = 5
TIP_KARTING = 6
TIP_GOLF = 7
TipTitle = 'TOON TIP:'
TipDict = {TIP_NONE: ('',),
 TIP_GENERAL: ('Quickly check your ToonTask progress by holding down the "End" key.',
               'Quickly check your Gag page by holding down the "Home" key.',
               'Open your Friends List by pressing the "F7" key.',
               'Open or close your Shticker Book by pressing the "F8" key.',
               'You can look up by pressing the "Page Up" key and look down by pressing the "Page Down" key.',
               'Press the "F9" key to take a screenshot, which will be saved in your Project Altis folder on your computer.',
               'You can change your screen resolution, adjust audio, and control other options on the Options Page in the Shticker Book.',
               "Try on your friend's clothing at the closet in their house.",
               'You can go to your house using the "Go Home" button on your map.',
               'Every time you turn in a completed ToonTask your Laff points are automatically refilled.',
               'You can browse the selection at Clothing Stores even without a clothing ticket.',
               'Rewards for some ToonTasks allow you to carry more gags and Jellybeans.',
               'You can have up to 300 friends on your Friends List.',
               'Some ToonTask rewards let you teleport to playgrounds in Toontown by using the Map Page in the Shticker Book.',
               'Increase your Laff points in the Playgrounds by collecting treasures like stars and ice cream cones.',
               'To heal quickly after a battle, go to your estate and play with your Doodle.',
               'Change to different views of your Toon by pressing the Tab Key.',
               'Sometimes you can find several different ToonTasks offered for the same reward. Shop around!',
               'Finding friends with similar ToonTasks is a fun way to progress through the game.',
               'You never need to save your Toontown progress. The Project Altis servers continually save all the necessary information.',
               'You can whisper to other Toons either by clicking on them or by selecting them from your Friends List.',
               'Some SpeedChat phrases play emotion animations on your Toon.',
               'If the area you are in is crowded, try changing Districts. Go to the District Page in the Shticker Book and select a different one.',
               'If you actively rescue buildings you will get a bronze, silver, or gold star above your Toon.',
               'If you rescue enough buildings to get a star above your head you may find your name on the blackboard in a Toon HQ.',
               'Rescued buildings are sometimes recaptured by the Cogs. The only way to keep your star is to go out and rescue more buildings!',
               'The names of your True Friends will appear in Blue.',
               'Different ponds hold different fish. Try them all!',
               'When your fishing bucket is full sell your fish to the Fishermen in the Playgrounds.',
               'You can sell your fish to the Fishermen or inside Pet Shops.',
               'Stronger fishing rods catch heavier fish but cost more Jellybeans to use.',
               'You can purchase stronger fishing rods in the Cattlelog.',
               'You can sometimes find bags of Jellybeans while fishing.',
               'Some ToonTasks require fishing items out of the ponds.',
               'Fishing ponds in the Playgrounds have different fish than ponds on the streets.',
               'Some fish are really rare. Keep fishing until you collect them all!',
               'The pond at your estate has fish that can only be found there.',
               'For every 10 species you catch, you will get a fishing trophy!',
               'You can see what fish you have collected in your Shticker Book.',
               'Some fishing trophies reward you with a Laff boost.',
               'Fishing is a good way to earn more Jellybeans.',
               'Pet Shops get new Doodles to sell every day.',
               'Visit the Pet Shops every day to see what new Doodles they have.',
               'Different neighborhoods have different Doodles offered for adoption.',
               'When using the new battle GUI, you can press Alt + a number to change tracks, and Ctrl + a number to select a gag!',
               'When using the new battle GUI, you can use the mousewheel to swap between tracks.',
               'Goofy Speedway has six different race tracks. '),
 TIP_STREET: ('There are five types of Cogs: Lawbots, Cashbots, Sellbots, Bossbots, and Boardbots.',
              'Each Gag Track has different amounts of accuracy and damage.',
              'Sound gags will affect all Cogs but will wake up any lured Cogs.',
              'Zap gags deal three times as much damage if a Squirt gag is used before it, it also has a chance to shortcircuit a cog!',
              'Defeating Cogs in strategic order can greatly increase your chances of winning battles.',
              'The Toon-Up Gag Track lets you heal other Toons in battle.',
              'Gag experience points are doubled during a Cog Invasion!',
              'Multiple Toons can team up and use the same Gag Track in battle to get bonus Cog damage.',
              'In battle, gags are used in order from top to bottom as displayed on the Gag Menu.',
              'The row of circular lights over Cog Building elevators show how many floors will be inside.',
              'Click on a Cog to see more details.',
              'Using high level gags against low level Cogs will not earn any experience points.',
              'A gag that will earn experience has a blue background on the Gag Menu in battle.',
              'Gag experience is multiplied when used inside Cog Buildings. Higher floors have higher multipliers.',
              'When a Cog is defeated, each Toon in that round will get credit for the Cog when the battle is over.',
              'Each street in Toontown has different Cog levels and types.',
              'Sidewalks are safe from Cogs.',
              'On the streets, side doors tell knock-knock jokes when approached.',
              'Some ToonTasks train you for new Gag Tracks. You only get to choose seven of the eight Gag Tracks, so choose carefully!',
              'Traps are only useful if you or your friends coordinate using Lure in battle.',
              'Higher level Lures are less likely to miss.',
              'Lower level gags have a lower accuracy against high level Cogs.',
              'Cogs cannot attack once they have been lured in battle.',
              'When you and your friends defeat a Cog building you are rewarded with portraits inside the rescued Toon Building.',
              'Using a Toon-Up gag on a Toon with a full Laff meter will not earn Toon-Up experience.',
              'Cogs will be briefly stunned when hit by any gag. This increases the chance that other gags in the same round will hit.',
              'Drop gags have low chance of hitting, but accuracy is increased when Cogs are first hit by another gag in the same round.',
              'When you\'ve defeated enough Cogs, use the "Cog Radar" by clicking the Cog icons on the Cog Gallery page in your Shticker Book.',
              'During a battle, you can tell which Cog your teammates are attacking by looking at the dashes (-) and Xs.',
              'During a battle, Cogs have a light on them that displays their health; green is healthy, red is nearly destroyed.',
              'A maximum of four Toons can battle at once.',
              'On the street, Cogs are more likely to join a fight against multiple Toons than just one Toon.',
              'The highest ranking Cog of each type can only be found in buildings.',
              'Drop gags never work against lured Cogs.',
              'Cogs tend to attack the Toon that has done them the most damage.',
              'Sound gags do not get bonus damage against lured Cogs.',
              'If you wait too long to attack a lured Cog, it will wake up. Higher level lures last longer.',
              'There are fishing ponds on every street in Toontown. Some streets have unique fish.'),
 TIP_MINIGAME: ('After you fill up your Jellybean jar, any Jellybeans you get from Trolley Games automatically spill over into your bank.',
                'You can use the arrow keys instead of the mouse in the "Match Tubby" Trolley Game.',
                'In the Cannon Game you can use the arrow keys to move your cannon and press the "Control" key to fire.',
                'In the Ring Game, bonus points are awarded when the entire group successfully swims through its rings.',
                'A perfect game of Match Tubby will double your points.',
                'In the Tug-of-War you are awarded more Jellybeans if you play against a tougher Cog.',
                'Trolley Game difficulty varies by neighborhood; ' + lToontownCentral + ' has the easiest and ' + lDonaldsDreamland + ' has the hardest.',
                'Certain Trolley Games can only be played in a group.'),
 TIP_COGHQ: ('You must complete your Sellbot Disguise before visiting the V.P.',
             'You must complete your Cashbot Disguise before visiting the C.F.O.',
             'You must complete your Lawbot Disguise before visiting the Chief Justice.',
             'You must complete your Boardbot Disguise before visiting the ???.',
             'You can jump on Cog Goons to temporarily disable them.',
             'Collect Cog Merits by defeating Sellbot Cogs in battle.',
             'Collect Cogbucks by defeating Cashbot Cogs in battle.',
             'Collect Subpoenas by defeating Lawbot Cogs in battle.',
             'Collect Stock Options by defeating Bossbot Cogs in battle.',
             'Collect ??? by defeating ??? in battle.',
             'You get more Merits, Cogbucks, Subpoenas, Stock Options, or Gears from higher level Cogs.',
             'When you collect enough Cog Merits to earn a promotion, go see the Sellbot V.P.!',
             'When you collect enough Cogbucks to earn a promotion, go see the Cashbot C.F.O.!',
             'When you collect enough Subpoenas to earn a promotion, go see the Lawbot Chief Justice!',
             'When you collect enough Stock Options to earn a promotion, go see the Bossbot C.E.O.!',
             'When you collect enough ??? to earn a promotion, go see the ???!',
             'You can talk like a Cog when you are wearing your Cog Disguise.',
             'Up to eight Toons can join together to fight the Sellbot V.P.',
             'Up to eight Toons can join together to fight the Cashbot C.F.O.',
             'Up to eight Toons can join together to fight the Lawbot Chief Justice.',
             'Up to eight Toons can join together to fight the Bossbot C.E.O.',
             'Up to eight Toons can join together to fight the ???.',
             'Inside Cog Headquarters follow stairs leading up to find your way.',
             'Each time you battle through a Sellbot HQ factory, you will gain one part of your Sellbot Cog Disguise.',
             'Each time you battle through a Cashbot HQ Mint, you will gain one part of your Cashbot Cog Disguise.',
             'Each time you battle through a Lawbot HQ District Attorney\'s Office, you will gain one part of your Lawbot Cog Disguise.',
             'Each time you battle through a Bossbot HQ Cog Golf Course, you will gain one part of your Bossbot Cog Disguise.',
             'Each time you battle through a "CLASSIFIED INFORMATION", you will gain one part of your ???.',
             'You can check the progress of your Cog Disguise in your Shticker Book.',
             'You can check your promotion progress on your Disguise Page in your Shticker Book.',
             'Make sure you have full gags and a full Laff Meter before going to Cog Headquarters.',
             'As you get promoted, your Cog disguise updates.',
             'You must defeat the ' + Foreman + ' to recover a Sellbot Cog Disguise part.',
             'You must defeat the ' + Supervisor + ' to recover a Cashbot Cog Disguise part.',
             'You must defeat the ' + Clerk + ' to recover a Lawbot Cog Disguise part.',
             'You must defeat the ' + President + ' to recover a Bossbot Cog Disguise part.',
             'You must defeat the "This is above your paygrade, toon." to recover a ???.',
             'Cashbots manufacture and distribute their currency, Cogbucks, in three Mints - Coin, Dollar and Bullion.',
             'Wait until the C.F.O. is dizzy to throw a safe, or he will use it as a helmet! Hit the helmet with another safe to knock it off.',
             "It pays to be puzzled: the virtual Cogs in Lawbot HQ won't reward you with Subpoenas."),
 TIP_ESTATE: ('Doodles can understand some SpeedChat phrases. Try them!',
              'Use the "Pet" SpeedChat menu to ask your Doodle to do tricks.',
              "You can teach Doodles tricks with training lessons from Clarabelle's Cattlelog.",
              'Reward your Doodle for doing tricks.',
              "If you visit a friend's estate, your Doodle will come too.",
              'Feed your Doodle a Jellybean when it is hungry.',
              'Click on a Doodle to get a menu where you can Feed, Scratch, and Call him.',
              'Doodles love company. Invite your friends over to play!',
              'All Doodles have unique personalities.',
              'You can return your Doodle and adopt a new one at the Pet Shops.',
              'When a Doodle performs a trick, the Toons around it heal.',
              'Doodles become better at tricks with practice. Keep at it!',
              'More advanced Doodle tricks heal Toons faster.',
              'Experienced Doodles can perform more tricks before getting tired.',
              'You can see a list of nearby Doodles in your Friends List.',
              "Purchase furniture from Clarabelle's Cattlelog to decorate your house.",
              'The bank inside your house holds extra Jellybeans.',
              'The closet inside your house holds extra clothes.',
              "Go to your friend's house and try on his clothes.",
              "Purchase better fishing rods from Clarabelle's Cattlelog.",
              'Call Clarabelle using the phone inside your house.',
              'Clarabelle sells a larger closet that holds more clothing.',
              'Make room in your closet before using a Clothing Ticket.',
              'Clarabelle sells everything you need to decorate your house.',
              'Check your mailbox for deliveries after ordering from Clarabelle.',
              "Clothing from Clarabelle's Cattlelog takes one hour to be delivered.",
              "Wallpaper and flooring from Clarabelle's Cattlelog take one hour to be delivered.",
              "Furniture from Clarabelle's Cattlelog takes a full day to be delivered.",
              'Store extra furniture in your attic.',
              'You will get a notice from Clarabelle when a new Cattlelog is ready.',
              'You will get a notice from Clarabelle when a Cattlelog delivery arrives.',
              'New Cattlelogs are delivered each week.',
              'Look for limited-edition holiday items in the Cattlelog.',
              'Move unwanted furniture to the trash can.',
              'Some fish, like the Holey Mackerel, are more commonly found in Toon Estates.',
              'You can invite your friends to your Estate using SpeedChat.',
              'Did you know the color of your house matches the color of your Pick-A-Toon panel?'),
 TIP_KARTING: ("Buy a Roadster, TUV, or Cruiser kart in Goofy's Auto Shop.",
               "Customize your kart with decals, rims and more in Goofy's Auto Shop.",
               'Earn tickets by kart racing at Goofy Speedway.',
               "Tickets are the only currency accepted at Goofy's Auto Shop.",
               'Tickets are required as deposits to race.',
               'A special page in the Shticker Book allows you to customize your kart.',
               'A special page in the Shticker Book allows you to view records on each track.',
               'A special page in the Shticker Book allows you to display trophies.',
               'Screwball Stadium is the easiest track at Goofy Speedway.',
               'Airborne Acres has the most hills and jumps of any track at Goofy Speedway.',
               'Blizzard Boulevard is the most challenging track at Goofy Speedway.'),
 TIP_GOLF: ('Press the Tab key to see a top view of the golf course.', 'Press the Up Arrow key to point yourself towards the golf hole.', 'Swinging the club is just like throwing a pie.')}
FishGenusNames = {0: 'Balloon Fish',
 2: 'Cat Fish',
 4: 'Clown Fish',
 6: 'Frozen Fish',
 8: 'Star Fish',
 10: 'Holey Mackerel',
 12: 'Dog Fish',
 14: 'Amore Eel',
 16: 'Nurse Shark',
 18: 'King Crab',
 20: 'Moon Fish',
 22: 'Sea Horse',
 24: 'Pool Shark',
 26: 'Bear Acuda',
 28: 'Cutthroat Trout',
 30: 'Piano Tuna',
 32: 'Peanut Butter & Jellyfish',
 34: 'Devil Ray'}
FishSpeciesNames = {0: ('Balloon Fish',
     'Hot Air Balloon Fish',
     'Weather Balloon Fish',
     'Water Balloon Fish',
     'Red Balloon Fish'),
 2: ('Cat Fish',
     'Siamese Cat Fish',
     'Alley Cat Fish',
     'Tabby Cat Fish',
     'Tom Cat Fish'),
 4: ('Clown Fish',
     'Sad Clown Fish',
     'Party Clown Fish',
     'Circus Clown Fish'),
 6: ('Frozen Fish',),
 8: ('Star Fish',
     'Five Star Fish',
     'Rock Star Fish',
     'Shining Star Fish',
     'All Star Fish'),
 10: ('Holey Mackerel',),
 12: ('Dog Fish',
      'Bull Dog Fish',
      'Hot Dog Fish',
      'Dalmatian Dog Fish',
      'Puppy Dog Fish'),
 14: ('Amore Eel', 'Electric Amore Eel'),
 16: ('Nurse Shark', 'Clara Nurse Shark', 'Florence Nurse Shark'),
 18: ('King Crab', 'Alaskan King Crab', 'Old King Crab'),
 20: ('Moon Fish',
      'Full Moon Fish',
      'Half Moon Fish',
      'New Moon Fish',
      'Crescent Moon Fish',
      'Harvest Moon Fish'),
 22: ('Sea Horse',
      'Rocking Sea Horse',
      'Clydesdale Sea Horse',
      'Arabian Sea Horse'),
 24: ('Pool Shark',
      'Kiddie Pool Shark',
      'Swimming Pool Shark',
      'Olympic Pool Shark'),
 26: ('Brown Bear Acuda',
      'Black Bear Acuda',
      'Koala Bear Acuda',
      'Honey Bear Acuda',
      'Polar Bear Acuda',
      'Panda Bear Acuda',
      'Kodiac Bear Acuda',
      'Grizzly Bear Acuda'),
 28: ('Cutthroat Trout', 'Captain Cutthroat Trout', 'Scurvy Cutthroat Trout'),
 30: ('Piano Tuna',
      'Grand Piano Tuna',
      'Baby Grand Piano Tuna',
      'Upright Piano Tuna',
      'Player Piano Tuna'),
 32: ('Peanut Butter & Jellyfish',
      'Grape PB&J Fish',
      'Crunchy PB&J Fish',
      'Strawberry PB&J Fish',
      'Concord Grape PB&J Fish'),
 34: ('Devil Ray',)}
CogPartNames = ('Upper Left Leg',
 'Lower Left Leg',
 'Left Foot',
 'Upper Right Leg',
 'Lower Right Leg',
 'Right Foot',
 'Left Shoulder',
 'Right Shoulder',
 'Chest',
 'Health Meter',
 'Pelvis',
 'Upper Left Arm',
 'Lower Left Arm',
 'Left Hand',
 'Upper Right Arm',
 'Lower Right Arm',
 'Right Hand')
CogPartNamesSimple = ('Upper Torso',)
SellbotLegFactorySpecMainEntrance = 'Front Entrance'
SellbotLegFactorySpecLobby = 'Lobby'
SellbotLegFactorySpecLobbyHallway = 'Lobby Hallway'
SellbotLegFactorySpecGearRoom = 'Gear Room'
SellbotLegFactorySpecBoilerRoom = 'Boiler Room'
SellbotLegFactorySpecEastCatwalk = 'East Catwalk'
SellbotLegFactorySpecPaintMixer = 'Paint Mixer'
SellbotLegFactorySpecPaintMixerStorageRoom = 'Paint Mixer Storage Room'
SellbotLegFactorySpecWestSiloCatwalk = 'West Silo Catwalk'
SellbotLegFactorySpecPipeRoom = 'Pipe Room'
SellbotLegFactorySpecDuctRoom = 'Duct Room'
SellbotLegFactorySpecSideEntrance = 'Side Entrance'
SellbotLegFactorySpecStomperAlley = 'Stomper Alley'
SellbotLegFactorySpecLavaRoomFoyer = 'Lava Room Foyer'
SellbotLegFactorySpecLavaRoom = 'Lava Room'
SellbotLegFactorySpecLavaStorageRoom = 'Lava Storage Room'
SellbotLegFactorySpecWestCatwalk = 'West Catwalk'
SellbotLegFactorySpecOilRoom = 'Oil Room'
SellbotLegFactorySpecLookout = 'Lookout'
SellbotLegFactorySpecWarehouse = 'Warehouse'
SellbotLegFactorySpecOilRoomHallway = 'Oil Room Hallway'
SellbotLegFactorySpecEastSiloControlRoom = 'East Silo Control Room'
SellbotLegFactorySpecWestSiloControlRoom = 'West Silo Control Room'
SellbotLegFactorySpecCenterSiloControlRoom = 'Center Silo Control Room'
SellbotLegFactorySpecEastSilo = 'East Silo'
SellbotLegFactorySpecWestSilo = 'West Silo'
SellbotLegFactorySpecCenterSilo = 'Center Silo'
SellbotLegFactorySpecEastSiloCatwalk = 'East Silo Catwalk'
SellbotLegFactorySpecWestElevatorShaft = 'West Elevator Shaft'
SellbotLegFactorySpecEastElevatorShaft = 'East Elevator Shaft'
FishBingoBingo = 'BINGO!'
FishBingoVictory = 'VICTORY!!'
FishBingoJackpot = 'JACKPOT!'
FishBingoGameOver = 'GAME OVER'
FishBingoIntermission = 'Intermission\nEnds In:'
FishBingoNextGame = 'Next Game\nStarts In:'
FishBingoTypeNormal = 'Classic'
FishBingoTypeCorners = 'Four Corners'
FishBingoTypeDiagonal = 'Diagonals'
FishBingoTypeThreeway = 'Three Way'
FishBingoTypeBlockout = 'BLOCKOUT!'
FishBingoStart = "It's time for Fish Bingo!  Go to any available pier to play!"
FishBingoOngoing = 'Welcome! Fish Bingo is currently in progress.'
FishBingoEnd = 'Hope you had fun playing Fish Bingo.'
FishBingoHelpMain = 'Welcome to Toontown Fish Bingo!  Everyone at the pond works together to fill the card before time runs out.'
FishBingoHelpFlash = 'When you catch a fish, click on one of the flashing squares to mark the card.'
FishBingoHelpNormal = 'This is a Classic Bingo card.  Mark any row down, across or diagonally to win.'
FishBingoHelpDiagonals = 'Mark both of the diagonals to win.'
FishBingoHelpCorners = 'An easy Corners card.  Mark all four corners to win.'
FishBingoHelpThreeway = "Three-way.  Mark both diagonals and the middle row to win.  This one isn't easy!"
FishBingoHelpBingo = 'Bingo!'
FishBingoHelpBlockout = 'Blockout!.  Mark the entire card to win.  You are competing against all the other ponds for a huge jackpot!'
FishBingoOfferToSellFish = 'Your fish bucket is full. Would you like to sell your fish?'
FishBingoJackpotWin = 'Win %s Jellybeans!'
ResistanceToonupMenu = 'Toon-up'
ResistanceToonupItem = '%s Toon-up'
ResistanceToonupItemMax = 'Max'
ResistanceToonupChat = 'Toons of the World, Toon-up!'
ResistanceDanceMenu = 'Dance'
ResistanceDanceItem = 'Make them %s'
ResistanceDanceChat = 'Toons of the World, Dance with me!'
ResistanceRestockMenu = 'Gag-up'
ResistanceRestockItem = 'Gag-up %s'
ResistanceRestockItemAll = 'All'
ResistanceRestockChat = 'Toons of the World, Gag-up!'
ResistanceMoneyMenu = 'Jellybeans'
ResistanceMoneyItem = '%s Jellybeans'
ResistanceMoneyChat = 'Toons of the World, Spend Wisely!'
ResistanceEmote1 = NPCToonNames[9228] + ': Welcome to the Resistance!'
ResistanceEmote2 = NPCToonNames[9228] + ': Use your new emote to identify yourself to other members.'
ResistanceEmote3 = NPCToonNames[9228] + ': Good luck!'
KartUIExit = 'Leave Kart'
KartShop_Cancel = lCancel
KartShop_BuyKart = 'Buy Kart'
KartShop_BuyAccessories = 'Buy Accessories'
KartShop_BuyAccessory = 'Buy Accessory'
KartShop_Cost = 'Cost: %d Tickets'
KartShop_ConfirmBuy = 'Buy the %s for %d Tickets?'
KartShop_NoAvailableAcc = 'No available accessories of this type'
KartShop_FullTrunk = 'Your trunk is full.'
KartShop_ConfirmReturnKart = 'Are you sure you want to return your current Kart?'
KartShop_ConfirmBoughtTitle = 'Congratulations!'
KartShop_NotEnoughTickets = 'Not Enough Tickets!'
KartView_Rotate = 'Rotate'
KartView_Right = 'Right'
KartView_Left = 'Left'
StartingBlock_NotEnoughTickets = "You don't have enough tickets! Try a practice race instead."
StartingBlock_NoBoard = 'Boarding has ended for this race. Please wait for the next race to begin.'
StartingBlock_NoKart = 'You need a kart first! Try asking one of the clerks in the Kart Shop.'
StartingBlock_Occupied = 'This block is currently occupied! Please try another spot.'
StartingBlock_TrackClosed = 'Sorry, this track is closed for remodeling.'
StartingBlock_EnterPractice = 'Would you like to enter a practice race?'
StartingBlock_EnterNonPractice = 'Would you like to enter a %s race for %s tickets?'
StartingBlock_EnterShowPad = 'Would you like to park your car here?'
StartingBlock_KickSoloRacer = 'Toon Battle and Grand Prix races require two or more racers.'
StartingBlock_Loading = 'Goofy Speedway'
LeaderBoard_Time = 'Time'
LeaderBoard_Name = 'Racer Name'
LeaderBoard_Daily = 'Daily Scores'
LeaderBoard_Weekly = 'Weekly Scores'
LeaderBoard_AllTime = 'All Time Best Scores'
RecordPeriodStrings = [LeaderBoard_Daily, LeaderBoard_Weekly, LeaderBoard_AllTime]
KartRace_RaceNames = ['Practice', 'Toon Battle', 'Grand Prix']
from toontown.racing import RaceGlobals
KartRace_Go = 'Go!'
KartRace_Reverse = ' Rev'
KartRace_TrackNames = {RaceGlobals.RT_Speedway_1: 'Screwball Stadium',
 RaceGlobals.RT_Speedway_1_rev: 'Screwball Stadium' + KartRace_Reverse,
 RaceGlobals.RT_Rural_1: 'Rustic Raceway',
 RaceGlobals.RT_Rural_1_rev: 'Rustic Raceway' + KartRace_Reverse,
 RaceGlobals.RT_Urban_1: 'City Circuit',
 RaceGlobals.RT_Urban_1_rev: 'City Circuit' + KartRace_Reverse,
 RaceGlobals.RT_Speedway_2: 'Corkscrew Coliseum',
 RaceGlobals.RT_Speedway_2_rev: 'Corkscrew Coliseum' + KartRace_Reverse,
 RaceGlobals.RT_Rural_2: 'Airborne Acres',
 RaceGlobals.RT_Rural_2_rev: 'Airborne Acres' + KartRace_Reverse,
 RaceGlobals.RT_Urban_2: 'Blizzard Boulevard',
 RaceGlobals.RT_Urban_2_rev: 'Blizzard Boulevard' + KartRace_Reverse}
KartRace_Unraced = 'N/A'
KartDNA_KartNames = {0: 'Cruiser',
 1: 'Roadster',
 2: 'Toon Utility Vehicle'}
KartDNA_AccNames = {1000: 'Air Cleaner',
 1001: 'Four Barrel',
 1002: 'Flying Eagle',
 1003: 'Steer Horns',
 1004: 'Straight Six',
 1005: 'Small Scoop',
 1006: 'Single Overhead',
 1007: 'Medium Scoop',
 1008: 'Single Barrel',
 1009: 'Flugle Horn',
 1010: 'Striped Scoop',
 2000: 'Space Wing',
 2001: 'Patched Spare',
 2002: 'Roll Cage',
 2003: 'Single Fin',
 2004: 'Double-decker Wing',
 2005: 'Single Wing',
 2006: 'Standard Spare',
 2007: 'Single Fin',
 2008: 'sp9',
 2009: 'sp10',
 3000: 'Dueling Horns',
 3001: "Freddie's Fenders",
 3002: 'Cobalt Running Boards',
 3003: 'Cobra Sidepipes',
 3004: 'Straight Sidepipes',
 3005: 'Scalloped Fenders',
 3006: 'Carbon Running Boards',
 3007: 'Wood Running Boards',
 3008: 'fw9',
 3009: 'fw10',
 4000: 'Curly Tailpipes',
 4001: 'Splash Fenders',
 4002: 'Dual Exhaust',
 4003: 'Plain Dual Fins',
 4004: 'Plain Mudflaps',
 4005: 'Quad Exhaust',
 4006: 'Dual Flares',
 4007: 'Mega Exhaust',
 4008: 'Striped Dual Fins',
 4009: 'Bubble Duals Fins',
 4010: 'Striped Mudflaps',
 4011: 'Mickey Mudflaps',
 4012: 'Scalloped Mudflaps',
 5000: 'Turbo',
 5001: 'Moon',
 5002: 'Patched',
 5003: 'Three Spoke',
 5004: 'Paint Lid',
 5005: 'Heart',
 5006: 'Mickey',
 5007: 'Five Bolt',
 5008: 'Daisy',
 5009: 'Basketball',
 5010: 'Hypno',
 5011: 'Tribal',
 5012: 'Gemstone',
 5013: 'Five Spoke',
 5014: 'Knockoff',
 6000: 'Number Five',
 6001: 'Splatter',
 6002: 'Checkerboard',
 6003: 'Flames',
 6004: 'Hearts',
 6005: 'Bubbles',
 6006: 'Tiger',
 6007: 'Flowers',
 6008: 'Lightning',
 6009: 'Angel',
 7000: 'Chartreuse',
 7001: 'Peach',
 7002: 'Bright Red',
 7003: 'Red',
 7004: 'Maroon',
 7005: 'Sienna',
 7006: 'Brown',
 7007: 'Tan',
 7008: 'Coral',
 7009: 'Orange',
 7010: 'Yellow',
 7011: 'Cream',
 7012: 'Citrine',
 7013: 'Lime',
 7014: 'Sea Green',
 7015: 'Green',
 7016: 'Light Blue',
 7017: 'Aqua',
 7018: 'Blue',
 7019: 'Periwinkle',
 7020: 'Royal Blue',
 7021: 'Slate Blue',
 7022: 'Purple',
 7023: 'Lavender',
 7024: 'Pink',
 7025: 'Plum',
 7026: 'Black'}
RaceHoodSpeedway = 'Speedway'
RaceHoodRural = 'Rural'
RaceHoodUrban = 'Urban'
RaceTypeCircuit = 'Tournament'
RaceQualified = 'qualified'
RaceSwept = 'swept'
RaceWon = 'won'
Race = 'race'
Races = 'races'
Total = 'total'
GrandTouring = 'Grand Touring'

def getTrackGenreString(genreId):
    genreStrings = ['Speedway', 'Country', 'City']
    return genreStrings[genreId].lower()


def getTunnelSignName(trackId, padId):
    if trackId == 2 and padId == 0:
        return 'tunne1l_citysign'
    elif trackId == 1 and padId == 0:
        return 'tunnel_countrysign1'
    else:
        genreId = RaceGlobals.getTrackGenre(trackId)
        return 'tunnel%s_%ssign' % (padId + 1, RaceGlobals.getTrackGenreString(genreId))


KartTrophyDescriptions = [str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.QualifiedRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.TotalQualifiedRaces) + ' ' + Total + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodSpeedway + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodSpeedway + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodRural + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodRural + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[0]) + ' ' + RaceHoodUrban + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[1]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonRaces[2]) + ' ' + RaceHoodUrban + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.TotalWonRaces) + ' ' + Total + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceQualified,
 str(RaceGlobals.WonCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.WonCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceWon,
 str(RaceGlobals.SweptCircuitRaces[0]) + ' ' + RaceTypeCircuit + ' ' + Race + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[1]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 str(RaceGlobals.SweptCircuitRaces[2]) + ' ' + RaceTypeCircuit + ' ' + Races + ' ' + RaceSwept,
 GrandTouring,
 str(RaceGlobals.TrophiesPerCup) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 2) + ' Kart Racing trophies won! Laff point boost!',
 str(RaceGlobals.TrophiesPerCup * 3) + ' Kart Racing trophies won! Laff point boost!']
KartRace_TitleInfo = 'Get Ready to Race'
KartRace_SSInfo = 'Welcome to Screwball Stadium!\nPut the pedal to the metal and hang on tight!\n'
KartRace_CoCoInfo = 'Welcome to Corkscrew Coliseum!\nUse the banked turns to keep your speed up!\n'
KartRace_RRInfo = 'Welcome to Rustic Raceway!\nPlease be kind to the fauna and stay on the track!\n'
KartRace_AAInfo = 'Welcome to Airborne Acres!\nHold onto your hats! It looks bumpy up ahead...\n'
KartRace_CCInfo = 'Welcome to City Circuit!\nWatch out for pedestrians as you speed through downtown!\n'
KartRace_BBInfo = 'Welcome to Blizzard Boulevard!\nWatch your speed. There might be ice out there.\n'
KartRace_GeneralInfo = 'Use Control to throw gags you pick up on the track, and the arrow keys to control your kart.'
KartRace_TrackInfo = {RaceGlobals.RT_Speedway_1: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_1_rev: KartRace_SSInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Speedway_2_rev: KartRace_CoCoInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_1_rev: KartRace_RRInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Rural_2_rev: KartRace_AAInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_1_rev: KartRace_CCInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2: KartRace_BBInfo + KartRace_GeneralInfo,
 RaceGlobals.RT_Urban_2_rev: KartRace_BBInfo + KartRace_GeneralInfo}
KartRecordStrings = {RaceGlobals.Daily: 'daily',
 RaceGlobals.Weekly: 'weekly',
 RaceGlobals.AllTime: 'all time'}
KartRace_FirstSuffix = 'st'
KartRace_SecondSuffix = '    nd'
KartRace_ThirdSuffix = '  rd'
KartRace_FourthSuffix = '   th'
KartRace_WrongWay = 'Wrong\nWay!'
KartRace_LapText = 'Lap %s'
KartRace_FinalLapText = 'Final Lap!'
KartRace_Exit = 'Exit Race'
KartRace_NextRace = 'Next Race'
KartRace_Leave = 'Leave Race'
KartRace_Qualified = 'Qualified!'
KartRace_Record = 'Record!'
KartRace_RecordString = 'You have set a new %s record for %s! Your bonus is %s tickets.'
KartRace_Tickets = 'Tickets'
KartRace_Exclamations = '!'
KartRace_Deposit = 'Deposit'
KartRace_Winnings = 'Winnings'
KartRace_Bonus = 'Bonus'
KartRace_RaceTotal = 'Race Total'
KartRace_CircuitTotal = 'Circuit Total'
KartRace_Trophies = 'Trophies'
KartRace_Zero = '0'
KartRace_Colon = ':'
KartRace_TicketPhrase = '%s ' + KartRace_Tickets
KartRace_DepositPhrase = KartRace_Deposit + KartRace_Colon + '\n'
KartRace_QualifyPhrase = 'Qualify:\n'
KartRace_RaceTimeout = 'You timed out of that race.  Your tickets have been refunded.  Keep trying!'
KartRace_RaceTimeoutNoRefund = 'You timed out of that race.  Your tickets have not been refunded because the Grand Prix had already started.  Keep trying!'
KartRace_RacerTooSlow = 'You took too long to finish the race.  Your tickets have not been refunded.  Keep trying!'
KartRace_PhotoFinish = 'Photo Finish!'
KartRace_CircuitPoints = 'Circuit Points'
CircuitRaceStart = 'The Toontown Grand Prix at Goofy Speedway is about to begin!  To win, collect the most points in three consecutive races!'
CircuitRaceOngoing = 'Welcome! The Toontown Grand Prix is currently in progress.'
CircuitRaceEnd = "That's all for today's Toontown Grand Prix at Goofy Speedway.  See you next week!"
TrickOrTreatMsg = 'You have already\nfound this treat!'
WinterCarolingMsg = 'You have already been caroling here!'
LawbotBossTempIntro0 = "Hmmm what's on the docket today?"
LawbotBossTempIntro1 = 'Aha, we have a Toon on trial!'
LawbotBossTempIntro2 = "The prosecution's case is strong."
LawbotBossTempIntro3 = 'And here are the public defenders.'
LawbotBossTempIntro4 = "Wait a minute... You're Toons!"
LawbotBossTempJury1 = 'Jury selection will now commence.'
LawbotBossHowToGetEvidence = 'Touch the witness stand to get evidence.'
LawbotBossTrialChat1 = 'Court is now in session'
LawbotBossHowToThrowPies = 'Press the Delete key to throw the evidence\n at the lawyers or into the scale!'
LawbotBossNeedMoreEvidence = 'You need to get more evidence!'
LawbotBossDefenseWins1 = 'Impossible! The defense won?'
LawbotBossDefenseWins2 = 'No. I declare a mistrial! A new one will be scheduled.'
LawbotBossDefenseWins3 = "Hrrmpphh. I'll be in my chambers."
LawbotBossDefenseWins4 = "Oh, I forgot about the paperwork needed to file a mistrial..."
LawbotBossProsecutionWins = 'I find in favor of the plaintiff'
LawbotBossReward = 'I award a promotion and the ability to summon Cogs'
LawbotBossLeaveCannon = 'Leave cannon'
LawbotBossPassExam = 'Bah, so you passed the bar exam.'
LawbotBossTaunts = ['%s, I find you in contempt of court!',
 'Objection sustained!',
 'Strike that from the record.',
 'Your appeal has been rejected. I sentence you to sadness!',
 'Order in the court!']
LawbotBossAreaAttackTaunt = "You're all in contempt of court!"
WitnessToonName = 'Bumpy Bumblebehr'
WitnessToonPrepareBattleTwo = "Oh no! They're putting only Cogs on the jury!\x07Quick, use the cannons and shoot some Toon jurors into the jury chairs.\x07We need %d to get a balanced scale."
WitnessToonNoJuror = 'Oh oh, no Toon jurors. This will be a tough trial.'
WitnessToonOneJuror = 'Cool! There is 1 Toon in the jury!'
WitnessToonSomeJurors = 'Cool! There are %d Toons in the jury!'
WitnessToonAllJurors = 'Awesome! All the jurors are Toons!'
WitnessToonPrepareBattleThree = 'Hurry, touch the witness stand to get evidence.\x07Press the Delete key to throw the evidence at the lawyers, or at the defense pan.'
WitnessToonCongratulations = "You did it!  Thank you for a spectacular defense!\x07Here, take these papers the Chief Justice left behind.\x07With it you'll be able to summon Cogs from your Cog Gallery page."
WitnessToonHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
WitnessToonLevelPromotion = "\x07Say--that C.J. Cog left behind your promotion papers.\x07I'll file them for you on the way out, so you'll get your promotion!"
WitnessToonSuitPromotion = "\x07It seems like you've reached the highest level you can for a %s.\x07You can continue upgrading your Cog suit through the disguise page in your Shticker Book.\x07Along with getting a new Cog suit, you will also get a 1 point Laff boost!"
WitnessToonLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07I'm pretty sure Cogs don't get promoted higher than that.\x07You can begin upgrading your V2.0 Cog suit through hard mode bosses!!"
WitnessToonLastRevivePromotion = "\x07Wow, you've reached level %s on your V2.0 Cog suit!\x07I'm pretty sure Cogs don't get promoted higher than that.\x07You cant upgrade your Cog suit anymore, but you can certainly keep working for the Resistance!!"
WitnessToonMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
WitnessToonBonus = 'Wonderful! All the lawyers are stunned. Your evidence weight is %s times heavier for %s seconds'
WitnessToonJuryWeightBonusSingular = {6: 'This is a tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon juror, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon juror, so your evidence has a bonus weight of %d.'}
WitnessToonJuryWeightBonusPlural = {6: 'This is a tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 7: 'This is a very tough case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.',
 8: 'This is the toughest case. You seated %d Toon jurors, so your evidence has a bonus weight of %d.'}
IssueSummons = 'Summon'
SummonDlgTitle = 'Issue a Cog Summons'
SummonDlgButton1 = 'Summon a Cog'
SummonDlgButton2 = 'Summon a Cog Building'
SummonDlgButton3 = 'Summon a Cog Invasion'
SummonDlgSingleConf = 'Would you like to issue a summons to a %s?'
SummonDlgBuildingConf = 'Would you like to summon a %s to a nearby Toon building?'
SummonDlgInvasionConf = 'Would you like to summon a %s invasion?'
SummonDlgNumLeft = 'You have %s left.'
SummonDlgDelivering = 'Delivering Summons...'
SummonDlgSingleSuccess = 'You have successfully summoned the Cog.'
SummonDlgSingleBadLoc = "Sorry, Cogs aren't allowed here.  Try somewhere else."
SummonDlgBldgSuccess = 'You have successfully summoned the Cogs. %s has agreed to let them temporarily take over %s!'
SummonDlgBldgSuccess2 = 'You have successfully summoned the Cogs. A Shopkeeper has agreed to let them temporarily take over their building!'
SummonDlgBldgBadLoc = 'Sorry, there are no Toon buildings nearby for the Cogs to take over.'
SummonDlgInvasionSuccess = "You have successfully summoned the Cogs. It's an invasion!"
SummonDlgInvasionBusy = 'A %s cannot be found now.  Try again when the Cog invasion is over.'
SummonDlgInvasionFail = 'Sorry, the Cog invasion has failed.'
SummonDlgShopkeeper = 'The Shopkeeper '
ShopkeeperThanks = 'Thanks for saving my shop! Have this reward of %s jellybeans!'
PolarPlaceEffect1 = NPCToonNames[3306] + ': Welcome to Polar Place!'
PolarPlaceEffect2 = NPCToonNames[3306] + ': Try this on for size.'
PolarPlaceEffect3 = NPCToonNames[3306] + ': Your new look will only work in ' + lTheBrrrgh + '.'
GreenToonEffectMsg = NPCToonNames[5312] + ': You look Toontastic in green!'
LaserGameMine = 'Skull Finder!'
LaserGameRoll = 'Matching'
LaserGameAvoid = 'Avoid the Skulls'
LaserGameDrag = 'Drag three of a color in a row'
LaserGameDefault = 'Unknown Game'
PinballHiScore = 'High Score:     %s\n'
PinballHiScoreAbbrev = '...'
PinballYourBestScore = 'Your Best Score:\n'
PinballScore = 'Score:            %d x %d = '
PinballScoreHolder = '%s\n'
GagTreeFeather = 'Feather Gag Tree'
GagTreeJugglingBalls = 'Juggling Balls Gag Tree'
StatuaryFountain = 'Fountain'
StatuaryDonald = 'Statue'
StatuaryMinnie = 'Statue'
StatuaryMickey1 = 'Statue'
StatuaryMickey2 = 'Fountain'
StatuaryToon = 'Toon Statue'
StatuaryToonWave = 'Toon Wave Statue'
StatuaryToonVictory = 'Toon Victory Statue'
StatuaryToonCrossedArms = 'Toon Authority Statue'
StatuaryToonThinking = 'Toon Thinking Statue'
StatuaryMeltingSnowman = 'Melting Snowman'
StatuaryMeltingSnowDoodle = 'Melting SnowDoodle'
StatuaryGardenAccelerator = 'Insta-Grow Fertilizer'
StatuaryGazebo = 'Gazebo'
AnimatedStatuaryFlappyCog = 'Flappy Cog'
FlowerColorStrings = ['Red',
 'Orange',
 'Violet',
 'Blue',
 'Pink',
 'Yellow',
 'White',
 'Green']
FlowerSpeciesNames = {49: 'Daisy',
 50: 'Tulip',
 51: 'Carnation',
 52: 'Lily',
 53: 'Daffodil',
 54: 'Pansy',
 55: 'Petunia',
 56: 'Rose'}
FlowerFunnyNames = {49: ('School Daisy',
      'Lazy Daisy',
      'Midsummer Daisy',
      'Freshasa Daisy',
      'Whoopsie Daisy',
      'Upsy Daisy',
      'Crazy Daisy',
      'Hazy Dazy'),
 50: ('Onelip', 'Twolip', 'Threelip'),
 51: ('What-in Carnation',
      'Instant Carnation',
      'Hybrid Carnation',
      'Side Carnation',
      'Model Carnation'),
 52: ('Lily-of-the-Alley',
      'Lily Pad',
      'Tiger Lily',
      'Livered Lily',
      'Chili Lily',
      'Silly Lily',
      'Indubitab Lily',
      'Dilly Lilly'),
 53: ('Laff-o-dil',
      'Daffy Dill',
      'Giraff-o-dil',
      'Time and a half-o-dil'),
 54: ('Dandy Pansy',
      'Chim Pansy',
      'Potsen Pansy',
      'Marzi Pansy',
      'Smarty Pansy'),
 55: ('Car Petunia', 'Platoonia'),
 56: ("Summer's Last Rose",
      'Corn Rose',
      'Tinted Rose',
      'Stinking Rose',
      'Istilla Rose')}
FlowerVarietyNameFormat = '%s %s'
FlowerUnknown = '????'
FloweringNewEntry = 'New Entry'
ShovelNameDict = {0: 'Tin',
 1: 'Bronze',
 2: 'Silver',
 3: 'Gold'}
WateringCanNameDict = {0: 'Small',
 1: 'Medium',
 2: 'Large',
 3: 'Huge'}
GardeningPlant = 'Plant'
GardeningWater = 'Water'
GardeningRemove = 'Remove'
GardeningPick = 'Pick'
GardeningFull = 'Full'
GardeningSkill = 'Skill'
GardeningWaterSkill = 'Water Skill'
GardeningShovelSkill = 'Shovel Skill'
GardeningNoSkill = 'No Skill Up'
GardeningPlantFlower = 'Plant\nFlower'
GardeningPlantTree = 'Plant\nTree'
GardeningPlantItem = 'Plant\nItem'
PlantingGuiOk = 'Plant'
PlantingGuiCancel = 'Cancel'
PlantingGuiReset = 'Reset'
GardeningChooseBeans = 'Choose the Jellybeans you want to plant.'
GardeningChooseBeansItem = 'Choose the Jellybeans / item you want to plant.'
GardeningChooseToonStatue = 'Choose the toon you want to create a statue of.'
GardenShovelLevelUp = "Congratulations you've earned a %(shovel)s! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillLevelUp = "Congratulations! You've mastered the %(oldbeans)d bean flower! To progress you should pick %(newbeans)d bean flowers."
GardenShovelSkillMaxed = "Amazing! You've maxed out your shovel skill!"
GardenWateringCanLevelUp = "Congratulations you've earned a new watering can!"
GardenMiniGameWon = "Congratulations you've watered the plant!"
ShovelTin = 'Tin Shovel'
ShovelSteel = 'Bronze Shovel'
ShovelSilver = 'Silver Shovel'
ShovelGold = 'Gold Shovel'
WateringCanSmall = 'Small Watering Can'
WateringCanMedium = 'Medium Watering Can'
WateringCanLarge = 'Large Watering Can'
WateringCanHuge = 'Huge Watering Can'
BeanColorWords = ('red',
 'green',
 'orange',
 'violet',
 'blue',
 'pink',
 'yellow',
 'cyan',
 'silver')
PlantItWith = ' Plant with %s.'
MakeSureWatered = ' Make sure all your plants are watered first.'
UseFromSpecialsTab = ' Use from the specials tab of the garden page.'
UseSpecial = 'Use Special'
UseSpecialBadLocation = 'You can only use that in your garden.'
UseSpecialSuccess = 'Success! Your watered plants just grew.'
ConfirmWiltedFlower = '%(plant)s is wilted.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmUnbloomingFlower = '%(plant)s is not blooming.  Are you sure you want to remove it?  It will not go into your flower basket, nor will you get an increase in skill.'
ConfirmNoSkillupFlower = 'Are you sure you want to pick the %(plant)s? It will go into your flower basket, but you will NOT get an increase in skill.'
ConfirmSkillupFlower = 'Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will also get an increase in skill.'
ConfirmMaxedSkillFlower = "Are you sure you want to pick the %(plant)s?  It will go into your flower basket. You will NOT get an increase in skill since you've maximized it already."
ConfirmBasketFull = 'Your flower basket is full. Sell some flowers first.'
ConfirmRemoveTree = 'Are you sure you want to remove the %(tree)s?'
ConfirmWontBeAbleToHarvest = " If you remove this tree, you won't be able to harvest gags from the higher level trees."
ConfirmRemoveStatuary = 'Are you sure you want to permanently delete the %(item)s?'
ResultPlantedSomething = 'Congratulations! You just planted a %s.'
ResultPlantedSomethingAn = 'Congratulations! You just planted an %s.'
ResultPlantedNothing = "That didn't work.  Please try a different combination of Jellybeans."
GardenGagTree = ' Gag Tree'
GardenUberGag = 'Uber Gag'

def getRecipeBeanText(beanTuple):
    retval = ''
    if not beanTuple:
        return retval
    allTheSame = True
    for index in xrange(len(beanTuple)):
        if index + 1 < len(beanTuple):
            if not beanTuple[index] == beanTuple[index + 1]:
                allTheSame = False
                break

    if allTheSame:
        if len(beanTuple) > 1:
            retval = '%d %s Jellybeans' % (len(beanTuple), BeanColorWords[beanTuple[0]])
        else:
            retval = 'a %s Jellybean' % BeanColorWords[beanTuple[0]]
    else:
        retval += 'a'
        maxBeans = len(beanTuple)
        for index in xrange(maxBeans):
            if index == maxBeans - 1:
                retval += ' and %s Jellybean' % BeanColorWords[beanTuple[index]]
            elif index == 0:
                retval += ' %s' % BeanColorWords[beanTuple[index]]
            else:
                retval += ', %s' % BeanColorWords[beanTuple[index]]

    return retval


GardenTextMagicBeans = 'Magic Beans'
GardenTextMagicBeansB = 'Some Other Beans'
GardenSpecialDiscription = 'This text should explain how to use a certain garden special'
GardenSpecialDiscriptionB = 'This text should explain how to use a certain garden special, in yo face foo!'
GardenTrophyAwarded = 'Wow! You collected %s of %s flowers. That deserves a trophy and a Laff boost!'
GardenTrophyNameDict = {0: 'Wheelbarrow',
 1: 'Shovels',
 2: 'Flower',
 3: 'Watering Can',
 4: 'Shark',
 5: 'Swordfish',
 6: 'Killer Whale'}
SkillTooLow = 'Skill\nToo Low'
NoGarden = 'No\nGarden'

def isVowelStart(str):
    retval = False
    if str and len(str) > 0:
        vowels = ['A',
         'E',
         'I',
         'O',
         'U']
        firstLetter = str.upper()[0:1]
        if firstLetter in vowels:
            retval = True
    return retval


def getResultPlantedSomethingSentence(flowerName):
    if isVowelStart(flowerName):
        retval = ResultPlantedSomethingAn % flowerName
    else:
        retval = ResultPlantedSomething % flowerName
    return retval


TravelGameTitle = 'Trolley Tracks'
TravelGameInstructions = 'Click up or down to set your number of votes.  Click the vote button to cast it. Reach your secret goal to get bonus beans. Earn more votes by doing well in the other games.'
TravelGameRemainingVotes = 'Remaining Votes:'
TravelGameUse = 'Use'
TravelGameVotesWithPeriod = 'votes.'
TravelGameVotesToGo = 'votes to go'
TravelGameVoteToGo = 'vote to go'
TravelGameUp = 'UP.'
TravelGameDown = 'DOWN.'
TravelGameVoteWithExclamation = 'Vote!'
TravelGameWaitingChoices = 'Waiting for other players to vote...'
TravelGameDirections = ['UP', 'DOWN']
TravelGameTotals = 'Totals '
TravelGameReasonVotes = 'The trolley is moving %(dir)s, winning by %(numVotes)d votes.'
TravelGameReasonVotesPlural = 'The trolley is moving %(dir)s, winning by %(numVotes)d votes.'
TravelGameReasonVotesSingular = 'The trolley is moving %(dir)s, winning by %(numVotes)d vote.'
TravelGameReasonPlace = '%(name)s breaks the tie. The trolley is moving %(dir)s.'
TravelGameReasonRandom = 'The trolley is randomly moving %(dir)s.'
TravelGameOneToonVote = '%(name)s used %(numVotes)s votes to go %(dir)s\n'
TravelGameBonusBeans = '%(numBeans)d Beans'
TravelGamePlaying = 'Up next, the %(game)s trolley game.'
TravelGameGotBonus = '%(name)s got a bonus of %(numBeans)s Jellybeans!'
TravelGameNoOneGotBonus = 'No one reached their secret goal.  Everyone gets 1 Jellybean.'
TravelGameConvertingVotesToBeans = 'Converting some votes to Jellybeans...'
TravelGameGoingBackToShop = "Only 1 player left. Going to Goofy's Gag Shop."
PairingGameTitle = 'Toon Memory Game'
PairingGameInstructions = 'Press Delete to open a card. Match 2 cards to score a point.  Make a match with the bonus glow and earn an extra point.  Earn more points by keeping the flips low.'
PairingGameInstructionsMulti = 'Press Delete to open a card. Press Control to signal another player to open a card. Match 2 cards to score a point.  Make a match with the bonus glow and earn an extra point.  Earn more points by keeping the flips low.'
PairingGamePerfect = 'PERFECT!!'
PairingGameFlips = 'Flips:'
PairingGamePoints = 'Points:'
TrolleyHolidayStart = 'Trolley Tracks is about to begin!  Board any trolley with 2 or more toons to play.'
TrolleyHolidayOngoing = 'Welcome! Trolley Tracks is currently in progress.'
TrolleyHolidayEnd = "That's all for today's Trolley Tracks.  See you next week!"
TrolleyWeekendStart = 'Trolley Tracks Weekend is about to begin!  Board any trolley with 2 or more toons to play.'
TrolleyWeekendEnd = "That's all for Trolley Tracks Weekend."
VineGameTitle = 'Jungle Vines'
VineGameInstructions = 'Get to the rightmost vine in time. Press Up or Down to climb the vine.  Press Left or Right to change facing and jump.  The lower you are on the vine, the faster you jump off.  Collect the bananas if you can, but avoid the bats and spiders.'
ValentinesDayStart = "Happy ValenToon's Day!"
ValentinesDayEnd = "That's all for ValenToon's Day!"
GolfCourseNames = {0: 'Walk In The Par',
 1: 'Hole Some Fun',
 2: 'The Hole Kit And Caboodle'}
GolfHoleNames = {0: 'Whole In Won',
 1: 'No Putts About It',
 2: 'Down The Hatch',
 3: 'Seeing Green',
 4: 'Hot Links',
 5: 'Peanut Putter',
 6: 'Swing-A-Long',
 7: 'Afternoon Tee',
 8: 'Hole In Fun',
 9: 'Rock And Roll In',
 10: 'Bogey Nights',
 11: 'Tea Off Time',
 12: 'Holey Mackerel!',
 13: 'One Little Birdie',
 14: 'At The Drive In',
 15: 'Swing Time',
 16: 'Hole On The Range',
 17: 'Second Wind',
 18: 'Whole In Won-2',
 19: 'No Putts About It-2',
 20: 'Down The Hatch-2',
 21: 'Seeing Green-2',
 22: 'Hot Links-2',
 23: 'Peanut Putter-2',
 24: 'Swing-A-Long-2',
 25: 'Afternoon Tee-2',
 26: 'Hole In Fun-2',
 27: 'Rock And Roll In-2',
 28: 'Bogey Nights-2',
 29: 'Tea Off Time-2',
 30: 'Holey Mackerel!-2',
 31: 'One Little Birdie-2',
 32: 'At The Drive In-2',
 33: 'Swing Time-2',
 34: 'Hole On The Range-2',
 35: 'Second Wind-2'}
GolfHoleInOne = 'Hole In One'
GolfCondor = 'Condor'
GolfAlbatross = 'Albatross'
GolfEagle = 'Eagle'
GolfBirdie = 'Birdie'
GolfPar = 'Par'
GolfBogey = 'Bogey'
GolfDoubleBogey = 'Double Bogey'
GolfTripleBogey = 'Triple Bogey'
GolfShotDesc = {-4: GolfCondor,
 - 3: GolfAlbatross,
 - 2: GolfEagle,
 - 1: GolfBirdie,
 0: GolfPar,
 1: GolfBogey,
 2: GolfDoubleBogey,
 3: GolfTripleBogey}
from toontown.golf import GolfGlobals
CoursesCompleted = 'Courses Completed'
CoursesUnderPar = 'Courses Under Par'
HoleInOneShots = 'Hole In One Shots'
EagleOrBetterShots = 'Eagle Or Better Shots'
BirdieOrBetterShots = 'Birdie Or Better Shots'
ParOrBetterShots = 'Par Or Better Shots'
MultiPlayerCoursesCompleted = 'Multiplayer Courses Completed'
TwoPlayerWins = 'Two Player Wins'
ThreePlayerWins = 'Three Player Wins'
FourPlayerWins = 'Four Player Wins'
CourseZeroWins = GolfCourseNames[0] + ' Wins'
CourseOneWins = GolfCourseNames[1] + ' Wins'
CourseTwoWins = GolfCourseNames[2] + ' Wins'
GolfHistoryDescriptions = [CoursesCompleted,
 CoursesUnderPar,
 HoleInOneShots,
 EagleOrBetterShots,
 BirdieOrBetterShots,
 ParOrBetterShots,
 MultiPlayerCoursesCompleted,
 CourseZeroWins,
 CourseOneWins,
 CourseTwoWins]
GolfTrophyDescriptions = [str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][0]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][1]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesCompleted][2]) + ' ' + CoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][0]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][1]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CoursesUnderPar][2]) + ' ' + CoursesUnderPar,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][0]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][1]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.HoleInOneShots][2]) + ' ' + HoleInOneShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][0]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][1]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.EagleOrBetterShots][2]) + ' ' + EagleOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][0]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][1]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.BirdieOrBetterShots][2]) + ' ' + BirdieOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][0]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][1]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.ParOrBetterShots][2]) + ' ' + ParOrBetterShots,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][0]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][1]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.MultiPlayerCoursesCompleted][2]) + ' ' + MultiPlayerCoursesCompleted,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][0]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][1]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseZeroWins][2]) + ' ' + CourseZeroWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][0]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][1]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseOneWins][2]) + ' ' + CourseOneWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][0]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][1]) + ' ' + CourseTwoWins,
 str(GolfGlobals.TrophyRequirements[GolfGlobals.CourseTwoWins][2]) + ' ' + CourseTwoWins]
GolfCupDescriptions = [str(GolfGlobals.TrophiesPerCup) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 2) + ' Trophies won', str(GolfGlobals.TrophiesPerCup * 3) + ' Trophies won']
GolfAvReceivesHoleBest = '%(name)s scored a new hole best at %(hole)s!'
GolfAvReceivesCourseBest = '%(name)s scored a new course best at %(course)s!'
GolfAvReceivesCup = '%(name)s receives the %(cup)s cup!!  Laff point boost!'
GolfAvReceivesTrophy = '%(name)s receives the %(award)s trophy!!'
GolfRanking = 'Ranking: \n'
GolfPowerBarText = '%(power)s%%'
GolfChooseTeeInstructions = 'Press Left or Right to change tee spot.\nPress Control to select.'
GolfWarningMustSwing = 'Warning: You must press Control on your next swing.'
GolfAimInstructions = 'Press Left or Right to aim.\nPress and hold Control to swing.'
GolferExited = '%s has left the golf course.'
GolfPowerReminder = 'Hold Down Control Longer to\nHit the Ball Further'
GolfPar = 'Par'
GolfHole = 'Hole'
GolfTotal = 'Total'
GolfExitCourse = 'Exit Course'
GolfUnknownPlayer = '???'
GolfPageTitle = 'Golf'
GolfPageTitleCustomize = 'Golf Customizer'
GolfPageTitleRecords = 'Personal Best Records'
GolfPageTitleTrophy = 'Golfing Trophies'
GolfPageCustomizeTab = 'Customize'
GolfPageRecordsTab = 'Records'
GolfPageTrophyTab = 'Trophy'
GolfPageTickets = 'Tickets : '
GolfPageConfirmDelete = 'Delete Accessory?'
GolfTrophyTextDisplay = 'Trophy %(number)s : %(desc)s'
GolfCupTextDisplay = 'Cup %(number)s : %(desc)s'
GolfCurrentHistory = 'Current %(historyDesc)s : %(num)s'
GolfTieBreakWinner = '%(name)s wins the random tie breaker!'
GolfSeconds = ' -  %(time).2f seconds'
GolfTimeTieBreakWinner = '%(name)s wins the total aiming time tie breaker!!!'
RoamingTrialerWeekendStart = 'Tour Toontown is starting! Free players may now enter any neighborhood!'
RoamingTrialerWeekendOngoing = 'Welcome to Tour Toontown! Free players may now enter any neighborhood!'
RoamingTrialerWeekendEnd = "That's all for Tour Toontown."
MoreXpHolidayStart = 'Good news! Exclusive Test Toon 5x gag experience time has started.'
MoreXpHolidayOngoing = 'Welcome! Exclusive Test Toon 5x gag experience time is currently ongoing.'
MoreXpHolidayEnd = 'Exclusive Test Toon 5x gag experience time has ended. Thanks for helping us Test things!'
JellybeanDayHolidayStart = "It's Jellybean Day! Get Double Jellybean rewards at Parties!"
JellybeanDayHolidayEnd = "That's all for Jellybean Day. See you next year."
PartyRewardDoubledJellybean = 'Double Jellybeans!'
GrandPrixWeekendHolidayStart = "It's Grand Prix Weekend at Goofy Speedway! Free and paid players collect the most points in three consecutive races."
GrandPrixWeekendHolidayEnd = "That's all for Grand Prix Weekend. See you next year."
KartRace_DoubleTickets = 'Double Tickets'
SellbotNerfHolidayStart = 'Operation: Storm Sellbot is happening now! Battle the VP today!'
SellbotNerfHolidayEnd = 'Operation: Storm Sellbot has ended. Great work, Toons!'
JellybeanTrolleyHolidayStart = 'Double Bean Days for Trolley Games have begun!'
JellybeanTrolleyHolidayEnd = 'Double Bean Days for Trolley Games have ended!'
JellybeanFishingHolidayStart = 'Double Bean Days for Fishing have begun!'
JellybeanFishingHolidayEnd = 'Double Bean Days for Fishing have ended!'
JellybeanPartiesHolidayStart = "It's Jellybean Week! Get Double Jellybean rewards!"
JellybeanPartiesHolidayEnd = "That's all for Jellybean Week. See you next year."
JellybeanMonthHolidayStart = 'Celebrate Toontown with double beans, Cattlelog items and silly surprises!'
BankUpgradeHolidayStart = 'Something Toontastic happened to your Jellybean Bank!'
HalloweenPropsHolidayStart = "It's Halloween in Toontown!"
HalloweenPropsHolidayEnd = 'Halloween has ended. Boo!'
SpookyPropsHolidayStart = 'Silly Meter spins Toontown into spooky mode!'
BlackCatHolidayStart = 'Create a Black Cat - Today only!'
BlackCatHolidayEnd = 'Black Cat day has ended!'
SpookyBlackCatHolidayStart = 'Friday 13th means a Black Cat blast!'
TopToonsMarathonStart = "The Top Toons New Year's Day Marathon has begun!"
TopToonsMarathonEnd = "The Top Toons New Year's Day Marathon has ended."
WinterDecorationsStart = "It's Winter Holiday time in Toontown!"
WinterDecorationsEnd = 'Winter Holiday is over - Happy New Year!'
WackyWinterDecorationsStart = 'Brrr! Silly Meter goes from silly to chilly!'
WinterCarolingStart = 'Caroling has come to Toontown. Sing for your Snowman Head - see the News Post for details!'
ExpandedClosetsStart = 'Attention Toons: For a limited time, Members can purchase the new 50 item Closet from the Cattlelog for the low price of 50 Jellybeans!'
KartingTicketsHolidayStart = 'Get double tickets from Practice races at Goofy Speedway today!'
IdesOfMarchStart = 'Toons go GREEN!'
LogoutForced = 'You have done something wrong\n and are being logged out automatically,\n additionally your account may be frozen.\n Try going on a walk outside, it is fun.'
CountryClubToonEnterElevator = '%s \nhas jumped in the golf kart.'
CountryClubBossConfrontedMsg = '%s is battling the Club President!'
ElevatorBlockedRoom = 'All challenges must be defeated first.'
MolesLeft = 'Moles Left: %d'
MolesInstruction = 'Mole Stomp!\nJump on the red moles!'
MolesFinished = 'Mole Stomp successful!'
MolesPityWin = 'Stomp Failed! But the moles left.'
MolesRestarted = 'Stomp Failed! Restarting...'
BustACogInstruction = 'Remove the cog ball!'
BustACogExit = 'Exit for Now'
BustACogHowto = 'How to Play'
BustACogFailure = 'Out of Time!'
BustACogSuccess = 'Success!'
GolfGreenGameScoreString = 'Puzzles Left: %s'
GolfGreenGamePlayerScore = 'Solved %s'
GolfGreenGameBonusGag = 'You won %s!'
GolfGreenGameGotHelp = '%s solved a Puzzle!'
GolfGreenGameDirections = 'Shoot balls using the the mouse\n\n\nMatching three of a color causes the balls to fall\n\n\nRemove all Cog balls from the board'
enterHedgeMaze = 'Race through the Hedge Maze\n for a laff bonus!'
toonFinishedHedgeMaze = '%s \n  finished in %s place!'
hedgeMazePlaces = ['first',
 'second',
 'third',
 'Fourth']
mazeLabel = 'Maze Race!'
BoardingPartyReadme = 'Boarding Group?'
BoardingGroupHide = 'Hide'
BoardingGroupShow = 'Show Boarding Group'
BoardingPartyInform = 'Create an elevator Boarding Group by clicking on another Toon and Inviting them.\nIn this area Boarding Groups cannot have more than %s Toons.'
BoardingPartyTitle = 'Boarding Group'
BoardingPartyTitleMerge = 'Merge Group'
QuitBoardingPartyLeader = 'Disband'
QuitBoardingPartyNonLeader = 'Leave'
QuitBoardingPartyConfirm = 'Are you sure you want to quit this Boarding Group?'
BoardcodeMissing = 'Something went wrong; try again later.'
BoardcodeMinLaffLeader = 'Your group cannot board because you have less than %s laff points.'
BoardcodeMinLaffNonLeaderSingular = 'Your group cannot board because %s has less than %s laff points.'
BoardcodeMinLaffNonLeaderPlural = 'Your group cannot board because %s have less than %s laff points.'
BoardcodePromotionLeader = 'Your group cannot board because you do not have enough promotion merits.'
BoardcodePromotionNonLeaderSingular = 'Your group cannot board because %s does not have enough promotion merits.'
BoardcodePromotionNonLeaderPlural = 'Your group cannot board because %s do not have enough promotion merits.'
BoardcodeSpace = 'Your group cannot board because there is not enough space.'
BoardcodeBattleLeader = 'Your group cannot board because you are in battle.'
BoardcodeBattleNonLeaderSingular = 'Your group cannot board because %s is in battle.'
BoardcodeBattleNonLeaderPlural = 'Your group cannot board because %s are in battle.'
BoardingInviteMinLaffInviter = 'You need %s Laff Points before being a member of this Boarding Group.'
BoardingInviteMinLaffInvitee = '%s needs %s Laff Points before being a member of this Boarding Group.'
BoardingInvitePromotionInviter = 'You need to earn a promotion before being a member of this Boarding Group.'
BoardingInvitePromotionInvitee = '%s needs to earn a promotion before being a member of this Boarding Group.'
BoardingInviteNotPaidInvitee = '%s needs to be a paid Member to be a part of your Boarding Group.'
BoardingInviteeInDiffGroup = '%s is already in a different Boarding Group.'
BoardingInviteeInKickOutList = '%s had been removed by your leader. Only the leader can re-invite removed members.'
BoardingInviteePendingIvite = '%s has a pending invite; try again later.'
BoardingInviteeInElevator = '%s is currently busy; try again later.'
BoardingInviteGroupFull = 'Your Boarding Group is already full.'
BoardingGroupsToLarge = '%s is already in a different Boarding Group that is too large to merge.'
BoardingAlreadyInGroup = 'You cannot accept this invitation because you are part of another Boarding Group.'
BoardingGroupAlreadyFull = 'You cannot accept this invitation because the group is already full.'
BoardingKickOutConfirm = 'Are you sure you want to remove %s?'
BoardingPendingInvite = 'You need to deal with the\n pending invitation first.'
BoardingCannotLeaveZone = 'You cannot leave this area because you are part of a Boarding Group.'
BoardingInviteeMessage = '%s would like you to join their Boarding Group.'
BoardingInviteeMergeMessage = '%s would like you merge with their Boarding Group.'
BoardingInvitingMessage = 'Inviting %s to your Boarding Group.'
BoardingInvitationRejected = '%s has rejected to join your Boarding Group.'
BoardingMessageKickedOut = 'You have been removed from the Boarding Group.'
BoardingMessageInvited = '%s has invited %s to the Boarding Group.'
BoardingMessageLeftGroup = '%s has left the Boarding Group.'
BoardingMessageGroupDissolved = 'Your Boarding Group was disbanded by the group leader.'
BoardingMessageGroupDisbandedGeneric = 'Your Boarding Group was disbanded.'
BoardingMessageInvitationFailed = '%s tried to invite you to their Boarding Group.'
BoardingMessageGroupFull = '%s tried to accept your invitation but your group was full.'
BoardingGo = 'GO'
BoardingCancelGo = 'Click Again to\nCancel Go'
And = 'and'
BoardingGoingTo = 'Going To:'
BoardingTimeWarning = 'Boarding the elevator in '
BoardingMore = 'more'
BoardingGoShow = 'Going to\n%s in '
BoardingGoPreShow = 'Confirming...'
BossbotBossName = 'C.E.O.'
BossbotRTWelcome = 'You toons will need different disguises.'
BossbotRTRemoveSuit = 'First take off your cog suits...'
BossbotRTFightWaiter = 'and then fight these waiters.'
BossbotRTWearWaiter = "Good Job! Now put on the waiters' clothes."
BossbotBossPreTwo1 = "What's taking so long? "
BossbotBossPreTwo2 = 'Get cracking and serve my banquet!'
BossbotRTServeFood1 = 'Hehe, serve the food I place on these conveyor belts.'
BossbotRTServeFood2 = 'If you serve a cog three times in a row it will explode.'
BossbotResistanceToonName = "Good ol' Gil Giggles"
BossbotPhase3Speech1 = "What's happening here?!"
BossbotPhase3Speech2 = 'These waiters are toons!'
BossbotPhase3Speech3 = 'Get them!!!'
BossbotPhase4Speech1 = 'Hrrmmpph. When I need a job done right...'
BossbotPhase4Speech2 = "I'll do it myself."
BossbotRTPhase4Speech1 = 'Nice! You took out the diners! Use the seltzer bottles to squirt the C.E.O.'
BossbotRTPhase4Speech2 = 'Use the golf tees to slow down the C.E.O. and weaken his defenses.'
BossbotRTPhase4Speech3 = 'Powerful shots against the C.E.O., when he is slowed down, have a higher chance to stun him!'
BossbotPitcherLeave = 'Leave Bottle'
BossbotPitcherLeaving = 'Leaving Bottle'
BossbotPitcherAdvice = 'Use the left and right keys to rotate.\nHold down Ctrl increase power.\nRelease Ctrl to fire.'
BossbotGolfSpotLeave = 'Leave Golf Ball'
BossbotGolfSpotLeaving = 'Leaving Golf Ball'
BossbotGolfSpotAdvice = 'Use the left and right keys to rotate.\nCtrl to fire.'
BossbotRewardSpeech1 = "No! The Chairman won't like this."
BossbotRewardSpeech2 = 'Arrrggghhh!!!!'
BossbotRTCongratulations = "You did it!  You've demoted the C.E.O.!\x07Here, take these pink slips the C.E.O. left behind.\x07With it you'll be able to fire Cogs in a battle."
BossbotRTHPBoost = "\x07You've done a lot of work for the Resistance.\x07The Toon Council has decided to give you another Laff point. Congratulations!"
BossbotRTLevelPromotion = "\x07Say--that C.E.O. Cog left behind your promotion papers.\x07I'll file them for you on the way out, so you'll get your promotion!"
BossbotRTSuitPromotion = "\x07It seems like you've reached the highest level you can for a %s.\x07You can continue upgrading your Cog suit through the disguise page in your Shticker Book.\x07Along with getting a new Cog suit, you will also get a 1 point Laff boost!"
BossbotRTLastPromotion = "\x07Wow, you've reached level %s on your Cog suit!\x07I'm pretty sure Cogs don't get promoted higher than that.\x07You can begin upgrading your V2.0 Cog suit anymore through hard mode bosses!!"
BossbotRTLastRevivePromotion = "\x07Wow, you've reached level %s on your V2.0 Cog suit!\x07I'm pretty sure Cogs don't get promoted higher than that.\x07You can't upgrade your Cog suit anymore, but you can certainly keep working for the Resistance!!"
BossbotRTMaxed = '\x07I see that you have a level %s Cog suit. Very impressive!\x07On behalf of the Toon Council, thank you for coming back to rescue more Toons!'
GolfAreaAttackTaunt = 'Fore!'
OvertimeAttackTaunts = ["It's time to reorganize.", "Now let's downsize."]
ElevatorBossBotBoss = 'Bossbot Clubhouse'
ElevatorBossBotCourse0 = 'The Front Three'
ElevatorBossBotCourse1 = 'The Middle Six'
ElevatorBossBotCourse2 = 'The Back Nine'
ElevatorCashBotBoss = 'Cashbot Vault'
ElevatorCashBotMint0 = 'Coin Mint'
ElevatorCashBotMint1 = 'Dollar Mint'
ElevatorCashBotMint2 = 'Bullion Mint'
ElevatorSellBotBoss = 'Sellbot Towers'
ElevatorSellBotFactory0 = 'Front Entrance'
ElevatorSellBotFactory1 = 'Side Entrance'
ElevatorLawBotBoss = 'Lawbot Courthouse'
ElevatorLawBotCourse0 = 'Office A'
ElevatorLawBotCourse1 = 'Office B'
ElevatorLawBotCourse2 = 'Office C'
ElevatorLawBotCourse3 = 'Office D'
DaysToGo = 'Wait\n%s Days'
IceGameTitle = 'Ice Slide'
IceGameInstructions = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points and avoid the TNT!'
IceGameInstructionsNoTnt = 'Get as close to the center by the end of the second round. Use arrow keys to change direction and force. Press Ctrl to launch your toon.  Hit barrels for extra points.'
IceGameWaitingForPlayersToFinishMove = 'Waiting for other players...'
IceGameWaitingForAISync = 'Waiting for other players...'
IceGameInfo = 'Match %(curMatch)d/%(numMatch)d, Round %(curRound)d/%(numRound)d'
IceGameControlKeyWarning = 'Remember to press the Ctrl key!'
PicnicTableJoinButton = 'Join'
PicnicTableObserveButton = 'Observe'
PicnicTableCancelButton = 'Cancel'
PicnicTableTutorial = 'How To Play'
PicnicTableMenuTutorial = 'What game do you want to learn?'
PicnicTableMenuSelect = 'What game do you want to play?'
ChineseCheckersGetUpButton = 'Get Up'
ChineseCheckersStartButton = 'Start Game'
ChineseCheckersQuitButton = 'Quit Game'
ChineseCheckersIts = "It's "
ChineseCheckersYourTurn = 'Your Turn'
ChineseCheckersGreenTurn = "Green's Turn"
ChineseCheckersYellowTurn = "Yellow's Turn"
ChineseCheckersPurpleTurn = "Purple's Turn"
ChineseCheckersBlueTurn = "Blue's Turn"
ChineseCheckersPinkTurn = "Pink's Turn"
ChineseCheckersRedTurn = "Red's Turn"
ChineseCheckersColorG = 'You are Green'
ChineseCheckersColorY = 'You are Yellow'
ChineseCheckersColorP = 'You are Purple'
ChineseCheckersColorB = 'You are Blue'
ChineseCheckersColorPink = 'You are Pink'
ChineseCheckersColorR = 'You are Red'
ChineseCheckersColorO = 'You are Observing'
ChineseCheckersYouWon = 'You just won a game of Chinese Checkers!'
ChineseCheckers = 'Chinese Checkers.'
ChineseCheckersGameOf = ' has just won a game of '
ChineseTutorialTitle1 = 'Objective'
ChineseTutorialTitle2 = 'How to Play'
ChineseTutorialPrev = 'Previous Page'
ChineseTutorialNext = 'Next Page'
ChineseTutorialDone = 'Done'
ChinesePage1 = 'The goal of Chinese Checkers is to be the first  player to move all of your marbles from the bottom triangle across the board and into the triangle at the top. The first player to do so wins!'
ChinesePage2 = 'Players take turns moving any marble of their own color.  A marble can move into an adjacent hole or it can hop over other marbles. Hops must go over a marble and end in an empty hole. It is possible to chain hops together for longer moves!'
CheckersPage1 = 'The goal of Checkers is to leave the opponent without any possible moves. To do this you can either capture all of his peices or block them in such that he has no available moves.'
CheckersPage2 = 'Players take turns moving any peice of their own color. A peice can move one square diagonal and forward. A peice can only move into a square that is not occupied by another peice. Kings follow the same rules but are allowed to move backwards.'
CheckersPage3 = 'To capture an opponents peice your peice must jump over it diagonally into the vacant square beyond it. If you have any jump moves during a turn, you must do one of them. You can chain jump moves together as long as it is with the same peice.'
CheckersPage4 = 'A peice becomes a king when it reaches the last row on the board. A peice that has just become a king cannot continue jumping until the next turn. Additionally, kings are allowed to move all directions and are allowed to change directions while jumping.'
CheckersGetUpButton = 'Get Up'
CheckersStartButton = 'Start Game'
CheckersQuitButton = 'Quit Game'
CheckersIts = "It's "
CheckersYourTurn = 'Your Turn'
CheckersWhiteTurn = "White's Turn"
CheckersBlackTurn = "Black's Turn"
CheckersColorWhite = 'You are White'
CheckersColorBlack = 'You are Black'
CheckersObserver = 'You are Observing'
RegularCheckers = 'Checkers.'
RegularCheckersGameOf = ' has just won a game of '
RegularCheckersYouWon = 'You just won a game of Checkers!'
MailNotifyNewItems = "You've got mail!"
MailNewMailButton = 'Mail'
MailSimpleMail = 'Note'
MailFromTag = 'Note From: %s'
AwardNotifyNewItems = 'You have a new award in your mailbox!'
AwardNotifyOldItems = 'There are still awards waiting in your mailbox for you to pick up!'
InviteInvitation = 'the invitation'
InviteAcceptInvalidError = 'The invitation is no longer valid.'
InviteAcceptPartyInvalid = 'That party has been cancelled.'
InviteAcceptAllOk = 'The host has been informed of your reply.'
InviteRejectAllOk = 'The host has been informed that you declined the invitation.'
Months = {1: 'JANUARY',
 2: 'FEBRUARY',
 3: 'MARCH',
 4: 'APRIL',
 5: 'MAY',
 6: 'JUNE',
 7: 'JULY',
 8: 'AUGUST',
 9: 'SEPTEMBER',
 10: 'OCTOBER',
 11: 'NOVEMBER',
 12: 'DECEMBER'}
DayNames = ('Monday',
 'Tuesday',
 'Wednesday',
 'Thursday',
 'Friday',
 'Saturday',
 'Sunday')
DayNamesAbbrev = ('MON',
 'TUE',
 'WED',
 'THU',
 'FRI',
 'SAT',
 'SUN')
HolidayNamesInCalendar = {1: ('Summer Fireworks', 'Celebrate Summer with a fireworks show every hour in each playground!'),
 2: ('New Year Fireworks', 'Happy New Year! Enjoy a fireworks show every hour in each playground!'),
 3: ('Bloodsucker Invasion', 'Help defend Toontown from the Bloodsucker invasion!'),
 4: ('Winter Holiday', 'Celebrate the Winter Holiday with Toontastic decorations, party and Cattlelog items, and more!'),
 5: ('Skelecog Invasion', 'Stop the Skelecogs from invading Toontown!'),
 6: ('Mr. Hollywood Invasion', 'Stop the Mr. Hollywood Cogs from invading Toontown!'),
 7: ('Fish Bingo', 'Fish Bingo Wednesday! Everyone at the pond works together to complete the card before time runs out.'),
 8: ('Toon Species Election', 'Vote on the new Toon species! Will it be Goat? Will it be Pig?'),
 9: ('Black Cat Day', 'Happy Halloween! Create a Toontastic Black Cat Toon - Today Only!'),
 13: ('Trick or Treat', 'Happy Halloween! Trick or treat throughout Toontown to get a nifty Halloween pumpkin head reward!'),
 14: ('Grand Prix', 'Grand Prix Monday at Goofy Speedway! To win, collect the most points in three consecutive races!'),
 16: ('Grand Prix Weekend', 'Free and Paid players compete in circuit races at Goofy Speedway!'),
 17: ('Trolley Tracks', 'Trolley Tracks Thursday! Board any Trolley with two or more Toons to play.'),
 19: ('Silly Saturdays', 'Saturdays are silly with Fish Bingo and Grand Prix throughout the day!'),
 24: ('Ides of March', 'Beware the Ides of March! Stop the Backstabber Cogs from invading Toontown!'),
 25: ('5x Gag Experience', 'Recieve 5 times the gag experience from battles!'),
 26: ('Halloween Decor', 'Celebrate Halloween as spooky trees and streetlights transform Toontown!'),
 28: ('Winter Invasion', 'The sellbots are on the loose spreading their cold sales tactics!'),
 29: ("April Toons' Week", "Celebrate April Toons' Week - a holiday built by Toons for Toons!"),
 33: ('Sellbot Surprise 1', 'Sellbot Surprise! Stop the Cold Caller Cogs from invading Toontown!'),
 34: ('Sellbot Surprise 2', 'Sellbot Surprise! Stop the Name Dropper Cogs from invading Toontown!'),
 35: ('Sellbot Surprise 3', 'Sellbot Surprise! Stop the Gladhander Cogs from invading Toontown!'),
 36: ('Sellbot Surprise 4', 'Sellbot Surprise! Stop the Mover & Shaker Cogs from invading Toontown!'),
 37: ('A Cashbot Conundrum 1', 'A Cashbot Conundrum. Stop the Short Change Cogs from invading Toontown!'),
 38: ('A Cashbot Conundrum 2', 'A Cashbot Conundrum. Stop the Penny Pincher Cogs from invading Toontown!'),
 39: ('A Cashbot Conundrum 3', 'A Cashbot Conundrum. Stop the Bean Counter Cogs from invading Toontown!'),
 40: ('A Cashbot Conundrum 4', 'A Cashbot Conundrum. Stop the Number Cruncher Cogs from invading Toontown!'),
 41: ('The Lawbot Gambit 1', 'The Lawbot Gambit. Stop the Bottomfeeder Cogs from invading Toontown!'),
 42: ('The Lawbot Gambit 2', 'The Lawbot Gambit. Stop the Double Talker Cogs from invading Toontown!'),
 43: ('The Lawbot Gambit 3', 'The Lawbot Gambit. Stop the Ambulance Chaser Cogs from invading Toontown!'),
 44: ('The Lawbot Gambit 4', 'The Lawbot Gambit. Stop the Backstabber Cogs from invading Toontown!'),
 45: ('The Trouble With Bossbots 1', 'The Trouble with Bossbots. Stop the Flunky Cogs from invading Toontown!'),
 46: ('The Trouble With Bossbots 2', 'The Trouble with Bossbots. Stop the Pencil Pusher Cogs from invading Toontown!'),
 47: ('The Trouble With Bossbots 3', 'The Trouble with Bossbots. Stop the Micromanager Cogs from invading Toontown!'),
 48: ('The Trouble With Bossbots 4', 'The Trouble with Bossbots. Stop the Downsizer Cogs from invading Toontown!'),
 49: ('Jellybean Day', 'Celebrate Jellybean Day with double Jellybean rewards at parties!'),
 53: ('Cold Caller Invasion', 'Stop the Cold Caller Cogs from invading Toontown!'),
 54: ('Bean Counter Invasion', 'Stop the Bean Counter Cogs from invading Toontown!'),
 55: ('Double Talker Invasion', 'Stop the Double Talker Cogs from invading Toontown!'),
 56: ('Downsizer Invasion', 'Stop the Downsizer Cogs from invading Toontown!'),
 57: ('Caroling', 'Sing for your Snowman Head! See the News Post for details!'),
 59: ("ValenToon's Day", "Celebrate ValenToon's Day from Feb 09 to Feb 16!"),
 72: ('Yes Men Invasion', 'Stop the Yes Men Cogs from invading Toontown!'),
 73: ('Tightwad Invasion', 'Stop the Tightwad Cogs from invading Toontown!'),
 74: ('Telemarketers Invasion', 'Stop the Telemarketer Cogs from invading Toontown!'),
 75: ('Head Hunter Invasion', 'Stop the Head Hunter Cogs from invading Toontown!'),
 76: ('Spin Doctor Invasion', 'Stop the Spin Doctor Cogs from invading Toontown!'),
 77: ('Moneybags Invasion', 'Stop the Moneybags from invading Toontown!'),
 78: ('Two-faces Invasion', 'Stop the Two-faces from invading Toontown!'),
 79: ('Mingler Invasion', 'Stop the Mingler Cogs from invading Toontown!'),
 80: ('Loan Shark Invasion', 'Stop the Loanshark Cogs from invading Toontown!'),
 81: ('Corporate Raider Invasion', 'Stop the Corporate Raider Cogs from invading Toontown!'),
 82: ('Robber Baron Invasion', 'Stop the Robber Baron Cogs from invading Toontown!'),
 83: ('Legal Eagle Invasion', 'Stop the Legal Eagle Cogs from invading Toontown!'),
 84: ('Big Wig Invasion', 'Stop the Big Wig Cogs from invading Toontown!'),
 85: ('Big Cheese Invasion', 'Stop the Big Cheese from invading Toontown!'),
 86: ('Down Sizer Invasion', 'Stop the Down Sizer Cogs from invading Toontown!'),
 87: ('Mover And Shaker Invasion', 'Stop the Mover and Shaker Cogs from invading Toontown!'),
 88: ('Double Talker Invasion', 'Stop the Double Talkers Cogs from invading Toontown!'),
 89: ('Penny Pincher Invasion', 'Stop the Penny Pinchers Cogs from invading Toontown!'),
 90: ('Name Dropper Invasion', 'Stop the Name Dropper Cogs from invading Toontown!'),
 91: ('Ambulance Chaser Invasion', 'Stop the Ambulance Chaser Cogs from invading Toontown!'),
 92: ('Micro Manager Invasion', 'Stop the Micro Manager Cogs from invading Toontown!'),
 93: ('Number Cruncher Invasion', 'Stop the Number Cruncher Cogs from invading Toontown!'),
 95: ('Victory Parties', 'Celebrate our historic triumph against the Cogs!'),
 96: ('Operation: Storm Sellbot', "Sellbot HQ is open to everyone. Let's go fight the VP!"),
 97: ('Double Bean Days - Trolley Games', ''),
 98: ('Double Bean Days - Fishing', ''),
 99: ('Jellybean Week', 'Celebrate Jellybean Week with double Jellybean rewards!'),
 101: ("Top Toons New Year's Day Marathon", "Chances to win every hour! See the What's New Blog for details!"),
 105: ('Toons go GREEN!', 'Toons make a green scene at Green Bean Jeans on Oak Street in Daisy Gardens!')}
UnknownHoliday = 'Unknown Holiday %d'
HolidayFormat = '%b %d '
HourFormat = '12'
CogdoBarrelRoomTitle = 'Grab-O-Barrel'
CogdoBarrelIntroMovieDialogue = 'Grab as many barrels as you possibly can before the time runs out, and the COGS arrive!'
CogdoMemoGuiTitle = 'Memos:'
CogdoMemoNames = 'Barrel-Destruction Memos'
CogdoStomperName = 'Stomp-O-Matic'
BoardroomGameTitle = 'Boardroom Hijinks'
BoardroomGameInstructions = 'The COGS are having a meeting to decide what to do with stolen gags. Slide on through and grab as many gag-destruction memos as you can!'
CogdoCraneGameTitle = 'Vend-A-Stomper'
CogdoCraneGameInstructions = 'The COGS are using a coin-operated machine to destroy laff barrels. Use the cranes to pick up and throw money bags, in order to prevent barrel destruction!'
CogdoMazeGameTitle = 'Mover & Shaker\nField Office'
CogdoMazeGameInstructions = 'The big Mover & Shaker Cogs have the code to open the door. Defeat them with your water balloons in order to get it!'
CogdoMazeIntroMovieDialogue = (("This is the Toon Resistance! The Movers & Shakers\nhave our Jokes, and they've locked the exit!",), ('Grab water balloons at coolers, and throw them at Cogs!\nSmall Cogs drop Jokes, BIG COGS open the exit.',), ('The more Jokes you rescue, the bigger your Toon-Up\nat the end. Good luck!',))
CogdoMazeGameDoorOpens = 'THE EXIT IS OPEN FOR 60 SECONDS!\nGET THERE FAST FOR A BIGGER TOON-UP'
CogdoMazeGameLocalToonFoundExit = "The exit will open when\nyou've busted all four BIG COGS!"
CogdoMazeGameWaitingForToons = 'Waiting for other Toons...'
CogdoMazeGameTimeOut = 'Oh no, time ran out! You lost your jokes.'
CogdoMazeGameTimeAlert = 'Hurry up! 60 seconds to go!'
CogdoMazeGameBossGuiTitle = 'BIG COGS:'
CogdoMazeFindHint = 'Find a Water Cooler'
CogdoMazeThrowHint = "Press 'Ctrl' to throw your water balloon"
CogdoMazeSquashHint = 'Falling objects pop your balloon'
CogdoMazeBossHint = 'Big Cogs take TWO hits to defeat'
CogdoMazeMinionHint = 'Smaller Cogs drop jokes'
CogdoFlyingGameTitle = 'Legal Eagle Offices'
CogdoFlyingGameInstructions = "Fly through the Legal Eagles' lair. Watch out for obstacles and cogs along the way, and don't forget to refuel your helicopter!"
CogdoFlyingIntroMovieDialogue = (("You won't ruffle our feathers, Toons! We're destroying barrels of your Laff, and you cannot stop us!", "A flock of Toons! We're crushing barrels of your Laff in our %s, and there's nothing you can do about it!" % CogdoStomperName, "You can't egg us on, Toons! We're powering our offices with your Laff, and you're powerless to stop us!"), ('This is the Toon Resistance! A little bird told me you can use propellers to fly around, grab Barrel Destruction Memos, and keep Laff from being destroyed! Good luck, Toons!', 'Attention Toons! Wing it with a propeller and collect Barrel Destruction Memos to keep our Laff from being stomped! Toon Resistance out!', 'Toon Resistance here! Cause a flap by finding propellers, flying to the Barrel Destruction Memos, and keeping our Laff from being smashed! Have fun!'), ("Squawk! I'm a Silver Sprocket Award winner, I don't need this!", 'Do your best, Toons! You will find us to be quite talon-ted!', "We'll teach you to obey the pecking order, Toons!"))
CogdoFlyingGameWaiting = 'Waiting for other Toons%s'
CogdoFlyingGameFuelLabel = 'Fuel'
CogdoFlyingGameInvasionTargeting = 'A %s has noticed you!'
CogdoFlyingGameInvasionAttacking = 'Incoming %s!'
CogdoFlyingGameLegalEagleTargeting = 'A Legal Eagle has noticed you!'
CogdoFlyingGameLegalEagleAttacking = 'Incoming Eagle!'
CogdoFlyingGamePickUpAPropeller = 'You need a propeller to fly!'
CogdoFlyingGamePressCtrlToFly = "Press 'Ctrl' to fly up!"
CogdoFlyingGameYouAreInvincible = 'Red Tape protects you!'
CogdoFlyingGameTimeIsRunningOut = 'Time is running out!'
CogdoFlyingGameMinimapIntro = 'This meter shows your progress!\nX marks the finish line.'
CogdoFlyingGameMemoIntro = 'Memos prevent Laff Barrels in\nthe Stomper Room from being destroyed!'
CogdoFlyingGameOutOfTime = 'Oh No! You ran out of time!'
CogdoFlyingGameYouMadeIt = 'You made it on time!'
CogdoFlyingGameYouMadeIt = 'Good work, you made it on time!'
CogdoFlyingGameTakingMemos = 'The Legal Eagles took all your memos!'
CogdoFlyingGameTakingMemosInvasion = 'The %s took all your memos!'
CogdoElevatorRewardLaff = 'Great job, Toons!\nYou get a Toon-Up from the jokes you saved!'
CogdoExecutiveSuiteTitle = 'Executive Suite'
CogdoExecutiveSuiteIntroMessage = "Oh no, they've got the shop keeper!\nDefeat the Cogs and free the captive."
CogdoExecutiveSuiteToonThankYou = 'Thanks for the rescue!\nIf you need help in a fight, use this SOS card to call my friend %s.'
CogdoLawbotExecutiveSuiteToonThankYou = "Thanks for the rescue!\nIt seems the Cogs didn't leave behind the key to the Sprocket Award case.\x07Instead, use these summons I found laying around. You can summon Cogs with them!"
CogdoExecutiveSuiteToonBye = 'Bye!'
SillySurgeTerms = {1: 'Amusing Ascent!',
 2: 'Silly Surge!',
 3: 'Ridiculous Rise!',
 4: 'Giggle Growth!',
 5: 'Funny Fueling!',
 6: 'Thundering Thrill!',
 7: 'Crazy Climb!',
 8: 'Jolly Jump!',
 9: 'Loony Lift!',
 10: 'Hilarity Hike!',
 11: 'Insanity Increase!',
 12: 'Cracked-Uptick!'}
InteractivePropTrackBonusTerms = {0: 'Super Toon-Up!',
 1: '',
 2: '',
 3: '',
 4: 'Super Throw!',
 5: 'Super Squirt!',
 6: ''}
PlayingCardUnknown = 'Card Name is unknown'

# Controls
RemapPrompt = 'Choose the keys you wish to remap.'
RemapPopup = 'Press the key you wish to remap this control to.'
Controls = ['Move Up:', 'Move Left:', 'Move Down:', 'Move Right:',
            'Jump:', 'Action Key:', 'Options Hotkey:', 'Chatbox Hotkey:', 'Screenshot Key:', 'Interact Key:']
			
GatorChatter = ["Don't be a hater, vote for Gator!", 'My favorite jellybean color is green.', 'Wooow! I hope I win the election!', 'How are you guys doing?']
BeaverChatter = ["Got spring fever? Vote for Beaver!", 'My favorite jellybean color is brown.', "If I win, I will build new houses for all toons. How does that sound?", "Gator's alright, but you beaver belive that I'm winning.", 'Be a believer! Vote Beaver!']
FoxChatter = ["Fox Rox!", 'My favorite jellybean color is orange.', "I'm adorable, how could you not vote for me? Owoooo!", "I'm the perfect combination of cat and dog!", 'Nobody mocks the fox, ya hear?']
BatChatter = ["Don't be a brat, vote for Bat!", 'My favorite jellybean color is black.', "Whoooo dares awaken me!", "Got questions?", 'I gotta earn my wings, first.']
RaccoonChatter = ["Sing some tunes and vote Raccoon!", 'My favorite jellybean color is purple.', "Oooh! There is half of an apple in here!", 'My friends call me "Trash Panda."', "I'm not rabid, I swear!"]

