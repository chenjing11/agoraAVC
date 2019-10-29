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
        self.screeshot_path = "resource/images/"

    def tearDown(self):
        pass


    # 设置界面，昵称不超过18
    @pytest.mark.parametrize("nickname", ["1234567899876543210","732djshgdshGHCTbddfbhddh","37438"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_editNick(self,nickname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        sleep(1)
        avc.nick_comfirm(nickname)
        sleep(5)
        path1 = self.screeshot_path+"getNickname1.png"
        path2 = self.screeshot_path+"getNickname2.png"
        snapshot(path1)
        width,height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 4/9 * height, width, 1/2*height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert len(text) <=18

        # 返回AVC首页
        avc.nickBackHome()


    # 频道名不能超过18
    @pytest.mark.parametrize("channelname", ["1234567899876543210","eheygfFSFGCFTS378426","387642"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinchannel_1(self, channelname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(channelname)
        sleep(1)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 8/ 15 * height, width, 3 / 5 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert len(text) <=18


    # 频道名自动大写
    @pytest.mark.parametrize("channelname", ["sdagh"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinchannel_2(self, channelname):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(channelname)
        sleep(1)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 8/ 15 * height, width, 3 / 5 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text =="SDAGH"




     # 密码不能超过18
    @pytest.mark.parametrize("password", ["1234567899876543210","eheygfFSFGCFTS378426","387642"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinchannel_3(self, password):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(password)
        sleep(1)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 3/ 5 * height, width, 2 / 3 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert len(text) <=18



    #有效房间名，无密码加入房间
    @pytest.mark.parametrize("password", ["1234567899876543210","eheygfFSFGCFTS378426","387642"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_joinchannel_5(self, password):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        sleep(1)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 3/ 5 * height, width, 2 / 3 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert len(text) <=18









