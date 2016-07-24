CC = gcc
FILES = src/main.c src/speak/hello.c src/speak/goodbye.c
OUT_EXE = bin/speak

build: $(FILES)
	$(CC) -v -o $(OUT_EXE) $(FILES)

clean:
	rm -f *.o core

rebuild: clean build
