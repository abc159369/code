huskylens.initI2c()
huskylens.initMode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)
basic.forever(function () {
    huskylens.request()
    if (huskylens.readeBox(1, Content1.width) > 90) {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CCW, 255)
    } else if (huskylens.readeBox(1, Content1.width) > 30) {
        DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, 255)
    } else {
        DFRobotMaqueenPlus.mototStop(Motors.ALL)
    }
})
