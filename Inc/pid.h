#ifndef __PID_H__
#define __PID_H__

#include "stdint.h"
#include "motor.h"

extern void pid_init(void);

/*********
 * adjust when go straight with pid
 * @param int16_t error (positive for near left side now)
*********/
extern void straight_adjustment(int16_t error);


extern void straight_param_change(int16_t Kp, int16_t Ki, int16_t Kd);

#endif
