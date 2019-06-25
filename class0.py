'''
预置代码：创建一个窗口并显示
'''
from VipCode import *
import random

class Anim_Dialog(PyQt5_FramelessBox):
    def showDialog(self):
        self.show()
    def setupUI(self):
        self.setFixedSize(750, 550)
        self.setWindowsTransparent(True)
        self.label=PyQt5_Qlabel(self,0,0,750,550)
        self.label.setBackground("bg_canvas.png")

        self.exit=PyQt5_QPushButton(self,215,0,305,140)
        self.exit.setBackgroundColor("transparent")
        self.exit.clicked.connect(self.proExit)

        self.listXY=[[132,160], [319,160], [515,165], [100,250], [320,250], [520,250], [95,347], [320,352], [540,354]]
        self.hamsters=[]
        
        for x in range(9):
            self.addHamsters(x)

        # 计时器
        self.timer=QTimer()
        self.timer.start(1000)   # 1000 ms
        self.timer.timeout.connect(self.timeout)  # 超时

        self.flag=-1

        self.hammer=PyQt5_Qlabel(self,132,160,122,122)
        self.hammer.setBackground("hammer.png")
        self.hammer.setVisible(False)
       
        self.score = 0
        self.finalTime = 15

        self.timeLabel=PyQt5_Qlabel(self,250,160,120,25)
        self.timeLabel.setFont(QFont("手札体-简",16))
        self.timeLabel.setTextColor("white")
        self.timeLabel.setText("时间：%d"%self.finalTime)
        self.scoreLabel=PyQt5_Qlabel(self,380,160,100,25)
        self.scoreLabel.setFont(QFont("手札体-简",16))
        self.scoreLabel.setTextColor("white")
        self.scoreLabel.setText("得分：%d"%self.score)

    def timeout(self):

        while True:
            index=random.randint(0,8)
            self.r = random.randint(0,2)
            if self.hamsters[index][0].isVisible()==False:
                if self.r == 0:
                    self.hamsters[index][0].setBackground("rabbit.png")
                self.hamsters[index][0].setVisible(True)
                self.hamsters[self.flag][0].setVisible(True)
                self.hammer.setVisible(False)
                break

        for i in self.hamsters:
            if i[0].isVisible():
                i[1]+=1
                if i[1]>3:
                    i[0].setVisible(False)
                    i[1]=0 
                    i[0].setBackground("hamster.png")
                    i[0].setEnabled(True) 
        self.finalTime -= 1
        if self.finalTime <= 0:
            self.timer.stop()
            QMessageBox.information(self,"得分","本次的得分为:"+str(self.score)) 
            self.close()
            dialog1=Anim_Dialog()
            dialog1.setupUI()
            dialog1.showDialog()                 
        self.timeLabel.setText("时间：%d"%self.finalTime)
    def addHamsters(self,x):
        self.name=PyQt5_Qlabel(self,self.listXY[x][0],self.listXY[x][1],122,122)
        self.name.setBackground("hamster.png")
        self.hamsters.append([self.name,0])
        self.name.setVisible(False)
        self.name.pressed.connect(lambda:self.hitHamsters(x))
    def hitHamsters(self,x):
        
        self.hamsters[x][0].setBackground("hit.png")
        self.hamsters[x][0].setEnabled(False)
        self.hammer.setVisible(True)
        self.hammer.move(self.listXY[x][0],self.listXY[x][1]) 
        self.score += 1  
        self.scoreLabel.setText("得分：%d"%self.score)
    def proExit(self):
        app.quit() 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog =Anim_Dialog()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()       