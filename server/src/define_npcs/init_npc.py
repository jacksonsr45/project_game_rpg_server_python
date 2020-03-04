class Init_NPC:
    def __init__(self, recv_npc):
        self.world_npc = recv_npc['world_npc']
        self.name_npc = recv_npc['name_npc']
        self.pos_npc = recv_npc['pos_npc']
        self.func_npc = recv_npc['func_npc']

    
    
    def send_npc(self):
        pass
