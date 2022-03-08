# -*- coding: utf-8 -*-
import sys
import json


def GetPodsCount(sJson):
    """ decode the latest revision """

    lHistory = json.loads(sJson)
    dLatestVersion = lHistory[0]
    sLatestVersion = dLatestVersion["revision"]
    print(sLatestVersion)



if __name__ == '__main__':
    sJson = sys.argv[1]
    # print(sJson)
    # sJson = "0.0.1"
    # sJson = '[{"revision":66, "name":"cdk"}]'
    print(len(sJson))
    GetPodsCount(sJson)