#-*- coding:utf-8 -*-
from airtest.core.api import *
import pytest
from common import case_tag
from common.maincase import Android_AVC
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd=r'/usr/local/Cellar/tesseract/4.0.0.1/bin/tesseract'
# from poco.drivers.android.uiautomation import AndroidUiautomationPoco
# poco=AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

class TestAndroid:

    def setup(self):
        self.avc = Android_AVC()
        self.channel_name = "AVCAUTO"
        self.password = "avctest"
        self.packageName = "io.agora.vcall"
        self.nickname = "jkjl"
        self.screeshot_path = "resource/screenshot/"

    def tearDown(self):
        pass


    # 设置界面，昵称不超过18
    @pytest.mark.parametrize("nickname", ["1234567899876543210"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinChannel(self,nickname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        # avc.nick_comfirm(nickname)
        # sleep(5)
        path1 = self.screeshot_path+"getNickname.png"
        snapshot(path1)
        sleep(5)
        width,height = avc.getImageSize(path1)

        print(text)


        # poco("io.agora.vcall:id/me_back").click()

