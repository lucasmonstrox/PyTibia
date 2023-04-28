from src.repositories.radar.core import getBreakpointTileMovementSpeed


def test_should_return_50_when_tile_speed_is_255_and_char_speed_is_81351():
    result = getBreakpointTileMovementSpeed(81351, 255)
    assert result == 50


def test_should_return_100_when_tile_speed_is_255_and_char_speed_is_4557():
    result = getBreakpointTileMovementSpeed(4557, 255)
    assert result == 100


def test_should_return_150_when_tile_speed_is_255_and_char_speed_is_1591():
    result = getBreakpointTileMovementSpeed(1591, 255)
    assert result == 150


def test_should_return_200_when_tile_speed_is_255_and_char_speed_is_884():
    result = getBreakpointTileMovementSpeed(884, 255)
    assert result == 200


def test_should_return_250_when_tile_speed_is_255_and_char_speed_is_598():
    result = getBreakpointTileMovementSpeed(598, 255)
    assert result == 250


def test_should_return_300_when_tile_speed_is_255_and_char_speed_is_446():
    result = getBreakpointTileMovementSpeed(446, 255)
    assert result == 300


def test_should_return_350_when_tile_speed_is_255_and_char_speed_is_356():
    result = getBreakpointTileMovementSpeed(356, 255)
    assert result == 350


def test_should_return_400_when_tile_speed_is_255_and_char_speed_is_295():
    result = getBreakpointTileMovementSpeed(295, 255)
    assert result == 400


def test_should_return_450_when_tile_speed_is_255_and_char_speed_is_252():
    result = getBreakpointTileMovementSpeed(252, 255)
    assert result == 450


def test_should_return_500_when_tile_speed_is_255_and_char_speed_is_220():
    result = getBreakpointTileMovementSpeed(220, 255)
    assert result == 500


def test_should_return_550_when_tile_speed_is_255_and_char_speed_is_195():
    result = getBreakpointTileMovementSpeed(195, 255)
    assert result == 550


def test_should_return_600_when_tile_speed_is_255_and_char_speed_is_175():
    result = getBreakpointTileMovementSpeed(175, 255)
    assert result == 600


def test_should_return_650_when_tile_speed_is_255_and_char_speed_is_160():
    result = getBreakpointTileMovementSpeed(160, 255)
    assert result == 650


def test_should_return_700_when_tile_speed_is_255_and_char_speed_is_146():
    result = getBreakpointTileMovementSpeed(146, 255)
    assert result == 700


def test_should_return_750_when_tile_speed_is_255_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 255)
    assert result == 750


def test_should_return_800_when_tile_speed_is_255_and_char_speed_is_126():
    result = getBreakpointTileMovementSpeed(126, 255)
    assert result == 800


def test_should_return_850_when_tile_speed_is_255_and_char_speed_is_117():
    result = getBreakpointTileMovementSpeed(117, 255)
    assert result == 850


def test_should_return_850_when_tile_speed_is_255_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 255)
    assert result == 850


def test_should_return_50_when_tile_speed_is_250_and_char_speed_is_81351():
    result = getBreakpointTileMovementSpeed(81351, 250)
    assert result == 50


def test_should_return_100_when_tile_speed_is_250_and_char_speed_is_4557():
    result = getBreakpointTileMovementSpeed(4557, 250)
    assert result == 100


def test_should_return_150_when_tile_speed_is_250_and_char_speed_is_1591():
    result = getBreakpointTileMovementSpeed(1591, 250)
    assert result == 150


def test_should_return_200_when_tile_speed_is_250_and_char_speed_is_884():
    result = getBreakpointTileMovementSpeed(884, 250)
    assert result == 200


def test_should_return_250_when_tile_speed_is_250_and_char_speed_is_598():
    result = getBreakpointTileMovementSpeed(598, 250)
    assert result == 250


def test_should_return_300_when_tile_speed_is_250_and_char_speed_is_446():
    result = getBreakpointTileMovementSpeed(446, 250)
    assert result == 300


def test_should_return_350_when_tile_speed_is_250_and_char_speed_is_356():
    result = getBreakpointTileMovementSpeed(356, 250)
    assert result == 350


def test_should_return_400_when_tile_speed_is_250_and_char_speed_is_295():
    result = getBreakpointTileMovementSpeed(295, 250)
    assert result == 400


def test_should_return_450_when_tile_speed_is_250_and_char_speed_is_252():
    result = getBreakpointTileMovementSpeed(252, 250)
    assert result == 450


def test_should_return_500_when_tile_speed_is_250_and_char_speed_is_220():
    result = getBreakpointTileMovementSpeed(220, 250)
    assert result == 500


