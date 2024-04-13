/*
 * mypredic.c
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */


#include <stdio.h>
#include <limits.h>
#include "mypredic.h"


void initializeQueue(Queue *q)
{
    q->front = -1;
    q->rear = -1;
}

int isFull(Queue *q)
{
    return q->rear == MAX_SIZE - 1;
}

int isEmpty(Queue *q)
{
    return q->front == -1;
}

void enqueue(Queue *q, int value)
{
    if (isFull(q))
    {
        return;
    }
    if (isEmpty(q))
    {
        q->front = 0;
    }
    q->items[++q->rear] = value;
}

int dequeue(Queue *q)
{
    if (isEmpty(q))
    {
        return INT_MIN;
    }
    int item = q->items[q->front];
    if (q->front >= q->rear)
    {
        q->front = q->rear = -1; // Queue is now empty
    }
    else
    {
        q->front++;
    }
    return item;
}

void updateQueue(Queue *q, int position, int newValue)
{
    if (position < 0 || position >= MAX_SIZE)
    {
        return;
    }
    if (position > q->rear)
    {
        return;
    }
    q->items[position] = newValue;
}

int findMaxValue(Queue *q)
{
    if (isEmpty(q))
    {
        return INT_MIN;
    }
    int maxVal = q->items[q->front];
    int i = q->front + 1;
    for (; i <= q->rear; i++)
    {
        if (q->items[i] > maxVal)
        {
            maxVal = q->items[i];
        }
    }
    return maxVal;
}



