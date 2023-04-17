def hasCreaturesToAttack(context):
    context['targeting']['hasIgnorableCreatures'] = False
    if len(context['monsters']) == 0:
        context['targeting']['canIgnoreCreatures'] = True
        return False
    if context['targeting']['canIgnoreCreatures'] == False:
        return True
    ignorableHudCreatures = []
    for hudCreature in context['monsters']:
        shouldIgnoreCreature = context['targeting']['creatures'].get(hudCreature['name'], { 'ignore': False })['ignore']
        if shouldIgnoreCreature:
            context['targeting']['hasIgnorableCreatures'] = True
            ignorableHudCreatures.append(hudCreature)
    return len(ignorableHudCreatures) < len(context['monsters'])