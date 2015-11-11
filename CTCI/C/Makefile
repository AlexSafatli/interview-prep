CFLAGS = -g -pthread

all: linked_list

linked_list: test_linked_list.o linked_list.o
	gcc $(CFLAGS) -o test_linked_list linked_list.o test_linked_list.o

linked_list.o: linked_list.c linked_list.h
	gcc $(CFLAGS) -c linked_list.c

test_linked_list.o: test_linked_list.c
	gcc $(CFLAGS) -c test_linked_list.c

clean:
	-rm test_linked_list *.o