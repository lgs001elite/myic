/*
 * bonito.h
 *
 *  Created on: June 20, 2024
 *      Author: glu250
 */

#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "coordinator.h"

unsigned int hash(const char *key)
{
    unsigned long int value = 0;
    unsigned int i = 0;
    unsigned int key_len = strlen(key);

    // Do several rounds of multiplication
    for (; i < key_len; ++i)
    {
        value = value * 37 + key[i];
    }

    // Make sure value is 0 <= value < TABLE_SIZE
    value = value % TABLE_SIZE;

    return value;
}

HashTable *create_table()
{
    HashTable *table = malloc(sizeof(HashTable));
    table->entries = malloc(sizeof(HashTableEntry *) * TABLE_SIZE);
    for (int i = 0; i < TABLE_SIZE; ++i)
    {
        table->entries[i] = NULL;
    }
    return table;
}

HashTableEntry *create_entry(const char *key, const char *value)
{
    HashTableEntry *entry = malloc(sizeof(HashTableEntry));
    entry->key = strdup(key);
    entry->value = strdup(value);
    entry->next = NULL;
    return entry;
}

void hash_table_insert(HashTable *table, const char *key, const char *value)
{
    unsigned int slot = hash(key);

    // Try to look up an entry set
    HashTableEntry *entry = table->entries[slot];

    // If no entry exists, place new entry there
    if (entry == NULL)
    {
        table->entries[slot] = create_entry(key, value);
        return;
    }

    HashTableEntry *prev;

    // Walk through each entry until either the end is
    // reached or a matching key is found
    while (entry != NULL)
    {
        // Check if key matches
        if (strcmp(entry->key, key) == 0)
        {
            // Replace value
            free(entry->value);
            entry->value = strdup(value);
            return;
        }

        // Proceed to next bucket
        prev = entry;
        entry = prev->next;
    }

    // End of chain reached without finding key
    prev->next = create_entry(key, value);
}

char *hash_table_search(HashTable *table, const char *key)
{
    unsigned int slot = hash(key);

    // Try to look up an entry set
    HashTableEntry *entry = table->entries[slot];

    // Traverse linked list, looking for our value
    while (entry != NULL)
    {
        if (strcmp(entry->key, key) == 0)
        {
            return entry->value;
        }
        entry = entry->next;
    }

    // No match found
    return NULL;
}

void hash_table_delete(HashTable *table, const char *key)
{
    unsigned int slot = hash(key);

    // Try to look up an entry set
    HashTableEntry *entry = table->entries[slot];

    if (entry == NULL)
    {
        // No entry means nothing to delete
        return;
    }

    HashTableEntry *prev;
    int idx = 0;

    // Traverse linked list, looking for our value
    while (entry != NULL)
    {
        if (strcmp(entry->key, key) == 0)
        {
            if (idx == 0)
            {
                // First bucket is the match
                table->entries[slot] = entry->next;
            }
            else
            {
                // Remove from the list
                prev->next = entry->next;
            }

            // Free memory
            free(entry->key);
            free(entry->value);
            free(entry);
            return;
        }

        // Else, move on to next
        prev = entry;
        entry = prev->next;
        ++idx;
    }
}
