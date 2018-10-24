#ifndef __MOTOR_C__
#define __MOTOR_C__

#include "main.h"
#include "stm32f1xx_hal.h"
#include "i2c.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

#include "motor.h"

/* TIM Begin */

// D A
// C B

const Motor
	__MOTORA_F = {&htim1, TIM_CHANNEL_3}, __MOTORA_R = {&htim1, TIM_CHANNEL_4}, // swapped
	__MOTORB_F = {&htim1, TIM_CHANNEL_2}, __MOTORB_R = {&htim1, TIM_CHANNEL_1},
	__MOTORC_F = {&htim3, TIM_CHANNEL_3}, __MOTORC_R = {&htim3, TIM_CHANNEL_4},
	__MOTORD_F = {&htim3, TIM_CHANNEL_2}, __MOTORD_R = {&htim3, TIM_CHANNEL_1}; // swapped

const cpMotor
	MOTORA_F = &__MOTORA_F, MOTORA_R = &__MOTORA_R,
	MOTORB_F = &__MOTORB_F, MOTORB_R = &__MOTORB_R,
	MOTORC_F = &__MOTORC_F, MOTORC_R = &__MOTORC_R,
	MOTORD_F = &__MOTORD_F, MOTORD_R = &__MOTORD_R;

/**
 * initializes output compare config by pulse
 * @access private
 * @param TIM_OC_InitTypeDef * psConfigOC
 * @param uint16_t pulse
 */
void __oc_init_pulse(TIM_OC_InitTypeDef * psConfigOC, uint16_t pulse)
{
	psConfigOC->OCMode = TIM_OCMODE_PWM1;
	psConfigOC->Pulse = pulse;
	psConfigOC->OCPolarity = TIM_OCPOLARITY_HIGH;
	psConfigOC->OCFastMode = TIM_OCFAST_DISABLE;
}

/**
 * sets config for a single motor
 * @access private
 * @param const cpMotor motor
 * @param TIM_OC_InitTypeDef * psConfigOC
 */
void __pwm_set(const cpMotor motor, TIM_OC_InitTypeDef * psConfigOC)
{
	HAL_TIM_PWM_ConfigChannel(motor->phtim , psConfigOC, motor->channel);
	HAL_TIM_PWM_Start(motor->phtim, motor->channel);
}

/**
 * sets pulse for a single motor
 * @param cpMotor motor
 * @param uint16_t pulse
 */
void pwm_set_pulse_single(const cpMotor motor, uint16_t pulse)
{
	static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(motor, &sConfigOC);
}

/**
 * sets pulse for MOTORC_F, MOTORD_F (left)
 * @param uint16_t pulse
 */
void pwm_set_pulse_left_F(uint16_t pulse)
{
	static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORC_F, &sConfigOC);
	__pwm_set(MOTORD_F, &sConfigOC);
}

/**
 * sets pulse for MOTORB_F, MOTORA_F (right)
 * @param uint16_t pulse
 */
void pwm_set_pulse_right_F(uint16_t pulse)
{
	static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORB_F, &sConfigOC);
	__pwm_set(MOTORA_F, &sConfigOC);
}

/**
 * sets pulse for MOTORC_R, MOTORD_R (left)
 * @param uint16_t pulse
 */
void pwm_set_pulse_left_R(uint16_t pulse)
{
	static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORC_R, &sConfigOC);
	__pwm_set(MOTORD_R, &sConfigOC);
}

/**
 * sets pulse for MOTORB_R, MOTORA_R (right)
 * @param uint16_t pulse
 */
void pwm_set_pulse_right_R(uint16_t pulse)
{
	static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORB_R, &sConfigOC);
	__pwm_set(MOTORA_R, &sConfigOC);
}

/**
 * sets pulse for MOTOR*_F
 * @param uint16_t pulse
 */
void pwm_set_pulse_F(uint16_t pulse)
{
	static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORB_F, &sConfigOC);
	__pwm_set(MOTORC_F, &sConfigOC);
	__pwm_set(MOTORA_F, &sConfigOC);
	__pwm_set(MOTORD_F, &sConfigOC);
}

/**
 * sets pulse for MOTOR*_R
 * @param uint16_t pulse
 */
void pwm_set_pulse_R(uint16_t pulse)
{
	static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORB_R, &sConfigOC);
	__pwm_set(MOTORC_R, &sConfigOC);
	__pwm_set(MOTORA_R, &sConfigOC);
	__pwm_set(MOTORD_R, &sConfigOC);
}

/* TIM End */

#endif
