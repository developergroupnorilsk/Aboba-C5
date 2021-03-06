import sys
from net.sf.l2j.gameserver.lib import Rnd
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest
from net.sf.l2j.gameserver.serverpackets import CreatureSay
from net.sf.l2j.gameserver.serverpackets import PlaySound

# Boss: Core
class core(JQuest) :

    # init function.  Add in here variables that you'd like to be inherited by subclasses (if any)
    def __init__(self,id,name,descr):
        self.Core = 29006
        self.Minions = [29007,29008,29011]
        self.FirstAttacked = False
        # finally, don't forget to call the parent constructor to prepare the event triggering
        # mechanisms etc.
        JQuest.__init__(self,id,name,descr)

    def onAttack (self,npc,player):
        objId=npc.getObjectId()
        if self.FirstAttacked:
           if Rnd.get(100) : return
           npc.broadcastPacket(CreatureSay(objId,0,"Core","Removing intruders."))
        else :
           self.FirstAttacked = True
           npc.broadcastPacket(CreatureSay(objId,0,"Core","A non-permitted target has been discovered."))
           npc.broadcastPacket(CreatureSay(objId,0,"Core","Starting intruder removal system."))
        return 

    def onKill (self,npc,player):
        npcId = npc.getNpcId()
        if npcId == self.Core:
            objId=npc.getObjectId()
            npc.broadcastPacket(PlaySound(1, "BS02_D", 1, objId, npc.getX(), npc.getY(), npc.getZ()))
            npc.broadcastPacket(CreatureSay(objId,0,"Core","A fatal error has occurred."))
            npc.broadcastPacket(CreatureSay(objId,0,"Core","System is being shut down..."))
            npc.broadcastPacket(CreatureSay(objId,0,"Core","......"))
            self.FirstAttacked = False
            self.getPcSpawn(player).removeAllSpawn()
            self.getPcSpawn(player).addSpawn(31842,16502,110165,-6394,900000)
            self.getPcSpawn(player).addSpawn(31842,18948,110166,-6397,900000)
        elif self.FirstAttacked :
            self.getPcSpawn(player).addSpawn(npcId, npc.getX(), npc.getY(), npc.getZ())
        return 

# now call the constructor (starts up the ai)
QUEST		= core(-1,"core","ai")

QUEST.addKillId(QUEST.Core)
QUEST.addAttackId(QUEST.Core)

for minion in QUEST.Minions :
    QUEST.addKillId(minion)

print "AI: individuals: Core...loaded!"
