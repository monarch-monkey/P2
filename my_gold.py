'''
以下为预置代码（创建窗口，添加窗口标题和背景图）
'''
from VipCode import *
import random
#封装为一个     .exe   pyinstaller
 #       pyinstaller -F a.py

class UI_Gold(PyQt5_QDialog):

    def showDialog(self):
        self.show()
    def setupUI(self):
        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")

        self.listXY=[[10,300],[453,350],[76,260],[129,320],[520,160],[190,190],[209,322],[259,180],[356,159],[456,222],[513,346],[333,268],[153,159],[268,357],[550,263]]
        random.shuffle(self.listXY)
        self.namelist=[]
        for x in range(0,len(self.listXY),3):
            self.addmineral(x,self.listXY[x][0],self.listXY[x][1],30,"gold.png",30)
            self.addmineral(x,self.listXY[x+1][0],self.listXY[x+1][1],50,"stone.png",5)
            self.addmineral(x,self.listXY[x+2][0],self.listXY[x+2][1],20,"diamond.png",60)
        
        self.elder=PyQt5_Qlabel(self,278,12,70,70)
        self.elder.setBackground("init.png")
        self.hook=PyQt5_Qlabel(self,290,88,20,15)
        self.hook.setBackground("hook.png")

        self.finalX=0
        self.finalY=30

        self.downButton=PyQt5_QPushButton(self,0,0,600,400)
        self.downButton.clicked.connect(self.downButtonClicked)
        self.downButton.setBackgroundColor("transparent")
        self.isdo=0

        self.distanceX=0
        self.distanceY=0

        self.elderGif=PyQt5_QMovie("action.gif")
        self.elderGif.setScaledSize(self.elder.size())
        self.elder.setMovie(self.elderGif)

        self.finalTime=60
        self.finalTimeLabel=PyQt5_Qlabel(self,30,40,100,15)
        self.finalTimeLabel.setText("倒计时：%s"%self.finalTime)
        
        self.timer=QTimer(self)
        self.timer.timeout.connect(self.timeout)

        self.endLabel=PyQt5_Qlabel(self,0,0,600,400)
        self.endLabel.setBackground("gameOver.jpg")
        self.endLabel.setVisible(False)

        self.isinit=0
        self.beginLabel=PyQt5_Qlabel(self,0,0,600,400)
        self.beginLabel.setBackground("begin.png")
        self.beginButton=PyQt5_QPushButton(self,120,20,180,180)
        self.beginButton.setBackgroundColor("transparent")
        self.beginButton.clicked.connect(self.beginButtonClicked)
    def timeout(self):
        self.finalTime-=1
        if self.finalTime<=0:
            self.timer.stop()
            self.endLabel.setVisible(True)
        self.finalTimeLabel.setText("倒计时：%d"%self.finalTime)
    def beginButtonClicked(self):
        self.beginLabel.setVisible(False)
        self.beginButton.setVisible(False) 
        self.timer.start(1000)
        self.isinit=1   
    def downButtonClicked(self):
        self.elder.setBackground("") 
        self.elderGif.start()          
        self.isdo=1
    def paintEvent(self,paintEvent):
        qp=QPainter(self)
        qp.setPen(QPen(QColor(38,38,38),2)) 
        
        if self.isdo==1:
            qp.drawLine(300,60,300+self.finalX+self.distanceX,60+self.finalY+self.distanceY)
            judge(dialog,300+self.finalX+self.distanceX,60+self.finalY+self.distanceY,60,30,5,20,30,50)
            flag1,flag2=YesOrNo(dialog)
            if flag1 == 1 and flag2 == 0:
                #print("捞取东西，还没上岸")
                self.hook.setVisible(False)
                change_img(dialog,30,60,5)
                self.namelist[self.index][0].move(300-(getBorder()/2+3)+self.finalX+self.distanceX,60+self.finalY+self.distanceY)
                
            if flag1 == 1 and flag2 == 1:
                self.elderGif.stop() 
                #print("捞取东西，已经上岸")
                playAudio("success.mp3")
                self.namelist[self.index][0].setVisible(False)
                self.hook.setVisible(True)
                del self.listXY[self.index] 
                del self.namelist[self.index]     
        elif self.isinit==1:               
            qp.drawLine(300,60,300+self.finalX,60+self.finalY)
            self.hook.move(290+self.finalX,58+self.finalY)
            rock(dialog,30)         
        refresh(dialog,3)
    def addmineral(self,i,x,y,size,img,reward):
        name="mineral"+str(i)
        self.name=PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(img)
        self.namelist.append([self.name,reward])
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()