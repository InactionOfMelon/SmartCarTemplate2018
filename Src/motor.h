#ifndef __MOTOR_H__
#define __MOTOR_H__

#include "main.h"
#include "stm32f1xx_hal.h"
#include "i2c.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

typedef struct { TIM_HandleTypeDef * phtim; uint32_t channel; } Motor;
const Motor
	__MOTORA_F = {&htim1, TIM_CHANNEL_3}, __MOTORA_R = {&htim1, TIM_CHANNEL_4}, // swapped
	__MOTORB_F = {&htim1, TIM_CHANNEL_2}, __MOTORB_R = {&htim1, TIM_CHANNEL_1},
	__MOTORC_F = {&htim3, TIM_CHANNEL_3}, __MOTORC_R = {&htim3, TIM_CHANNEL_4},
	__MOTORD_F = {&htim3, TIM_CHANNEL_2}, __MOTORD_R = {&htim3, TIM_CHANNEL_1}; // swapped

typedef const Motor * cpMotor;
const cpMotor
	MOTORA_F = &__MOTORA_F, MOTORA_R = &__MOTORA_R,
	MOTORB_F = &__MOTORB_F, MOTORB_R = &__MOTORB_R,
	MOTORC_F = &__MOTORC_F, MOTORC_R = &__MOTORC_R,
	MOTORD_F = &__MOTORD_F, MOTORD_R = &__MOTORD_R;

void __pwm_set(const cpMotor motor, TIM_OC_InitTypeDef * psConfigOC)
{
	HAL_TIM_PWM_ConfigChannel(motor->phtim , psConfigOC, motor->channel);
	HAL_TIM_PWM_Start(motor->phtim, motor->channel);
}

void pwm_set_pulse_single(const cpMotor motor, uint16_t pulse)
{
	TIM_OC_InitTypeDef sConfigOC;
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = pulse;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
	__pwm_set(motor, &sConfigOC);
}

void pwm_set_pulse_F(uint16_t pulse)
{
  TIM_OC_InitTypeDef sConfigOC;
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = pulse;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
	__pwm_set(MOTORA_F, &sConfigOC);
	__pwm_set(MOTORB_F, &sConfigOC);
	__pwm_set(MOTORC_F, &sConfigOC);
	__pwm_set(MOTORD_F, &sConfigOC);
}

void pwm_set_pulse_R(uint16_t pulse)
{
  TIM_OC_InitTypeDef sConfigOC;
  sConfigOC.OCMode = TIM_OCMODE_PWM1;
  sConfigOC.Pulse = pulse;
  sConfigOC.OCPolarity = TIM_OCPOLARITY_HIGH;
  sConfigOC.OCFastMode = TIM_OCFAST_DISABLE;
	__pwm_set(MOTORA_R, &sConfigOC);
	__pwm_set(MOTORB_R, &sConfigOC);
	__pwm_set(MOTORC_R, &sConfigOC);
	__pwm_set(MOTORD_R, &sConfigOC);
}

#endif
