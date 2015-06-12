%let nmb=907;

filename in "c:\ajps\learning\mini_project_git\test_stmtm_flow.sas ";

filename out "c:\ajps\learning\mini_project_git\test_stmtm_flow_nocom.sas ";

data old;
length text $200;
infile in truncover;
input text $char200.;
run;

data temp_&nmb;
set old; 
* all the flags should be retained from line to line since the comments could be spread across
many lines. Note that the program reads one text line at a time and sets all the flags to 0;
retain open_q 0 open_dq 0 open_c 0 sm 0 c 0 ch 0; 
* the program processes the text lines one character in a time;

do i=1 to length(text);
/* This part of the code is searching for comments of the “ *…; ” type */
if substr(text,i,1)^= '*' and substr(text,i,1)^=' ' then ch=1;
/* Note that this statement checks for data availability starting from the first line of the processed
program. When data will be found the flag will be set. The statement is looking for ‘*’ because the first
star in the processed code would indicate the beginning of the comment;
The statement below checks for the ‘; ‘ in the text as the end of the SAS statement. The open_q,
open_dq and open_c should be equal to ‘0’ to make sure that the ‘;’ is not a part of the comment
or a literal. */
if substr(text,i,1)= ';' and open_q=0 and open_dq=0 and open_c=0 then
do;
if c=1 then
do;
/* Note that If the ‘;’ is found it would indicate an end of the starcomment
if ‘c’ or
starcomment
was identified. At this point, we reset the ‘c’ flag to 0 and set this ‘;’ to blank*/
c=0;

substr(text,i,1)= ' ';
end;
sm=1; /* since the ‘;’ is found we are setting the ‘sm’ flag to 1 */
end;
/* The following code looks for ‘*’ as the beginning of the starcomment.
It assures that
the cursor is not in the middle of the comment or a literal. ‘sm’ is set to 1 to indicate that it
is not in the middle of a mathematical formula, such as x=y*2. Note that the combination ‘*;’
could be erroneously considered as the second type of the comment. */
if substr(text,i,1)= '*' and
(open_q=0 and open_dq=0 and open_c=0 and sm=1) then c=1;
/* Here the program looks for starcomments
as the very first statement in the processed
program */
if substr(text,i,1)= '*' and ch=0 then c=1;
/* The following code looks for double quotes in the processed program and makes sure that
they are not a part of comment (open_c) */
if substr(text,i,1)= '"' and open_c=0 then
do;
/* The following logic checks whether the doublequote
was not set earlier; if not then we set
open_dq to 1. But if the doublequote
was encountered earlier then it would mean that we
have already found the closing doublequote
and the open_dq has to reset to 0 */
if open_dq=0 and open_q=0 then open_dq=1;
else if open_dq=1 then open_dq=0;
end;
/* The following logic checks whether the quote was not set earlier, and if it is true, we set open_q to 1.
But if the quote was encountered earlier then it would mean that we found the closing quote and the
open_q is reset to 0 */
if substr(text,i,1)= "'" and open_c=0 then
do;
if open_q=0 and open_dq=0 then open_q=1;
else if open_q=1 then open_q=0;
end;
/* The following logic checks whether the beginning of the comment indicator is found and is not a
part of the literal. If this is case, then the comment open flag (open_c) is set to 1 */
if substr(text,i,2)="/*" and open_c=0 then
do;
if open_q=0 and open_dq=0 then open_c=1;
end;
/* The following logic checks whether the end of the comment indicator was found and the beginning
of the comment flag is on. In this case, we clear the end of the comment indicator and set the flag
(open_c) to 0, indicating that the comment is closed */
if substr(text,i,2)= "*/" then
do;
if open_c=1 then
do;
substr(text,i,2)=' ';
open_c=0;
end;
end;

/* This part contains commentremoving
logic. If comment or starcomment
is open, and
the cursor is not in the middle of the quoted string, then the comment characters will be cleared
one digit in a time */
if (open_c=1 and open_q=0 and open_dq=0) or c=1 then
substr(text,i,1)=' ';
/* This part of code checks if ‘;’ was found and the new statement started. In this case the semicolon
flag should be set to 0. Note that the nonblank
and nonsemicolon
character would indicate the
start of a new statement */
if sm=1 and substr(text,i,1)^= ' ' and c^=1 and open_c=0
and substr(text,i,1)^= ';' then sm=0;
end;
run;

/* This data step recreates
the original SAS program without comments.
Note that the positions of all SAS statements are unchanged */
data _null_;
set temp_&nmb;
x=verify(text,' ');
file out;
put @x+1 text;
run;
