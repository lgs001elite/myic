/*
 * coordinator.h
 *
 *  Created on: June 20, 2024
 *      Author: glu250
 */

#ifndef COORDINATOR_H_
#define COORDINATOR_H_
#include <stdint.h>

typedef struct HashTableEntry
{
    char *key;
    char *value;
    struct HashTableEntry *next; // For handling collisions
} HashTableEntry;

#define TABLE_SIZE 10

typedef struct HashTable
{
    HashTableEntry **entries;
} HashTable;

unsigned int hash(const char *key);

HashTable *create_table();

HashTableEntry *create_entry(const char *key, const char *value);

void hash_table_insert(HashTable *table, const char *key, const char *value);

char *hash_table_search(HashTable *table, const char *key);

void hash_table_delete(HashTable *table, const char *key);

extern HashTable *g_locTable;
extern uint8_t g_globalLoc;

#endif