def test_should_return_550_when_tile_speed_is_250_and_char_speed_is_195():
    result = getBreakpointTileMovementSpeed(195, 250)
    assert result == 550


def test_should_return_600_when_tile_speed_is_250_and_char_speed_is_175():
    result = getBreakpointTileMovementSpeed(175, 250)
    assert result == 600


def test_should_return_650_when_tile_speed_is_250_and_char_speed_is_160():
    result = getBreakpointTileMovementSpeed(160, 250)
    assert result == 650


def test_should_return_700_when_tile_speed_is_250_and_char_speed_is_146():
    result = getBreakpointTileMovementSpeed(146, 250)
    assert result == 700


def test_should_return_750_when_tile_speed_is_250_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 250)
    assert result == 750


def test_should_return_800_when_tile_speed_is_250_and_char_speed_is_126():
    result = getBreakpointTileMovementSpeed(126, 250)
    assert result == 800


def test_should_return_850_when_tile_speed_is_250_and_char_speed_is_117():
    result = getBreakpointTileMovementSpeed(117, 250)
    assert result == 850


def test_should_return_850_when_tile_speed_is_250_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 250)
    assert result == 850


def test_should_return_50_when_tile_speed_is_249_and_char_speed_is_81351():
    result = getBreakpointTileMovementSpeed(81351, 249)
    assert result == 50


def test_should_return_100_when_tile_speed_is_249_and_char_speed_is_4557():
    result = getBreakpointTileMovementSpeed(4557, 249)
    assert result == 100


def test_should_return_150_when_tile_speed_is_249_and_char_speed_is_1591():
    result = getBreakpointTileMovementSpeed(1591, 249)
    assert result == 150


def test_should_return_200_when_tile_speed_is_249_and_char_speed_is_884():
    result = getBreakpointTileMovementSpeed(884, 249)
    assert result == 200


def test_should_return_250_when_tile_speed_is_249_and_char_speed_is_598():
    result = getBreakpointTileMovementSpeed(598, 249)
    assert result == 250


def test_should_return_300_when_tile_speed_is_249_and_char_speed_is_446():
    result = getBreakpointTileMovementSpeed(446, 249)
    assert result == 300


def test_should_return_350_when_tile_speed_is_249_and_char_speed_is_356():
    result = getBreakpointTileMovementSpeed(356, 249)
    assert result == 350


def test_should_return_400_when_tile_speed_is_249_and_char_speed_is_295():
    result = getBreakpointTileMovementSpeed(295, 249)
    assert result == 400


def test_should_return_450_when_tile_speed_is_249_and_char_speed_is_252():
    result = getBreakpointTileMovementSpeed(252, 249)
    assert result == 450


def test_should_return_500_when_tile_speed_is_249_and_char_speed_is_220():
    result = getBreakpointTileMovementSpeed(220, 249)
    assert result == 500


def test_should_return_550_when_tile_speed_is_249_and_char_speed_is_195():
    result = getBreakpointTileMovementSpeed(195, 249)
    assert result == 550


def test_should_return_600_when_tile_speed_is_249_and_char_speed_is_175():
    result = getBreakpointTileMovementSpeed(175, 249)
    assert result == 600


def test_should_return_650_when_tile_speed_is_249_and_char_speed_is_160():
    result = getBreakpointTileMovementSpeed(160, 249)
    assert result == 650


def test_should_return_700_when_tile_speed_is_249_and_char_speed_is_146():
    result = getBreakpointTileMovementSpeed(146, 249)
    assert result == 700


def test_should_return_750_when_tile_speed_is_249_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 249)
    assert result == 750


def test_should_return_800_when_tile_speed_is_249_and_char_speed_is_126():
    result = getBreakpointTileMovementSpeed(126, 249)
    assert result == 800


def test_should_return_850_when_tile_speed_is_249_and_char_speed_is_117():
    result = getBreakpointTileMovementSpeed(117, 249)
    assert result == 850


def test_should_return_850_when_tile_speed_is_249_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 249)
    assert result == 850


def test_should_return_50_when_tile_speed_is_200_and_char_speed_is_25761():
    result = getBreakpointTileMovementSpeed(25761, 200)
    assert result == 50


def test_should_return_100_when_tile_speed_is_200_and_char_speed_is_2444():
    result = getBreakpointTileMovementSpeed(2444, 200)
    assert result == 100


def test_should_return_150_when_tile_speed_is_200_and_char_speed_is_998():
    result = getBreakpointTileMovementSpeed(998, 200)
    assert result == 150


def test_should_return_200_when_tile_speed_is_200_and_char_speed_is_597():
    result = getBreakpointTileMovementSpeed(597, 200)
    assert result == 200


