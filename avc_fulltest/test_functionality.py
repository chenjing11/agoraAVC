#-*- coding:utf-8 -*-
from airtest.core.api import *
init_device("Android")
connect_device("Android:///")
import airtest.core.android.android
from PIL import Image
import cv2
import pytest
import time
from common import case_tag
from common.maincase import Android_AVC
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/Cellar/tesseract/4.0.0.1/bin/tesseract'
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco=AndroidUiautomationPoco()
poco.device.wake()

class TestAndroid:

    def setup(self):
        self.avc = Android_AVC()
        self.channel_name = "AVCAUTO"
        self.password = "avctest"
        self.packageName = "io.agora.vcall"

    def tearDown(self):
        pass

    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinChannel(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(self.password)
        avc.joinChannel()
