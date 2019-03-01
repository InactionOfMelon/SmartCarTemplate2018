/**
  ******************************************************************************
  * File Name          : SPI.c
  * Description        : This file provides code for the configuration
  *                      of the SPI instances.
  ******************************************************************************
  ** This notice applies to any and all portions of this file
  * that are not between comment pairs USER CODE BEGIN and
  * USER CODE END. Other portions of this file, whether 
  * inserted by the user or by software development tools
  * are owned by their respective copyright owners.
  *
  * COPYRIGHT(c) 2018 STMicroelectronics
  *
  * Redistribution and use in source and binary forms, with or without modification,
  * are permitted provided that the following conditions are met:
  *   1. Redistributions of source code must retain the above copyright notice,
  *      this list of conditions and the following disclaimer.
  *   2. Redistributions in binary form must reproduce the above copyright notice,
  *      this list of conditions and the following disclaimer in the documentation
  *      and/or other materials provided with the distribution.
  *   3. Neither the name of STMicroelectronics nor the names of its contributors
  *      may be used to endorse or promote products derived from this software
  *      without specific prior written permission.
  *
  * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
  * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
  * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
  * DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
  * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
  * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
  * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
  * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
  * OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
  * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
  *
  ******************************************************************************
  */

/* Includes ------------------------------------------------------------------*/
#include "spi.h"
#include "pid.h"
#include "gpio.h"

/* USER CODE BEGIN 0 */
#include "motor.h"
#include <string.h>
/* USER CODE END 0 */

SPI_HandleTypeDef hspi1;

