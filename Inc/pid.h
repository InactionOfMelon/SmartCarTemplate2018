#ifndef __PID_H__
#define __PID_H__

#include "stdint.h"
#include "motor.h"

void pid_init(void);

/*********
 * adjust when go straight with pid
 * @param int16_t error (positive for near left side now)
*********/
extern void straight_adjustment(int16_t error);
#endif
