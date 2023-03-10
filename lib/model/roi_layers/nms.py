# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
# from ._utils import _C
from model import _C
#import torchvision
#nms = torchvision.ops.nms
nms = _C.nms
# nms.__doc__ = """
# This function performs Non-maximum suppresion"""
