// LinkedList
// Author: Alex Safatli
// Date: Fri 16 Oct 2015

#include <stdlib.h>
#include "linked_list.h"

linked_list_t* linked_list_init() {

  linked_list_t* list = (linked_list_t*) malloc(sizeof(linked_list_t));
  if (list != NULL) {
    // Initialize head to NULL.
    list->head = NULL;
  }
  return list;

}

void linked_list_destroy(linked_list_t *list) {

  node_t *temp = NULL;
  if (list != NULL) {
    while (list->head != NULL) {
      // Keep setting head to next node. Free along the way.
      temp = list->head;
      list->head = list->head->next;
      free(temp);
    }
    list->head = NULL;
  }    

}

int linked_list_append_to_head(linked_list_t *list, void *data) {

  int status = 0;
  if (list != NULL) {
    node_t *node = (node_t*) malloc(sizeof(node_t));
    if (node != NULL) {
      node->next = list->head;
      node->data = data;
      list->head = node;
      status = 1;
    }
  }
  return status;
  
}

int linked_list_remove_head(linked_list_t *list, void **data) {

  int status = 0;
  if (list != NULL && data != NULL) {
    if (list->head != NULL) {
      // Get data.
      *data = list->head->data;
      // Remove node.
      node_t *temp = list->head;
      list->head = temp->next;
      free(temp);
      status = 1;
    }
    else *data = NULL;
  }
  return status;

}


