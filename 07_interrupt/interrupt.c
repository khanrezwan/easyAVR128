/*
 * interrupt.c
 *
 *  Created on: Oct 4, 2015
 *      Author: rezwan
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#include <avr/delay.h>
#define F_CPU 16000000UL

ISR(INT0_vect)
{
PORTC ^=(1<<PC0);/// Toggle interrupt
}

ISR(INT1_vect)
{
PORTC ^=(1<<PC1);/// Toggle interrupt
}

int main()
{
	DDRD &= ~(1<<DDD1)|~(1<<DDD0);/// Set int0 and int1 as input


	DDRC |= (1<<DDC0)|(1<<DDC1);/// set as output for led
	PORTC &= ~(1<<PC0)|~(1<<PC1) ;/// turn off led

	EICRA &= ~(1<<ISC01); /// EICRA – External Interrupt Control Register A ; ISC01, ISC00 = 0,0 a low level triggers interrupt
	EICRA &= ~(1<<ISC00);
	EICRA &= ~(1<<ISC10); /// EICRA – External Interrupt Control Register A ; ISC10, ISC11 = 0,0 a low level triggers interrupt
	EICRA &= ~(1<<ISC11);
	EIMSK|= (1<<INT0);/// Enable INT0
	EIMSK|= (1<<INT1);/// Enable INT1
	sei();/// Enable global interrupt
	while(1)
	{
		//wait for interrupt and do nothing
	}
}
