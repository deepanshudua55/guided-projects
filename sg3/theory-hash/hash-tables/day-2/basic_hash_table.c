#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/****
  Basic hash table key/value pair
 ****/
typedef struct Pair
{
    char *key;
    char *value;
} Pair;

/****
  Basic hash table
 ****/
typedef struct BasicHashTable
{
    int capacity;
    Pair **storage;
} BasicHashTable;

/****
  Create a key/value pair to be stored in the hash table.
 ****/
Pair *create_pair(char *key, char *value)
{
    Pair *pair = malloc(sizeof(Pair));
    pair->key = strdup(key);
    pair->value = strdup(value);

    return pair;
}

/****
  Use this function to safely destroy a hashtable pair.
 ****/
void destroy_pair(Pair *pair)
{
    if (pair != NULL)
    {
        free(pair->key);
        free(pair->value);
        free(pair);
    }
}

/****
  djb2 hash function
  Do not modify this!
 ****/
unsigned int hash(char *str, int max)
{
    unsigned long hash = 5381;
    int c;
    unsigned char *u_str = (unsigned char *)str;

    while ((c = *u_str++))
    {
        hash = ((hash << 5) + hash) + c;
    }

    return hash % max;
}

/****
  Fill this in.
  All values in storage should be initialized to NULL
  (hint: look up `calloc`)
 ****/
BasicHashTable *create_hash_table(int capacity)
{
    BasicHashTable *ht = malloc(sizeof(BasicHashTable));
    ht->storage = calloc(capacity, sizeof(Pair *));
    ht->capacity = capacity;

    return ht;
}

/****
  Fill this in.
  If you are overwriting a value with a different key, print a warning.
  Don't forget to free any malloc'ed memory!
 ****/
void hash_table_insert(BasicHashTable *ht, char *key, char *value)
{
    // our pair and the index to insert the pair
    Pair *pair = create_pair(key, value);
    unsigned int index = hash(key, ht->capacity);

    // the stored pair at the hashed index
    // if it exists
    Pair *exists = ht->storage[index];

    if (exists)
    {
        // print warning if overwriting value
        if (strcmp(key, exists->key))
        {
            fprintf(stderr, "Overwriting value.\n");
        }
        // free the malloc'd memory
        destroy_pair(exists);
    }
    // finally, set the pair at the hashed index to be the new pair
    ht->storage[index] = pair;
}

/****
  Fill this in.
  Don't forget to free any malloc'ed memory!
 ****/
void hash_table_remove(BasicHashTable *ht, char *key)
{
    // first, get the index from the key
    unsigned int index = hash(key, ht->capacity);

    // if key doesn't exist or current stored key is different
    if (!ht->storage[index] || strcmp(ht->storage[index]->key, key))
    {
        fprintf(stderr, "Unable to remove key.\n");
    }
    // otherwise, it exists and matches the passed in key
    else
    {
        destroy_pair(ht->storage[index]);
        ht->storage[index] = NULL;
    }
}

/****
  Fill this in.
  Should return NULL if the key is not found.
 ****/
char *hash_table_retrieve(BasicHashTable *ht, char *key)
{
    unsigned int index = hash(key, ht->capacity);
    if (!ht->storage[index] || strcmp(ht->storage[index]->key, key))
    {
        fprintf(stderr, "Unable to retrieve key.\n");
        return NULL;
    }
    // if we get down here, the key exists and it matches
    return ht->storage[index]->value;
}

/****
  Fill this in.
  Don't forget to free any malloc'ed memory!
 ****/
void destroy_hash_table(BasicHashTable *ht)
{
    // first, free every individual pair
    for (int i = 0; i < ht->capacity; i++)
    {
        // check if there is a pair
        if (ht->storage[i])
        {
            destroy_pair(ht->storage[i]);
        }
    }
    // free the storage
    free(ht->storage);
    free(ht);
}

#ifndef TESTING
int main(void)
{
    struct BasicHashTable *ht = create_hash_table(16);

    hash_table_insert(ht, "line", "Here today...\n");

    printf("%s", hash_table_retrieve(ht, "line"));

    hash_table_remove(ht, "line");

    if (hash_table_retrieve(ht, "line") == NULL)
    {
        printf("...gone tomorrow. (success)\n");
    }
    else
    {
        fprintf(stderr, "ERROR: STILL HERE\n");
    }

    destroy_hash_table(ht);

    return 0;
}
#endif