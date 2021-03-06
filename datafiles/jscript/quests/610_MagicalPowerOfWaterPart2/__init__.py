#Made by Emperorc
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.actor.instance import L2NpcInstance
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest
from net.sf.l2j.gameserver.datatables import SpawnTable
from net.sf.l2j.gameserver.serverpackets import CreatureSay
from java.util import Iterator
from net.sf.l2j.gameserver.datatables import NpcTable
from net.sf.l2j.gameserver.model import L2Spawn
from net.sf.l2j.gameserver.model.actor.instance import L2MonsterInstance

qn = "610_MagicalPowerOfWaterPart2"

#NPC
Asefa = 31372
Alter = 31560


#MOBS
Ketra_Orcs = [ 21324, 21325, 21327, 21328, 21329, 21331, 21332, 21334, 21335, \
21336, 21338, 21339, 21340, 21342, 21343, 21344, 21345, 21346, 21347, 21348, 21349 ]
Ashutar = 25316

#ITEMS
Totem2 = 7238
Ice_Heart = 7239

def FindTemplate (npcId) :
    for spawn in SpawnTable.getInstance().getSpawnTable().values():
        if spawn.getNpcid() == npcId:
            npcinstance=spawn.getLastSpawn()
            break
    return npcinstance

def AutoChat(npc,text) :
    chars = npc.getKnownList().getKnownPlayers().values().toArray()
    if chars != None:
       for pc in chars :
          sm = CreatureSay(npc.getObjectId(), 0, npc.getName(), text)
          pc.sendPacket(sm)

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self, event, st) :
   cond = st.getInt("cond")
   id = st.getInt("id")
   Green_Totem = st.getQuestItemsCount(Totem2)
   Heart = st.getQuestItemsCount(Ice_Heart)
   htmltext = event
   if event == "31372-04.htm" :
       if st.getPlayer().getLevel() >= 75 and st.getPlayer().getAllianceWithVarkaKetra() >= 2 :
           if Green_Totem :
                st.set("cond","1")
                st.set("id","1")
                st.setState(STARTED)
                st.playSound("ItemSound.quest_accept")
                htmltext = "31372-04.htm"
           else :
                htmltext = "31372-02.htm"
                st.exitQuest(1)
       else :
           htmltext = "31372-03.htm"
           st.exitQuest(1)
   elif event == "31372-08.htm" :
       if Heart:
           htmltext = "31372-08.htm"
           st.takeItems(Ice_Heart,-1)
           st.addExpAndSp(10000,0)
           st.unset("id")
           st.unset("cond")
           st.playSound("ItemSound.quest_finish")
           st.exitQuest(1)
       else :
           htmltext = "31372-09.htm"

   elif event == "31560-02.htm" :
       if Green_Totem :
           htmletext = "31560-02.htm"   #TODO add lights from above
           spawnId = st.getPcSpawn().addSpawn(Ashutar,104825,-36926,-1136)
           st.set("spawnId",str(spawnId))
           st.takeItems(Totem2,1)
           st.set("id","2")
           FindTemplate(Alter).setBusy(True)
           st.set("cond","2")
           st.startQuestTimer("Soul of Water Ashutar has despawned",1200000)#1200000)
           AutoChat(st.getPcSpawn().getSpawn(spawnId).getLastSpawn(),"Hey! I'll kick your aarse!")#this is only a temp message until we find out what it actually is! string = 61050
       else :
           htmltext = "31560-04.htm"
   elif event == "Soul of Water Ashutar has despawned" :
       npc1 = st.getPcSpawn().getSpawn(st.getInt("spawnId")).getLastSpawn()
       npc1.reduceCurrentHp(9999999,npc1)
       st.getPcSpawn().removeAllSpawn()
       st.unset("id")
       st.unset("cond")
       st.unset("spawnId")
       FindTemplate(Alter).setBusy(False)
       st.exitQuest(1)
       AutoChat(npc1,"May the gods forever condemn you! Udan Mardui, your power weakens!") #this is only a temp message until we find out what it actually is! string = 61051
   return htmltext

 def onTalk (self, npc, player):
   st = player.getQuestState(qn)
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   if st :
    npcId = npc.getNpcId()
    cond = st.getInt("cond")
    id = st.getInt("id")
    Green_Totem = st.getQuestItemsCount(Totem2)
    Heart = st.getQuestItemsCount(Ice_Heart)
    if npcId == Asefa :
        if st.getState()== CREATED :
            htmltext = "31372-01.htm"
        elif id == 1 or id == 2 :
            htmltext = "31372-05.htm"
        elif id == 3:
            if Heart :
                htmltext = "31372-06.htm"
            else :
                htmltext = "31372-07.htm"
    elif npcId == Alter :
       if npc.isBusy() :
           htmltext = "31560-03.htm"
       else :
        if id == 1 :
            htmltext = "31560-01.htm"
        elif id == 2 or id == 3 :
            htmltext = "31560-05.htm"
    return htmltext

 def onKill (self, npc, player):
   st = player.getQuestState(qn)
   if st :
    if st.getState() == STARTED :
        npcId = npc.getNpcId()
        cond = st.getInt("cond")
        id = st.getInt("id")
        Heart = st.getQuestItemsCount(Ice_Heart)
        if npcId == Ashutar :
            st.giveItems(Ice_Heart,1)
            FindTemplate(Alter).setBusy(False)
            st.set("id","3")
            st.set("cond","3")
            st.playSound("ItemSound.quest_middle")
            st.getQuestTimer("Soul of Water Ashutar has despawned").cancel()
        elif npcId in Ketra_Orcs :
            if Heart :
                st.takeItems(Ice_Heart,-1)
            st.unset("cond")
            st.unset("id")
            st.exitQuest(1)
    return


QUEST       = Quest(610,qn,"Magical Power of Water - Part 2")
CREATED     = State('Start', QUEST)
STARTED     = State('Started', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(Asefa)

QUEST.addTalkId(Asefa)
QUEST.addTalkId(Alter)

QUEST.addKillId(Ashutar)
STARTED.addQuestDrop(Ashutar,Ice_Heart,1)

for mobId in Ketra_Orcs:
    QUEST.addKillId(mobId)

print "importing quests: 610: Magical Power of Water - Part 2"