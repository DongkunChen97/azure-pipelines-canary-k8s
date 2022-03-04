# -*- coding: utf-8 -*-
import commands

sCommand = "kubectl describe statefulset sampleapp -n dongkun"


def GetPodsCount():
    sOutput = commands.getoutput(sCommand)
    lOutput = sOutput.split("\n")
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

GetPodsCount()
