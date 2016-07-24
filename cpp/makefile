CC = g++
FILES = src/main.cpp src/speak/hello.cpp src/speak/goodbye.cpp
OUT_EXE = bin/speak_cpp

build: $(FILES)
	$(CC) -v -o $(OUT_EXE) $(FILES)

clean:
	rm -f *.o core

rebuild: clean build
