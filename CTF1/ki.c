#define _POSIX_C_SOURCE 200112
#define _GNU_SOURCE

#include "sys/mman.h"
#include "fcntl.h"
#include "stdlib.h"
#include "string.h"
#include "stdio.h"
#include "unistd.h"
#include "sys/stat.h"
#include "elf.h"
#include "signal.h"

/*Loads program into memory then calls function
at set offset determined by disassembler.
Again Ki put in most of the work also
stole some of evans code as well*/

int main(int argc, char *argv[]) {

	int fd = open("crackme", O_RDONLY);

    if(fd == -1) {
        perror(NULL);
        exit(10);
    }

	struct stat st_fd;
    if(fstat(fd, &st_fd) == -1) {
        perror(NULL);
        exit(11);
    }

	void* ptr = mmap(NULL, st_fd.st_size,
		PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE, fd, 0
	);

	int (*func)(char* str) = (ptr + 0xea0);


	int ret = func(argv[1]);
	printf("%x\n", ret);
	return 0;
}