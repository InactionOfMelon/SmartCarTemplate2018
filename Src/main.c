
/**
  ******************************************************************************
  * @file           : main.c
  * @brief          : Main program body
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
#include "main.h"
#include "stm32f1xx_hal.h"
#include "i2c.h"
#include "spi.h"
#include "tim.h"
#include "usart.h"
#include "gpio.h"

/* USER CODE BEGIN Includes */
#include "motor.h"
/* USER CODE END Includes */

/* Private variables ---------------------------------------------------------*/

/* USER CODE BEGIN PV */
/* Private variables ---------------------------------------------------------*/

/* USER CODE END PV */

/* Private function prototypes -----------------------------------------------*/
void SystemClock_Config(void);

/* USER CODE BEGIN PFP */
/* Private function prototypes -----------------------------------------------*/
void user_pwm_setvalue ( uint16_t value );
/* USER CODE END PFP */

/* USER CODE BEGIN 0 */
/* USER CODE END 0 */

/**
  * @brief  The application entry point.
  *
  * @retval None
  */
int main(void)
{
  /* USER CODE BEGIN 1 */

  /* USER CODE END 1 */

  /* MCU Configuration----------------------------------------------------------*/

  /* Reset of all peripherals, Initializes the Flash interface and the Systick. */
  HAL_Init();

  /* USER CODE BEGIN Init */

  /* USER CODE END Init */

  /* Configure the system clock */
  SystemClock_Config();

  /* USER CODE BEGIN SysInit */

  /* USER CODE END SysInit */

  /* Initialize all configured peripherals */
  MX_GPIO_Init();
  MX_I2C1_Init();
  MX_SPI1_Init();
  MX_TIM1_Init();
  MX_TIM2_Init();
  MX_TIM3_Init();
  MX_USART1_UART_Init();
  MX_USART2_UART_Init();
  /* USER CODE BEGIN 2 */
  HAL_TIM_PWM_Start(&htim1 , TIM_CHANNEL_2) ;
  HAL_TIM_PWM_Start(&htim1 , TIM_CHANNEL_3) ;
  HAL_TIM_PWM_Start(&htim3 , TIM_CHANNEL_2) ;
  HAL_TIM_PWM_Start(&htim3 , TIM_CHANNEL_3) ;
  /* USER CODE END 2 */

  /* Infinite loop */
  /* USER CODE BEGIN WHILE */
  /*	int T0 = 500, T1 = 1000, T2 = 50;
  int32_t P0 = 800, P1 = 400, P2 = 2000;
	cpMotor cur = MOTORA_F;
	point_turn(1200,ANTICLOCKWISE);
	HAL_Delay(2000);
	pwm_set_stop();
	
	HAL_Delay(1000);
	
	point_turn(1200,CLOCKWISE);
	HAL_Delay(2000);
	pwm_set_stop();*/
	
	
	
	/*for (int i = 0; i < 4; ++i)

		pwm_set_pulse_F(P0);
		HAL_Delay(1000);
		pwm_set_pulse_F(0);
		HAL_Delay(1000);
		pwm_set_pulse_right_F(2000);
		HAL_Delay(380);
		pwm_set_pulse_F(0);
		HAL_Delay(1000);
	}*/
/*		pwm_set_pulse_F(P0);
		HAL_Delay(T0);
		pwm_set_pulse_left_F(650);
		pwm_set_pulse_right_F(1200);
		HAL_Delay(T2);
		pwm_set_pulse_left_F(500);
		pwm_set_pulse_right_F(1600);
		HAL_Delay(T2);
		pwm_set_pulse_left_F(P1);
		pwm_set_pulse_right_F(P2);
		HAL_Delay(T1);
		pwm_set_pulse_left_F(500);
		pwm_set_pulse_right_F(1600);
		HAL_Delay(T2);
		pwm_set_pulse_left_F(650);
		pwm_set_pulse_right_F(1200);
		HAL_Delay(T2);
		pwm_set_pulse_F(P0);
	}*/
	//pwm_set_pulse_F(0);
	
	
		/*corner_turn(1200,0,LEFT);
    HAL_Delay(3000);
		pwm_set_stop();
    HAL_Delay(1000);
		corner_turn(1200,600,LEFT);
    HAL_Delay(3000);
		pwm_set_stop();
    HAL_Delay(1000);
		corner_turn(1200,1200,LEFT);
    HAL_Delay(3000);
		pwm_set_stop();
		return 0;*/
		
		/*differ_turn(600,1500,RIGHT);
		return 0;*/
		
		//SPI_Receive();
		
	while (1)
  {
  /* USER CODE END WHILE */
		/*uint8_t data[2];
		data[0] = 233; data[1] = 233;
		HAL_SPI_MspInit(&hspi1);
    	while (HAL_SPI_Receive(&hspi1,data,2,100)!=HAL_OK);
		if (data[0] == 1) HAL_GPIO_WritePin(LED_A_GPIO_Port,LED_A_Pin,GPIO_PIN_SET);
		if (data[1] == 1) HAL_GPIO_WritePin(LED_B_GPIO_Port,LED_B_Pin,GPIO_PIN_SET);
		HAL_Delay(10000);
		HAL_GPIO_WritePin(LED_A_GPIO_Port,LED_A_Pin,GPIO_PIN_RESET);
		HAL_GPIO_WritePin(LED_B_GPIO_Port,LED_B_Pin,GPIO_PIN_RESET);
		if (data[0] == 0)
		{
			HAL_GPIO_WritePin(LED_B_GPIO_Port,LED_B_Pin,GPIO_PIN_SET);
			pwm_set_pulse_left_R(800);
		}
		else if (data[0] == 1)
		{
			HAL_GPIO_WritePin(LED_A_GPIO_Port,LED_A_Pin,GPIO_PIN_RESET);
			pwm_set_pulse_right_F(800);
		}
		HAL_SPI_MspDeInit(&hspi1);*/
		
  /* USER CODE BEGIN 3 */
  	SPI_Receive();
		HAL_Delay(3000);
  }
	//while (cur);//
  /* USER CODE END 3 */
}

