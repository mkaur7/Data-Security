#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int main()
{
	char filename[500];
	int frequency[26] = {0};
	char ch;
	
	printf("\n Enter input file: ");
	scanf("%s", filename);
	FILE *fileHandle;
	fileHandle = fopen(filename, "r");
 	
	if(fileHandle == NULL)
	{
    		return -1;
	}

	for (ch = 0; ch < 26; ch++)
	{
   		frequency[ch] = 0;
	}
	while((ch = fgetc(fileHandle)) != EOF)
	{
		if ('a' <= ch && ch  <= 'z')
        	{
			frequency[ch - 97]++;
		}
	}	

	for (ch = 0; ch < 26; ch++)
	{
		if(frequency[ch] != 0)
			printf("frequency[%c] = %d\n", 65+ch, frequency[ch]); 	
	}
	int maxCount, maxCount2;
	char maxChar, maxChar2;
	int i;
	int key;
	for (i = 0; i < 26; i++)
	{
  		if (frequency[i] > maxCount)
		{
			maxCount = frequency[i];
      			maxChar = i;
		}
	}
	printf("\n Character with highest frequency is: '%c' \n", 65+maxChar);
	
	for (i = 0; i < 26; i++)
        {
               	if (frequency[i] > frequency[maxChar])
                {
                	maxChar2 = maxChar;
                        maxChar = i;
                }
		else if (frequency[i] > frequency[maxChar2] && frequency[i] != frequency[maxChar])
		{
			maxChar2 = i;
        	}
	}
        printf("\n Character with second highest frequency is: '%c' \n", 65+maxChar2);
	
	if((maxChar - 'E') == (maxChar2 - 'T'))
	{
		key = maxChar - 'E';
	}
	printf("\n Key to encrypt the file is: %d \n\n", 65+key);	

	return 0; 
}
