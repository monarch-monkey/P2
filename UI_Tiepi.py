from VipCode import *
from UI_Answer import *


# 创建窗口类
class UI_TiePi(PyQt5_QDialog):

    #================代码书写位置======================
    #显示窗口的方法
    def showDialog(self):
        #让窗口显示出来
        self.show()
    def setupUI(self): 
        #设置窗口的大小，不可拖动更改窗口的大小
        self.answer = PyQt5_QPushButton(self,60,316,57,57)    
        self.answer.setBackground("main_answer_normal.png")
        self.answer.setPressedBackground("main_answer_pressed.png")
        self.answer.clicked.connect(self.answerClicked)
        
        self.setFixedSize(960,600)
         #设置窗口的标题
        self.setWindowTitle("Hello,铁皮！！")
        self.setBackground("mainBg.png")

        self.label = PyQt5_Qlabel(self,370,180,350,350)
        self.gif = PyQt5_QMovie("main_lion.gif")
        self.gif.setScaledSize(self.label.size())   #相片适应相框的大小
        self.label.setMovie(self.gif)
        self.gif.start()
        
        self.allGroup = PyQt5_QGroupBox(self,814,156,60,367)
        self.allGroup.setBackground("action_group.png")
        self.allGroup.setVisible(False)    #设置组控件隐藏

        self.halo = PyQt5_QPushButton(self.allGroup,9,5,42,42)
        self.halo.setBackground("main_halo_normal.png")
        self.halo.setPressedBackground("main_halo_pressed.png")
        self.halo.clicked.connect(self.haloClicked)
        
        self.anger = PyQt5_QPushButton(self.allGroup,9,56,42,42)
        self.anger.setBackground("main_anger_normal.png")
        self.anger.setPressedBackground("main_anger_pressed.png")
        self.anger.clicked.connect(self.angerClicked)

        self.cry = PyQt5_QPushButton(self.allGroup,9,107,42,42)
        self.cry.setBackground("main_cry_normal.png")
        self.cry.setPressedBackground("main_cry_pressed.png")
        self.cry.clicked.connect(self.cryClicked)

        self.glasses = PyQt5_QPushButton(self.allGroup,9,158,42,42)
        self.glasses.setBackground("main_glasses_normal.png")
        self.glasses.setPressedBackground("main_glasses_pressed.png")
        self.glasses.clicked.connect(self.glassesClicked)

        self.boxing = PyQt5_QPushButton(self.allGroup,9,209,42,42)
        self.boxing.setBackground("main_boxing_normal.png")
        self.boxing.setPressedBackground("main_boxing_pressed.png")
        self.boxing.clicked.connect(self.boxingClicked)

        self.disappear = PyQt5_QPushButton(self.allGroup,9,260,42,42)
        self.disappear.setBackground("main_disappear_normal.png")
        self.disappear.setPressedBackground("main_disappear_pressed.png")
        self.disappear.clicked.connect(self.disappearClicked)

        self.hamburger = PyQt5_QPushButton(self,60,388,57,57)
        self.hamburger.setBackground("main_hamburger_normal.png")
        self.hamburger.setPressedBackground("main_hamburger_pressed.png")
        self.hamburger.clicked.connect(self.hamburgerClicked)

        self.juice = PyQt5_QPushButton(self,60,460,57,57)
        self.juice.setBackground("main_juice_normal.png")
        self.juice.setPressedBackground("main_juice_pressed.png")
        self.juice.clicked.connect(self.juiceClicked)

        #控制all的按钮
        self.all = PyQt5_QCheckBox(self,815,465,58,58)
        self.all.setCheckedBackground("main_all_checked.png")
        self.all.setUncheckedBackground("main_all_unchecked.png")
        self.all.setIndicator(False)        #隐藏复选框指示器
        self.all.stateChanged.connect(self.allClicked) 
        
        # self.actionNum_text.setBackground("action_num.png")
        # self.actionNum_text.setTextColor("rgb(31,79,101)")
        # self.actionNum_text.setText("6")
    
        self.addBodyButton(self.label)
        self.tray=PyQt5_QSystemTrayIcon(self)
        self.tray._setIcon("icon.png")
        self.tray.show()

        self.menuShow = self.tray.addMenu("显示")
        self.menuShow.triggered.connect(self.trayShow)

        self.menuExit = self.tray.addMenu("退出")
        self.menuExit.triggered.connect(self.trayExit)


        self.framelessBox = PyQt5_FramelessBox()
        
        self.framelessBox.setWindowsTop(True)
        self.framelessBox.setWindowsTransparent(True)
        self.frameLabel = PyQt5_Qlabel(self.framelessBox,0,0,240,240)
        #self.frameLabel.setBackground("icon.png")
        self.playframeGif("frame_fly.gif")

        self.anim = PyQt5_Animation(self.framelessBox)
        self.anim.setDuration(4000)
        self.width = getDesktopWidth()
        self.height = getDesktopHeight()
        self.anim.setEndValues(self.width-340,self.height-340,140,140)
        self.anim.setMode(Mode.InOut)
        self.anim.valueChanged.connect(self.animChange)
        self.anim.animFinished.connect(self.animFinish)

        self.closeAnim = PyQt5_Animation(self.framelessBox)
        self.closeAnim.setDuration(4000)
        self.closeAnim.setEndValues(self.width/2-170,self.height/2-170,340,340)
        self.closeAnim.setMode(Mode.InOut)

        self.closeAnim.valueChanged.connect(self.animChange)
        self.closeAnim.animFinished.connect(self.closeAnimFinish)

        self.frameLabel.entered.connect(self.frameEnter)
        self.isAnimFinished = False
        self.frameLabel.leaved.connect(self.frameLeave)
        self.frameLabel.doubleclicked.connect(self.frameDouble)
        self.frameLabel.moved.connect(self.frameMove)
        self.frameLabel.pressed.connect(self.framePress)

        self.addBodyButton(self.label)
    def frameLeave(self):
        if self.isAnimFinished:
            self.playframeGif("frame_sleep.gif")
    def frameEnter(self):
        if self.isAnimFinished:
            self.playframeGif("frame_play.gif")    
    def framePress(self,event):
        self.posX = event.x()
        self.posY = event.y()    
    def frameMove(self,event):
        if self.isAnimFinished:
            self.globalX=event.globalX()
            self.globalY=event.globalY()
            self.framelessBox.move(self.globalX-self.posX,self.globalY-self.posY)    
    def frameDouble(self):
        self.trayShow()               
    def closeAnimFinish(self):
        self.framelessBox.close()
        self.show()    
    def changeGif(self):
        self.flyCount -= 1
        if self.flyCount == 1:
            self.frameGif.stop()
            self.playframeGif("frame_sleep.gif")
    def animFinish(self):
        self.isAnimFinished = True
        self.playframeGif("frame_down.gif")
        
        self.flyCount = self.frameGif.frameCount()
        self.frameGif.frameChanged.connect(self.changeGif)    
    def animChange(self):
    
        self.frameLabel.setSize(self.framelessBox.size())
        self.frameGif.setScaledSize(self.frameLabel.size())    

    def playframeGif(self,gif_name):
        self.frameGif = PyQt5_QMovie(gif_name)
        self.frameGif.setScaledSize(self.frameLabel.size())
        self.frameLabel.setMovie(self.frameGif)
        self.frameGif.start()    

    def trayExit(self):
        QApplication.quit()
    def trayShow(self):
        #self.framelessBox.close()
        #self.show()
        self.playframeGif("frame_fly.gif")
        self.isAnimFinished = False
        self.closeAnim.start()    
    def closeEvent(self,event):
        self.hide()
        self.framelessBox.show()
        self.anim.start()
        event.ignore()
      
        
    def allClicked(self,state):
        if state == 2:
            self.allGroup.setVisible(True)
        elif state == 0:
            self.allGroup.setVisible(False)        
    def hamburgerClicked(self):
        #QMessageBox.information(self,"提示信息","按钮被点击了。")
        self.playGif("hamburger.gif")
        self.playAudio("hamburger.wav")
    def returnGif(self):
        self.frameCount -= 1
        if self.frameCount == 0:
            self.gif.stop()
            self.gif = PyQt5_QMovie("main_lion.gif")
            self.gif.setScaledSize(self.label.size())
            self.label.setMovie(self.gif)
            self.gif.start()    
    def juiceClicked(self):
        #QMessageBox.information(self,"提示信息","按钮被点击")
        self.playGif("juice.gif")
        self.playAudio("juice.wav")
    def playGif(self,gif_name):
        self.gif = PyQt5_QMovie(gif_name)
        self.gif.setScaledSize(self.label.size())
        self.label.setMovie(self.gif)
        self.gif.start()
        self.frameCount = self.gif.frameCount()
        self.gif.frameChanged.connect(self.returnGif)
    def playAudio(self,audio_name):
        self.media = PyQt5_QMediaPlayer()
        self.media.prepare_audio(audio_name)
        self.media.play()  
    def haloClicked(self):
        self.playGif("halo.gif")
        self.playAudio("halo.wav")
    def angerClicked(self):
        self.playGif("anger.gif")
        self.playAudio("anger.wav")   
    def cryClicked(self):
        self.playGif("cry.gif")
        self.playAudio("cry.wav")
    def boxingClicked(self):
        self.playGif("boxing.gif")
        self.playAudio("boxing.wav")
    def glassesClicked(self):
        self.playGif("glasses.gif")
        self.playAudio("glasses.wav")
    def disappearClicked(self):
        self.playGif("disappear.gif")
        self.playAudio("disappear.wav")
    def answerClicked(self):
        dialog = UI_Answer()
        dialog.setupUI()
        dialog.showDialog()     
        dialog.exec_()                     
if __name__ == '__main__':
    # 通过QApplication创建应用
    app = QApplication(sys.argv)
    #================代码书写位置======================
    #创建一个窗口类对象
    dialog = UI_TiePi()
    dialog.setupUI()
    #调用显示窗口的方法
    dialog.showDialog()
    #================================================
    # 让应用持续保持运行
    app.exec_()
    
    
    