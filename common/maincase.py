#-*- coding:utf-8 -*-
from airtest.core.api import *
from PIL import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'/usr/local/Cellar/tesseract/4.0.0_1/bin/tesseract'
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco=AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

class Android_AVC():
    def __init__(self):
        self.interval = 2

    def setCurrentDevice(self,device):
        set_current(device)

    def startAVC(self,packageName):
        start_app(packageName)
        # wait(Template(r"resource/images/tpl1568208771836.png", record_pos=(-0.002, -0.009), resolution=(1080, 1920)))
        sleep(self.interval)

    def inputChannelName(self,channelname):
        poco("io.agora.vcall:id/edit_name").click()
        text(channelname)

    def inputPassword(self,password):
        poco("io.agora.vcall:id/edit_password").click()
        text(password)

    def joinChannel(self):
        poco("io.agora.vcall:id/btn_join").click()

    def nick_comfirm(self,nickname):
        poco("io.agora.vcall:id/me").click()
        poco("io.agora.vcall:id/nickname").click()
        poco("io.agora.vcall:id/nickEditText").click()
        text(nickname)
        poco("io.agora.vcall:id/nickConfirm").click()

    def getWordsInImage(self,image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image,lang='chi_sim')
        return text

