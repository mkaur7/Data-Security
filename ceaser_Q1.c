#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<ctype.h>

int encode(int ch, int key) { 
    if (islower(ch)) {
         ch = (ch-'a' + key) % 26 + 'a';
         ch += (ch < 'a') ? 26 : 0;
    }
    else if (isupper(ch)) {
         ch = (ch-'A' + key) % 26 + 'A';
         ch += (ch < 'A') ? 26 : 0;
    }
    return ch;
}

int main(void)
{
	FILE *file_in, *file_out;
	char ch;
	char textfile[500];
	int key;
	
	printf("\n Enter the input file: ");
	scanf("%s", textfile);
	file_in = fopen(textfile, "r"); 
 
	if( file_in == NULL )
	{
		perror("Error while opening the file.\n");
		exit(EXIT_FAILURE);
	}

	printf("\n Enter the output file: ");
    	scanf("%s", textfile);
    	file_out = fopen(textfile, "w");
     
    	printf("\n Enter the key: ");
    	scanf("%d", &key);
	
	while( (ch = fgetc(file_in) ) != EOF)
	{
		 if(isupper(ch))
                {
                        ch = ch + 32;
                }
                putc(ch, file_in);
		ch = encode(ch, key);
		fprintf(file_out, "%c", ch);
	}
	printf("\n File has been encoded! \n \n");
	fclose(file_out);
	fclose(file_in);
	
	return 0;
}
