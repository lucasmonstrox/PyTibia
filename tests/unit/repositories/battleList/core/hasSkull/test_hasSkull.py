import numpy as np
import pathlib
from src.repositories.battleList.core import hasSkull
from src.repositories.battleList.typings import Creature
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_where_there_are_no_creatures():
    content = loadFromRGBToGray(f'{currentPath}/emptyBattleListContent.png')
    creatures = np.array([], dtype=Creature)
    has = hasSkull(content, creatures)
    expectedHasSkull = False
    assert has == expectedHasSkull


def test_should_return_False_when_there_are_creatures_and_no_players():
    content = loadFromRGBToGray(f'{currentPath}/noPlayers.png')
    creatures = np.array([('Sandcrawler', False), ('Rat', False), ('Dragon', False)], dtype=Creature)
    has = hasSkull(content, creatures)
    expectedHasSkull = False
    assert has == expectedHasSkull


def test_should_return_True_when_has_player_with_black_skull():
    content = loadFromRGBToGray(f'{currentPath}/playerWithBlackSkull.png')
    creatures = np.array([('Rat', False), ('Unknown', False), ('Unknown', False)], dtype=Creature)
    has = hasSkull(content, creatures)
    expectedHasSkull = True
    assert has == expectedHasSkull


def test_should_return_True_when_has_player_with_orange_skull():
    content = loadFromRGBToGray(f'{currentPath}/playerWithOrangeSkull.png')
    creatures = np.array([('Unknown', False), ('Rat', False), ('Unknown', False)], dtype=Creature)
    has = hasSkull(content, creatures)
    expectedHasSkull = True
    assert has == expectedHasSkull


def test_should_return_True_when_has_player_with_red_skull():
    content = loadFromRGBToGray(f'{currentPath}/playerWithRedSkull.png')
    creatures = np.array([('Unknown', False), ('Rat', False), ('Unknown', False)], dtype=Creature)
    has = hasSkull(content, creatures)
    expectedHasSkull = True
    assert has == expectedHasSkull


def test_should_return_True_when_has_player_with_white_skull():
    content = loadFromRGBToGray(f'{currentPath}/playerWithWhiteSkull.png')
    creatures = np.array([('Unknown', False), ('Unknown', False), ('Rat', False)], dtype=Creature)
    has = hasSkull(content, creatures)
    expectedHasSkull = True
    assert has == expectedHasSkull


def test_should_return_True_when_has_player_with_yellow_skull():
    content = loadFromRGBToGray(f'{currentPath}/playerWithYellowSkull.png')
    creatures = np.array([('Unknown', False), ('Rat', False), ('Unknown', False)], dtype=Creature)
    has = hasSkull(content, creatures)
    expectedHasSkull = True
    assert has == expectedHasSkull
