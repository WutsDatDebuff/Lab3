import Lab2.bmi as bmi

def test_bmi_normal_weight():
    h=1.73
    w=57
    Bmi=bmi.cal_bmi(h,w)
    assert (Bmi == 0)

def test_bmi_over_weight():
    h = 1.73
    w = 100
    Bmi = bmi.cal_bmi(h, w)
    assert (Bmi == 1)

def test_bmi_under_weight():
    h = 1.73
    w = 30
    Bmi = bmi.cal_bmi(h, w)
    assert (Bmi == -1)

