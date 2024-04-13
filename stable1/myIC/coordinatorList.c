#include "coordinatorList.h"

// Initialize hashmap
void init_hashmap(Hashmap *map)
{
    int i = 0;
    for (; i < HASHMAP_SIZE; i++)
    {
        map->entries[i] = NULL;
    }
}

// Insert key-value pair
void hashmap_insert(Hashmap *map, char key, int value)
{
    // Create a new entry to hold our key-value pair
    Entry *entry = (Entry *)malloc(sizeof(Entry));
    entry->key = key;
    entry->value = value;
    entry->next = map->entries[key];
    map->entries[key] = entry;
}

// free hash maps
void hashmap_free(Hashmap *map)
{
    int i = 0;
    for (; i < HASHMAP_SIZE; i++)
    {
        if (map->entries[i] != NULL)
        {
            free(map->entries[i]);
            map->entries[i] = NULL;
        }
    }
}

// Retrieve value
int hashmap_find(Hashmap *map, char key)
{
    // Find the key-value pair in the chain
    Entry *entry = map->entries[key];
    while (entry != NULL)
    {
        if (entry->key == key)
        {
            return entry->value;
        }
        entry = entry->next;
    }
    return -1;
}

