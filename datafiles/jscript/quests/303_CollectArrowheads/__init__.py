# Made by Mr. Have fun! - Version 0.3 by DrLecter
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "303_CollectArrowheads"

ORCISH_ARROWHEAD = 963
ADENA = 57

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "30029-04.htm" :
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
     if st.getPlayer().getLevel() >= 10 :
        htmltext = "30029-03.htm"
     else:
        htmltext = "30029-02.htm"
        st.exitQuest(1)
   else :
     if st.getQuestItemsCount(ORCISH_ARROWHEAD)<10 :
       htmltext = "30029-05.htm"
     else :
       st.giveItems(ADENA,1000)
       st.takeItems(ORCISH_ARROWHEAD,-1)
       st.playSound("ItemSound.quest_finish")
       st.addExpAndSp(2000,0)
       htmltext = "30029-06.htm"
       st.exitQuest(1)
   return htmltext

 def onKill (self,npc,player):
   st = player.getQuestState(qn)
   if not st : return 
   if st.getState() != STARTED : return 
   
   count=st.getQuestItemsCount(ORCISH_ARROWHEAD)
   if count<10 and st.getRandom(100)<40 :
     st.giveItems(ORCISH_ARROWHEAD,1)
     if count == 9 :
       st.set("cond","2") 
       st.playSound("ItemSound.quest_middle")
     else:
       st.playSound("ItemSound.quest_itemget")
   return

QUEST       = Quest(303,qn,"Collect Arrowheads")
CREATED     = State('Start', QUEST)
STARTING    = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(30029)

QUEST.addTalkId(30029)

QUEST.addKillId(20361)
STARTED.addQuestDrop(20361,ORCISH_ARROWHEAD,1)

print "importing quests: 303: Collect Arrowheads"
