# Maked by Mr. Have fun! Version 0.2
# rewritten by Rolarga Version 0.3
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "222_TestOfDuelist"

MARK_OF_DUELIST_ID,  ORDER_GLUDIO_ID,      ORDER_DION_ID,        ORDER_GIRAN_ID,      ORDER_OREN_ID,      \
ORDER_ADEN_ID,       PUNCHERS_SHARD_ID,    NOBLE_ANTS_FEELER_ID, DRONES_CHITIN_ID,    DEADSEEKER_FANG_ID, \
OVERLORD_NECKLACE_ID,CRIMSONBINDS_CHAIN_ID,CHIEFS_AMULET_ID,     TEMPERED_EYE_MEAT_ID,TAMRIN_ORCS_RING_ID,\
TAMRIN_ORCS_ARROW_ID,FINAL_ORDER_ID,       EXCUROS_SKIN_ID,      KRATORS_SHARD_ID,    GRANDIS_SKIN_ID,    \
TIMAK_ORCS_BELT_ID,  RAKINS_MACE_ID = range(2762,2784)

DROPLIST={
20085:(1,10,PUNCHERS_SHARD_ID),
20090:(1,10,NOBLE_ANTS_FEELER_ID),
20234:(1,10,DRONES_CHITIN_ID),
20202:(1,10,DEADSEEKER_FANG_ID),
20270:(1,10,OVERLORD_NECKLACE_ID),
20552:(1,10,CRIMSONBINDS_CHAIN_ID),
20582:(1,10,CHIEFS_AMULET_ID),
20564:(1,10,TEMPERED_EYE_MEAT_ID),
20601:(1,10,TAMRIN_ORCS_RING_ID),
20602:(1,10,TAMRIN_ORCS_ARROW_ID),
20604:(2,3,RAKINS_MACE_ID),
20214:(2,3,EXCUROS_SKIN_ID),
20217:(2,3,KRATORS_SHARD_ID),
20588:(2,3,TIMAK_ORCS_BELT_ID),
20554:(2,3,GRANDIS_SKIN_ID)
}