def test_should_return_250_when_tile_speed_is_200_and_char_speed_is_419():
    result = getBreakpointTileMovementSpeed(419, 200)
    assert result == 250


def test_should_return_300_when_tile_speed_is_200_and_char_speed_is_322():
    result = getBreakpointTileMovementSpeed(322, 200)
    assert result == 300


def test_should_return_350_when_tile_speed_is_200_and_char_speed_is_261():
    result = getBreakpointTileMovementSpeed(261, 200)
    assert result == 350


def test_should_return_400_when_tile_speed_is_200_and_char_speed_is_219():
    result = getBreakpointTileMovementSpeed(219, 200)
    assert result == 400


def test_should_return_450_when_tile_speed_is_200_and_char_speed_is_190():
    result = getBreakpointTileMovementSpeed(190, 200)
    assert result == 450


def test_should_return_500_when_tile_speed_is_200_and_char_speed_is_167():
    result = getBreakpointTileMovementSpeed(167, 200)
    assert result == 500


def test_should_return_550_when_tile_speed_is_200_and_char_speed_is_149():
    result = getBreakpointTileMovementSpeed(149, 200)
    assert result == 550


def test_should_return_600_when_tile_speed_is_200_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 200)
    assert result == 600


def test_should_return_650_when_tile_speed_is_200_and_char_speed_is_124():
    result = getBreakpointTileMovementSpeed(124, 200)
    assert result == 650


def test_should_return_700_when_tile_speed_is_200_and_char_speed_is_114():
    result = getBreakpointTileMovementSpeed(114, 200)
    assert result == 700


def test_should_return_750_when_tile_speed_is_200_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 200)
    assert result == 750


def test_should_return_50_when_tile_speed_is_199_and_char_speed_is_25761():
    result = getBreakpointTileMovementSpeed(25761, 199)
    assert result == 50


def test_should_return_100_when_tile_speed_is_199_and_char_speed_is_2444():
    result = getBreakpointTileMovementSpeed(2444, 199)
    assert result == 100


def test_should_return_150_when_tile_speed_is_199_and_char_speed_is_998():
    result = getBreakpointTileMovementSpeed(998, 199)
    assert result == 150


def test_should_return_200_when_tile_speed_is_199_and_char_speed_is_597():
    result = getBreakpointTileMovementSpeed(597, 199)
    assert result == 200


def test_should_return_250_when_tile_speed_is_199_and_char_speed_is_419():
    result = getBreakpointTileMovementSpeed(419, 199)
    assert result == 250


def test_should_return_300_when_tile_speed_is_199_and_char_speed_is_322():
    result = getBreakpointTileMovementSpeed(322, 199)
    assert result == 300


def test_should_return_350_when_tile_speed_is_199_and_char_speed_is_261():
    result = getBreakpointTileMovementSpeed(261, 199)
    assert result == 350


def test_should_return_400_when_tile_speed_is_199_and_char_speed_is_219():
    result = getBreakpointTileMovementSpeed(219, 199)
    assert result == 400


def test_should_return_450_when_tile_speed_is_199_and_char_speed_is_190():
    result = getBreakpointTileMovementSpeed(190, 199)
    assert result == 450


def test_should_return_500_when_tile_speed_is_199_and_char_speed_is_167():
    result = getBreakpointTileMovementSpeed(167, 199)
    assert result == 500


def test_should_return_550_when_tile_speed_is_199_and_char_speed_is_149():
    result = getBreakpointTileMovementSpeed(149, 199)
    assert result == 550


def test_should_return_600_when_tile_speed_is_199_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 199)
    assert result == 600


def test_should_return_650_when_tile_speed_is_199_and_char_speed_is_124():
    result = getBreakpointTileMovementSpeed(124, 199)
    assert result == 650


def test_should_return_700_when_tile_speed_is_199_and_char_speed_is_114():
    result = getBreakpointTileMovementSpeed(114, 199)
    assert result == 700


def test_should_return_750_when_tile_speed_is_199_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 199)
    assert result == 750


def test_should_return_50_when_tile_speed_is_160_and_char_speed_is_10167():
    result = getBreakpointTileMovementSpeed(10167, 160)
    assert result == 50


def test_should_return_100_when_tile_speed_is_160_and_char_speed_is_1443():
    result = getBreakpointTileMovementSpeed(1443, 160)
    assert result == 100


def test_should_return_150_when_tile_speed_is_160_and_char_speed_is_663():
    result = getBreakpointTileMovementSpeed(663, 160)
    assert result == 150


def test_should_return_200_when_tile_speed_is_160_and_char_speed_is_419():
    result = getBreakpointTileMovementSpeed(419, 160)
    assert result == 200


