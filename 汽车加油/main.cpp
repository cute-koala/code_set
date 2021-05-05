#include<bits/stdc++.h>
using namespace std;
int main()
{
    fstream ss,cs;
    ss.open("input.txt",ios::in);
    cs.open("output.txt",ios::out);
    if(!ss.is_open())
    {
        cout<<"not open"<<endl;
        return 0;
    }
    int n,k;

    ss>>n>>k;
    int way[k+1];
    int i;
    for(i=0;i<k+1;i++)
        ss>>way[i];
    ss.close();
    int num=0,m=n;
    for(i=0;i<k+1;i++)
    {
        if(n<way[i])
        {
            cs<<"No Solution";
            return 0;
        }
        if(m>=way[i])
        {
            m=m-way[i];
            continue;
        }
        else
        {
            m=n;
            num++;
            m=m-way[i];
        }
    }
    cs<<num;
    return 0;

}
