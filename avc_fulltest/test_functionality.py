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




    # 获取版本号 (当前V4.0.0、RTC 2.9.1、RTM 1.0.1)
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_getversion(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 41/ 50* height, width, 8/9*height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "V4.0.0"
        avc.checkversion()
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 41/ 50 * height, width,8/9*height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "RTC 2.9.1"
        avc.checkversion()
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 41/ 50 * height, width, 8/9*height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text == "RTM 1.0.1"
        avc.key_back()


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
        avc.key_back()


    # 频道名不能超过18
    @pytest.mark.parametrize("channelname", ["1234567899876543210","eheygfFSFGCFTS378426","387642"])
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_Namelength(self, channelname):
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
    def test_Nameauto_capitalized(self, channelname):
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
    def test_PWDlength(self, password):
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
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_name_valid(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        avc.leaveChannel()


    #房间名小于3，无密码加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_namelength_less_3(self):
        self.channel_name="12"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.joinChannel()
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 27/50 * height, width, 29/50* height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text =="不 能 少 于 3 位"
        # avc.leaveChannel()



    #房间名大于18，无密码加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_namelength_longer_18(self):
        self.channel_name="123456789123456789000"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        # avc.nick_comfirm(self.nickname)
        # avc.nick_back()
        avc.inputChannelName(self.channel_name)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 49/100 * height, width, 13/25 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text =="123456789123456789"
        avc.joinChannel()
        avc.leaveChannel()



    #房间名有效，密码大于18加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_PWDlength_longer_18(self):
        self.password="123456789123456789000"
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(self.password)
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 29/50 * height, width, 31/50 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text =="123456789123456789"
        avc.joinChannel()
        avc.leaveChannel()



    #房间名有效，密码有效，mute本地视频加入房间
    @pytest.mark.tags(case_tag.ANDROID, case_tag.MEDIUM, case_tag.AUTOMATED, case_tag.FUNCTIONALITY)
    def test_mutelocalvideo_joinchanel(self):
        avc = self.avc
        avc.setCurrentDevice(0)
        avc.startAVC(self.packageName)
        avc.nick_comfirm(self.nickname)
        avc.mutelocalvideo_channelout()
        avc.settings_back()
        avc.inputChannelName(self.channel_name)
        avc.inputPassword(self.password)
        avc.joinChannel()
        path1 = self.screeshot_path + "getNickname1.png"
        path2 = self.screeshot_path + "getNickname2.png"
        snapshot(path1)
        width, height = avc.getImageSize(path1)
        avc.getCustomizeImage(path1, path2, 0, 29/50 * height, width, 31/50 * height)
        text = avc.getWordsInImage(path2)
        print(text)
        assert text =="123456789123456789"
        avc.leaveChannel()


















