def chickenFly(num = 100, position = 10):
    for i in range(num):
        mobs.spawn(CHICKEN, pos(0, position, 0))
def buildPlatform(length, Material):
    agent.teleport_to_player()
    agent.move(FORWARD, 1)
    agent.set_assist(PLACE_ON_MOVE, True)
    agent.set_item(Material, 100, 1)
    agent.set_slot(1)
    k = length - 1
    while k > 0:
        for i in range(4):
            agent.move(FORWARD, k) 
            if agent.detect(AgentDetection.BLOCK, FORWARD):
                agent.turn_left()
                agent.move(FORWARD, 1)
            else:
                agent.turn_left()
        k -= 2
    agent.move(UP, 1)

buildPlatform(30, STONE)