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
	HAL_TIM_PWM_Stop(motor->phtim, motor->channel);
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
	
	/*static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(motor, &sConfigOC);*/ 
	
	
	HAL_TIM_PWM_Stop(motor->phtim, motor->channel);
	__HAL_TIM_SET_COMPARE(motor->phtim, motor->channel, pulse);
	HAL_TIM_PWM_Start(motor->phtim, motor->channel);
}

/**
 * sets pulse for MOTORC_F, MOTORD_F (left)
 * @param uint16_t pulse
 */
void pwm_set_pulse_left_F(uint16_t pulse)
{
	/*static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORC_F, &sConfigOC);
	__pwm_set(MOTORD_F, &sConfigOC);*/
	
	pwm_set_pulse_single(MOTORC_F, pulse);
	pwm_set_pulse_single(MOTORD_F, pulse);
}

/**
 * sets pulse for MOTORB_F, MOTORA_F (right)
 * @param uint16_t pulse
 */
void pwm_set_pulse_right_F(uint16_t pulse)
{
	/*static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORB_F, &sConfigOC);
	__pwm_set(MOTORA_F, &sConfigOC);
	*/
	
	pwm_set_pulse_single(MOTORB_F, pulse);
	pwm_set_pulse_single(MOTORA_F, pulse);
}

/**
 * sets pulse for MOTORC_R, MOTORD_R (left)
 * @param uint16_t pulse
 */
void pwm_set_pulse_left_R(uint16_t pulse)
{
	/*static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORC_R, &sConfigOC);
	__pwm_set(MOTORD_R, &sConfigOC);
	*/
	
	pwm_set_pulse_single(MOTORC_R, pulse);
	pwm_set_pulse_single(MOTORD_R, pulse);
}

/**
 * sets pulse for MOTORB_R, MOTORA_R (right)
 * @param uint16_t pulse
 */
void pwm_set_pulse_right_R(uint16_t pulse)
{
	/*static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORB_R, &sConfigOC);
	__pwm_set(MOTORA_R, &sConfigOC);
	*/
	
	pwm_set_pulse_single(MOTORB_R, pulse);
	pwm_set_pulse_single(MOTORA_R, pulse);
}

/**
 * sets pulse for MOTOR*_F
 * @param uint16_t pulse
 */
void pwm_set_pulse_F(uint16_t pulse)
{
	/*static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORB_F, &sConfigOC);
	__pwm_set(MOTORC_F, &sConfigOC);
	__pwm_set(MOTORA_F, &sConfigOC);
	__pwm_set(MOTORD_F, &sConfigOC);
	*/
	
	pwm_set_pulse_single(MOTORB_F, pulse);
	pwm_set_pulse_single(MOTORC_F, pulse);
	pwm_set_pulse_single(MOTORA_F, pulse);
	pwm_set_pulse_single(MOTORD_F, pulse);
}

/**
 * sets pulse for MOTOR*_R
 * @param uint16_t pulse
 */
void pwm_set_pulse_R(uint16_t pulse)
{
	/*static TIM_OC_InitTypeDef sConfigOC;
	__oc_init_pulse(&sConfigOC, pulse);
	__pwm_set(MOTORB_R, &sConfigOC);
	__pwm_set(MOTORC_R, &sConfigOC);
	__pwm_set(MOTORA_R, &sConfigOC);
	__pwm_set(MOTORD_R, &sConfigOC);
	*/
	
	pwm_set_pulse_single(MOTORB_R, pulse);
	pwm_set_pulse_single(MOTORC_R, pulse);
	pwm_set_pulse_single(MOTORA_R, pulse);
	pwm_set_pulse_single(MOTORD_R, pulse);
}

/**
 * point turn clockwise or anticlockwise
 * @param uint16_t pulse PointTurnDirDef dir
 */
void point_turn(uint16_t pulse,PointTurnDirDef dir)
{
	if (dir==ANTICLOCKWISE){
		pwm_set_pulse_right_F(pulse);
		pwm_set_pulse_left_R(pulse);
	}else if (dir==CLOCKWISE){
		pwm_set_pulse_right_R(pulse);
		pwm_set_pulse_left_F(pulse);
	}
}


/**
 * corner turn left or right
 * Usually InsidePulse should be 0.Or be positive for smaller radii.
 * @param uint16_t OutsidePulse uint16_t InsidePulse TurnDir dir
 */
void corner_turn(uint16_t OutsidePulse,uint16_t InsidePulse,TurnDirDef dir)
{
	if (dir==LEFT){
		pwm_set_pulse_right_F(OutsidePulse);
		pwm_set_pulse_left_R(InsidePulse);
	}else if (dir==RIGHT){
		pwm_set_pulse_left_F(OutsidePulse);
		pwm_set_pulse_right_R(InsidePulse);
	}
}


/**
 * turn left or right with differential speed
 * @param uint16_t Pulse,uint16_t differ,TurnDirDef dir
 */
void differ_turn(uint16_t Pulse,uint16_t differ,TurnDirDef dir)
{
	int16_t OutsidePulse=Pulse,InsidePulse=Pulse-differ;
	if (InsidePulse<-Speed_Now) InsidePulse=-Speed_Now;
	if (dir==LEFT){
		pwm_set_pulse_right_F((uint16_t) OutsidePulse);
		if (InsidePulse>0){
			pwm_set_pulse_left_F((uint16_t) InsidePulse);
		}else{
			pwm_set_pulse_left_R((uint16_t) -InsidePulse);
		}
	}else if (dir==RIGHT){
		pwm_set_pulse_left_F((uint16_t) OutsidePulse);
		if (InsidePulse>0){
			pwm_set_pulse_right_F((uint16_t) InsidePulse);
		}else{
			pwm_set_pulse_right_R((uint16_t) -InsidePulse);
		}
	}
}


/**
 * set to stop all pwm 
 */
void pwm_set_stop(void)
{
	HAL_TIM_PWM_Stop(MOTORA_F->phtim, MOTORA_F->channel);
	HAL_TIM_PWM_Stop(MOTORB_F->phtim, MOTORB_F->channel);
	HAL_TIM_PWM_Stop(MOTORC_F->phtim, MOTORC_F->channel);
	HAL_TIM_PWM_Stop(MOTORD_F->phtim, MOTORD_F->channel);
	HAL_TIM_PWM_Stop(MOTORA_R->phtim, MOTORA_R->channel);
	HAL_TIM_PWM_Stop(MOTORB_R->phtim, MOTORB_R->channel);
	HAL_TIM_PWM_Stop(MOTORC_R->phtim, MOTORC_R->channel);
	HAL_TIM_PWM_Stop(MOTORD_R->phtim, MOTORD_R->channel);
}
/* TIM End */

#endif
