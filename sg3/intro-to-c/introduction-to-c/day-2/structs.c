#include <stdio.h>
#include <stdlib.h> // <-- include this for free and malloc
#include <string.h>

// a struct is a conglomeration of types
// the main usecase of structs is to define custom types from other types
struct Animal
{
    char *name;
    int leg_count;
};

// once this function goes out of scope
// our goat struct doesn't exist anymore
void temp_goat(void)
{
    struct Animal goat;

    goat.name = "goat";
    goat.leg_count = 4;

    printf("Name: %s\nLeg Count: %d\n", goat.name, goat.leg_count);
}

void temp_dog(void)
{

    struct Animal *p;

    struct Animal dog;

    p = &dog;

    p->name = "dog";
    p->leg_count = 4;

    // these are all the same thing
    printf("Name: %s\nLeg Count: %d\n", p->name, p->leg_count);
    printf("Name: %s\nLeg Count: %d\n", (*p).name, (*p).leg_count);
    printf("Name: %s\nLeg Count: %d\n", dog.name, dog.leg_count);
}

// essentially a class constructor function
struct Animal *create_animal(char *name, int leg_count)
{
    // allocate memory for the struct
    // by using malloc, we're creating something
    // that lives on the heap
    struct Animal *a = malloc(sizeof(struct Animal));

    // we allocate the length + 1 for the null terminating character
    a->name = malloc(strlen(name) + 1);
    strcpy(a->name, name);

    a->leg_count = leg_count;

    return a;
}

// we need a destructor function to clean up our instances
// we're passing an instance of the Animal struct by reference
void free_animal(struct Animal *a)
{
    // first we need to free any mallocated properties of the struct
    free(a->name);
    // after all properties are freed, free the struct itself
    free(a);
}

void set_animal_name(struct Animal *a, char *name)
{
    // we'll use realloc - reallocating memory
    // if (a->name)
    // {
    //     free(a->name);
    // }
    // a->name = malloc(strlen(name) + 1);
    // strcpy(a->name, name);

    a->name = realloc(a->name, strlen(name + 1));
    strcpy(a->name, name);
}

int main(void)
{

    temp_goat();
    temp_dog();
    struct Animal *cat = create_animal("cat", 4);
    printf("Name: %s\nLeg Count: %d\n", cat->name, cat->leg_count);
    set_animal_name(cat, "lion");
    printf("Name: %s\nLeg Count: %d\n", cat->name, cat->leg_count);
    free(cat);
    return 0;
}