/* SPI1 init function */
void MX_SPI1_Init(void)
{

  hspi1.Instance = SPI1;
  hspi1.Init.Mode = SPI_MODE_SLAVE;
  hspi1.Init.Direction = SPI_DIRECTION_2LINES;
  hspi1.Init.DataSize = SPI_DATASIZE_8BIT;
  hspi1.Init.CLKPolarity = SPI_POLARITY_LOW;
  hspi1.Init.CLKPhase = SPI_PHASE_1EDGE;
  hspi1.Init.NSS = SPI_NSS_HARD_INPUT;
  hspi1.Init.BaudRatePrescaler = SPI_BAUDRATEPRESCALER_32;
  hspi1.Init.FirstBit = SPI_FIRSTBIT_MSB;
  hspi1.Init.TIMode = SPI_TIMODE_DISABLE;
  hspi1.Init.CRCCalculation = SPI_CRCCALCULATION_DISABLE;
  hspi1.Init.CRCPolynomial = 10;
  if (HAL_SPI_Init(&hspi1) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

}

void HAL_SPI_MspInit(SPI_HandleTypeDef* spiHandle)
{

  GPIO_InitTypeDef GPIO_InitStruct;
  if(spiHandle->Instance==SPI1)
  {
  /* USER CODE BEGIN SPI1_MspInit 0 */

  /* USER CODE END SPI1_MspInit 0 */
    /* SPI1 clock enable */
    __HAL_RCC_SPI1_CLK_ENABLE();
  
    /**SPI1 GPIO Configuration    
    PA15     ------> SPI1_NSS
    PB3     ------> SPI1_SCK
    PB4     ------> SPI1_MISO
    PB5     ------> SPI1_MOSI 
    */
    GPIO_InitStruct.Pin = GPIO_PIN_15;
    GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOA, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_3|GPIO_PIN_5;
    GPIO_InitStruct.Mode = GPIO_MODE_INPUT;
    GPIO_InitStruct.Pull = GPIO_NOPULL;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

    GPIO_InitStruct.Pin = GPIO_PIN_4;
    GPIO_InitStruct.Mode = GPIO_MODE_AF_PP;
    GPIO_InitStruct.Speed = GPIO_SPEED_FREQ_HIGH;
    HAL_GPIO_Init(GPIOB, &GPIO_InitStruct);

    __HAL_AFIO_REMAP_SPI1_ENABLE();

  /* USER CODE BEGIN SPI1_MspInit 1 */

  /* USER CODE END SPI1_MspInit 1 */
  }
}

void HAL_SPI_MspDeInit(SPI_HandleTypeDef* spiHandle)
{

  if(spiHandle->Instance==SPI1)
  {
  /* USER CODE BEGIN SPI1_MspDeInit 0 */

  /* USER CODE END SPI1_MspDeInit 0 */
    /* Peripheral clock disable */
    __HAL_RCC_SPI1_CLK_DISABLE();
  
    /**SPI1 GPIO Configuration    
    PA15     ------> SPI1_NSS
    PB3     ------> SPI1_SCK
    PB4     ------> SPI1_MISO
    PB5     ------> SPI1_MOSI 
    */
    HAL_GPIO_DeInit(GPIOA, GPIO_PIN_15);

    HAL_GPIO_DeInit(GPIOB, GPIO_PIN_3|GPIO_PIN_4|GPIO_PIN_5);

  /* USER CODE BEGIN SPI1_MspDeInit 1 */

  /* USER CODE END SPI1_MspDeInit 1 */
  }
} 

/* USER CODE BEGIN 1 */

/**
 * Receive information from berry
 */


void SPI_Receive(uint8_t *data, uint8_t SPI_SIZE)
{
  //HAL_SPI_MspInit(&hspi1);
	
	while (!data[4])
	HAL_SPI_IRQHandler(&hspi1);
	
	/*if (data[0] <= 100) 
	{
		HAL_GPIO_WritePin(LED_A_GPIO_Port,LED_A_Pin,GPIO_PIN_SET);
		HAL_Delay(500);
		HAL_GPIO_WritePin(LED_A_GPIO_Port,LED_A_Pin,GPIO_PIN_RESET);
	}
	if (data[0] >= 112)
	{
		HAL_GPIO_WritePin(LED_B_GPIO_Port,LED_B_Pin,GPIO_PIN_SET);
		HAL_Delay(500);
		HAL_GPIO_WritePin(LED_B_GPIO_Port,LED_B_Pin,GPIO_PIN_RESET);
	}*/
	
	
	//if (data[0] == 101) pwm_set_pulse_F(600);
	//if (data[0] == 102) pwm_set_stop();
	
	
	
  uint16_t g = (data[2] << 8) | data[1];
	
	switch (data[0])
	{
		case 1: Speed_Now = g; break;//set new speed
		case 2: straight_adjustment(g); break;//need turn right
		case 3: straight_adjustment(-g); break;//need turn left
		case 101: pwm_set_stop(); pwm_set_pulse_F(Speed_Now); break;
		case 102: pwm_set_stop(); break;
		case 103: pwm_set_stop(); pwm_set_pulse_R(Speed_Now); break;
		case 104: pwm_set_stop(); corner_turn(Speed_Now, 0, LEFT); break;
		case 105: pwm_set_stop(); corner_turn(Speed_Now, 0, RIGHT); break;
		case 106: pwm_set_stop(); point_turn(Speed_Now, ANTICLOCKWISE); break;
		case 107: pwm_set_stop(); point_turn(Speed_Now, CLOCKWISE); break;
		case 108: pwm_set_stop(); pwm_set_pulse_F(g / 5); break;
		case 109: pwm_set_stop(); pwm_set_pulse_R(g / 5); break;
		case 110: pwm_set_stop(); differ_turn(Speed_Now, g, LEFT); break;
		case 111: pwm_set_stop(); differ_turn(Speed_Now, g, RIGHT); break;
		case 112: straight_param_change(((float)g)/256, -1, -1); break;
		case 113: straight_param_change(-1, ((float)g)/256, -1); break;
		case 114: straight_param_change(-1, -1, ((float)g)/256); break;
		case 115: pid_init(); break;
		
		case 200: pwm_set_pulse_single(MOTORA_F, g); break;
		case 201: pwm_set_pulse_single(MOTORB_F, g); break;
		case 202: pwm_set_pulse_single(MOTORC_F, g); break;
		case 203: pwm_set_pulse_single(MOTORD_F, g); break;
		
		case 210: pwm_set_pulse_single(MOTORA_R, g); break;
		case 211: pwm_set_pulse_single(MOTORB_R, g); break;
		case 212: pwm_set_pulse_single(MOTORC_R, g); break;
		case 213: pwm_set_pulse_single(MOTORD_R, g); break;
		
		case 220: MIN_Speed = g; break;
		case 221: Speed_Up = g; break;
		case 222: GoBack = g; break;
		case 223:	pwm_set_stop();
							pwm_set_pulse_F(500);
							HAL_Delay(1500);
							pwm_set_stop();
							pwm_set_pulse_R(500);
							HAL_Delay(1500);
							pwm_set_stop();
							break;
	}
	
	for (int i = 0; i < SPI_SIZE; i++) data[i] = 0;
	
	//HAL_SPI_MspDeInit(&hspi1);
	/*}
	else
	{
			HAL_GPIO_WritePin(LED_A_GPIO_Port,LED_A_Pin,GPIO_PIN_SET);
			HAL_GPIO_WritePin(LED_B_GPIO_Port,LED_B_Pin,GPIO_PIN_SET);
	}*/
}


/* USER CODE END 1 */

/**
  * @}
  */

/**
  * @}
  */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
