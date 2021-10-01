// 2017 카카오코드 예선 - 카카오프렌즈 컬러링북 - cpp파일 , 재귀, floodfill
#include <vector>
#include <iostream>

using namespace std;

vector<vector<int>> p;

int floodfill(int x, int y, int color) {
    int area = 1;
    
    if((x > 0) && (p[x-1][y] == color)) { // up
        p[x][y] = 0;
        area += floodfill(x-1,y,color);
    }
    
    if((x < p.size()-1) && (p[x+1][y] == color)) { // down
        p[x][y] = 0;
        area += floodfill(x+1,y,color);
    }
    
    if((y > 0) && (p[x][y-1] == color)) { // left
        p[x][y] = 0;
        area += floodfill(x,y-1,color);
    }
    
    if((y < p[0].size()-1) && (p[x][y+1] == color)) { // right
        p[x][y] = 0;
        area += floodfill(x,y+1,color);
    }
    
    p[x][y] = 0;
    
    return area;
}

// 전역 변수를 정의할 경우 함수 내에 초기화 코드를 꼭 작성해주세요.
vector<int> solution(int m, int n, vector<vector<int>> picture) {
    int number_of_area = 0;
    int max_size_of_one_area = 0;
    p = picture;
    int size_of_one_area = 0;
    
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(p[i][j] != 0) {
                size_of_one_area = floodfill(i,j,p[i][j]);
                number_of_area++;
                
                if(max_size_of_one_area < size_of_one_area)
                    max_size_of_one_area = size_of_one_area;
            }
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;

    return answer;
}
