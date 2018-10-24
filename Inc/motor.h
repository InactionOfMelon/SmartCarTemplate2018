#ifndef __MOTOR_H__
#define __MOTOR_H__

#include "main.h"
#include "stm32f1xx_hal.h"
#include "i2c.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

#ifdef __cplusplus
extern "C" {
#endif

/* TIM Begin */

typedef struct { TIM_HandleTypeDef * phtim; uint32_t channel; } Motor;
typedef const Motor * cpMotor;

extern const cpMotor
	MOTORA_F, MOTORA_R,
	MOTORB_F, MOTORB_R,
	MOTORC_F, MOTORC_R,
	MOTORD_F, MOTORD_R;

/**
 * sets pulse for a single motor
 * @param cpMotor motor
 * @param uint16_t pulse
 */
void pwm_set_pulse_single(const cpMotor motor, uint16_t pulse);

/**
 * sets pulse for MOTORC_F, MOTORD_F (left)
 * @param uint16_t pulse
 */
void pwm_set_pulse_left_F(uint16_t pulse);

/**
 * sets pulse for MOTORB_F, MOTORA_F (right)
 * @param uint16_t pulse
 */
void pwm_set_pulse_right_F(uint16_t pulse);

/**
 * sets pulse for MOTORC_R, MOTORD_R (left)
 * @param uint16_t pulse
 */
void pwm_set_pulse_left_R(uint16_t pulse);

/**
 * sets pulse for MOTORB_R, MOTORA_R (right)
 * @param uint16_t pulse
 */
void pwm_set_pulse_right_R(uint16_t pulse);

/**
 * sets pulse for MOTOR*_F
 * @param uint16_t pulse
 */
void pwm_set_pulse_F(uint16_t pulse);

/**
 * sets pulse for MOTOR*_R
 * @param uint16_t pulse
 */
void pwm_set_pulse_R(uint16_t pulse);

/* TIM End */

#ifdef __cplusplus
}
#endif

#endif