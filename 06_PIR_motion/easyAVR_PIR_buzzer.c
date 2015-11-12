/*
 * easyAVR_PIR_buzzer.c
 *
 *  Created on: Nov 1, 2015
 *      Author: rezwan
 */

#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>
#define F_CPU 8000000UL

#define PIR_DDR DDRC
#define PIR_PIN_Reg PINC
#define PIR_IN PORTC0
uint8_t pirState = 0;

#define Buzzer_DDR DDRG
#define Buzzer_PORT PORTG
#define Buzzer_OUT PORTG3


#define FOSC 8000000 /**< Clock speed for UBRR calculation. refer page 179 of 328p datasheet. */
#define BAUD 9600 /**< Baud Rate in bps. refer page 179 of 328p datasheet. */
#define MYUBRR FOSC/16/BAUD-1 /**< UBRR = (F_CPU/(16*Baud))-1 for asynch USART page 179 328p datasheet. Baud rate 9600bps, assuming	16MHz clock UBRR0 becomes 0x0067*/

/**
 * @brief Initialize USART for 8 bit data transmit no parity and 1 stop bit.
 *
 *@details This is a code snippet from datasheet page 182
 *
 * @param ubrr The UBRR value calculated in macro MYUBRR
 * @see MYUBRR
 */
void USART_init(unsigned int ubrr)
{

	UCSR0C = (0<<USBS0)|(3<<UCSZ00); /// Step 1. Set UCSR0C in Asynchronous mode, no parity, 1 stop bit, 8 data bits
	UCSR0A = 0b00000000;/// Step 2. Set UCSR0A in Normal speed, disable multi-proc

	UBRR0H = (unsigned char)(ubrr>>8);/// Step 3. Load ubrr into UBRR0H and UBRR0L
	UBRR0L = (unsigned char)ubrr;


	UCSR0B = 0b00011000;/// Step 4. Enable Tx Rx and disable interrupt in UCSR0B
}

/**
 * @brief Send 8bit data.
 *
 *@details This is a code snippet from datasheet page 184
 *
 * @param data The 8 bit data to be sent
 */

int USART_send(char c, FILE *stream)
{

	while ( !( UCSR0A & (1<<UDRE0)) )/// Step 1.  Wait until UDRE0 flag is high. Busy Waitinig
	{;}

	UDR0 = c; /// Step 2. Write char to UDR0 for transmission
}

/**
 * @brief Receive 8bit sata.
 *
 *@details This is a code snippet from datasheet page 187
 *
 * @return Returns received data from UDR0
 */
int USART_receive(FILE *stream )
{

	while ( !(UCSR0A & (1<<RXC0)) )/// Step 1. Wait for Receive Complete Flag is high. Busy waiting
		;

	return UDR0;/// Step 2. Get and return received data from buffer
}

int main(void)
{
	PIR_DDR &= ~(1<<PIR_IN);
	Buzzer_DDR |= (1<<Buzzer_OUT);
	Buzzer_PORT &= ~(1<<Buzzer_OUT);
	
	USART_init(MYUBRR);
	stdout = fdevopen(USART_send, NULL);
	stdin = fdevopen(NULL, USART_receive);

	while(1)
	{
		if(bit_is_set(PIR_PIN_Reg,PIR_IN))
		{
			Buzzer_PORT|= (1<<Buzzer_OUT);
			if(pirState==0)
			{
				pirState=1;
				printf("Motion started\n");

			}
		}
		else
		{
			Buzzer_PORT &= ~(1<<Buzzer_OUT);
			if(pirState==1)
			{
				pirState=0;
				printf("Motion End\n");
			}

		}
	}
}
