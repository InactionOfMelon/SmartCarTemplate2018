# Week6 5-4 Manchery

汇报：

## 定点旋转

 - 任务：定点旋转逆时针、顺时针
 - 具体方法：两轮同速不同向转动
 - 特点：滑动在所难免，需要较大功率客服阻力，个人认为暂时不用考虑磨损
 - 代码实现：补充在 `motor.c & motor.h`，参见具体代码，注意使用了枚举类型 `PointTurnDirDef` 来表示旋转方向。
 - p.s. **划重点** 根据参赛手册的意思，在start_pwm前一定要stop，所以添加一函数 `pwm_set_stop`，给八个定时器的channel全部stop（有点暴力）

## 分工

 - 初赛任务：上位机与树莓派MQTT协议通讯（1）、树莓派与单片机SPI协议通讯（2）、电机完成相应动作
 - 分工
 	- （1）维钧、睿中
 	- （2）吴佳龙
 	- （3）晓腾
 
 