# coding:utf8

from . import boc, jsl, sina, tencent, daykline, hkqoute, timekline


def use(source):
    if source in ["sina"]:
        return sina.Sina()
    if source in ["jsl"]:
        return jsl.Jsl()
    if source in ["qq", "tencent"]:
        return tencent.Tencent()
    if source in ["boc"]:
        return boc.Boc()
    if source in ["timekline"]:
        return timekline.TimeKline()
    if source in ["daykline"]:
        return daykline.DayKline()
    if source in ["hkquote"]:
        return hkqoute.HKQuote()
    raise NotImplementedError
