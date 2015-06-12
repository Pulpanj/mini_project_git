%let nmb=908;
/* Input file to clean */
filename in "Z:\master\fics\ruben\prg&nmb..sas";
/* Output file to with comments removed */
filename out "Z:\master\fics\ruben\prg&nmb._clean.sas";

*
Here the text of the program. Note that the flags used here are as follows:
flag_eq is for finding ‘=’ sign,
flag is for identifying ‘/*’ and ‘*/’,
flag_s is for identifying ‘*’ and ’;’,
;

%let lg= 200; *declare the length of each input line;
data temp(keep=text1 textn); * we keep both the original and cleaned version of program lines;
length text1 $&lg.; * defining the length of the new string;
infile in truncover; * reading of the SAS code as a text file;
input textn $char%eval(&lg+1).; * the whole line is treated as one character variable;
retain flag 0 flags 0 flg_eq 0 Icur Istartn; * these flags and variables will be retained;
Istartn=1; * initialization of starting index;
start:; * the label of the goto loop below;
Istart=Istartn; * assuming the current index as the start value ;
do I=Istart to &lg; * starting loop to go over the string;
if substr(textn,I,1)='=' then flg_eq=1; * if ‘=’ is encounterd flg_eq is 1;
5
else if substr(textn,I,1)=';' then flg_eq=0; * otherwise it is zero;
/* This section applies when comments of the second type are present */
if substr(textn,I,2)='/*' or flag=1 then
do; Icur=I; /* flag is initialized if ‘/*’ is encountered for the
first time or the cursor is still within the comment
area opened at some moment earlier */
do I=Istart to &lg; * starting of the new loop;
if I>=Icur then
do; * defining the area of nontrivial changes;
if substr(textn,I,1)='/' and substr(textn,I+1,1)='*' then flag=1;
* condition when flag is assigned to 0;
else if substr(textn,I,1)='/' and substr(textn,I1,1)='*'
then
do; * condition when the comment is closed;
flag=0; Istartn=I+1; * redefining flag and the outer loop star value;
substr(text1,I,1)=' '; * assigning space;
goto start; *go to label start;
end;
if flag=1 then substr(text1,I,1)=' '; * assigning space;
end;
end;
end;
/* This section applies when double quotes are present */
else if substr(textn,I,1)="'" then
do; Icur=I; * double quote is found;
do I=Istart to &lg; * start of the new cycle;
if I>=Icur then
do;
substr(text1,I,1)=substr(textn,I,1); *every character from the
original string is copied to the new one;
if substr(textn,I,1)="'" and I ^=Icur then
do;
Istartn=I+1;
goto start; * return back in case the next double quote is found;
end;
end;
end;
end;
/* This section applies when single quotes are present */
else if substr(textn,I,1)='"' then
do; Icur=I; * single quote is found;
do I=Istart to &lg; * start of the new cycle;
if I>=Icur then
do;
substr(text1,I,1)=substr(textn,I,1); * every character from the
original string is copied to the new one;
if substr(textn,I,1)='"' and I ^=Icur then
do;
Istartn=I+1;
goto start; * returns back in case the next single quote is found;
end;
end;
end;
end;
/* This section applies when comments of the second type are present */
6
else if (substr(textn,I,1)='*' and flg_eq=0)
or (flags=1) then
do; Icur=I; * identifying the beginning of the comment;
do I=Istart to &lg; * looping through all the fields;
if I>=Icur then
do; * the beginning of the comment;
if substr(textn,I,1)='*' then flags=1;
if substr(textn,I,1)=';' then
do; *the comment ends with a semicolon;
flags=0;
Istartn=I+1;
goto start; * leaving the loop;
end;
if flags=1 then substr(text1,I,1)=' '; * characters
are replaced with blanks if they are positioned within a comment;
end;
end;
end;
/* This part copies all the characters in case “*..;” is not a comment */
else if (substr(textn,I,1)='*' and flg_eq=1) then
do;
substr(text1,I,1)= substr(textn,I,1);
end;
/* Copy the string as it is if the cursor is out of the areas mentioned above */
else if substr(textn,I,2)^='/*'
and substr(textn,I,1)^="'"
and substr(textn,I,1)^='"'
and substr(textn,I,1)^='*'
then substr(text1,I,1)= substr(textn,I,1);
end;
if text1='' then delete;
run;
/* This data step creates the cleaned version of the program without comments */
data _null_;
set temp;
x=verify(text1,' ');
file out;
put @x+1 text1;
run;
RESULTS
We now demonstrate several examples where the programs remove the comments from the input SAS
programs. Note that the programs can be applied to SAS logs as well as SAS programs. The following
examples were run with both program versions provided, linear and modular, with similar results. One
difference between the two programs is the linear version retains blank lines, whereas the modular one
removes them.
INPUT WITH ‘*’ BUT NO COMMENTS
Suppose that initial text contains no comments but it has asterisks embedded in mathematical expressions.
Say the text in the prg01.sas program is as follows:
7
Data prg01;
x=2; y=x*3;
z=2*x+3*y;
run;
Note that the some lines have preceding spaces. After running the code, the following cleaned version of the
program (prg01.sas) results:
Data prg01;
x=2; y=x*3;
z=2*x+3*y;
run;
We see that the text of the program did not change. For this example the code does not alter the text if there
are no comments in it. Note that the code identifies that the strings ‘*3;’ and ‘3*y;’ are constituent parts of
mathematical expressions rather than the comments of the second type.
INPUT WITH ‘/*…*/’ COMMENTS
In this case, we consider a standard SAS program (prg02.sas) containing /*…*/ comments, which could be
located on one line and/or spread over many lines.
In this specific case, the SAS program with comments has the following form:
/* This is comment
spread across
many lines */
Data prg02; /* comment after a statement */
/* comment before a statement */ x=2;
/* comment before a statement */ y=2; /* comment after
a statement a spread across
many lines*/
run;
/* Another comment after the program */
After using our program, the cleaned version is as follows:
Data prg02;
x=2;
y=2;
run;
Note that the program leaves the SAS code statements in their original locations (columns). If necessary, all
indented lines can be leftjustified
with a simple update to the last data step that writes the commentfree
file.
INPUT WITH ‘*…;’ COMMENTS
In this case we consider a standard SAS program (prg03.sas) containing *…; comments, which could be
located on one line and/or spread over many lines.
Say, the contaminated version has the following form:
* This is comment of the second type
spread across
many lines ;
Data prg03; * comment after a statement;
* comment before a statement; x=2;
* comment before a statement; y=2; * comment after
a statement a spread across
many lines;
run;
This is another comment after the program ;
8
After applying our program, the cleaned version (prg03.sas) is as follows:
Data prg03;
x=2;
y=2;
run;
COMMENTS INSIDE THE VALUE OF THE CHARACTER VARIABLE
In this case we consider a standard SAS program (prg04.sas) containing both types of
comments, as well as some comments that are part of character strings. The commented version has the
following form:
Data prg04;
x="asd /*hgf*/ dfg";
x="asd *hgf; dfg";
/* asdgfvjn "gd jhf" */
y='asd * hgf ; dfg';
run;
After running our program, the cleaned version takes the following form:
Data prg04;
x="asd /*hgf*/ dfg";
x="asd *hgf; dfg";
y='asd * hgf ; dfg';
run;
CONCLUSION
We acknowledge the need for well documented source code, but have experienced the reality where
extensive commenting impedes a programmer’s task of understanding legacy code. Our programs to
remove comments from a SAS program or log are intended as a tool for any level programmer. By
providing two methods we demonstrate the versatility of base SAS, and hope they serve a basic but useful
purpose.
CONTACT INFORMATION
Your comments and questions are valued and encouraged. Contact the author at:
Susan Myers Ruben Chiflikyan
RTI International RTI International
3040 Cornwallis Road, PO Box 12194 3040 Cornwallis Road, PO Box 12194
Research Triangle Park, NC, 277092194
Research Triangle Park, NC, 277092194
Work Phone: (919) 5417441
Work Phone: (919) 5416064
Fax: (919) 9908368
Fax: (919) 9908368
Email:
smyers@rti.org Email:
rchiflikyan@rti.org
Web: http://www.rti.org Web: http://www.rti.org
Mila Chiflikyan
RTI International
3040 Cornwallis Road, PO Box 12194
Research Triangle Park, NC, 277092194
Work Phone: (919) 3163360
Fax: (919) 9908368
Email:
milachif@rti.org
9
Web: http://www.rti.org
SAS and all other SAS Institute Inc. product or service names are registered trademarks or trademarks of
SAS Institute Inc. in the USA and other countries. ® indicates USA registration.
Other brand and product names are trademarks of their respective companies.
