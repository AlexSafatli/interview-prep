#ifndef _linked_list_h_
#define _linked_list_h_

typedef struct linked_list_node {
  void *data; // pointer to some data
  struct linked_list_node *next;
} node_t;

typedef struct {
  node_t *head;
} linked_list_t;

linked_list_t *linked_list_init ( );
void linked_list_destroy ( linked_list_t *list );
int linked_list_append_to_head ( linked_list_t *list, void *data );
int linked_list_remove_head ( linked_list_t *list, void **data);

#endif /* _linked_list_h_ */
