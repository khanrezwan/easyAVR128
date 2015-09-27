/*
 * button.c
 *
 *  Created on: Sep 28, 2015
 *      Author: rezwan
 */
#include <avr/io.h>
#include <util/delay.h>
#define F_CPU 7372800UL

void scan_buttons(void)
	{
		 if ((PINB & (1 << PB0)) == 0)
		 {
//			PORTC &= ~(1 << PC0);
			PORTC = ~(1 << PC0);
//			 PORTC ^=(1<<PC0);
		 }

		 if ((PINB & (1 << PB1)) == 0)
		 {
//			PORTC &= ~(1 << PC1);
			PORTC = ~(1 << PC1);
//			PORTC ^=(1<<PC1);
		 }

		 if ((PINB & (1 << PB2)) == 0)
		 {
//			PORTC &= ~(1 << PC2);
			 PORTC = ~(1 << PC2);
//			 PORTC ^=(1<<PC2);
		 }
		 if ((PINB & (1 << PB3)) == 0)
		 {
//			PORTC &= ~(1 << PC3);
			 PORTC = ~(1 << PC3);
//			 PORTC ^=(1<<PC3);
		 }

		  if ((PINB & (1 << PB4)) == 0)
		 {
//			PORTC &= ~(1 << PC4);
			  PORTC = ~(1 << PC4);
//			  PORTC ^=(1<<PC4);
		 }

		  if ((PINB & (1 << PB5)) == 0)
		 {
//			PORTC &= ~(1 << PC5);
			  PORTC = ~(1 << PC5);
//			  PORTC ^=(1<<PC5);
		 }

		  if ((PINB & (1 << PB6)) == 0)
		 {
//			PORTC &= ~(1 << PC6);
			  PORTC = ~(1 << PC6);
//			  PORTC ^=(1<<PC6);
		 }

		 if ((PINB & (1 << PB7)) == 0)
		 {
//			PORTC &= ~(1 << PC7);
			 PORTC = ~(1 << PC7);
//			 PORTC ^=(1<<PC7);
		 }
	}

int main(void)
{
	DDRC = 0xFF; // output for LEDs
	PORTC = 0xFF; //Turn off all LEDs
	DDRB = 0x00; // input for buttons
//	PORTB=0xFF; // pull up


	while(1)
	{
		scan_buttons();

	}
}

