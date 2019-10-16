#-*- coding:utf-8 -*-
from airtest.core.api import *
from airtest import aircv
from airtest.core.cv import Predictor
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
        poco("io.agora.vcall:id/btSettings").click()
        poco("io.agora.vcall:id/editNickName").click()
        text(nickname)


    def getWordsInImage(self,image_path):
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image,lang='chi_sim')
        return text

    def getImageSize(self, img_path):
        img = Image.open(img_path)
        width = img.size[0]
        height = img.size[1]
        print("width:%s,height:%s" % (width, height))
        return width, height

    def getCustomizeImage(self, origin_image_path, new_image_path, left, upper, right, lower):
        """
        :param origin_image_path: 原始图片的路径
        :param new_image_path: 图片裁剪后的路径
        :param left: 左 坐标
        :param upper: 上 坐标
        :param right: 右 坐标
        :param lower: 下 坐标
        :return:
        """
        img = Image.open(origin_image_path)
        cropped = img.crop((left, upper, right, lower))
        cropped.save(new_image_path)





