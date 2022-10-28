#include <iostream>
#include <string>
#include <cstring>
using namespace std;

void print_figure(char arr[3][3])
{
    for(int i = 0; i < 3; i++)
    {
        for(int j = 0; j < 3; j++)
        {
            cout<< arr[i][j];
            
        }
        cout<<endl;
    }
    
}

void hand_to_head(char arr[3][3], bool left)
{
    if(left == true)
    {
        arr[0][2] = ')';
        arr[1][2] = ' ';
    }
    
    else
    {
        arr[0][0] = '(';
        arr[1][0] = ' ';
    }
    

}

void hand_to_hip(char arr[3][3], bool left)
{
    if(left == true)
    {
        arr[0][2] = ' ';
        arr[1][2] = '>';
    }
    else
     {  
         arr[0][0] = ' ';
         arr[1][0] = '<';
     }
}

void hand_to_start(char arr[3][3], bool left)
{
    if(left == true)
    {
        arr[0][2] = ' ';
        arr[1][2] = '\\';        
    }
    
    else
    {   
        arr[0][0] = ' ';
        arr[1][0] = '/';
    }
    

}

void leg_in(char arr[3][3], bool left)
{
    if(left == true)
        arr[2][2] = '>';
    
    else
        arr[2][0] = '<';
}

void leg_out(char arr[3][3], bool left)
{   
    if(left == true)
        arr[2][2] = '\\';
    else
        arr[2][0] = '/';   
}

void turn(char arr[3][3])
{
    
    char ab[3];
    
    ab[0] = arr[0][2];
    ab[1] = arr[1][2];
    ab[2] = arr[2][2];
    
    if (arr[0][0] == '(')
    {
        arr[0][2] = ')';
    }
    
    else if (arr[0][0] == ' ')
    {
        arr[0][2] = ' ';
    }
    
    if (arr[1][0] == '/')
    {
        arr[1][2] = '\\';
    }
    
    else if (arr[1][0] == '<')
    {
        arr[1][2] = '>';
    }
    
    else if (arr[1][0] == ' ')
    {
        arr[1][2] = ' ';
    }
    
    if (arr[2][0] == '/')
    {
        arr[2][2] = '\\';
    }
    
    else if (arr[2][0] == '<')
    {
        arr[2][2] = '>';
    }
    
    if (ab[0] == ')')
    {
        arr[0][0] = '(';
    }
    
    else if (ab[0] == ' ')
    {
        arr[0][0] = ' ';
    }
    
    if (ab[1] == '\\')
    {
        arr[1][0] = '/';
    }
    
    else if (ab[1] == '>')
    {
        arr[1][0] = '<';
    }
    
    else if (ab[1] == ' ')
    {
        arr[1][0] = ' ';
    }
    
    if (ab[2] == '\\')
    {
        arr[2][0] = '/';
    }
    
    else if (ab[2] == '>')
    {
        arr[2][0] = '<';    
    }
    
    //sksk
}

void input(char arr[][3], string str)
{
    string say = "say";
    string left_leg_in = "left leg in";
    string right_leg_in = "right leg in";
    string left_leg_out = "left leg out";
    string right_leg_out = "right leg out";
    string left_hand_to_head = "left hand to head";
    string right_hand_to_head = "right hand to head";
    string left_hand_to_start = "left hand to start";
    string right_hand_to_start = "right hand to start";
    string left_hand_to_hip = "left hand to hip";
    string right_hand_to_hip = "right hand to hip";
    string turner = "turn";
    
    if (str.substr(0,3) == say)
    {
        string output = str.substr(4, str.length() - 4);
        cout << output << endl;
    }
    
    if(str == left_leg_in)
    {
        leg_in(arr, 1);
        print_figure(arr);
    }
    
    else if (str == right_leg_in)
    {
        leg_in(arr, 0);
        print_figure(arr);
    }
    
    else if (str == left_leg_out)
    {
        leg_out(arr, 1);
        print_figure(arr);
    }
    
    else if (str == right_leg_out)
    {
        leg_out(arr, 0);
        print_figure(arr);
    }
    
    else if (str == left_hand_to_head)
    {
        hand_to_head(arr, 1);
        print_figure(arr);
    }
    
    else if (str == right_hand_to_head)
    {
        hand_to_head(arr, 0);
        print_figure(arr);
    }
    
    else if (str == left_hand_to_hip)
    {
        hand_to_hip(arr, 1);
        print_figure(arr);
    }
    
    else if (str == right_hand_to_hip)
    {
        hand_to_hip(arr, 0);
        print_figure(arr);
    }
    
    else if (str == left_hand_to_start)
    {
        hand_to_start(arr, 1);
        print_figure(arr);
    }
    
    else if (str == right_hand_to_start)
    {
        hand_to_start(arr, 0);
        print_figure(arr);
    }
    
    else if (str == turner)
    {
        turn(arr);
        print_figure(arr);
    }
}
    

int main() {
    
    char arr[3][3] = {{' ', 'o', ' '}, {'/', '|', '\\'}, {'/', ' ', '\\'}};
    
    
    int T, d;
    cin >> T;
    
    for (int i = 0; i < T; i++)
    {
        cin >> d;
        for (int j = 0; j <= d; j++)
        {
            string str;
            getline(cin, str);
            if(j > 0)
            {
                //cout << str << endl;
                input(arr,str);
            }
        }
    }
    
    return 0;
}