def test_should_return_250_when_tile_speed_is_160_and_char_speed_is_304():
    result = getBreakpointTileMovementSpeed(304, 160)
    assert result == 250


def test_should_return_300_when_tile_speed_is_160_and_char_speed_is_238():
    result = getBreakpointTileMovementSpeed(238, 160)
    assert result == 300


def test_should_return_350_when_tile_speed_is_160_and_char_speed_is_196():
    result = getBreakpointTileMovementSpeed(196, 160)
    assert result == 350


def test_should_return_400_when_tile_speed_is_160_and_char_speed_is_167():
    result = getBreakpointTileMovementSpeed(167, 160)
    assert result == 400


def test_should_return_450_when_tile_speed_is_160_and_char_speed_is_145():
    result = getBreakpointTileMovementSpeed(145, 160)
    assert result == 450


def test_should_return_500_when_tile_speed_is_160_and_char_speed_is_129():
    result = getBreakpointTileMovementSpeed(129, 160)
    assert result == 500


def test_should_return_550_when_tile_speed_is_160_and_char_speed_is_116():
    result = getBreakpointTileMovementSpeed(116, 160)
    assert result == 550


def test_should_return_600_when_tile_speed_is_160_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 160)
    assert result == 600


def test_should_return_50_when_tile_speed_is_159_and_char_speed_is_10167():
    result = getBreakpointTileMovementSpeed(10167, 159)
    assert result == 50


def test_should_return_100_when_tile_speed_is_159_and_char_speed_is_1443():
    result = getBreakpointTileMovementSpeed(1443, 159)
    assert result == 100


def test_should_return_150_when_tile_speed_is_159_and_char_speed_is_663():
    result = getBreakpointTileMovementSpeed(663, 159)
    assert result == 150


def test_should_return_200_when_tile_speed_is_159_and_char_speed_is_419():
    result = getBreakpointTileMovementSpeed(419, 159)
    assert result == 200


def test_should_return_250_when_tile_speed_is_159_and_char_speed_is_304():
    result = getBreakpointTileMovementSpeed(304, 159)
    assert result == 250


def test_should_return_300_when_tile_speed_is_159_and_char_speed_is_238():
    result = getBreakpointTileMovementSpeed(238, 159)
    assert result == 300


def test_should_return_350_when_tile_speed_is_159_and_char_speed_is_196():
    result = getBreakpointTileMovementSpeed(196, 159)
    assert result == 350


def test_should_return_400_when_tile_speed_is_159_and_char_speed_is_167():
    result = getBreakpointTileMovementSpeed(167, 159)
    assert result == 400


def test_should_return_450_when_tile_speed_is_159_and_char_speed_is_145():
    result = getBreakpointTileMovementSpeed(145, 159)
    assert result == 450


def test_should_return_500_when_tile_speed_is_159_and_char_speed_is_129():
    result = getBreakpointTileMovementSpeed(129, 159)
    assert result == 500


def test_should_return_550_when_tile_speed_is_159_and_char_speed_is_116():
    result = getBreakpointTileMovementSpeed(116, 159)
    assert result == 550


def test_should_return_600_when_tile_speed_is_159_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 159)
    assert result == 600


def test_should_return_50_when_tile_speed_is_150_and_char_speed_is_8036():
    result = getBreakpointTileMovementSpeed(8036, 150)
    assert result == 50


def test_should_return_100_when_tile_speed_is_150_and_char_speed_is_1258():
    result = getBreakpointTileMovementSpeed(1258, 150)
    assert result == 100


def test_should_return_150_when_tile_speed_is_150_and_char_speed_is_595():
    result = getBreakpointTileMovementSpeed(595, 150)
    assert result == 150


def test_should_return_200_when_tile_speed_is_150_and_char_speed_is_380():
    result = getBreakpointTileMovementSpeed(380, 150)
    assert result == 200


def test_should_return_250_when_tile_speed_is_150_and_char_speed_is_278():
    result = getBreakpointTileMovementSpeed(278, 150)
    assert result == 250


def test_should_return_300_when_tile_speed_is_150_and_char_speed_is_219():
    result = getBreakpointTileMovementSpeed(219, 150)
    assert result == 300


def test_should_return_350_when_tile_speed_is_150_and_char_speed_is_181():
    result = getBreakpointTileMovementSpeed(181, 150)
    assert result == 350


def test_should_return_400_when_tile_speed_is_150_and_char_speed_is_155():
    result = getBreakpointTileMovementSpeed(155, 150)
    assert result == 400


def test_should_return_450_when_tile_speed_is_150_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 150)
    assert result == 450


def test_should_return_500_when_tile_speed_is_150_and_char_speed_is_120():
    result = getBreakpointTileMovementSpeed(120, 150)
    assert result == 500

