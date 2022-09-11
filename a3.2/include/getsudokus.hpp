#pragma once

#include <vector>
#include <string>
#include <ios>
#include <fstream>
#include <sstream>
#include <iostream>
#include <cctype>
#include <algorithm>

std::string GetSudokus(std::string filepath);
std::string ReadFile(std::string filepath);
std::vector<std::string> SplitString(std::string stringtosplit, char delimeter);
template<class T>
std::vector<T> RemoveFromVector(std::vector<T> base, std::vector<T> toremove);