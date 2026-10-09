# Arduino Template Generator
`arduino-cli`用にテンプレートを用意するCLIツールです．
新たなプログラムファイルを作る度，ディレクトリ構造を一々手動で用意するのが面倒だったので作りました．

## 機能
以下のようなディレクトリ構造を用意します．
```
project
 ├─ src           # directory
 └─ project.ino   # file
```
また，`project.ino`へ，基礎プログラム文が書き込まれます．
```cpp
#include <Arduino.h>

void setup(){

}

void loop(){

}
```

## How to use
```
python atg.py <project_name> [-s|--serial baudrate]
# project_name: 作成するプロジェクト名
```
オプションとして，`-s(--serial)`でシリアル通信のボードレート指定できます．
```
python atg.py new_project -s 115200
```
引数の値は**整数値**で指定する必要があります．
このオプションを指定すると，作成される`ino`ファイルの`setup()`関数にシリアル通信の初期化構文が追加されます．
```cpp
void setup(){
  Serial.begin(115200);
  while(!Serial);
}
```

## Example
以下を実行すると，
```
python atg.py new_robot -s 9600
```
以下のようなディレクトリ構造が出来上がり，
```
new_robot
 ├─ src             # directory
 └─ new_robot.ino   # file
```
`new_robot.ino`へ以下が書き込まれます．
```cpp
#include <Arduino.h>

void setup(){
  Serial.begin(9600);
  while(!Serial);

}

void loop(){

}
```

## 免責  
- Arduino  
[Arduino.cc](https://www.arduino.cc/)  
*本プロジェクトはArduino環境を利用していますが，Arduino公式プロジェクトとは無関係です．*  
*「Arduino(R)」は，Arduino Srlの商標または登録商標です．*