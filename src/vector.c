#include <stdlib.h>
#include <stdio.h>
#include "vector.h"

_vector* create_new_vector() {
    _vector* vector = (_vector*) malloc(sizeof(_vector));

    return vector;
}

void free_vector(_vector* vector) {
    free(vector);
}

void set_x(_vector* vector, double x) {
    vector->x = x;
}

void set_y(_vector* vector, double y) {
    vector->y = y;
}

double get_x(_vector* vector) {
    return vector->x;
}

double get_y(_vector* vector) {
    return vector->y;
}