def test_should_return_550_when_tile_speed_is_150_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 150)
    assert result == 550


def test_should_return_50_when_tile_speed_is_149_and_char_speed_is_8036():
    result = getBreakpointTileMovementSpeed(8036, 149)
    assert result == 50


def test_should_return_100_when_tile_speed_is_149_and_char_speed_is_1258():
    result = getBreakpointTileMovementSpeed(1258, 149)
    assert result == 100


def test_should_return_150_when_tile_speed_is_149_and_char_speed_is_595():
    result = getBreakpointTileMovementSpeed(595, 149)
    assert result == 150


def test_should_return_200_when_tile_speed_is_149_and_char_speed_is_380():
    result = getBreakpointTileMovementSpeed(380, 149)
    assert result == 200


def test_should_return_250_when_tile_speed_is_149_and_char_speed_is_278():
    result = getBreakpointTileMovementSpeed(278, 149)
    assert result == 250


def test_should_return_300_when_tile_speed_is_149_and_char_speed_is_219():
    result = getBreakpointTileMovementSpeed(219, 149)
    assert result == 300


def test_should_return_350_when_tile_speed_is_149_and_char_speed_is_181():
    result = getBreakpointTileMovementSpeed(181, 149)
    assert result == 350


def test_should_return_400_when_tile_speed_is_149_and_char_speed_is_155():
    result = getBreakpointTileMovementSpeed(155, 149)
    assert result == 400


def test_should_return_450_when_tile_speed_is_149_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 149)
    assert result == 450


def test_should_return_500_when_tile_speed_is_149_and_char_speed_is_120():
    result = getBreakpointTileMovementSpeed(120, 149)
    assert result == 500

def test_should_return_550_when_tile_speed_is_149_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 149)
    assert result == 550


def test_should_return_50_when_tile_speed_is_140_and_char_speed_is_6341():
    result = getBreakpointTileMovementSpeed(6341, 140)
    assert result == 50


def test_should_return_100_when_tile_speed_is_140_and_char_speed_is_1092():
    result = getBreakpointTileMovementSpeed(1092, 140)
    assert result == 100


def test_should_return_150_when_tile_speed_is_140_and_char_speed_is_531():
    result = getBreakpointTileMovementSpeed(531, 140)
    assert result == 150


def test_should_return_200_when_tile_speed_is_140_and_char_speed_is_344():
    result = getBreakpointTileMovementSpeed(344, 140)
    assert result == 200


def test_should_return_250_when_tile_speed_is_140_and_char_speed_is_254():
    result = getBreakpointTileMovementSpeed(254, 140)
    assert result == 250


def test_should_return_300_when_tile_speed_is_140_and_char_speed_is_201():
    result = getBreakpointTileMovementSpeed(201, 140)
    assert result == 300


def test_should_return_350_when_tile_speed_is_140_and_char_speed_is_167():
    result = getBreakpointTileMovementSpeed(167, 140)
    assert result == 350


def test_should_return_400_when_tile_speed_is_140_and_char_speed_is_143():
    result = getBreakpointTileMovementSpeed(143, 140)
    assert result == 400


def test_should_return_450_when_tile_speed_is_140_and_char_speed_is_125():
    result = getBreakpointTileMovementSpeed(125, 140)
    assert result == 450


def test_should_return_500_when_tile_speed_is_140_and_char_speed_is_111():
    result = getBreakpointTileMovementSpeed(111, 140)
    assert result == 500


def test_should_return_550_when_tile_speed_is_140_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 140)
    assert result == 550


def test_should_return_100_when_tile_speed_is_139_and_char_speed_is_1092():
    result = getBreakpointTileMovementSpeed(1092, 139)
    assert result == 100


def test_should_return_150_when_tile_speed_is_139_and_char_speed_is_531():
    result = getBreakpointTileMovementSpeed(531, 139)
    assert result == 150


def test_should_return_200_when_tile_speed_is_139_and_char_speed_is_344():
    result = getBreakpointTileMovementSpeed(344, 139)
    assert result == 200


def test_should_return_250_when_tile_speed_is_139_and_char_speed_is_254():
    result = getBreakpointTileMovementSpeed(254, 139)
    assert result == 250


def test_should_return_300_when_tile_speed_is_139_and_char_speed_is_201():
    result = getBreakpointTileMovementSpeed(201, 139)
    assert result == 300


def test_should_return_350_when_tile_speed_is_139_and_char_speed_is_167():
    result = getBreakpointTileMovementSpeed(167, 139)
    assert result == 350


def test_should_return_400_when_tile_speed_is_139_and_char_speed_is_143():
    result = getBreakpointTileMovementSpeed(143, 139)
    assert result == 400


