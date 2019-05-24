
'''
以下为预置代码（创建窗口，添加窗口标题和背景图）
'''
from VipCode import *
import random
class UI_Gold(PyQt5_QDialog):

    def showDialog(self):
        self.show()
    def setupUI(self):
        self.setFixedSize(600,400)
        self.setWindowTitle("黄金矿工")
        self.setBackground("bg1.png")
        # 存放矿石坐标的列表
        self.listXY=[[10,300],[453,350],[76,260],[129,320],[520,160],[190,190],[209,322],[259,180],[356,159],[456,222],[513,346],[333,268],[153,159],[268,357],[550,263]]
        random.shuffle(self.listXY)
        # 存放矿石的列表
        self.namelist=[]
        # 添加矿石  石头 金子 钻石
        for x in range(0,15,3):        
            self.addMineral(self.listXY[x][0],self.listXY[x][1],30,"gold.png",30)
            self.addMineral(self.listXY[x+1][0],self.listXY[x+1][1],20,"diamond.png",20)
            self.addMineral(self.listXY[x+2][0],self.listXY[x+2][1],50,"stone.png",50)      
        # 添加矿工和钩子
        self.elder=PyQt5_Qlabel(self,278,12,70,70)
        self.elder.setBackground("init.png")
        self.hook=PyQt5_Qlabel(self,290,88,20,15)
        self.hook.setBackground("hook.png")
        # 控制绳子摆动的变量
        self.finalX=0    
        self.finalY=30  
        # 启动游戏的按钮
        self.downButton=PyQt5_QPushButton(self,10,10,60,60)
        self.downButton.clicked.connect(self.downButtonclicked)
        self.isdo=0
        # 控制延长绳子的两个变量
        self.distanceX=0
        self.distanceY=0
    def downButtonclicked(self):  # 启动按钮的响应函数
        self.isdo=1
    def paintEvent(self,QpaintEvent):     # 绘制绳子的函数
        qp=QPainter(self)                 # 调用画笔
        qp.setPen(QPen(QColor(38,38,38),2))    #设置画笔的颜色和宽度

        if self.isdo==1:
            #"延长线断，检测碰撞"
            qp.drawLine(300,60,300+self.finalX+self.distanceX,60+self.finalY+self.distanceY)
            # 判断结果
            judge(dialog,300+self.finalX+self.distanceX,60+self.finalY+self.distanceY,60,30,5,20,30,50)
            # 返回结果
            flag1,flag2=YesOrNo(dialog)     # 判断结果的返回值
            if flag1==1 and flag2==0:               
                self.hook.setVisible(False)   # 隐藏钩子
                change_img(dialog,30,60,5)     # 替换矿石的图片为带钩子的图片
                print("捞取东西，还没上岸")
                # 将够到的矿石跟随绳子末端移动
                self.namelist[self.index][0].move( 300 - (getBorder()/2+3)+self.finalX+self.distanceX,60+self.finalY+self.distanceY)
            if flag1==1 and flag2==1:
                print("捞取东西，已经上岸") 
                playAudio("success.mp3")
                self.hook.setVisible(True)    # 钩子显示
                self.namelist[self.index][0].setVisible(False)  # 将捞上来的矿石隐藏
                # 删除捞到的矿石对应的坐标数据和列表数据
                del self.listXY[self.index]   
                del self.namelist[self.index] 
            #self.isdo=0
        else:
            # 绳子呈扇形摆动
            qp.drawLine(300,60,300+self.finalX,60+self.finalY)
            self.hook.move(290+self.finalX,59+self.finalY)  #将钩子移动到绳子末端的位置
            rock(dialog,30)       # 绳子摆动    （长度）

        refresh(dialog,3)         # 刷新页面     （速度）
    # 添加矿石的函数    
    def addMineral(self,x,y,size,png,reword):
        self.name=PyQt5_Qlabel(self,x,y,size,size)
        self.name.setBackground(png)
        self.namelist.append([self.name,reword])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = UI_Gold()
    dialog.setupUI()
    dialog.showDialog()
    app.exec_()