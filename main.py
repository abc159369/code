huskylens.init_i2c()
huskylens.init_mode(protocolAlgorithm.ALGORITHM_FACE_RECOGNITION)

def on_forever():
    huskylens.request()
    if huskylens.reade_box(1, Content1.WIDTH) > 90:
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CCW, 255)
    elif huskylens.reade_box(1, Content1.WIDTH) > 30:
        DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, 255)
    else:
        DFRobotMaqueenPlus.motot_stop(Motors.ALL)
basic.forever(on_forever)