def test_should_return_450_when_tile_speed_is_139_and_char_speed_is_125():
    result = getBreakpointTileMovementSpeed(125, 139)
    assert result == 450


def test_should_return_500_when_tile_speed_is_139_and_char_speed_is_111():
    result = getBreakpointTileMovementSpeed(111, 139)
    assert result == 500


def test_should_return_550_when_tile_speed_is_139_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 139)
    assert result == 550


def test_should_return_50_when_tile_speed_is_125_and_char_speed_is_4419():
    result = getBreakpointTileMovementSpeed(4419, 125)
    assert result == 50


def test_should_return_100_when_tile_speed_is_125_and_char_speed_is_876():
    result = getBreakpointTileMovementSpeed(876, 125)
    assert result == 100


def test_should_return_150_when_tile_speed_is_125_and_char_speed_is_444():
    result = getBreakpointTileMovementSpeed(444, 125)
    assert result == 150


def test_should_return_200_when_tile_speed_is_125_and_char_speed_is_293():
    result = getBreakpointTileMovementSpeed(293, 125)
    assert result == 200


def test_should_return_250_when_tile_speed_is_125_and_char_speed_is_219():
    result = getBreakpointTileMovementSpeed(219, 125)
    assert result == 250


def test_should_return_300_when_tile_speed_is_125_and_char_speed_is_175():
    result = getBreakpointTileMovementSpeed(175, 125)
    assert result == 300


def test_should_return_350_when_tile_speed_is_125_and_char_speed_is_146():
    result = getBreakpointTileMovementSpeed(146, 125)
    assert result == 350


def test_should_return_400_when_tile_speed_is_125_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 125)
    assert result == 400


def test_should_return_50_when_tile_speed_is_124_and_char_speed_is_4419():
    result = getBreakpointTileMovementSpeed(4419, 124)
    assert result == 50


def test_should_return_100_when_tile_speed_is_124_and_char_speed_is_876():
    result = getBreakpointTileMovementSpeed(876, 124)
    assert result == 100


def test_should_return_150_when_tile_speed_is_124_and_char_speed_is_444():
    result = getBreakpointTileMovementSpeed(444, 124)
    assert result == 150


def test_should_return_200_when_tile_speed_is_124_and_char_speed_is_293():
    result = getBreakpointTileMovementSpeed(293, 124)
    assert result == 200


def test_should_return_250_when_tile_speed_is_124_and_char_speed_is_219():
    result = getBreakpointTileMovementSpeed(219, 124)
    assert result == 250


def test_should_return_300_when_tile_speed_is_124_and_char_speed_is_175():
    result = getBreakpointTileMovementSpeed(175, 124)
    assert result == 300


def test_should_return_350_when_tile_speed_is_124_and_char_speed_is_146():
    result = getBreakpointTileMovementSpeed(146, 124)
    assert result == 350


def test_should_return_400_when_tile_speed_is_124_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 124)
    assert result == 400


def test_should_return_50_when_tile_speed_is_110_and_char_speed_is_3060():
    result = getBreakpointTileMovementSpeed(3060, 110)
    assert result == 50


def test_should_return_100_when_tile_speed_is_110_and_char_speed_is_696():
    result = getBreakpointTileMovementSpeed(696, 110)
    assert result == 100


def test_should_return_150_when_tile_speed_is_110_and_char_speed_is_367():
    result = getBreakpointTileMovementSpeed(367, 110)
    assert result == 150


def test_should_return_200_when_tile_speed_is_110_and_char_speed_is_248():
    result = getBreakpointTileMovementSpeed(248, 110)
    assert result == 200


def test_should_return_250_when_tile_speed_is_110_and_char_speed_is_187():
    result = getBreakpointTileMovementSpeed(187, 110)
    assert result == 250


def test_should_return_300_when_tile_speed_is_110_and_char_speed_is_150():
    result = getBreakpointTileMovementSpeed(150, 110)
    assert result == 300


def test_should_return_350_when_tile_speed_is_110_and_char_speed_is_126():
    result = getBreakpointTileMovementSpeed(126, 110)
    assert result == 350


def test_should_return_400_when_tile_speed_is_110_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 110)
    assert result == 400


def test_should_return_50_when_tile_speed_is_109_and_char_speed_is_3060():
    result = getBreakpointTileMovementSpeed(3060, 109)
    assert result == 50


def test_should_return_100_when_tile_speed_is_109_and_char_speed_is_696():
    result = getBreakpointTileMovementSpeed(696, 109)
    assert result == 100


