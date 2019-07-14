# -*- coding: utf-8 -*-

POPULATION_SIZE = 10  # 基因组数
MUTA_RATE = 20        # 变异概率
ROTATIONS = 1    # 旋转选择， 1： 不能旋转
# 单位都是MM(毫米)
SPACING = 2      # 图形间隔空间
# 不同面料尺寸
BIN_HEIGHT = 1400
BIN_WIDTH = 4000
BIN_NORMAL = [[0, 0], [0, 1400],[4000, 1400], [4000, 0]] # 一般布是无限长