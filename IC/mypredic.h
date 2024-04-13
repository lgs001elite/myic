/*
 * mypredic.h
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */

#ifndef MYPREDIC_H_
#define MYPREDIC_H_

#define MAX_SIZE 10

typedef struct
{
    int items[MAX_SIZE];
    int front, rear;
} Queue;


void initializeQueue(Queue *q);
void updateQueue(Queue *q, int position, int newValue);
int findMaxValue(Queue *q);
void enqueue(Queue *q, int value);
int dequeue(Queue *q);


#endif /* MYPREDIC_H_ */