def test_should_return_150_when_tile_speed_is_109_and_char_speed_is_367():
    result = getBreakpointTileMovementSpeed(367, 109)
    assert result == 150


def test_should_return_200_when_tile_speed_is_109_and_char_speed_is_248():
    result = getBreakpointTileMovementSpeed(248, 109)
    assert result == 200


def test_should_return_250_when_tile_speed_is_109_and_char_speed_is_187():
    result = getBreakpointTileMovementSpeed(187, 109)
    assert result == 250


def test_should_return_300_when_tile_speed_is_109_and_char_speed_is_150():
    result = getBreakpointTileMovementSpeed(150, 109)
    assert result == 300


def test_should_return_350_when_tile_speed_is_109_and_char_speed_is_126():
    result = getBreakpointTileMovementSpeed(126, 109)
    assert result == 350


def test_should_return_400_when_tile_speed_is_109_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 109)
    assert result == 400


def test_should_return_50_when_tile_speed_is_100_and_char_speed_is_2382():
    result = getBreakpointTileMovementSpeed(2382, 100)
    assert result == 50


def test_should_return_100_when_tile_speed_is_100_and_char_speed_is_592():
    result = getBreakpointTileMovementSpeed(592, 100)
    assert result == 100


def test_should_return_150_when_tile_speed_is_100_and_char_speed_is_321():
    result = getBreakpointTileMovementSpeed(321, 100)
    assert result == 150


def test_should_return_200_when_tile_speed_is_100_and_char_speed_is_219():
    result = getBreakpointTileMovementSpeed(219, 100)
    assert result == 200


def test_should_return_250_when_tile_speed_is_100_and_char_speed_is_167():
    result = getBreakpointTileMovementSpeed(167, 100)
    assert result == 250


def test_should_return_300_when_tile_speed_is_100_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 100)
    assert result == 300


def test_should_return_350_when_tile_speed_is_100_and_char_speed_is_113():
    result = getBreakpointTileMovementSpeed(113, 100)
    assert result == 350


def test_should_return_400_when_tile_speed_is_100_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 100)
    assert result == 400


def test_should_return_50_when_tile_speed_is_99_and_char_speed_is_2382():
    result = getBreakpointTileMovementSpeed(2382, 99)
    assert result == 50


def test_should_return_100_when_tile_speed_is_99_and_char_speed_is_592():
    result = getBreakpointTileMovementSpeed(592, 99)
    assert result == 100


def test_should_return_150_when_tile_speed_is_99_and_char_speed_is_321():
    result = getBreakpointTileMovementSpeed(321, 99)
    assert result == 150


def test_should_return_200_when_tile_speed_is_99_and_char_speed_is_219():
    result = getBreakpointTileMovementSpeed(219, 99)
    assert result == 200


def test_should_return_250_when_tile_speed_is_99_and_char_speed_is_167():
    result = getBreakpointTileMovementSpeed(167, 99)
    assert result == 250


def test_should_return_300_when_tile_speed_is_99_and_char_speed_is_135():
    result = getBreakpointTileMovementSpeed(135, 99)
    assert result == 300


def test_should_return_350_when_tile_speed_is_99_and_char_speed_is_113():
    result = getBreakpointTileMovementSpeed(113, 99)
    assert result == 350


def test_should_return_400_when_tile_speed_is_99_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 99)
    assert result == 400


def test_should_return_50_when_tile_speed_is_95_and_char_speed_is_2096():
    result = getBreakpointTileMovementSpeed(2096, 95)
    assert result == 50


def test_should_return_100_when_tile_speed_is_95_and_char_speed_is_543():
    result = getBreakpointTileMovementSpeed(543, 95)
    assert result == 100


def test_should_return_150_when_tile_speed_is_95_and_char_speed_is_299():
    result = getBreakpointTileMovementSpeed(299, 95)
    assert result == 150


def test_should_return_200_when_tile_speed_is_95_and_char_speed_is_205():
    result = getBreakpointTileMovementSpeed(205, 95)
    assert result == 200


def test_should_return_250_when_tile_speed_is_95_and_char_speed_is_157():
    result = getBreakpointTileMovementSpeed(157, 95)
    assert result == 250


def test_should_return_300_when_tile_speed_is_95_and_char_speed_is_127():
    result = getBreakpointTileMovementSpeed(127, 95)
    assert result == 300


def test_should_return_350_when_tile_speed_is_95_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 95)
    assert result == 350


def test_should_return_100_when_tile_speed_is_94_and_char_speed_is_543():
    result = getBreakpointTileMovementSpeed(543, 94)
    assert result == 100


def test_should_return_150_when_tile_speed_is_94_and_char_speed_is_299():
    result = getBreakpointTileMovementSpeed(299, 94)
    assert result == 150


