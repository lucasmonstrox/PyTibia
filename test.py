import src.repositories.gameWindow.creatures as gameWindowCreatures
import src.utils.core
import src.repositories.battleList.core
import src.repositories.battleList.extractors
import src.repositories.gameWindow.config
import src.repositories.gameWindow.core



grayScreenshot = src.utils.core.getScreenshot()
radarCoordinate = src.repositories.radar.core.getCoordinate(grayScreenshot)
content = src.repositories.battleList.extractors.getContent(grayScreenshot)
battleListCreatures = src.repositories.battleList.core.getCreatures(content)
beingAttackedCreatureCategory = src.repositories.battleList.core.getBeingAttackedCreatureCategory(battleListCreatures)
gameWindowSize = src.repositories.gameWindow.config.gameWindowSizes[1080]
gameWindowCoordinate = src.repositories.gameWindow.core.getCoordinate(grayScreenshot, gameWindowSize)
gameWindowImg = src.repositories.gameWindow.core.getImageByCoordinate(grayScreenshot, gameWindowCoordinate, gameWindowSize)
gameWindowCreaturess = src.repositories.gameWindow.creatures.getCreatures(battleListCreatures, 'left', gameWindowCoordinate, gameWindowImg, radarCoordinate,beingAttackedCreatureCategory=beingAttackedCreatureCategory)
isTrapped = gameWindowCreatures.isTrappedByCreatures(gameWindowCreaturess, radarCoordinate)

print('isTrapped', isTrapped)