#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun June 12 12:06:21 2020

@author: weiquan fan
"""

import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QCompleter, QFileDialog
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtCore import pyqtSignal, QEvent
from PyQt5.Qt import QUrl
from my_win import Ui_MainWindow
import csv

root_path_metadata = "./data/"

if not os.path.exists(root_path_metadata):
    os.makedirs(root_path_metadata)

class mainWin(QMainWindow, Ui_MainWindow):
    doubleClicked_speaker = pyqtSignal()
    doubleClicked_dialog = pyqtSignal()

    def __init__(self, parent=None):
        super(mainWin, self).__init__(parent)
        self.setupUi(self)

        ## emotion
        self.refresh_1()
        self.radioButton.clicked.connect(self.showPos)
        self.radioButton_2.clicked.connect(self.showNeu)
        self.radioButton_3.clicked.connect(self.showNeg)

        ## DA
        self.refresh_2()

        ## dialog identity
        self.refresh_3()
        self.frame_9.setHidden(True)
        self.checkBox_5.stateChanged.connect(self.use_subsysdem3)
        self.radioButton_5.clicked.connect(self.personA)
        self.radioButton_4.clicked.connect(self.personB)

        ## save buttons
        self.refresh_save()
        self.btn_save.clicked.connect(self.save_data)
        self.btn_save_2.clicked.connect(self.save_dialog_data)

        ## history
        self.list_speaker = []
        self.list_dialog = []

        self.lineEdit_speaker.installEventFilter(self)
        self.lineEdit.installEventFilter(self)
        self.doubleClicked_speaker.connect(self.completer_name_speaker)
        self.doubleClicked_dialog.connect(self.completer_name_dialog)

        ## video player
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_player)
        self.btn_open.clicked.connect(self.openVideoFile)
        self.btn_play_pause.clicked.connect(self.playPause)
        self.player.durationChanged.connect(self.getDuration)
        self.player.positionChanged.connect(self.getPosition)
        self.sld_duration.sliderMoved.connect(self.updatePosition)

    ## for opening video
    def openVideoFile(self):
        name = QFileDialog.getOpenFileName()[0]
        self.lineEdit.setText(name.split('/')[-1])
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(name)))
        # self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
        self.player.play()
    def playPause(self):
        if self.player.state()==1:
            self.player.pause()
        else:
            self.player.play()
    def getDuration(self, d):
        self.sld_duration.setRange(0, d)
        self.sld_duration.setEnabled(True)
        self.displayTime(d)
    def getPosition(self, p):
        self.sld_duration.setValue(p)
        self.displayTime(p)
    def displayTime(self, ms):
        minutes = int(ms/60000)
        seconds = int((ms-minutes*60000)/1000)
        dur_ms = self.sld_duration.maximum()
        dur_min = int(dur_ms/60000)
        dur_sec = int((dur_ms-dur_min*60000)/1000)
        self.lab_duration.setText('{:0>2d}:{:0>2d} / {:0>2d}:{:0>2d}'.format(minutes, seconds, dur_min, dur_sec))
    def updatePosition(self, v):
        self.player.setPosition(v)
        self.displayTime(self.sld_duration.maximum()-v)

    ## for history
    def eventFilter(self, widget, event):
        if widget == self.lineEdit_speaker:
            if event.type() == QEvent.MouseButtonDblClick:
                self.doubleClicked_speaker.emit()
        elif widget == self.lineEdit:
            if event.type() == QEvent.MouseButtonDblClick:
                self.doubleClicked_dialog.emit()
        return super().eventFilter(widget, event)

    def completer_name_dialog(self):
        self.completer = QCompleter(self.list_dialog)
        self.lineEdit.setCompleter(self.completer)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.completer.complete()
        self.completer.popup()

    def completer_name_speaker(self):
        self.completer = QCompleter(self.list_speaker)
        self.lineEdit_speaker.setCompleter(self.completer)
        self.completer.setCompletionMode(QCompleter.UnfilteredPopupCompletion)
        self.completer.complete()
        self.completer.popup()

    ## for label 1
    def showPos(self):
        self.listWidget.clear()
        self.listWidget.addItem("高兴")
        self.listWidget.addItem("兴奋")
        self.listWidget.addItem("自豪")
        self.listWidget.addItem("满足")
        self.listWidget.addItem("感激")
        self.listWidget.addItem("自信")
        self.listWidget.addItem("轻松")
        self.listWidget.addItem("羡慕")
    def showNeg(self):
        self.listWidget.clear()
        self.listWidget.addItem("生气")
        self.listWidget.addItem("伤心")
        self.listWidget.addItem("害怕")
        self.listWidget.addItem("烦恼")
        self.listWidget.addItem("孤独")
        self.listWidget.addItem("羞愧")
        self.listWidget.addItem("恶心")
        self.listWidget.addItem("失望")
        self.listWidget.addItem("郁闷")
        self.listWidget.addItem("不安")
        self.listWidget.addItem("紧张")
        self.listWidget.addItem("无奈")
        self.listWidget.addItem("纠结")
    def showNeu(self):
        self.listWidget.clear()
        self.listWidget.addItem("共情")
        self.listWidget.addItem("平静")


    ## for label 3
    def use_subsysdem3(self):
        if self.checkBox_5.isChecked():
            self.frame_9.setHidden(False)
        else:
            self.refresh_3()
            self.frame_9.setHidden(True)

    def personA(self):
        self.frame_3.setHidden(False)
        self.frame_8.setHidden(True)

    def personB(self):
        self.frame_3.setHidden(True)
        self.frame_8.setHidden(False)


    def refresh_gui(self):
        self.refresh_1()
        self.refresh_2()
        self.refresh_3()
        self.refresh_save()


    def refresh_1(self):
        self.buttonGroup_2.setExclusive(False)
        self.radioButton.setChecked(False)
        self.radioButton_2.setChecked(False)
        self.radioButton_3.setChecked(False)
        self.buttonGroup_2.setExclusive(True)
        self.listWidget.clear()
        self.checkBox_3.setChecked(True)
        self.checkBox_2.setChecked(True)
        self.checkBox.setChecked(True)
        self.checkBox_4.setChecked(False)

    def refresh_2(self):
        self.listWidget_2.clear()
        self.listWidget_2.addItem("问候")
        self.listWidget_2.addItem("提问")
        self.listWidget_2.addItem("回答")
        self.listWidget_2.addItem("陈述观点")
        self.listWidget_2.addItem("陈述非观点")
        self.listWidget_2.addItem("道歉")
        self.listWidget_2.addItem("命令")
        self.listWidget_2.addItem("赞同")
        self.listWidget_2.addItem("反对")
        self.listWidget_2.addItem("表达知会")
        self.listWidget_2.addItem("欣赏")
        self.listWidget_2.addItem("叹词")
        self.listWidget_2.addItem("结束对话")
        self.listWidget_2.addItem("引用")
        self.listWidget_2.addItem("其他")

    def refresh_3(self):
        # self.checkBox_5.setChecked(False)
        self.buttonGroup.setExclusive(False)
        self.radioButton_4.setChecked(False)
        self.radioButton_5.setChecked(False)
        self.buttonGroup.setExclusive(True)
        self.buttonGroup_3.setExclusive(False)
        self.radioButton_6.setChecked(False)
        self.radioButton_7.setChecked(False)
        self.radioButton_8.setChecked(False)
        self.radioButton_9.setChecked(False)
        self.radioButton_10.setChecked(False)
        self.buttonGroup_3.setExclusive(True)
        # self.frame_9.setHidden(True)
        self.frame_3.setHidden(True)
        self.frame_8.setHidden(True)

    def refresh_save(self):
        self.lineEdit_2.setText('0')
        self.lineEdit_3.setText('0')
        self.lineEdit_4.setText('0')
        self.lineEdit_5.setText('0')
        self.lineEdit_6.setText('0')
        self.lineEdit_7.setText('0')
        self.lineEdit_speaker.setText('')

    def save_data(self):

        ## check many things
        try:
            self.label_val = self.buttonGroup_2.checkedButton().text()
            self.label_emotion = self.listWidget.selectedItems()[0].text()
        except:
            QMessageBox.information(self,'提示','请选择具体情感后再重新保存', QMessageBox.Yes)
            return False

        try:
            self.label_da = self.listWidget_2.selectedItems()[0].text()
        except:
            QMessageBox.information(self,'提示','请选择对话状态后再重新保存', QMessageBox.Yes)
            return False

        self.label_iden_isok = self.checkBox_5.isChecked()
        if self.label_iden_isok:
            if self.buttonGroup.checkedId() == -1:
                QMessageBox.information(self,'提示','您已勾选该对话身份可标，请选择说话人身份后再重新保存', QMessageBox.Yes)
                return False
            else:
                self.label_iden = self.buttonGroup.checkedButton().text()
                if self.label_iden == "倾诉者":
                    self.label_reason = self.lineEdit_reason.text()
                    self.label_result = self.lineEdit_result.text()
                    self.label_reaction = "空"
                else:
                    self.label_reason = "空"
                    self.label_result = "空"
                    try:
                        self.label_reaction = self.buttonGroup_3.checkedButton().text()
                    except:
                        QMessageBox.information(self,'提示','您已勾选该对话身份可标，请选择倾诉者反应后再重新保存', QMessageBox.Yes)
                        return False
        else:
            self.label_iden = "不可标"
            self.label_reason = "不可标"
            self.label_result = "不可标"
            self.label_reaction = "不可标"


        if self.lineEdit_speaker.text() == '':
            QMessageBox.information(self,'提示','请输入说话人姓名', QMessageBox.Yes)
            return False
        else:
            self.name_speaker = self.lineEdit_speaker.text()

        try:
            self.start_time = "{}:{}:{}".format(int(self.lineEdit_2.text()), int(self.lineEdit_3.text()), int(self.lineEdit_4.text()))
            self.end_time = "{}:{}:{}".format(int(self.lineEdit_5.text()), int(self.lineEdit_6.text()), int(self.lineEdit_7.text()))
        except:
            QMessageBox.information(self,'提示','时间应输入整数', QMessageBox.Yes)
            return False

        if self.lineEdit.text() == '':
            QMessageBox.information(self,'提示','请输入视频名字', QMessageBox.Yes)
            return False
        else:
            self.name_dialog = self.lineEdit.text()


        if not os.path.exists(root_path_metadata+self.name_dialog+'.csv'):
            with open(root_path_metadata+self.name_dialog+'.csv',"a",newline='',encoding='utf_8_sig') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                writer.writerow(['视频名字', '说话者姓名', '起始时间', '结束时间', '情绪（粗粒度）', '情绪（细粒度）', '是否基于音频', '是否基于视频', '是否基于文本', '是否难以标注', '对话状态', '是否可标对话身份', '说话人身份', '起因', '结果', '倾诉者反应'])

        ## save
        self.label_emotion_audio_based = self.checkBox_3.isChecked()
        self.label_emotion_video_based = self.checkBox_2.isChecked()
        self.label_emotion_text_based = self.checkBox.isChecked()
        self.label_emotion_hard = self.checkBox_4.isChecked()


        onelist = [self.name_dialog, self.name_speaker, self.start_time, self.end_time, self.label_val, self.label_emotion, self.label_emotion_audio_based, self.label_emotion_video_based, self.label_emotion_text_based, self.label_emotion_hard, self.label_da, self.label_iden_isok, self.label_iden, self.label_reason, self.label_result, self.label_reaction]
        with open(root_path_metadata+self.name_dialog+'.csv',"a",newline='',encoding='utf_8_sig') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(onelist)

        self.refresh_gui()
        self.list_dialog.append(self.name_dialog)
        self.list_speaker.append(self.name_speaker)
        self.list_dialog = list(set(self.list_dialog))
        self.list_speaker = list(set(self.list_speaker))
        # self.lineEdit.setCompleter(QCompleter(self.list_dialog))
        # self.lineEdit_speaker.setCompleter(QCompleter(self.list_speaker))

        return True

    def save_dialog_data(self):
        flag_save_success = self.save_data()
        if flag_save_success == False: return 0
        QMessageBox.about(self,'提示','对话保存成功')
        self.refresh_gui()
        self.lineEdit.setText('')
        self.lineEdit_reason.setText('')
        self.lineEdit_result.setText('')
        self.checkBox_5.setChecked(False)
        self.frame_9.setHidden(True)


    def del_last_data(self):
        try:
            with open(root_path_metadata+self.name_dialog+'.csv',"r",newline='',encoding='utf_8_sig') as csvfile:
                data = csvfile.readlines()
                del data[-1]
            with open(root_path_metadata+self.name_dialog+'.csv',"w",newline='',encoding='utf_8_sig') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                for row in data:
                    writer.writerow(row.strip().split(','))
                # writer.writerows(data)
            QMessageBox.about(self,'提示','上一句的标注已删除')
        except:
            QMessageBox.information(self,'提示','该视频尚未保存任何数据', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = mainWin()
    main_win.show()
    # main_win.showFullScreen()
    sys.exit(app.exec_())