def test_should_return_200_when_tile_speed_is_94_and_char_speed_is_205():
    result = getBreakpointTileMovementSpeed(205, 94)
    assert result == 200


def test_should_return_250_when_tile_speed_is_94_and_char_speed_is_157():
    result = getBreakpointTileMovementSpeed(157, 94)
    assert result == 250


def test_should_return_300_when_tile_speed_is_94_and_char_speed_is_127():
    result = getBreakpointTileMovementSpeed(127, 94)
    assert result == 300


def test_should_return_350_when_tile_speed_is_94_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 94)
    assert result == 350


def test_should_return_50_when_tile_speed_is_90_and_char_speed_is_1842():
    result = getBreakpointTileMovementSpeed(1842, 90)
    assert result == 50


def test_should_return_100_when_tile_speed_is_90_and_char_speed_is_499():
    result = getBreakpointTileMovementSpeed(499, 90)
    assert result == 100


def test_should_return_150_when_tile_speed_is_90_and_char_speed_is_278():
    result = getBreakpointTileMovementSpeed(278, 90)
    assert result == 150


def test_should_return_200_when_tile_speed_is_90_and_char_speed_is_192():
    result = getBreakpointTileMovementSpeed(192, 90)
    assert result == 200


def test_should_return_250_when_tile_speed_is_90_and_char_speed_is_147():
    result = getBreakpointTileMovementSpeed(147, 90)
    assert result == 250


def test_should_return_300_when_tile_speed_is_90_and_char_speed_is_120():
    result = getBreakpointTileMovementSpeed(120, 90)
    assert result == 300


def test_should_return_350_when_tile_speed_is_90_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 90)
    assert result == 350


def test_should_return_50_when_tile_speed_is_80_and_char_speed_is_1842():
    result = getBreakpointTileMovementSpeed(1842, 80)
    assert result == 50


def test_should_return_100_when_tile_speed_is_80_and_char_speed_is_499():
    result = getBreakpointTileMovementSpeed(499, 80)
    assert result == 100


def test_should_return_150_when_tile_speed_is_80_and_char_speed_is_278():
    result = getBreakpointTileMovementSpeed(278, 80)
    assert result == 150


def test_should_return_200_when_tile_speed_is_80_and_char_speed_is_192():
    result = getBreakpointTileMovementSpeed(192, 80)
    assert result == 200


def test_should_return_250_when_tile_speed_is_80_and_char_speed_is_147():
    result = getBreakpointTileMovementSpeed(147, 80)
    assert result == 250


def test_should_return_300_when_tile_speed_is_80_and_char_speed_is_120():
    result = getBreakpointTileMovementSpeed(120, 80)
    assert result == 300


def test_should_return_350_when_tile_speed_is_80_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 80)
    assert result == 350


def test_should_return_50_when_tile_speed_is_70_and_char_speed_is_1070():
    result = getBreakpointTileMovementSpeed(1070, 70)
    assert result == 50


def test_should_return_100_when_tile_speed_is_70_and_char_speed_is_342():
    result = getBreakpointTileMovementSpeed(342, 70)
    assert result == 100


def test_should_return_150_when_tile_speed_is_70_and_char_speed_is_200():
    result = getBreakpointTileMovementSpeed(200, 70)
    assert result == 150


def test_should_return_200_when_tile_speed_is_70_and_char_speed_is_142():
    result = getBreakpointTileMovementSpeed(142, 70)
    assert result == 200


def test_should_return_250_when_tile_speed_is_70_and_char_speed_is_111():
    result = getBreakpointTileMovementSpeed(111, 70)
    assert result == 250


def test_should_return_300_when_tile_speed_is_70_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 70)
    assert result == 300


def test_should_return_50_when_tile_speed_is_60_and_char_speed_is_1070():
    result = getBreakpointTileMovementSpeed(1070, 60)
    assert result == 50


def test_should_return_100_when_tile_speed_is_60_and_char_speed_is_342():
    result = getBreakpointTileMovementSpeed(342, 60)
    assert result == 100


def test_should_return_150_when_tile_speed_is_60_and_char_speed_is_200():
    result = getBreakpointTileMovementSpeed(200, 60)
    assert result == 150


def test_should_return_200_when_tile_speed_is_60_and_char_speed_is_142():
    result = getBreakpointTileMovementSpeed(142, 60)
    assert result == 200


def test_should_return_250_when_tile_speed_is_60_and_char_speed_is_111():
    result = getBreakpointTileMovementSpeed(111, 60)
    assert result == 250


def test_should_return_300_when_tile_speed_is_60_and_char_speed_is_0():
    result = getBreakpointTileMovementSpeed(0, 60)
    assert result == 300