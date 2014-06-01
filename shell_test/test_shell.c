#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>

int main() {

	char buf[10000];
	read(0, buf, 0x100000);
	int *map = mmap(NULL, 4096, PROT_READ|PROT_WRITE|PROT_EXEC, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0);
	memcpy(map, buf, 4096);
	((void (*)(void))map)();
}


