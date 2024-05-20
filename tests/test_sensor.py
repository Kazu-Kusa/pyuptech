import unittest

from pyuptech import OnBoardSensors


class DisplayTests(unittest.TestCase):

    def setUp(self):
        self.sen = OnBoardSensors()

    def test_adc(self):
        print(self.sen.adc_io_open().adc_all_channels())

    def test_io(self):
        print(
            self.sen.adc_io_open()
            .set_all_io_mode(0)
            .set_all_io_level(1)
            .io_all_channels()
        )

    def test_mpu(self):
        print(self.sen.MPU6500_Open().atti_all())
        print(self.sen.gyro_all())
        print(self.sen.acc_all())
        print("finished")


if __name__ == "__main__":
    unittest.main()
