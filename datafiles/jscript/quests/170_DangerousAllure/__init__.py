# Maked by Mr. Have fun! Version 0.2
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "170_DangerousAllure"

NIGHTMARE_CRYSTAL = 1046

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "1" :
       htmltext = "30305-04.htm"
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
   cond=st.getInt("cond")
   if id == COMPLETED :
      htmltext = "<html><head><body>This quest have already been completed.</body></html>"
   elif cond == 0 :
      if st.getPlayer().getRace().ordinal() != 2 :
         htmltext = "30305-00.htm"
         st.exitQuest(1)
      elif st.getPlayer().getLevel() > 20 :
         htmltext = "30305-03.htm"
      else:
         htmltext = "30305-02.htm"
         st.exitQuest(1)
   elif cond :
      if st.getQuestItemsCount(NIGHTMARE_CRYSTAL) :
         htmltext = "30305-06.htm"
         st.giveItems(57,102680)
         st.takeItems(NIGHTMARE_CRYSTAL,-1)
         st.setState(COMPLETED)
         st.playSound("ItemSound.quest_finish")
      else :
         htmltext = "30305-05.htm"
   return htmltext

 def onKill (self,npc,player):
   st = player.getQuestState(qn)
   if not st : return 
   if st.getState() != STARTED : return

   npcId = npc.getNpcId()
   if int(st.get("cond")) == 1 :
      st.giveItems(NIGHTMARE_CRYSTAL,1)
      st.playSound("ItemSound.quest_middle")
      st.set("cond","2")
   return

QUEST       = Quest(170,qn,"Dangerous Allure")
CREATED     = State('Start', QUEST)
STARTING     = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(30305)

QUEST.addTalkId(30305)

QUEST.addKillId(27022)
STARTED.addQuestDrop(27022,NIGHTMARE_CRYSTAL,1)

print "importing quests: 170: Dangerous Allure"
