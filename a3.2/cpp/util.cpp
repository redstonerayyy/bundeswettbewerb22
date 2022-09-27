#include "util.hpp"

namespace Utils {
    std::vector<std::string> SplitString(std::string startString, std::string delimiter)
    {
        size_t pos = 0;
        std::vector<std::string> tokens;
        while ((pos = startString.find(delimiter)) != std::string::npos)
        {
            tokens.push_back(startString.substr(0, pos));
            startString.erase(0, pos + delimiter.length());
        }
        tokens.push_back(startString);
        return tokens;
    }

    // utility function
    std::string readStringFromFile(std::string filePath)
    {
        std::ifstream file;
        file.exceptions(std::ifstream::failbit | std::ifstream::badbit);
        try {
            file.open(filePath);
            std::stringstream fileStream;
            fileStream << file.rdbuf();
            file.close();
            return fileStream.str();
        } catch (std::ifstream::failure e) {
            std::cout << "File not succesfully read!" << std::endl;
            return NULL;
        };
    }

    template<class T>
    std::vector<T> RemoveFromVector(std::vector<T> base, std::vector<T> toremove){
        for(int i = 0; i < base.size(); ++i){
            // std::cout << base[i].size() << ":" << base[i] << "\n";
            for(int k = 0; k < toremove.size(); ++k){
                if(base[i] == toremove[k]){
                    base.erase(base.begin() + i);
                }
            }
        }
        return base;
    }

    std::string RemoveFromString(std::string base, std::vector<std::string> toremove){
        for(int i = 0; i < base.length(); ++i){
            for(int j = 0; j < toremove.size(); ++j){
                if(base[i] == toremove[j]){
                    base.erase(base.begin() + i);
                }
            }
        }
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

    std::vector<int> lineToVec(std::string line){
        std::vector<std::string> numbersasstring = Utils::SplitString(line, " ");
        std::vector<int> linenumbers;
        for(int i = 0; i < numbersasstring.size(); ++i){
            linenumbers.push_back(std::stoi(numbersasstring[i]));
        }
        return linenumbers;
    }

    std::vector<std::vector<int>> GetSudokus(std::string filepath)
    {
        std::string filecontents = Utils::readStringFromFile(filepath);
        std::vector<std::string> lines = Utils::SplitString(filecontents, "\n");

        lines = Utils::RemoveFromVector(lines, { "", "\t", "\v", "\f", "\r", " ", "\n" });
        
        std::vector<std::vector<int>> s1;
        std::vector<std::vector<int>> s2;

        for(int i = 0; i < 9; ++i){
            s1.push_back(lineToVec(lines[i]));
        }

        for(int i = 9; i < 18; ++i){
            s1.push_back(lineToVec(lines[i]));
        }

        return std::vector<std::vector<int>>{{34}, {34}};
    }
}