class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
    htmltext = event
    if event == "30623-07.htm" :
        if int(st.get("step"))==0 :
           st.set("cond","1")
           st.set("step","1")
           st.setState(STARTED)
           st.playSound("ItemSound.quest_accept")
           st.giveItems(ORDER_GLUDIO_ID,1)
           st.giveItems(ORDER_DION_ID,1)
           st.giveItems(ORDER_GIRAN_ID,1)
           st.giveItems(ORDER_OREN_ID,1)
           st.giveItems(ORDER_ADEN_ID,1)
    elif event == "30623-04.htm" :
          if st.getPlayer().getRace().ordinal() == 3 :
            htmltext = "30623-05.htm"
    elif event == "30623-16.htm" :
        if st.getQuestItemsCount(FINAL_ORDER_ID)==0:
            for i in [
            PUNCHERS_SHARD_ID,
            NOBLE_ANTS_FEELER_ID,
            DEADSEEKER_FANG_ID,
            DRONES_CHITIN_ID,
            OVERLORD_NECKLACE_ID,
            CRIMSONBINDS_CHAIN_ID,
            CHIEFS_AMULET_ID,
            TEMPERED_EYE_MEAT_ID,
            TAMRIN_ORCS_RING_ID,
            TAMRIN_ORCS_ARROW_ID,
            ORDER_GLUDIO_ID,
            ORDER_DION_ID,
            ORDER_GIRAN_ID,
            ORDER_OREN_ID,
            ORDER_ADEN_ID
            ]:
             st.takeItems(i,-1)
            st.set("step","2")
            st.giveItems(FINAL_ORDER_ID,1)
    return htmltext


 def onTalk (self,npc,player):
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   st = player.getQuestState(qn)
   if not st : return htmltext

   npcId = npc.getNpcId()
   id = st.getState()
   if id == CREATED :
     st.set("step","0")
     st.set("cond","0")
   if id == COMPLETED :
      htmltext = "<html><head><body>This quest has already been completed.</body></html>"
   elif int(st.get("step"))==0 :
      if st.getPlayer().getClassId().getId() in [0x01,0x2f,0x13,0x20] :
         if st.getPlayer().getLevel() >= 39 :
            htmltext = "30623-03.htm"
         else:
            htmltext = "30623-01.htm"
            st.exitQuest(1)
      else:
         htmltext = "30623-02.htm"
         st.exitQuest(1)
   elif int(st.get("step"))==1 :
      if st.getQuestItemsCount(ORDER_GLUDIO_ID) and st.getQuestItemsCount(ORDER_DION_ID) and st.getQuestItemsCount(ORDER_GIRAN_ID) and st.getQuestItemsCount(ORDER_OREN_ID) and st.getQuestItemsCount(ORDER_ADEN_ID) :
        if st.getQuestItemsCount(PUNCHERS_SHARD_ID)==st.getQuestItemsCount(NOBLE_ANTS_FEELER_ID)==st.getQuestItemsCount(DRONES_CHITIN_ID)==st.getQuestItemsCount(DEADSEEKER_FANG_ID)==st.getQuestItemsCount(OVERLORD_NECKLACE_ID)==st.getQuestItemsCount(CRIMSONBINDS_CHAIN_ID)==st.getQuestItemsCount(CHIEFS_AMULET_ID)==st.getQuestItemsCount(TEMPERED_EYE_MEAT_ID)==st.getQuestItemsCount(TAMRIN_ORCS_RING_ID)==st.getQuestItemsCount(TAMRIN_ORCS_ARROW_ID) == 10 :
          htmltext = "30623-13.htm"
        else:
          htmltext = "30623-14.htm"
      else:
          htmltext = "30623-14.htm"
          for i in [ORDER_GLUDIO_ID,ORDER_DION_ID,ORDER_GIRAN_ID,ORDER_OREN_ID,ORDER_ADEN_ID]:
            if st.getQuestItemsCount(i)==0:
                st.giveItems(i,1) 
   elif int(st.get("step"))==2 and st.getQuestItemsCount(FINAL_ORDER_ID) :
        if st.getQuestItemsCount(EXCUROS_SKIN_ID)==st.getQuestItemsCount(KRATORS_SHARD_ID)==st.getQuestItemsCount(RAKINS_MACE_ID)==st.getQuestItemsCount(GRANDIS_SKIN_ID)==st.getQuestItemsCount(TIMAK_ORCS_BELT_ID)>2 :
            st.takeItems(EXCUROS_SKIN_ID,-1)
            st.takeItems(KRATORS_SHARD_ID,-1)
            st.takeItems(GRANDIS_SKIN_ID,-1)
            st.takeItems(TIMAK_ORCS_BELT_ID,-1)
            st.takeItems(RAKINS_MACE_ID,-1)
            st.addExpAndSp(47015,20000)
            st.giveItems(MARK_OF_DUELIST_ID,1)
            st.takeItems(FINAL_ORDER_ID,1)
            htmltext = "30623-18.htm"
            st.unset("step")
            st.set("cond","0")
            st.setState(COMPLETED)
            st.playSound("ItemSound.quest_finish")
        else :
          htmltext = "30623-17.htm"
   return htmltext

 def onKill (self,npc,player):
  st = player.getQuestState(qn)
  if not st : return 
  if st.getState() != STARTED : return 
   
  npcId = npc.getNpcId()
  step,maxcount,item=DROPLIST[npcId]
  count=st.getQuestItemsCount(item)
  if int(st.get("step"))==step and count<maxcount:
   st.giveItems(item,1)
   if count == maxcount-1:
     st.playSound("ItemSound.quest_middle")
   else:
     st.playSound("ItemSound.quest_itemget")
  return

QUEST       = Quest(222,qn,"Test Of Duelist")
CREATED     = State('Start', QUEST)
STARTING    = State('Starting', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)


QUEST.setInitialState(CREATED)
QUEST.addStartNpc(30623)

QUEST.addTalkId(30623)

for i in DROPLIST.keys():
    QUEST.addKillId(i)

print "importing quests: 222: Test Of Duelist"
