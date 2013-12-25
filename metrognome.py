#!/usr/bin/python
 
import sys
import time
import os
 
from PySide import QtGui
from PySide.QtMultimedia import QAudioOutput, QAudioFormat
from PySide.QtCore import QFile, QIODevice, QTimer, QObject, QEvent

from main_ui import Ui_MainWindow

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, frequency, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        wd = os.path.dirname(os.path.abspath(__file__))

        self.tick_pixmaps = {True:  QtGui.QPixmap(os.path.join(wd, 'pics', 'blinkenlicht_on.png')),
                             False: QtGui.QPixmap(os.path.join(wd, 'pics', 'blinkenlicht_off.png'))}
        self.speaker_pixmaps = {True:  QtGui.QIcon(QtGui.QPixmap(os.path.join(wd, 'pics', 'speaker_on.png'))),
                                False: QtGui.QIcon(QtGui.QPixmap(os.path.join(wd, 'pics', 'speaker_off.png')))}
        
        self.tick_soundFile=QFile()
        self.tick_soundFile.setFileName(os.path.join(wd, 'sounds', 'tick.raw'))
        self.tick_soundFile.open(QIODevice.ReadOnly)

        self.play_sound = True

        self.format = QAudioFormat()  
        self.format.setChannels(1)  
        self.format.setFrequency(44050)  
        self.format.setSampleSize(16)  
        self.format.setCodec("audio/pcm")  
        self.format.setByteOrder(QAudioFormat.LittleEndian)  
        self.format.setSampleType(QAudioFormat.SignedInt) 

        self.audio_output = QAudioOutput(self.format)

  

       
        self.ui.ping_icon.setPixmap(self.tick_pixmaps[False])
        self.ui.speaker_button.setIcon(self.speaker_pixmaps[self.play_sound])

        self.blink_timer = QTimer()
        self.blink_timer.setSingleShot(True)
        self.blink_timer.timeout.connect(self.clear_blink)
        
        self.timer   = QTimer()                
        self.frequency = frequency
        self.last_played = 0
        self.count = 0
        
        self.ui.f_spin.setValue(self.frequency)
        self.set_speed()
        self.timer.timeout.connect(self.play_tick)

        self.play_ctrl = {True: 'Stop',
                          False: 'Start'}
        self.ui.play_button.setText(self.play_ctrl[False])
        self.ui.statusBar.showMessage('{count:04d} - Dev.: {delta:.3f} ms'.format(delta=0, count=self.count))

    def set_frequency(self, frequency):
        self.frequency = frequency
        self.set_speed()
        self.last_played = 0
        self.count = 0

    def set_speed(self):
        self.speed = 1000.0 / (self.frequency / 60.0)
        self.timer.setInterval(self.speed)

    def clear_blink(self):
        self.ui.ping_icon.setPixmap(self.tick_pixmaps[False])

    def toggle_play(self):
        if self.timer.isActive():
            self.timer.stop()
            self.last_played = 0
            self.count = 0
            self.ui.statusBar.clearMessage()
        else:
            self.timer.start(self.speed)
            self.play_tick()
        self.ui.play_button.setText(self.play_ctrl[self.timer.isActive()])

    def toggle_play_sound(self):
        if self.play_sound:
            self.play_sound = False
            self.audio_output.stop()
        else:
            self.play_sound = True
        self.ui.speaker_button.setIcon(self.speaker_pixmaps[self.play_sound])

    def play_tick(self):
        if self.last_played:
            delta = ((time.time() - self.last_played) * 1000.0) - self.speed
        else:
            delta = 0
        self.last_played = time.time()

        self.audio_output.stop()
        self.audio_output.reset()
        if self.play_sound:
            self.tick_soundFile.seek(0)
            self.audio_output.start(self.tick_soundFile)

        self.count += 1
        self.ui.statusBar.showMessage('{count:04d} - Dev.: {delta:.3f} ms'.format(delta=delta, count=self.count))

        self.blink_timer.stop()
        self.ui.ping_icon.setPixmap(self.tick_pixmaps[True])
        self.blink_timer.start(100)
                
        self.timer.start(self.speed - max(0, delta))

if __name__ == "__main__":
    if sys.platform == 'win32':
        rc_filename = os.path.join(os.environ['USERPROFILE'], '.metrognome.rc')
    else:
        rc_filename = os.path.join(os.environ['HOME'], '.metrognome.rc')
    try:
        f = int(file(rc_filename).read())
    except:
        f = 60

    app = QtGui.QApplication(sys.argv)
    myapp = MyMainWindow(f)
    myapp.show()
    ec = app.exec_()

    try:
        rc_file = open(rc_filename, 'w')
        rc_file.write(str(myapp.frequency))
    except:
        pass

    sys.exit(ec)
