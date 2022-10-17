import numpy as np
import pyautogui
from scipy.spatial import distance
import time
import hud.core
import hud.slot
from . import waypoint as wp


def isNearToHole(context, roleRadarCoordinate):
    distances = distance.cdist(
        [context['radarCoordinate']], [roleRadarCoordinate])
    distanceBetweenRoleAndChar = distances[0][0]
    isNear = distanceBetweenRoleAndChar <= 1
    return isNear


def makeIsNearToHoleTask(waypoint):
    task = {
        'taskType': 'isNearToHole',
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delay': 0.5,
        'shouldExec': lambda context: isNearToHole(context, waypoint['coordinate']),
        'do': lambda _: True,
        'did': lambda _: True,
        'status': 'notStarted',
    }
    return task


def openHole(hudCoordinate, radarCoordinate, roleRadarCoordinate):
    slot = hud.core.getSlotFromCoordinate(radarCoordinate, roleRadarCoordinate)
    pyautogui.press('f9')
    hud.slot.clickSlot(slot, hudCoordinate)


def makeIsHoleClosedTask(waypoint):
    task = {
        'taskType': 'isHoleClosed',
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delay': 0,
        'shouldExec': lambda context: hud.core.isHoleOpen(context['hudImg'], context['radarCoordinate'], waypoint['coordinate']) == False,
        'do': lambda context: openHole(context['hudCoordinate'], context['radarCoordinate'], waypoint['coordinate']),
        'did': lambda _: True,  # TODO: verificar se o buraco está aberto
        'status': 'notStarted',
    }
    return task


def makePressLeftKeyTask(waypoint):
    task = {
        'taskType': 'pressLeftKey',
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delay': 0.5,
        'shouldExec': lambda _: True,
        'do': lambda _: pyautogui.press('left'),
        'did': lambda _: True,
        'status': 'notStarted',
    }
    return task


def makeUseShovelTasks(context, waypoint):
    tasks = []
    floorTasks = makeFloorTasks(context, waypoint)
    for floorTask in floorTasks:
        tasks.append(floorTask)
    tasks.append(makeIsNearToHoleTask(waypoint))
    tasks.append(makeIsHoleClosedTask(waypoint))
    tasks.append(makePressLeftKeyTask(waypoint))
    return tasks


def makeFloorTasks(context, waypoint):
    nextCoordinate = wp.resolveShovelWaypointCoordinate(
        context['radarCoordinate'], waypoint['coordinate'])
    walkpoints = wp.generateFloorWalkpoints(
        context['radarCoordinate'], nextCoordinate)
    tasks = []
    for i, walkpoint in enumerate(walkpoints):
        nextWalkpoint = None if len(walkpoints) - 1 == i else walkpoints[i + 1]
        walkpointTask = makeWalkpointTask(walkpoint, nextWalkpoint)
        tasks.append(walkpointTask)
    return tasks


def shouldExecWalkpoint(radarCoordinate, walkpoint):
    fa = np.any(radarCoordinate == walkpoint)
    shouldExec = fa == True
    return shouldExec


def didWalkpointTask(radarCoordinate, nextwalkpoint):
    response = np.any(radarCoordinate == nextwalkpoint)
    didTask = response == True
    return didTask


def makeWalkpointTask(walkpoint, nextwalkpoint):
    task = {
        'taskType': 'walk',
        'createdAt': time.time(),
        'startedAt': None,
        'finishedAt': None,
        'delay': 0,
        'shouldExec': lambda _: True,
        'do': lambda _: True,  # Se não tiver pressionado a tecla desejada, skipar
        'did': lambda context: didWalkpointTask(context['radarCoordinate'], walkpoint),
        'status': 'notStarted',
    }
    return task
