/*
 * blink.c
 *
 *  Created on: Sep 28, 2015
 *      Author: rezwan
 */


#include <avr/io.h>
#include <util/delay.h>
#define F_CPU 7372800UL
int main(void)
{
	DDRC = 0xFF;

	while(1)
	{
		PORTC|=_BV(PORTC0); //turn off
		_delay_ms(500);
		PORTC&=~_BV(PORTC0);//turn on
		_delay_ms(500);
//		PORTC = 0x00;
//		uint8_t data = 0x01;
//		for (int i=0;i<8;i++)
//		{
//			PORTC = ~(data);
//			data = data<<1; /// 3. Right shift the data by 1 position to get next bit to 0th position
//			_delay_ms(50);
//		}
	}
}
