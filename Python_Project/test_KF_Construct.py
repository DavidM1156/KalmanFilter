from KF_Script import KF
import unittest

class TestKF(unittest.TestCase):

    def test_Construct_x_v(self):
        x_test=0.2
        v_test=0.5
        accel_variance_test=1.2
        KF_test = KF(x_test,v_test,accel_variance_test)
        self.assertAlmostEqual(KF_test.pos,x_test)
        self.assertAlmostEqual(KF_test.vel,v_test)

    def test_predict_build(self):
        x_test=0.2
        v_test=0.5
        accel_variance_test=1.2
        KF_test = KF(x_test,v_test,accel_variance_test)
        KF_test.predict(dt=0.1)
        #self.assertAlmostEqual(KF_test.predict,x_test)

if __name__ == '__main__':
   unittest.main()
