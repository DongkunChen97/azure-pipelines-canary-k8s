# -*- coding: utf-8 -*-
import sys
import json


def GetPodsCount(sFile):
    """ decode the latest revision """
    oFile = open(sFile, "r")
    sJson = oFile.read()
    lHistory = json.loads(sJson)
    dLatestVersion = lHistory[-1]
    sLatestVersion = dLatestVersion["revision"]
    print(sLatestVersion)

if __name__ == '__main__':
    sFile = sys.argv[1]
    # print(sJson)
    # sJson = "0.0.1"
    # sJson = '[{"revision":66, "name":"cdk"}]'
    GetPodsCount(sFile)