# -*- coding: utf-8 -*-
import sys


def GetPodsCount(sDescribe):
    lOutput = sDescribe.split("\n")
    for sLine in lOutput:
        if sLine.startswith("Replicas:"):
            lWords = sLine.split(" ")
            sPodsCount = lWords[-2]

            if sPodsCount.isalnum():
                oFile = open("result.file", "w")
                oFile.write(sPodsCount)
                oFile.close()
                print("99999999999999999999999")
                return

if __name__ == '__main__':
    sDescribe = sys.argv[1]
    GetPodsCount(sDescribe)