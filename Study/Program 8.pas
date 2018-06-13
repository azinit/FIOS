var
  b:array [1..26] of integer;
  a, words:array [1..50] of string;
  l:array [1..50] of integer;
  leng,n,i,j:integer;
  s,q:string;
  bool:boolean;
begin
  assign(input,'input.txt');
  assign(output,'output.txt');
  reset(input);
  rewrite(output);
  readln(n);
  leng:=0;
  for i:=1 to n do
    readln(a[i]);
  for i:=1 to n do
    begin
      s:= a[i];
      bool:= True;
      for j:=1 to 26 do
        b[j]:= 0;
      for j:=1 to length(s) do
        b[ord(s[j])-96] := b[ord(s[j])-96] + 1;
      s:= '';
      for j:=1 to 26 do
        begin
          str(b[j], q);
          s := s + q + '|';
        end;
      for j:=1 to leng do
        if words[j] <> s then continue
        else
          begin
            bool:=False;
            l[j]:= l[j] + 1;
            break;
          end;
      if bool = True then
        begin
          words[leng + 1]:= s;
          leng:= leng + 1;
        end;
    end;
  n:=0;
  for i:=1 to leng do
    n:=max(n, l[i]);
  write(n+1);
  close(input);
  close(output);
end.