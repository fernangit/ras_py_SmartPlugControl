# おまじない
import RPi.GPIO as GPIO
import time
import signal
import sys

###smartPlug
import tplink_smartplug_py3 as plug
#####################

# Ctrl+CによってSIGINTシグナルが送信された時のハンドラ。終了前にGPIO.cleanupを呼び出す
def handler(signum, frame):
  print('Signal handler called with signal', signum)
  GPIO.cleanup()
  sys.exit(0)

# ハンドラの登録
signal.signal(signal.SIGINT, handler)

# GPIO9を入力として利用
GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.IN)
before = 0
flag = 0

# 無限ループ
while True:
  # 押された場合には1、押されていない場合0を返す
  now = GPIO.input(9)
  if before == 0 and now == 1:
    print("Push!!!")

###smartPlug
    if(flag == 0):
       plug.control('192.168.0.106', 'on')
       flag = 1
    else:
       plug.control('192.168.0.106', 'off')
       flag = 0
#####################

  time.sleep(0.1)
  before = now