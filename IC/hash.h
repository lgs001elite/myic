/*
 * hash.h
 *
 *  Created on: Dec 20, 2023
 *      Author: glu250
 */

#ifndef HASH_H_
#define HASH_H_

#include <stdint.h>
#include <stddef.h>

typedef  int  WORD;  // 32-bit word, change to "long" for 16-bit machines

typedef struct {
    int32_t data[64];
    int32_t datalen;
    uint64_t bitlen;
    int32_t state[8];
} SHA256_CTX;


void sha256_init(SHA256_CTX *ctx);
void sha256_update(SHA256_CTX *ctx, const char data[], int32_t len);
void sha256_final(SHA256_CTX *ctx, char hash[]);

#endif /* HASH_H_ */
