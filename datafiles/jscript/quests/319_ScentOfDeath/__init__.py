# Made by Mr. - Version 0.3 by DrLecter
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "319_ScentOfDeath"

ZOMBIE_SKIN = 1045
ADENA = 57
HEALING_POTION = 1061

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "30138-04.htm" :
      st.set("cond","1")
      st.setState(STARTED)
      st.playSound("ItemSound.quest_accept")
    return htmltext

 def onTalk (self,npc,player):
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   st = player.getQuestState(qn)
   if not st : return htmltext

   npcId = npc.getNpcId()
   id = st.getState()
   if id == CREATED :
     st.set("cond","0")
   if int(st.get("cond"))==0 :
     if st.getPlayer().getLevel() >= 11 :
       htmltext = "30138-03.htm"
     else:
       htmltext = "30138-02.htm"
       st.exitQuest(1)
   else :
     if st.getQuestItemsCount(ZOMBIE_SKIN)<5 :
       htmltext = "30138-05.htm"
     else :
       htmltext = "30138-06.htm"
       st.giveItems(ADENA,3350)
       st.giveItems(HEALING_POTION,1)
       st.takeItems(ZOMBIE_SKIN,-1)
       st.exitQuest(1)
       st.playSound("ItemSound.quest_finish")
   return htmltext

 def onKill (self,npc,player):
   st = player.getQuestState(qn)
   if not st : return 
   if st.getState() != STARTED : return 
   
   count = st.getQuestItemsCount(ZOMBIE_SKIN)
   if count < 5 and st.getRandom(10) > 7 :
     st.giveItems(ZOMBIE_SKIN,1)
     if count == 4 :
       st.playSound("ItemSound.quest_middle")
       st.set("cond","2")
     else :
       st.playSound("ItemSound.quest_itemget")
   return

QUEST       = Quest(319,qn,"Scent Of Death")
CREATED     = State('Start', QUEST)
STARTING    = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(30138)

QUEST.addTalkId(30138)

QUEST.addKillId(20015)
QUEST.addKillId(20020)

STARTED.addQuestDrop(20015,ZOMBIE_SKIN,1)

print "importing quests: 319: Scent Of Death"
