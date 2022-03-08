# -*- coding: utf-8 -*-
import sys


def GetPodsCount(sVersion):
    lVersion = sVersion.split(".")
    if len(lVersion) != 3:
        print("0.0.0")
    else:
        lVersion[-1] = str(int(lVersion[-1])+1)
        sNewVersion = ".".join(lVersion)
        print(sNewVersion)


if __name__ == '__main__':
    sVersion = sys.argv[1]
    # sVersion = "0.0.1"
    GetPodsCount(sVersion)