/**
  * @brief System Clock Configuration
  * @retval None
  */
void SystemClock_Config(void)
{

  RCC_OscInitTypeDef RCC_OscInitStruct;
  RCC_ClkInitTypeDef RCC_ClkInitStruct;

    /**Initializes the CPU, AHB and APB busses clocks 
    */
  RCC_OscInitStruct.OscillatorType = RCC_OSCILLATORTYPE_HSE;
  RCC_OscInitStruct.HSEState = RCC_HSE_ON;
  RCC_OscInitStruct.HSEPredivValue = RCC_HSE_PREDIV_DIV1;
  RCC_OscInitStruct.HSIState = RCC_HSI_ON;
  RCC_OscInitStruct.PLL.PLLState = RCC_PLL_ON;
  RCC_OscInitStruct.PLL.PLLSource = RCC_PLLSOURCE_HSE;
  RCC_OscInitStruct.PLL.PLLMUL = RCC_PLL_MUL9;
  if (HAL_RCC_OscConfig(&RCC_OscInitStruct) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

    /**Initializes the CPU, AHB and APB busses clocks 
    */
  RCC_ClkInitStruct.ClockType = RCC_CLOCKTYPE_HCLK|RCC_CLOCKTYPE_SYSCLK
                              |RCC_CLOCKTYPE_PCLK1|RCC_CLOCKTYPE_PCLK2;
  RCC_ClkInitStruct.SYSCLKSource = RCC_SYSCLKSOURCE_PLLCLK;
  RCC_ClkInitStruct.AHBCLKDivider = RCC_SYSCLK_DIV1;
  RCC_ClkInitStruct.APB1CLKDivider = RCC_HCLK_DIV2;
  RCC_ClkInitStruct.APB2CLKDivider = RCC_HCLK_DIV1;

  if (HAL_RCC_ClockConfig(&RCC_ClkInitStruct, FLASH_LATENCY_2) != HAL_OK)
  {
    _Error_Handler(__FILE__, __LINE__);
  }

    /**Configure the Systick interrupt time 
    */
  HAL_SYSTICK_Config(HAL_RCC_GetHCLKFreq()/1000);

    /**Configure the Systick 
    */
  HAL_SYSTICK_CLKSourceConfig(SYSTICK_CLKSOURCE_HCLK);

  /* SysTick_IRQn interrupt configuration */
  HAL_NVIC_SetPriority(SysTick_IRQn, 0, 0);
}

/* USER CODE BEGIN 4 */


/* USER CODE END 4 */

/**
  * @brief  This function is executed in case of error occurrence.
  * @param  file: The file name as string.
  * @param  line: The line in file as a number.
  * @retval None
  */
void _Error_Handler(char *file, int line)
{
  /* USER CODE BEGIN Error_Handler_Debug */
  /* User can add his own implementation to report the HAL error return state */
  while(1)
  {
  }
  /* USER CODE END Error_Handler_Debug */
}

#ifdef  USE_FULL_ASSERT
/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t* file, uint32_t line)
{ 
  /* USER CODE BEGIN 6 */
  /* User can add his own implementation to report the file name and line number,
     tex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */
  /* USER CODE END 6 */
}
#endif /* USE_FULL_ASSERT */

/**
  * @}
  */

/**
  * @}
  */

/************************ (C) COPYRIGHT STMicroelectronics *****END OF FILE****/
