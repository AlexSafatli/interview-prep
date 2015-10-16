CFLAGS = -g -pthread

all: linked_list

linked_list: linked_list_test.o linked_list.o
	gcc $(CFLAGS) -o linked_list_test linked_list.o linked_list_test.o

linked_list.o: linked_list.c linked_list.h
	gcc $(CFLAGS) -c linked_list.c

linked_list_test.o: linked_list_test.c
	gcc $(CFLAGS) -c linked_list_test.c

clean:
	-rm linked_list_test *.o
