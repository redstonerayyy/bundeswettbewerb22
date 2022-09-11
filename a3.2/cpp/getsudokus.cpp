#include "getsudokus.hpp"

std::string GetSudokus(std::string filepath)
{
    std::string filecontents = ReadFile(filepath);
    std::vector<std::string> lines = SplitString(filecontents, '\n');

    RemoveFromVector(lines, { " ", "\n" });
    std::cout << "-------\n" << std::flush;

    std::vector<std::vector<int>> sudoku1;
    
    for(int i = 0; i < 9; ++i){
        std::vector<std::string> numbers = SplitString(lines[i], ' ');
        std::vector<int> nums;
        for(auto& num : numbers){
           nums.push_back(stoi(num)); 
        }
        sudoku1.push_back(nums);
    }
    
    std::vector<std::vector<int>> sudoku2;

    for(int i = 9; i < 18; ++i){
        std::vector<std::string> numbers = SplitString(lines[i], ' ');
        std::vector<int> nums;
        for(auto& num : numbers){
           nums.push_back(atoi(num.c_str())); 
        }
        sudoku2.push_back(nums);
    }


    return "fff";
}

std::string ReadFile(std::string filepath)
{
    // read string from file
    // https://stackoverflow.com/questions/116038/how-do-i-read-an-entire-file-into-a-stdstring-in-c
    constexpr auto read_size = std::size_t(4096);
    auto stream = std::ifstream(filepath);
    stream.exceptions(std::ios_base::badbit);

    auto out = std::string();
    auto buf = std::string(read_size, '\0');
    while (stream.read(&buf[0], read_size))
    {
        out.append(buf, 0, stream.gcount());
    }
    out.append(buf, 0, stream.gcount());
    return out;
}

std::vector<std::string> SplitString(std::string stringtosplit, char delimeter)
{
    std::stringstream ss(stringtosplit);
    std::string line;
    std::vector<std::string> lines;

    while (std::getline(ss, line, delimeter)){
        lines.push_back(line);
    }

    return lines;
}

template<class T>
std::vector<T> RemoveFromVector(std::vector<T> base, std::vector<T> toremove){
    for(int i = 0; i < base.size(); ++i){
        for(int j = 0; j < toremove.size(); ++j){
            if(base[i] == toremove[j]){
                base.erase(base.begin() + i);
            }
        }
    }

    return base;
}