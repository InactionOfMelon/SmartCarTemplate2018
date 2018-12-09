#ifndef __PID_C__
#define __PID_C__
#include "pid.h"

struct Pid{
	int16_t error_last;
	int16_t integral;
	int16_t differ;
	float Kp;
	float Ki;
	float Kd;
}straight;

void pid_init(){
	straight.error_last = 0;
	straight.integral = 0;
	straight.differ = 0;
	straight.Kp = 5;
	straight.Ki = 2;
	straight.Kd = 1;
}

/*********
 * adjust when go straight with pid
 * @param int16_t error (positive for near left side now)
*********/
void straight_adjustment(int16_t error){
	straight.differ = error * straight.Kp + straight.integral * straight.Ki - straight.error_last * straight.Kd;
	
	pwm_set_stop();
	if (straight.differ > 0){
		if (straight.differ > 10000) straight.differ = 10000;
		differ_turn(Speed_Now, straight.differ, RIGHT);
	}else{
		straight.differ *=-1;
		if (straight.differ > 10000) straight.differ = 10000;
		differ_turn(Speed_Now, straight.differ, LEFT);
	}
	
	straight.error_last=error;
	straight.integral += error;
}
#endif
