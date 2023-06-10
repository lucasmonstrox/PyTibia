from src.repositories.radar.core import getBreakpointTileMovementSpeed, getTileFrictionByCoordinate
from src.repositories.skills.core import getSpeed
from ...typings import Context


def setCharSkillsMiddleware(context: Context) -> Context:
    context['skills']['speed'] = getSpeed(context['screenshot'])
    context['skills']['tileFriction'] = getTileFrictionByCoordinate(context['radar']['coordinate'])
    context['skills']['movementSpeed'] = getBreakpointTileMovementSpeed(
        context['skills']['speed'], context['skills']['tileFriction'])
    return context