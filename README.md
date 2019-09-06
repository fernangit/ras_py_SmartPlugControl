# ras_py_SmartPlugControl
SmartPlug Control by python on the raspberry pie  
---
TP-LINK社製スマートプラグ HS105(https://www.tp-link.com/jp/home-networking/smart-plug/hs105/) をコントロールするための Python スクリプト。  
「TP-Link スマートコンセント HS105を試してみた(https://lmjs7.net/blog/tag/hs105/) 」を参考にカスタマイズ

## HOW TO USE
### アカウントの作成  
アカウントを作成してスマホアプリから端末をコントロールできるようにする。  
「TP-Link社製品のKasa初期設定手順まとめ 接続から設定までこれで解決！(https://www.braveryk7.com/start-kasa/) 」を参照。  
  
Step.1 専用アプリのインストール  
Step.2 アカウント作成・ログイン  
Step.3 端末を追加  
Step.4 Wi-Fi接続  
Step.5 端末に名前をつける  

### 端末のIP確認  
APIから端末を制御するには登録した端末のIPが必要。

#### LAN内で使われているIPアドレスを調べる方法  
1.スマホアプリで調べる(ios, android)  
* Fingを使う

2.ping + arpで調べる(Linux)  
```
for a in `seq 1 254`; do ping -c 1 -w 0.5 対象セグメント(第３オクテットまで).$a > /dev/null && arp -a 対象セグメント(第３オクテットまで).$a | grep ether; done
```
* 対象セグメント(第３オクテットまで)→「192.168.0」など  

3.ping + arpで調べる(Windows)  
```
for /l %i in (0,1,255) do ping -w 1 -n 1 対象セグメント(第３オクテットまで).%i && arp -a 192.168.0.%i
```

### API  

#### PythonベースのAPIを取得  
「Reverse Engineering the TP-Link HS110(https://www.softscheck.com/en/reverse-engineering-tp-link-hs110/) 」を参照。  
https://github.com/softScheck/tplink-smartplug からスクリプトを取得。  
* tplink_smartplug.py(python2用)  

#### スクリプト実行 
以下のコマンドで電源ON  
```
python tplink_smartplug.py -t 192.168.0.2 -c on
```
以下のコマンドで電源OFF  
```
python tplink_smartplug.py -t 192.168.0.2 -c off
```
* IPには端末のIPを指定する。  

#### Python3用に書き換え  
* 「TP-Link スマートコンセントHS-105をAPIから操作（３）」を参照

#### モジュールからの呼び出し
```
import tplink_smartplug_py3 as plug
plug.control('192.168.0.2', 'on')
```

## 参考情報
* TP-Link スマートコンセント HS105を試してみた
  * https://lmjs7.net/blog/tag/hs105/
* Reverse Engineering the TP-Link HS110
  * https://www.softscheck.com/en/reverse-engineering-tp-link-hs110/
* TP-Link社製品のKasa初期設定手順まとめ 接続から設定までこれで解決！
  * https://www.braveryk7.com/start-kasa/
* Fing：自宅のWi-Fiルーターの不正利用を簡単に調べられるアプリ【Android/iOS/基本無料】
  * https://nansikanews.com/2018/04/05/life-app-fing/
* LAN内で使われているIPアドレスを調べる6つの方法(Linux/Windows)
  * https://orebibou.com/2015/05/lan内で使われているipアドレスを調べる6つの方法linuxwindows/

## License
Apache License 2.0. See [LICENSE](/LICENSE).
