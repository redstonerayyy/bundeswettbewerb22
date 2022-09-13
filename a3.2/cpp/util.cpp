#include "util.hpp"

std::vector<std::vector<int>> GetSudokus(std::string filepath)
{
    std::string filecontents = ReadFile(filepath);
    std::vector<std::string> lines = SplitString(filecontents, '\n');

    RemoveFromVector(lines, { "", "\t", "\v", "\f", "\r", " ", "\n" });

    std::vector<std::vector<int>> sudoku1;
    
    // std::cout << lines[0].size() << "\n";
    // for(int i = 0; i < 9; ++i){
    //     std::cout << lines[0][i] << "\n";
    //     std::cout << "-----" << std::endl;
    // }

    for(int i = 0; i < 9; ++i){
        std::vector<std::string> numbers = SplitString(lines[i], ' ');
        std::vector<int> nums;
        for(auto& num : numbers){
           nums.push_back(atoi(num.c_str())); 
        }
        sudoku1.push_back(nums);
    }

    PrintSudoku(sudoku1);
    std::cout << "-----" << std::endl;

    std::vector<std::vector<int>> sudoku2;
    
    for(int i = 9; i < 18; ++i){
        std::vector<std::string> numbers = SplitString(lines[i], ' ');
        std::vector<int> nums;
        std::cout << lines[i] << "\n";
        std::cout << numbers.size() << "\n";
        for(auto& num : numbers){
           nums.push_back(atoi(num.c_str())); 
        }
        std::cout << nums.size() << "\n";
        sudoku2.push_back(nums);
    }

    PrintSudoku(sudoku2);

    return sudoku1;
}

std::string ReadFile(std::string filepath)
{
    // read string from file
    // https://stackoverflow.com/questions/116038/how-do-i-read-an-entire-file-into-a-stdstring-in-c
    constexpr auto read_size = std::size_t(4096);
    auto stream = std::ifstream(filepath);
    stream.exceptions(std::ios_base::badbit);
    stream.seekg(3); // because of BOM

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
    std::cout << base.size() << "\n";
    for(int i = 0; i < base.size(); ++i){
        // std::cout << base[i].size() << ":" << base[i] << "\n";
        for(int k = 0; k < toremove.size(); ++k){
            if(base[i] == toremove[k]){
                std::cout << "found" << std::endl;
                base.erase(base.begin() + i);
            }
        }
    }
    std::cout << base.size() << "\n";
    return base;
}

void PrintSudoku(std::vector<std::vector<int>> sudokutoprint){
    for(int i = 0; i < sudokutoprint.size(); ++i){
        for(int j = 0; j < sudokutoprint[i].size(); ++j){
            std::cout << sudokutoprint[i][j] << "  ";
        }
        std::cout << "\n";
    }
}
