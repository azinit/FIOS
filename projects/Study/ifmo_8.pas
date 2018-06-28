var
  n,i,j,len:byte;
  s,c:string;
  a:array [1..26] of shortint;
  res:array [1..50] of string;
  iters:array [1..50] of byte;
  f:boolean;
begin
  assign(input,'input.txt');
  assign(output,'output.txt');
  reset(input);
  rewrite(output);
  readln(n);
  len:=0;
  for i:=1 to n do
    begin
      for j:=1 to 26 do
        a[j]:= 0;
      readln(s);
      f:= True;
      //write(s, ' ');
      for j:=1 to length(s) do
        inc(a[ord(s[j])-96]);
      s:= '';
      for j:=1 to 26 do
        begin
          str(a[j], c);
          s := s + c + '.';
        end;
      //writeln(s);
      for j:=1 to len do
        if res[j] <> s then continue
        else
          begin
            f:=False;
            inc(iters[j]);
            break;
          end;
      if f then
        begin
          inc(len);
          res[len]:= s;
        end;
    end;
  //writeln(len);
  n:=0;
  for i:=1 to len do
    n:=max(n, iters[i]);
  write(n+1);
  close(input);
  close(output);
end.