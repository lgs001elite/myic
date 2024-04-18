#ifndef COORDINATORLIST_H_
#define COORDINATORLIST_H_

#include <stdlib.h>
#include <stdint.h>

#define HASHMAP_SIZE 10

// Define the structure for hashmap entries
typedef struct Entry
{
    char key;
    int value;
    struct Entry *next;
} Entry;

// Define the hashmap structure
typedef struct
{
    Entry *entries[HASHMAP_SIZE];
} Hashmap;

void init_hashmap(Hashmap *map);
void hashmap_insert(Hashmap *map, char key, int value);
void hashmap_free(Hashmap *map);
int hashmap_find(Hashmap *map, char key);

#endif
