.PHONY: build
build:
	C=clang CXX=clang++ cmake -B ./build -S . -G Ninja
	ninja -C ./build

clean:
	rm -rf ./build
	rm -rf ./sudokucheck

run: build
	cp ./build/sudokucheck ./sudokucheck
	./sudokucheck