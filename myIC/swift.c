/*
 * swift.c
 *
 *  Created on: April 10, 2024
 *      Author: glu250
 */

#include "swift.h"

uint16_t swift_role1(uint16_t chr)
{
    swift_attempt = swift_attempt + 1;
    uint16_t chrThreshold = chr * 3;
    if (swift_attempt == chrThreshold)
    {
        swift_attempt = 0;
        swift_inc = swift_inc + 1;
    }
    if (swift_inc > 10)
    {
        swift_inc = 0;
    }
    return swift_inc;
} 


uint16_t swift_role2(uint16_t chr)
{
    return 0;
}

