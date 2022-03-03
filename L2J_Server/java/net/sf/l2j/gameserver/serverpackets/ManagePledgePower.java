 /*
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2, or (at your option)
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA
 * 02111-1307, USA.
 *
 * http://www.gnu.org/copyleft/gpl.html
 */
package net.sf.l2j.gameserver.serverpackets;

import net.sf.l2j.gameserver.model.L2Clan;


public class ManagePledgePower extends ServerBasePacket
{
    private static final String _S__30_MANAGEPLEDGEPOWER = "[S] 30 ManagePledgePower";
    
    private int _action;
    private L2Clan _clan;
    private int _rank;
    private int privs;
    
    public ManagePledgePower(L2Clan clan, int action, int rank)
    {
        _clan = clan;
        _action = action;
        _rank = rank;
    }   
    
    final void runImpl()
    {
        // no long-running tasks
    }
    
    final void writeImpl()
    {
        if(_action == 1)
        	privs = _clan.getRankPrivs(_rank);
        else
        {
            return;
        	/*
            if (L2World.getInstance().findObject(_clanId) == null)
                return;
            
			privs = ((L2PcInstance)L2World.getInstance().findObject(_clanId)).getClanPrivileges();
			*/
        }
        writeC(0x30);
        writeD(0);
        writeD(0);
        writeD(privs);
   }
    
    /* (non-Javadoc)
     * @see net.sf.l2j.gameserver.serverpackets.ServerBasePacket#getType()
     */
    public String getType()
    {
        return _S__30_MANAGEPLEDGEPOWER;
    }

}
