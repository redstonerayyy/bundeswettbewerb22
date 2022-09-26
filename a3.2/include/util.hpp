#pragma once

#include <vector>
#include <string>
#include <ios>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cctype>
#include <algorithm>

namespace Utils {
	std::vector<std::vector<int>> GetSudokus(std::string filepath);
	std::string readStringFromFile(std::string filePath);
	std::vector<std::string> SplitString(std::string stringtosplit, char delimeter);
	template<class T>
	std::vector<T> RemoveFromVector(std::vector<T> base, std::vector<T> toremove);
	void PrintSudoku(std::vector<std::vector<int>> sudokutoprint);
}
